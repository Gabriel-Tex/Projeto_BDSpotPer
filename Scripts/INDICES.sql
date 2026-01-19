USE BDSpotPer
GO

/* Defina um índice primário para a tabela de Faixas sobre o 
atributo código do álbum com taxa de preenchimento máximo.  */

CREATE CLUSTERED INDEX idxC_Faixa
ON Faixa (album)
WITH (PAD_INDEX = OFF, FILLFACTOR = 100)
ON fg_PlaylistFaixa
GO

/* Defina um índice secundário para a mesma tabela sobre o atributo tipo de
composição com taxa de preenchimento máxima. */

CREATE NONCLUSTERED INDEX idxNC_Faixa1
ON Faixa (tipo_composicao)
WITH (PAD_INDEX = OFF, FILLFACTOR = 100)
ON fg_PlaylistFaixa
GO