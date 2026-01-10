USE BDSpotPer
GO

--Defina uma função que tem como parâmetro de entrada o nome (ou parte do)
--nome do compositor e o parâmetro de saída todos os álbuns com obras
--compostas pelo compositor.

CREATE FUNCTION fun_ObrasDoCompositor (@nome VARCHAR(50))
RETURNS TABLE
AS
RETURN(
    SELECT DISTINCT a.codigo as 'Código do Álbum',
        a.descricao as 'Descrição',
        a.data_gravacao as 'Data de gravação',
        a.preco_de_compra as 'Preço',
        a.meio_fisico as 'Meio físico'
    FROM Album a
    INNER JOIN Faixa f
        ON a.codigo = f.album
    INNER JOIN Compoe ce
        ON f.album = ce.album
       AND f.num_faixa = ce.num_faixa
       AND f.num_disc = ce.num_disc
    INNER JOIN Compositor c
        ON ce.compositor = c.codigo
    WHERE c.nome LIKE '%' + @nome + '%'
)
GO