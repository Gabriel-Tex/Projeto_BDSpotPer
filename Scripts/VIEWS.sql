USE BDSpotPer
GO

/* Criar uma vis�o materializada que tem como atributos o nome da playlist 
e a quantidade de �lbuns que a comp�em. */
 
CREATE OR ALTER VIEW vw_AlbunsDaPlaylist
WITH SCHEMABINDING
AS
	SELECT p.codigo AS codigo,
	p.nome AS 'Nome da Playlist', 
	COUNT_BIG(DISTINCT f.album) AS 'Quantidade de �lbuns' 
	FROM dbo.Playlist p
	INNER JOIN dbo.PlaylistFaixa pf 
		ON p.codigo = pf.playlist
	INNER JOIN dbo.Faixa f 
		ON pf.album = f.album
		AND pf.num_faixa = f.num_faixa
		AND pf.num_disc = f.num_disc
	GROUP BY p.codigo, p.nome
GO

-- N�O FUNCIONA:
	--CREATE UNIQUE CLUSTERED INDEX idxC_vw_AlbunsDaPlaylist
	--ON dbo.vw_AlbunsDaPlaylist (codigo)
	--GO
