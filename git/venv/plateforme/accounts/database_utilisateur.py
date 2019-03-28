import psycopg2


def create_database_user(username):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""CREATE TABLE aliment_de_{}
                (id serial PRIMARY KEY,
                name_aliment TEXT,
                username VARCHAR(20) not null,
                id_aliment int not null
                );""".format(username))



    conn.commit()

def insert_database_user(username):


    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""INSERT INTO aliment_de_{0}
                (username)
                VALUES('{1}');""".format(username, username))



    conn.commit()



