# DB CONFIG
check_table_versions_sql = '''
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='versions'
            '''
check_version_sql = '''
            SELECT version FROM versions
            WHERE id = 1
            '''
create_versions_table_sql = '''
            CREATE TABLE IF NOT EXISTS versions (
               id INTEGER PRIMARY KEY,
               version INTEGER
               )
            '''
insert_version_table_sql = '''
            INSERT OR IGNORE INTO versions (id, version)
            VALUES (1, 0)
            '''
update_version_table_sql = '''
            UPDATE versions
            SET version = ?
            WHERE id = 1
            '''
create_users_table_sql = '''
            CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               telegram_id INTEGER UNIQUE,
               name TEXT
               )
            '''
create_sayings_table_sql = '''
            CREATE TABLE IF NOT EXISTS sayings (
               id INTEGER PRIMARY KEY,
               title TEXT,
               description TEXT,
               author TEXT,
               user_id INTEGER DEFAULT 0
               )
            '''
# USERS SENTENCES
insert_user_sql = '''
            INSERT OR IGNORE INTO users (telegram_id, name)
            VALUES (?, ?)
            '''

get_user_sql = '''
            SELECT * FROM users 
            WHERE telegram_id = ?
            '''
# SAYINGS SENTENCES
insert_new_saying_sql = '''
            INSERT OR IGNORE INTO sayings (title, description, author, user_id)
            VALUES (?, ?, ?, ?)
            '''
count_sayings_sql = '''
            SELECT COUNT(*) FROM sayings
            '''
select_all_sayings_sql = '''
            SELECT * FROM sayings
            ORDER BY id ASC
            LIMIT ? OFFSET ? 
            '''
select_saying_by_id_sql = '''
            SELECT * FROM sayings
            WHERE id = ? 
            '''
delete_saying_by_id_sql = '''
            DELETE FROM sayings
            WHERE id = ? 
            '''
delete_saying_sql = '''
            INSERT OR IGNORE INTO users (telegram_id, name)
            VALUES (?, ?)
            '''
update_saying_sql = '''
            INSERT OR IGNORE INTO users (telegram_id, name)
            VALUES (?, ?)
            '''
