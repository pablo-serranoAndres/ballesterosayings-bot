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
               user_id INTEGER UNIQUE,
               username TEXT,
               menu_status TEXT,
               offset INTEGER DEFAULT 0, 
               page_limit INTEGER DEFAULT 10,
               lang TEXT DEFAULT 'es',
               autorized BOOLEAN DEFAULT FALSE
               )
            '''
create_sayings_table_sql = '''
            CREATE TABLE IF NOT EXISTS sayings (
               id INTEGER AUTO_INCREMENT PRIMARY KEY,
               title TEXT,
               description TEXT,
               author TEXT,
               user_id INTEGER DEFAULT 0
               )
            '''
# USERS SENTENCES
insert_user_sql = '''
            INSERT OR IGNORE INTO users (user_id, username, menu_status, offset, page_limit, lang)
            VALUES (?, ?, ?, ?, ?, ?)
            '''

get_user_by_id_sql = '''
            SELECT * FROM users 
            WHERE user_id = ?
            '''
get_all_users_sql = '''
            SELECT * FROM users 
            '''

get_all_sayings_by_users_sql = '''
            SELECT * FROM sayings
            WHERE user_id = ? 
            '''

update_lang_config_sql = '''
            UPDATE users
            SET lang = ?
            WHERE user_id = ?
            '''
update_autorized_sql = '''
            UPDATE users
            SET autorized = ?
            WHERE user_id = ?
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
select_last_insert_saying_sql = '''
            SELECT * FROM sayings
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT 1 
            '''

delete_saying_by_id_sql = '''
            DELETE FROM sayings
            WHERE id = ? 
            '''
update_saying_by_id_sql = '''
            UPDATE sayings
            SET title = ?, description = ?, author = ?
            WHERE id = ?
            '''
