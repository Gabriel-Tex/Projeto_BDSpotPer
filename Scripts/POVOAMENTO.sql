INSERT INTO PeriodoMusical VALUES
(1, 'Idade Média', 500, 1400),
(2, 'Renascença', 1400, 1600),
(3, 'Barroco', 1600, 1750),
(4, 'Clássico', 1750, 1820),
(5, 'Romântico', 1820, 1910),
(6, 'Moderno', 1910, 2025);

INSERT INTO Compositor VALUES
(1, 'Bach', 'Eisenach', 'Alemanha', '1685-03-31', '1750-07-28', 3),
(2, 'Vivaldi', 'Veneza', 'Itália', '1678-03-04', '1741-07-28', 3),
(3, 'Mozart', 'Salzburgo', 'Áustria', '1756-01-27', '1791-12-05', 4),
(4, 'Beethoven', 'Bonn', 'Alemanha', '1770-12-17', '1827-03-26', 5),
(5, 'Dvorack', 'Nelahozeves', 'República Tcheca', '1841-09-08', '1904-05-01', 5);

INSERT INTO Gravadora VALUES
(1, 'Deutsche Grammophon', 'Berlim, Alemanha', 'www.dg.com'),
(2, 'Sony Classical', 'Nova York, EUA', 'www.sonyclassical.com'),
(3, 'EMI Classics', 'Londres, Reino Unido', 'www.emiclassics.com'),
(4, 'Naxos', 'Hong Kong, China', 'www.naxos.com'),
(5, 'Philips Classics', 'Amsterdã, Holanda', 'www.philipsclassics.com');

INSERT INTO Telefone VALUES
(1, '1111-1111'),
(2, '2222-2222'),
(3, '3333-3333'),
(4, '4444-4444'),
(5, '5555-5555');

INSERT INTO Album VALUES
(1, 'Obras de Bach', 50.00, '2005-01-01', '2005-06-01', 'CD', 1),
(2, 'Concertos de Vivaldi', 45.00, '2006-01-01', '2006-06-01', 'CD', 4),
(3, 'Sinfonias de Mozart', 60.00, '2010-01-01', '2010-06-01', 'CD', 2),
(4, 'Sonatas de Beethoven', 70.00, '2015-01-01', '2015-06-01', 'CD', 3),
(5, 'Sinfonia Novo Mundo', 80.00, '2018-01-01', '2018-06-01', 'CD', 5);

INSERT INTO Faixa VALUES
(1, 1, 1, 'Fuga em Ré menor', 300, 'DDD', 'Concerto'),
(1, 2, 1, 'Prelúdio em Dó maior', 280, 'DDD', 'Concerto'),
(2, 1, 1, 'Primavera', 320, 'DDD', 'Concerto'),
(3, 1, 1, 'Sinfonia 40', 420, 'ADD', 'Sinfonia'),
(5, 1, 1, 'Novo Mundo', 480, 'ADD', 'Sinfonia');

INSERT INTO Compoe VALUES
(1, 1, 1, 1),
(1, 2, 1, 1),
(2, 1, 1, 2),
(3, 1, 1, 3),
(5, 1, 1, 5);

INSERT INTO Interprete VALUES
(1, 'Berlin Philharmonic', 'Orquestra'),
(2, 'London Symphony', 'Orquestra'),
(3, 'New York Philharmonic', 'Orquestra'),
(4, 'Vienna Philharmonic', 'Orquestra'),
(5, 'Royal Concertgebouw', 'Orquestra');

INSERT INTO Interpretada VALUES
(1, 1, 1, 1),
(1, 2, 1, 1),
(2, 1, 1, 2),
(3, 1, 1, 4),
(5, 1, 1, 5);

INSERT INTO Playlist VALUES
(2, 'Barroco Puro', GETDATE(), 0),
(3, 'Clássicos Eternos', GETDATE(), 0),
(4, 'Românticos', GETDATE(), 0),
(5, 'Favoritas', GETDATE(), 0),
(6, 'Concerto Barroco', GETDATE(), 0),
(9, 'Removível', GETDATE(), 0);

INSERT INTO PlaylistFaixa VALUES
(GETDATE(), 0, 1, 1, 1, 2),
(GETDATE(), 0, 1, 2, 1, 2),
(GETDATE(), 0, 2, 1, 1, 6),
(GETDATE(), 0, 3, 1, 1, 3),
(GETDATE(), 0, 5, 1, 1, 5);