insert_current_sayings_sql = '''
            INSERT OR IGNORE INTO sayings (id, title, description, author) 
            VALUES
               (1, "Los hijos del corazón y el marido del talon", "", ""),
               (2, "Quien quiere la flor quiere las hojas de alrededor", "", ""),
               (3, "Me casé con una tonta por hacer caso a unos familiares, ellos están en su casa y yo con la tonta siempre", "", ""),
               (4, "Cada olla tiene su cobertura", "", ""),
               (5, "Si quieres hacer duelo, muerete luego", "", ""),
               (6, "Casate niña a tu gusto que tus padres moriran y no vendrán del otro mundo a ver si estas bien o mal", "", ""),
               (7, "Cuando suena la corneta, el medico a la puñeta", "", ""),
               (8, "Con dos pedos y una bufa, la cama mas caliente que una estufa", "", ""),
               (9, "Cuando el pobre amasa se hunde el horno", "", ""),
               (10, "Cuando el rico se pone el sombrero, pontelo aunque no sepas para que es", "", ""),
               (11, "Por hacer feliz a un vecino hice cornudo a mi marido", "", ""),
               (12, "Si tienes hambre muerdete el culo y comerás carne", "", ""),
               (13, "De molinero cambiarás pero de ladron no escaparás", "", ""),
               (14, "El que de servilleta llega a mantel no te fies de él", "", ""),
               (15, "Si truena por Valdegreta agua hasta la bragueta", "", ""),
               (16, "Cuando hay hambre no hay pan duro", "", ""),
               (17, "Para San Antón pasico raton y para Santa Maria hora y media crece el dia", "", ""),
               (18, "Lo que te enseña a apizar, el parir y el criar", "", ""),
               (19, "Mira si me quiere mi suegra que cuando limpia ensalada me da las hojas de afuera", "", ""),
               (20, "En la puerta del rezador no pongas trigo al sol, y en el que no reza ni trigo ni cerveza", "", ""),
               (21, "Don Preciso ya murió. No murió, que no nació", "", ""),
               (22, "Ha durado menos que una morcilla a la puerta de una perrera ", "", ""),
               (23, "El que cierne y amasa todo le pasa", "", ""),
               (24, "El que sirve sus placeres vende", "", ""),
               (25, "El que paga y miente su bolsa lo siente", "", ""),
               (26, "El que por comer no se mata lo demas tatarata", "", ""),
               (27, "El que sabe muhco no quiere mas que aprender y el que sabe poco no quiere mas que enseñar", "", ""),
               (28, "En la boca del mentiroso lo cierto se hace dudoso", "", ""),
               (29, "Cada uno con lo suyo y dios con lo de todos", "", ""),
               (30, "Hacer y deshacer todo es quiacer", "", ""),
               (31, "Ande yo caliente riase la gente", "", ""),
               (32, "Mi mujer ha malparido, trabajo perdido", "", ""),
               (33, "Al que quiere saber, se le dice poco y al revés", "", ""),
               (34, "Si sale con barbas San Antón y si no la purisima concepción", "", ""),
               (35, "Hambre que espera a comer no es hambre", "", ""),
               (36, "Quien trille quien quiera, mio no es ni el pajar ni la hera", "", ""),
               (37, "La madre y el hijo se quedan en casa haciendo sus merendolas, al marido lo mandan al huerto con un pimiento y todo el dia contento", "", ""),
               (38, "100 hijos de un vientre, cada uno de su temple", "", ""),
               (39, "El comer y el rascar no cal mas que empezar", "", ""),
               (40, "Las del moño Macoco duermen sentadas paqel maño Macoco no se deshaga", "", ""),
               (41, "Pintas tanto como taragaña en Alcorisa, ¿Qué pintan? una mierda", "", ""),
               (42, "Miau que es gata", "", ""),
               (43, "Ni en Caspe mejores chicas", "", ""),
               (44, "Señores las once han dado, si yo estuviera en su casa como usted en la mia, señores me marcharía", "", ""),
               (45, "Buenas noches, por ahi te enroches", "", ""),
               (46, "Si esto es verdad, mis cojones son claveles", "", ""),
               (47, "Esto es un pan amasado por la gracia de Dios, si no es mas grande porque no han echado mas masa", "", ""),
               (48, "Ya viene el dorodon", "", ""),
               (49, "Si en Berge esta la culebra y en Alcorisa el gazapo, en Molinos chicas guapas pa tirarlas al barranco", "", ""),
               (50, "La suegra y la nuera son ""ansas"" de caldero mala pegadas", "", ""),
               (51, "Buen genio tengo yo para llevar la capa larga", "", ""),
               (52, "Todos son familias, menos la nuera que no era", "", ""),
               (53, "Jugar por necesidad perder por obligación", "", ""),
               (54, "Pal ayuntamiento pasico lento y pal estao sentado", "", ""),
               (55, "A las penas puñaladas y a los pesares tragos de vino", "", ""),
               (56, "El que no trabaja de pollino, despues de asno fino", "", ""),
               (57, "La semana que viene vendrán los sastres, si no vienen el lunes vendrán el martes", "", ""),
               (58, "A los 40 no hagas cuentas", "", ""),
               (59, "Como el herrero de Calatayud, corto de bienes y largo de salud", "", ""),
               (60, "Aunque reviente Teresa de Ababuj a de ser la dehesa", "", ""),
               (61, "Dos hijas y una madre la perdicion de un padre", "", ""),
               (62, "Si haces 100 y no haces una como si no hubieras hecho ninguna", "", ""),
               (63, "Vas como una refinalla", "", ""),
               (64, "¿Santa Barbara y no merendar?", "", ""),
               (65, "Gastas menos que un ciego en novelas", "", ""),
               (66, "Eso esta un poco escoscao", "", ""),
               (67, "Si quieres que un duro no te falte, el primero que tengas no lo gastes", "", ""),
               (68, "Esto es cagar y envolver", "", ""),
               (69, "El mal del taco, poco mal y mucho trago", "", ""),
               (70, "De caracol para arriba todo para casa", "", ""),
               (71, "No vales ni pa tacos de escopeta", "", ""),
               (72, "Todas las manchas se quitan con agua y jabón, todas las manchas se quitan menos las del corazón", "", ""),
               (73, "A mí me da igual, ni es el pajar ni la era", "", ""),
               (74, "Quien tiene un defecto y lo reconoce, no tiene un defecto, tiene una virtud", "", ""),
               (75, "Siempre me toca bailar con la mas fea y la pieza mas larga", "", ""),
               (76, "Morena que se viste de verde ella sola se pierde", "", ""),
               (77, "A trapuchar", "", ""),
               (78, "El que de verano viste a Navidad, no preguntes como le va", "", ""),
               (79, "El que por gusto duerme en el suelo no hay que compadecerlo", "", ""),
               (80, "Sarna a gusto no pica... aunque mortifica", "", ""),
               (81, "El que por comer no se mata por el resto... tatarata", "", ""),
               (82, "El casamiento y la mortaja del cielo baja", "", ""),
               (83, "Un padre nuestro pa los tontos", "", ""),
               (84, "Mi cabeza solo sirve para criar piojos", "", ""),
               (85, "El que gana 6 y gasta 7 no necesita bolsete", "", ""),
               (86, "Mientras haya quien te presete, cuerpo no lo pases mal, madrugas una mañana y con todos quedas igual", "", ""),
               (87, "Una mujer sin pendientes es como un parador sin fuentes", "", ""),
               (88, "Poco se gana a hilar pero menos a mirar", "", ""),
               (89, "- Chica que no has hecho nudo + Si me hubiera gustado el mulo, cien veces hubiera hecho el nudo", "", ""),
               (90, "Es mejor que digan: ""ahi va un cobarde"", que ""ahi murió un valiente""", "", ""),
               (91, "El que no guarda leña para abril no sabe vivir", "", ""),
               (92, "El que compra barato compra por cuatro", "", ""),
               (93, "El que compra barato compra por cuatro", "", ""),
               (94, "Esgarrifar", "", ""),
               (95, "En el campo las matizas tienen ojos", "", ""),
               (96, "Dejalo que llore que ya tiene el mellico atao", "", ""),
               (97, "Cuando no hay pan buenas son tortas", "", ""),
               (98, "Si nazco y nazco feo,  me caso y soy cabron, me muero y voy al infierno....bien poco le debo a Dios", "", ""),
               (99, "Va como una refinadera", "", ""),
               (100, "Lo poco enternece, lo mucho endurece. ", "", ""),
               (101, "Sacar y no meter es menguar y no crecer", "", ""),
               (102, "Aparta mierda... Queviene mi suegra", "", ""),
               (103, "El que mal te quiera en juicios te vea", "", ""),
               (104, "Hay madres, madrecicas y madrazas", "", ""),
               (105, "Una madre es una madre y a ti te encontré en la calle", "", ""),
               (106, "El casado su casa quiere", "", ""),
               (107, "Poco a poco hila a la vieja el copo", "", ""),
               (108, "Como va a serla gente........si Dios es bueno y mata a la gente", "", ""),
               (109, "El que dice lo que no debe , se siente lo que no quiere", "", ""),
               (110, "No te des en la cabeza, ni te des en el tozuelo. Chocolate hemos de hacer aunque sea en un cazuelo", "", ""),
               (111, "Viendo la garita... se ve el guardia", "", ""),
               (112, "El primero que siente la.olor....debajo tiene la flor", "", ""),
               (113, "La carne que crece no pue parar", "", ""),
               (114, "Que si si que si no...que si verdes las han segao.", "", ""),
               (115, "Pagar no me pagó, pero hablar que bien me habló", "", ""),
               (116, "No te metas en camisa de once baras.", "", ""),
               (117, "Donde se esté bien buen rato", "", ""),
               (118, "Noches alegres ....mañanas tristes", "", ""),
               (119, "Conoces a lelo mientras lo mandas hacelo", "", ""),
               (120, "Entre noche y día no hay pared", "", ""),
               (121, "Toda mi vida he andado, este quiero, este no quiero y he ido a parar al peor atascadero.", "", ""),
               (122, "Si el sol fuera jornalero...no madrugaria tanto y se iria mas ligero.", "", ""),
               (123, "O todos al tajo o todos al tocino", "", ""),
               (124, "Para vicios no quitar, vicios no dar.", "", ""),
               (125, "Has matao a quien te mataba?", "", ""),
               (126, "Si usted quiere comer algo de bueno y barato, que te pongan caracoles que estará siempre lleno el plato", "", ""),
               (127, "De padres gatos, hijos mininos", "", ""),
               (128, "Una mas y una menos", "", ""),
               (129, "O cortas caña o a España", "", ""),
               (130, "De cojon le canta el pecho", "", ""),
               (131, "¿A la cama me voy a ir? Que ahí se muere la gente", "", ""),
               (132, "El que da de comer a perro ajeno, se queda sin pan y sin perro", "", ""),
               (133, "Agua al cuello y tarquin a la rodilla", "", ""),
               (134, "La tierra que nací por madre la conocí", "", ""),
               (135, "Con perras chufletes", "", ""),
               (136, "No digas a nadie mocoso llevando nariz", "", ""),
               (137, "Dame gordura y te dare hermosura", "", ""),
               (138, "Vale más un vecino a la puerta que un familiar a la traspuerta", "", ""),
               (139, "Nos os llevais ni un pelo conejo. ", "", ""),
               (140, "Al desnudo le hacen mas bien dos que uno", "", ""),
               (141, "O todos mochos o todos cornudos", "", ""),
               (142, "Ricos de pueblo...pobres de capital.", "", ""),
               (143, "De los 40 pa arriba no te mojes la barriga", "", ""),
               (144, "A cascala putas que llueve", "", ""),
               (145, "Los hijos criaos los males doblas y casaos multiplicaos", "", ""),
               (146, "No busques al que ha sido ni al que será sino al que es", "", ""),
               (147, "Que suerte que haya críos para echarle la culpa", "", "")
            '''
