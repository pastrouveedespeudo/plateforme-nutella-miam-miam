import psycopg2

def create_data_score_user(username):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""CREATE TABLE score_de_{}
                (id serial PRIMARY KEY,
                score int not null,
                username VARCHAR(20) not null
                );""".format(username))



    conn.commit()


def insert_data_score_user(username):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""INSERT INTO score_de_{}
                (score, username)
                value(0, '{}'
                );""".format(username, username))



    conn.commit()
