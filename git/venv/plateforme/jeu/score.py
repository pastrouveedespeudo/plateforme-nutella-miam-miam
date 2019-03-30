import psycopg2

#a changé
def update_score(username, scoring):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""UPDATE score_de_{}
                set score = score + {};""".format(username, scoring))


    conn.commit()
    
    cur.execute("""select score from score_de_{};""".format(username))
    
    conn.commit()

    rows = cur.fetchall()
    pts = [i for i in rows]
    print("score a changé, il est maintenant de : {}".format(pts[0][0]))
    print("update_score, score.py")

    return pts[0][0]

def score(username):

    
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""select score
                from score_de_{};""".format(username))



    conn.commit()




    rows = cur.fetchall()

    score = [i for i in rows]

    print("le score du mec est de :", score)
    print("score(), score.py")
    

    return score
    



















    
