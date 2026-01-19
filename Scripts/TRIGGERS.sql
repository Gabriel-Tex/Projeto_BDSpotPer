USE BDSpotPer
GO
/* a) Um álbum, com faixas de músicas do período barroco, só pode ser inserido no
banco de dados, caso o tipo de gravação seja DDD. */

CREATE TRIGGER tg_barrocoDDD
ON Faixa
FOR INSERT, UPDATE
AS
BEGIN
	IF EXISTS (
		SELECT * FROM PeriodoMusical pm
		INNER JOIN Compositor c ON pm.codigo = c.periodo_musical
		INNER JOIN Compoe c_aux ON c.codigo = c_aux.compositor
		INNER JOIN inserted i 
			ON c_aux.album = i.album 
			AND c_aux.num_faixa = i.num_faixa 
			AND c_aux.num_disc = i.num_disc
		WHERE pm.descricao = 'Barroco' AND 
		(i.tipo_gravacao IS NULL OR i.tipo_gravacao <> 'DDD')
	)
	BEGIN
		RAISERROR('Uma faixa do período barroco só pode ser inserida caso o tipo de gravação seja DDD.',16,1)
		ROLLBACK TRANSACTION
	END
END
GO

-- b) Um álbum não pode ter mais que 64 faixas.

CREATE TRIGGER tg_album64
ON Faixa
FOR INSERT, UPDATE
AS
BEGIN
	IF EXISTS (
		SELECT i.album FROM Faixa f
		INNER JOIN inserted i
		ON f.album = i.album
		GROUP BY i.album
		HAVING count(*) > 64
	)
	BEGIN
		RAISERROR('Um álbum não pode ter mais que 64 faixas.',16,1)
		ROLLBACK TRANSACTION
	END
END 
GO

/* c) No caso de remoção de um álbum do banco de dados, todas as suas faixas
devem ser removidas. Lembre-se que faixas podem apresentar, por sua vez,
outros relacionamentos. */

-- ESSA RESTRIÇÃO JÁ É GARANTIDA PELO ON DELETE CASCADE

/* d) O preço de compra de um álbum não dever ser superior a trás vezes a média
do preço de compra de álbuns, com todas as faixas com tipo de gravação DDD. */

CREATE TRIGGER tg_precoAlbumDDD
ON Album
FOR INSERT, UPDATE
AS
BEGIN
    DECLARE @media DEC(11,2)

	-- média do preço de compra de álbuns com todas as faixas do tipo DDD
    SELECT @media = AVG(a.preco_de_compra) FROM Album a
    WHERE NOT EXISTS (
        SELECT * FROM Faixa f
        WHERE f.album = a.codigo
        AND (f.tipo_gravacao IS NULL OR f.tipo_gravacao <> 'DDD')
    )

	-- se não houver álbuns com todas as faixas DDD, não é preciso aplicar a restrição
    IF @media IS NULL
        RETURN

	-- verificando se o álbum tem preço de compra inválido
    IF EXISTS (
        SELECT * FROM inserted i
        WHERE i.preco_de_compra > 3 * @media
    )
    BEGIN
        RAISERROR (
            'O preço de compra de um álbum não dever ser superior a trás vezes a média do preçoo de compra de álbuns com todas as faixas do tipo DDD.',16, 1)
        ROLLBACK TRANSACTION
    END
END
GO

-- ======================================================================================

-- Outras restrições

/* se num_disc = 0, meio físico = vinil ou download.
Senão, num_disc = numeração do CD que contém um
subconjunto do álbum com aquela faixa (1, 2) */

CREATE TRIGGER tg_num_disc
ON Faixa
FOR INSERT, UPDATE
AS
BEGIN
	IF EXISTS (
		SELECT * FROM Album a
		INNER JOIN inserted i
		ON a.codigo = i.album
		WHERE (i.num_disc = 0 AND a.meio_fisico NOT IN ('vinil', 'download'))
		OR (i.num_disc IN (1, 2) AND a.meio_fisico <> 'CD')
	)
	BEGIN
		RAISERROR('Número do disco da faixa não casa com o meio físco do álbum',16,1)
		ROLLBACK TRANSACTION
	END
END
GO

/* Quando o meio físico de armazenamento é CD, o tipo de gravação tem que
	ser ADD ou DDD. Quando o meio físico de armazenamento é vinil ou
	download, o tipo de gravação não terá valor algum */

CREATE TRIGGER tg_meioFisico_tipoGravacao
ON Faixa
FOR INSERT, UPDATE
AS
BEGIN
	IF EXISTS (
		SELECT * FROM Album a
		INNER JOIN inserted i
		ON a.codigo = i.album
		WHERE (a.meio_fisico = 'CD' AND i.tipo_gravacao NOT IN ('ADD', 'DDD'))
		OR (a.meio_fisico IN ('vinil', 'download') AND i.tipo_gravacao IS NOT NULL)
	)
	BEGIN
		RAISERROR('Meio físico do álbum não casa com o tipo de gravação da faixa.',16,1)
		ROLLBACK TRANSACTION
	END
END
GO