insert_current_sayings_sql = '''
            INSERT OR IGNORE INTO sayings (id, title, description, author, user_id) 
            VALUES
               (1, "Los hijos del corazón y el marido del talon", "", "", "8564800397"),
               (2, "Quien quiere la flor quiere las hojas de alrededor", "", "", "8564800397"),
               (3, "Me casé con una tonta por hacer caso a unos familiares, ellos están en su casa y yo con la tonta siempre", "", "", "8564800397"),
               (4, "Cada olla tiene su cobertura", "", "", "8564800397"),
               (5, "Si quieres hacer duelo, muerete luego", "", "", "8564800397"),
               (6, "Casate niña a tu gusto que tus padres moriran y no vendrán del otro mundo a ver si estas bien o mal", "", "", "8564800397"),
               (7, "Cuando suena la corneta, el medico a la puñeta", "", "", "8564800397"),
               (8, "Con dos pedos y una bufa, la cama mas caliente que una estufa", "", "", "8564800397"),
               (9, "Cuando el pobre amasa se hunde el horno", "", "", "8564800397"),
               (10, "Cuando el rico se pone el sombrero, pontelo aunque no sepas para que es", "", "", "8564800397"),
               (11, "Por hacer feliz a un vecino hice cornudo a mi marido", "", "", "8564800397"),
               (12, "Si tienes hambre muerdete el culo y comerás carne", "", "", "8564800397"),
               (13, "De molinero cambiarás pero de ladron no escaparás", "", "", "8564800397"),
               (14, "El que de servilleta llega a mantel no te fies de él", "", "", "8564800397"),
               (15, "Si truena por Valdegreta agua hasta la bragueta", "", "", "8564800397"),
               (16, "Cuando hay hambre no hay pan duro", "", "", "8564800397"),
               (17, "Para San Antón pasico raton y para Santa Maria hora y media crece el dia", "", "", "8564800397"),
               (18, "Lo que te enseña a apizar, el parir y el criar", "", "", "8564800397"),
               (19, "Mira si me quiere mi suegra que cuando limpia ensalada me da las hojas de afuera", "", "", "8564800397"),
               (20, "En la puerta del rezador no pongas trigo al sol, y en el que no reza ni trigo ni cerveza", "", "", "8564800397"),
               (21, "Don Preciso ya murió. No murió, que no nació", "", "", "8564800397"),
               (22, "Ha durado menos que una morcilla a la puerta de una perrera ", "", "", "8564800397"),
               (23, "El que cierne y amasa todo le pasa", "", "", "8564800397"),
               (24, "El que sirve sus placeres vende", "", "", "8564800397"),
               (25, "El que paga y miente su bolsa lo siente", "", "", "8564800397"),
               (26, "El que por comer no se mata lo demas tatarata", "", "", "8564800397"),
               (27, "El que sabe muhco no quiere mas que aprender y el que sabe poco no quiere mas que enseñar", "", "", "8564800397"),
               (28, "En la boca del mentiroso lo cierto se hace dudoso", "", "", "8564800397"),
               (29, "Cada uno con lo suyo y dios con lo de todos", "", "", "8564800397"),
               (30, "Hacer y deshacer todo es quiacer", "", "", "8564800397"),
               (31, "Ande yo caliente riase la gente", "", "", "8564800397"),
               (32, "Mi mujer ha malparido, trabajo perdido", "", "", "8564800397"),
               (33, "Al que quiere saber, se le dice poco y al revés", "", "", "8564800397"),
               (34, "Si sale con barbas San Antón y si no la purisima concepción", "", "", "8564800397"),
               (35, "Hambre que espera a comer no es hambre", "", "", "8564800397"),
               (36, "Quien trille quien quiera, mio no es ni el pajar ni la hera", "", "", "8564800397"),
               (37, "La madre y el hijo se quedan en casa haciendo sus merendolas, al marido lo mandan al huerto con un pimiento y todo el dia contento", "", "", "8564800397"),
               (38, "100 hijos de un vientre, cada uno de su temple", "", "", "8564800397"),
               (39, "El comer y el rascar no cal mas que empezar", "", "", "8564800397"),
               (40, "Las del moño Macoco duermen sentadas paqel maño Macoco no se deshaga", "", "", "8564800397"),
               (41, "Pintas tanto como taragaña en Alcorisa, ¿Qué pintan? una mierda", "", "", "8564800397"),
               (42, "Miau que es gata", "", "", "8564800397"),
               (43, "Ni en Caspe mejores chicas", "", "", "8564800397"),
               (44, "Señores las once han dado, si yo estuviera en su casa como usted en la mia, señores me marcharía", "", "", "8564800397"),
               (45, "Buenas noches, por ahi te enroches", "", "", "8564800397"),
               (46, "Si esto es verdad, mis cojones son claveles", "", "", "8564800397"),
               (47, "Esto es un pan amasado por la gracia de Dios, si no es mas grande porque no han echado mas masa", "", "", "8564800397"),
               (48, "Ya viene el dorodon", "", "", "8564800397"),
               (49, "Si en Berge esta la culebra y en Alcorisa el gazapo, en Molinos chicas guapas pa tirarlas al barranco", "", "", "8564800397"),
               (50, "La suegra y la nuera son ""ansas"" de caldero mala pegadas", "", "", "8564800397"),
               (51, "Buen genio tengo yo para llevar la capa larga", "", "", "8564800397"),
               (52, "Todos son familias, menos la nuera que no era", "", "", "8564800397"),
               (53, "Jugar por necesidad perder por obligación", "", "", "8564800397"),
               (54, "Pal ayuntamiento pasico lento y pal estao sentado", "", "", "8564800397"),
               (55, "A las penas puñaladas y a los pesares tragos de vino", "", "", "8564800397"),
               (56, "El que no trabaja de pollino, despues de asno fino", "", "", "8564800397"),
               (57, "La semana que viene vendrán los sastres, si no vienen el lunes vendrán el martes", "", "", "8564800397"),
               (58, "A los 40 no hagas cuentas", "", "", "8564800397"),
               (59, "Como el herrero de Calatayud, corto de bienes y largo de salud", "", "", "8564800397"),
               (60, "Aunque reviente Teresa de Ababuj a de ser la dehesa", "", "", "8564800397"),
               (61, "Dos hijas y una madre la perdicion de un padre", "", "", "8564800397"),
               (62, "Si haces 100 y no haces una como si no hubieras hecho ninguna", "", "", "8564800397"),
               (63, "Vas como una refinalla", "", "", "8564800397"),
               (64, "¿Santa Barbara y no merendar?", "", "", "8564800397"),
               (65, "Gastas menos que un ciego en novelas", "", "", "8564800397"),
               (66, "Eso esta un poco escoscao", "", "", "8564800397"),
               (67, "Si quieres que un duro no te falte, el primero que tengas no lo gastes", "", "", "8564800397"),
               (68, "Esto es cagar y envolver", "", "", "8564800397"),
               (69, "El mal del taco, poco mal y mucho trago", "", "", "8564800397"),
               (70, "De caracol para arriba todo para casa", "", "", "8564800397"),
               (71, "No vales ni pa tacos de escopeta", "", "", "8564800397"),
               (72, "Todas las manchas se quitan con agua y jabón, todas las manchas se quitan menos las del corazón", "", "", "8564800397"),
               (73, "A mí me da igual, ni es el pajar ni la era", "", "", "8564800397"),
               (74, "Quien tiene un defecto y lo reconoce, no tiene un defecto, tiene una virtud", "", "", "8564800397"),
               (75, "Siempre me toca bailar con la mas fea y la pieza mas larga", "", "", "8564800397"),
               (76, "Morena que se viste de verde ella sola se pierde", "", "", "8564800397"),
               (77, "A trapuchar", "", "", "8564800397"),
               (78, "El que de verano viste a Navidad, no preguntes como le va", "", "", "8564800397"),
               (79, "El que por gusto duerme en el suelo no hay que compadecerlo", "", "", "8564800397"),
               (80, "Sarna a gusto no pica... aunque mortifica", "", "", "8564800397"),
               (81, "El que por comer no se mata por el resto... tatarata", "", "", "8564800397"),
               (82, "El casamiento y la mortaja del cielo baja", "", "", "8564800397"),
               (83, "Un padre nuestro pa los tontos", "", "", "8564800397"),
               (84, "Mi cabeza solo sirve para criar piojos", "", "", "8564800397"),
               (85, "El que gana 6 y gasta 7 no necesita bolsete", "", "", "8564800397"),
               (86, "Mientras haya quien te presete, cuerpo no lo pases mal, madrugas una mañana y con todos quedas igual", "", "", "8564800397"),
               (87, "Una mujer sin pendientes es como un parador sin fuentes", "", "", "8564800397"),
               (88, "Poco se gana a hilar pero menos a mirar", "", "", "8564800397"),
               (89, "- Chica que no has hecho nudo + Si me hubiera gustado el mulo, cien veces hubiera hecho el nudo", "", "", "8564800397"),
               (90, "Es mejor que digan: ""ahi va un cobarde"", que ""ahi murió un valiente""", "", "", "8564800397"),
               (91, "El que no guarda leña para abril no sabe vivir", "", "", "8564800397"),
               (92, "El que compra barato compra por cuatro", "", "", "8564800397"),
               (93, "El que compra barato compra por cuatro", "", "", "8564800397"),
               (94, "Esgarrifar", "", "", "8564800397"),
               (95, "En el campo las matizas tienen ojos", "", "", "8564800397"),
               (96, "Dejalo que llore que ya tiene el mellico atao", "", "", "8564800397"),
               (97, "Cuando no hay pan buenas son tortas", "", "", "8564800397"),
               (98, "Si nazco y nazco feo,  me caso y soy cabron, me muero y voy al infierno....bien poco le debo a Dios", "", "", "8564800397"),
               (99, "Va como una refinadera", "", "", "8564800397"),
               (100, "Lo poco enternece, lo mucho endurece. ", "", "", "8564800397"),
               (101, "Sacar y no meter es menguar y no crecer", "", "", "8564800397"),
               (102, "Aparta mierda... Queviene mi suegra", "", "", "8564800397"),
               (103, "El que mal te quiera en juicios te vea", "", "", "8564800397"),
               (104, "Hay madres, madrecicas y madrazas", "", "", "8564800397"),
               (105, "Una madre es una madre y a ti te encontré en la calle", "", "", "8564800397"),
               (106, "El casado su casa quiere", "", "", "8564800397"),
               (107, "Poco a poco hila a la vieja el copo", "", "", "8564800397"),
               (108, "Como va a serla gente........si Dios es bueno y mata a la gente", "", "", "8564800397"),
               (109, "El que dice lo que no debe , se siente lo que no quiere", "", "", "8564800397"),
               (110, "No te des en la cabeza, ni te des en el tozuelo. Chocolate hemos de hacer aunque sea en un cazuelo", "", "", "8564800397"),
               (111, "Viendo la garita... se ve el guardia", "", "", "8564800397"),
               (112, "El primero que siente la.olor....debajo tiene la flor", "", "", "8564800397"),
               (113, "La carne que crece no pue parar", "", "", "8564800397"),
               (114, "Que si si que si no...que si verdes las han segao.", "", "", "8564800397"),
               (115, "Pagar no me pagó, pero hablar que bien me habló", "", "", "8564800397"),
               (116, "No te metas en camisa de once baras.", "", "", "8564800397"),
               (117, "Donde se esté bien buen rato", "", "", "8564800397"),
               (118, "Noches alegres ....mañanas tristes", "", "", "8564800397"),
               (119, "Conoces a lelo mientras lo mandas hacelo", "", "", "8564800397"),
               (120, "Entre noche y día no hay pared", "", "", "8564800397"),
               (121, "Toda mi vida he andado, este quiero, este no quiero y he ido a parar al peor atascadero.", "", "", "8564800397"),
               (122, "Si el sol fuera jornalero...no madrugaria tanto y se iria mas ligero.", "", "", "8564800397"),
               (123, "O todos al tajo o todos al tocino", "", "", "8564800397"),
               (124, "Para vicios no quitar, vicios no dar.", "", "", "8564800397"),
               (125, "Has matao a quien te mataba?", "", "", "8564800397"),
               (126, "Si usted quiere comer algo de bueno y barato, que te pongan caracoles que estará siempre lleno el plato", "", "", "8564800397"),
               (127, "De padres gatos, hijos mininos", "", "", "8564800397"),
               (128, "Una mas y una menos", "", "", "8564800397"),
               (129, "O cortas caña o a España", "", "", "8564800397"),
               (130, "De cojon le canta el pecho", "", "", "8564800397"),
               (131, "¿A la cama me voy a ir? Que ahí se muere la gente", "", "", "8564800397"),
               (132, "El que da de comer a perro ajeno, se queda sin pan y sin perro", "", "", "8564800397"),
               (133, "Agua al cuello y tarquin a la rodilla", "", "", "8564800397"),
               (134, "La tierra que nací por madre la conocí", "", "", "8564800397"),
               (135, "Con perras chufletes", "", "", "8564800397"),
               (136, "No digas a nadie mocoso llevando nariz", "", "", "8564800397"),
               (137, "Dame gordura y te dare hermosura", "", "", "8564800397"),
               (138, "Vale más un vecino a la puerta que un familiar a la traspuerta", "", "", "8564800397"),
               (139, "Nos os llevais ni un pelo conejo. ", "", "", "8564800397"),
               (140, "Al desnudo le hacen mas bien dos que uno", "", "", "8564800397"),
               (141, "O todos mochos o todos cornudos", "", "", "8564800397"),
               (142, "Ricos de pueblo...pobres de capital.", "", "", "8564800397"),
               (143, "De los 40 pa arriba no te mojes la barriga", "", "", "8564800397"),
               (144, "A cascala putas que llueve", "", "", "8564800397"),
               (145, "Los hijos criaos los males doblas y casaos multiplicaos", "", "", "8564800397"),
               (146, "No busques al que ha sido ni al que será sino al que es", "", "", "8564800397"),
               (147, "Que suerte que haya críos para echarle la culpa", "", "", "8564800397"),
               (148, "Más vale tarde que nunca", "", "", "6377687868"),
               (149, "El que mucho abarca, poco aprieta", "", "", "6377687868"),
               (150, "No hay mal que por bien no venga", "", "", "6377687868"),
               (151, "A quien madruga, Dios le ayuda", "", "", "6377687868"),
               (152, "En casa de herrero, cuchillo de palo", "", "", "6377687868"),
               (153, "Más sabe el diablo por viejo que por diablo", "", "", "6377687868"),
               (154, "El hábito no hace al monje", "", "", "6377687868"),
               (155, "Cría cuervos y te sacarán los ojos", "", "", "6377687868"),
               (156, "Ojos que no ven, corazón que no siente", "", "", "6377687868"),
               (157, "Al mal tiempo, buena cara", "", "", "6377687868")

            '''
