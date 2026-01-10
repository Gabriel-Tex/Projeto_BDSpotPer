CREATE DATABASE BDSpotPer
ON PRIMARY
(
    NAME = 'BDSP_Primary',
    FILENAME = 'C:\SQLData\BDSP_Primary.mdf',
    SIZE = 50MB,
    FILEGROWTH = 10MB
),
FILEGROUP fg_BDSP
(
    NAME = 'BDSP_arq1',
    FILENAME = 'C:\SQLData\BDSP_arq1.ndf',
    SIZE = 100MB,
    MAXSIZE = 500MB,
    FILEGROWTH = 50MB
),
(
    NAME = 'BDSP_arq2',
    FILENAME = 'C:\SQLData\BDSP_arq2.ndf',
    SIZE = 100MB,
    MAXSIZE = 500MB,
    FILEGROWTH = 50MB
),
FILEGROUP fg_PlaylistFaixa
(
    NAME = 'PlaylistFaixa',
    FILENAME = 'C:\SQLData\PlaylistFaixa.ndf',
    SIZE = 100MB,
    MAXSIZE = 300MB,
    FILEGROWTH = 50MB
)
LOG ON
(
    NAME = 'BDSP_Log',
    FILENAME = 'C:\SQLData\BDSP_Log.ldf',
    SIZE = 50MB,
    FILEGROWTH = 25MB
);
