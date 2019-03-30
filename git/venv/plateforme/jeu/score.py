import psycopg2


def update_score(username, scoring):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""UPDATE score_de_{}
                set score = + {};""".format(username, scoring))



    conn.commit()

