USE BDSpotPer
GO

/* Criar uma visão materializada que tem como atributos o nome da playlist 
e a quantidade de álbuns que a compõem. */
 
CREATE OR ALTER VIEW vw_AlbunsDaPlaylist
WITH SCHEMABINDING
AS
	SELECT p.codigo as codigo,
	p.nome as 'Nome da Playlist', 
	COUNT_BIG(DISTINCT f.album) as 'Quantidade de álbuns' 
	FROM dbo.Playlist p
	INNER JOIN dbo.PlaylistFaixa pf 
		ON p.codigo = pf.playlist
	INNER JOIN dbo.Faixa f 
		ON pf.album = f.album
		AND pf.num_faixa = f.num_faixa
		AND pf.num_disc = f.num_disc
	GROUP BY p.codigo, p.nome
GO

-- NÃO FUNCIONA:
	--CREATE UNIQUE CLUSTERED INDEX idxC_vw_AlbunsDaPlaylist
	--ON dbo.vw_AlbunsDaPlaylist (codigo)
	--GO
