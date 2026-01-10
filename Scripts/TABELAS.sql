USE BDSpotPer

CREATE TABLE Gravadora(
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	nome VARCHAR(50) NOT NULL,
	endereco VARCHAR(100) NOT NULL,
	home_page VARCHAR(100) NOT NULL
	
	-- constraints
	CONSTRAINT pk_gravadora
	PRIMARY KEY (codigo),

	CONSTRAINT uk_endereco
	UNIQUE (endereco),

	CONSTRAINT uk_home_page
	UNIQUE (home_page)

) ON fg_BDSP

CREATE TABLE Telefone(
	-- chave primária composta
	gravadora SMALLINT NOT NULL,
	numero VARCHAR(20) NOT NULL

	-- constraints
	CONSTRAINT pk_telefone
	PRIMARY KEY (gravadora, numero),

	CONSTRAINT fk_gravadoraTel
	FOREIGN KEY (gravadora) 
	REFERENCES Gravadora 
	ON DELETE CASCADE ON UPDATE CASCADE

) ON fg_BDSP

CREATE TABLE Album(
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	descricao VARCHAR(100),
	preco_de_compra DEC(11,2),
	data_gravacao DATE NOT NULL,
	data_compra DATE,
	meio_fisico VARCHAR(8) NOT NULL,
	-- chave estrangeira
	gravadora SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_album
	PRIMARY KEY(codigo),

	CONSTRAINT fk_gravadoraAlbum 
	FOREIGN KEY (gravadora) 
	REFERENCES Gravadora
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT ck_meio_fisico
	CHECK (meio_fisico IN ('CD', 'vinil', 'download')),

	CONSTRAINT ck_data_gravacao
	CHECK (data_gravacao > '2000-01-01')

) ON fg_BDSP

CREATE TABLE Playlist (
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	nome VARCHAR(50) NOT NULL,
	data_de_criacao DATETIME NOT NULL,
	tempo SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_playlist
	PRIMARY KEY (codigo),

	CONSTRAINT uk_tempoPL
	CHECK (tempo >= 0)

) ON fg_PlaylistFaixa

CREATE TABLE Faixa(
	-- chave primária composta
	album SMALLINT NOT NULL,
	num_faixa SMALLINT NOT NULL,
	num_disc TINYINT NOT NULL,
	-- demais atributos
	descricao VARCHAR(100),
	tempo SMALLINT NOT NULL,
	tipo_gravacao VARCHAR(3),
	tipo_composicao VARCHAR(30)

	-- constraints
	CONSTRAINT pk_faixa
	PRIMARY KEY NONCLUSTERED (album, num_faixa, num_disc),

	CONSTRAINT fk_album
	FOREIGN KEY (album) 
	REFERENCES Album
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT uk_tempoFaixa
	CHECK (tempo >= 0),

	CONSTRAINT ck_num_disc
	CHECK (num_disc IN (0, 1, 2)),

	CONSTRAINT ck_tipo_gravacao
	CHECK (tipo_gravacao IS NULL OR tipo_gravacao IN ('ADD', 'DDD'))

	-- OBS.:

	/* se num_disc = 0, meio físico = vinil ou download.
	Senão, num_disc = numeração do CD que contém um
	subconjunto do álbum com aquela faixa (1, 2) */

	/* Quando o meio físico de armazenamento é CD, o tipo de gravação tem que
	ser ADD ou DDD. Quando o meio físico de armazenamento é vinil ou
	download, o tipo de gravação não terá valor algum */

) ON fg_PlaylistFaixa

CREATE TABLE PlaylistFaixa(
	-- atributos
	ultima_vez_tocada DATETIME NOT NULL,
	quantidade_tocada SMALLINT NOT NULL,
	-- chave estrangeira
	album SMALLINT NOT NULL,
	num_faixa SMALLINT NOT NULL,
	num_disc TINYINT NOT NULL,
	playlist SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_playlistFaixa
	PRIMARY KEY (album, num_faixa, num_disc, playlist),

	CONSTRAINT fk_faixaPF
	FOREIGN KEY (album, num_faixa, num_disc) 
	REFERENCES Faixa
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT fk_playlist
	FOREIGN KEY (playlist) 
	REFERENCES Playlist
	ON DELETE CASCADE ON UPDATE CASCADE

) ON fg_PlaylistFaixa

CREATE TABLE Interprete(
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	nome VARCHAR(50) NOT NULL,
	tipo VARCHAR(20)

	-- constraints
	CONSTRAINT pk_interprete
	PRIMARY KEY (codigo)
) ON fg_BDSP

CREATE TABLE PeriodoMusical(
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	descricao VARCHAR(50) NOT NULL,
	intervaloInicio SMALLINT NOT NULL,
	intervaloFim SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_periodoMusical
	PRIMARY KEY (codigo),

	CONSTRAINT ck_intervalo
	CHECK (intervaloInicio < intervaloFim),

	CONSTRAINT ck_descricao
	CHECK (descricao in ('Idade Média',
'Renascença', 'Barroco', 'Clássico', 'Romântico', 'Moderno'))

) ON fg_BDSP

CREATE TABLE Compositor(
	-- chave primária
	codigo SMALLINT NOT NULL,
	-- demais atributos
	nome VARCHAR(50) NOT NULL,
	cidade_natal VARCHAR(30),
	pais_de_nascimento VARCHAR(30),
	data_de_nascimento DATE NOT NULL,
	data_de_falecimento DATE,
	-- chave estrangeira
	periodo_musical SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_compositor
	PRIMARY KEY (codigo),

	CONSTRAINT fk_periodo
	FOREIGN KEY (periodo_musical) 
	REFERENCES PeriodoMusical
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT ck_datas
	CHECK (data_de_falecimento IS NULL OR data_de_falecimento > data_de_nascimento)

) ON fg_BDSP

CREATE TABLE Compoe (
	-- chave primária composta
	album SMALLINT NOT NULL,
	num_faixa SMALLINT NOT NULL,
	num_disc TINYINT NOT NULL,
	compositor SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_compoe
	PRIMARY KEY (album, num_faixa, num_disc, compositor),

	CONSTRAINT fk_faixaCompoe
	FOREIGN KEY (album, num_faixa, num_disc) 
	REFERENCES Faixa
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT fk_compositor
	FOREIGN KEY (compositor) 
	REFERENCES Compositor
	ON DELETE CASCADE ON UPDATE CASCADE

) ON fg_BDSP

CREATE TABLE Interpretada(
	-- chave primária composta
	album SMALLINT NOT NULL,
	num_faixa SMALLINT NOT NULL,
	num_disc TINYINT NOT NULL,
	interprete SMALLINT NOT NULL

	-- constraints
	CONSTRAINT pk_interp
	PRIMARY KEY (album, num_faixa, num_disc, interprete),

	CONSTRAINT fk_faixaInterp
	FOREIGN KEY (album, num_faixa, num_disc) 
	REFERENCES Faixa
	ON DELETE CASCADE ON UPDATE CASCADE,

	CONSTRAINT fk_interprete
	FOREIGN KEY (interprete) 
	REFERENCES Interprete
	ON DELETE CASCADE ON UPDATE CASCADE

) ON fg_BDSP