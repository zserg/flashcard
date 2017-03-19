import psycopg2
from config.settings.local import DATABASES

# class Flashcard(models.Model):
#     owner = models.ForeignKey(User,on_delete=models.CASCADE)
#     deck = models.ForeignKey(Deck)
#     question = models.TextField()
#     answer = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_shown_at = models.DateTimeField(auto_now_add=True)
#     next_due_date = models.DateTimeField(auto_now_add=True)
#     easiness = models.FloatField(default=2.5)
#     consec_correct_answers = models.IntegerField(default=0)

sql_deck ="""
INSERT INTO api_deck(name, description, owner_id) VALUES('%s', '%s', '%s');
"""
sql_card ="""
INSERT INTO api_flashcard(question, answer, created_at,
last_shown_at, next_due_date, easiness,
consec_correct_answers,owner_id, deck_id)
VALUES('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s');
"""

# cur.execute("select id from auth_user where username='test_user';")


try:
    #import ipdb; ipdb.set_trace()
    conn = psycopg2.connect("dbname='%s' user='%s' port='%s' password='%s'"%(DATABASES['default']['NAME'],
                             DATABASES['default']['USER'],
                             DATABASES['default']['PORT'],
                             DATABASES['default']['PASSWORD']))

    cur = conn.cursor()
    cur.execute("select id from auth_user where username='test_user';")
    data = cur.fetchone()
    if data:
        user_id = data[0]
        print("User 'test_user' is found (id=%s)"%user_id)

        #Create decks
        cur.execute(sql_deck % ('Deck1', 'deck1 description',user_id))
        cur.execute(sql_deck % ('Deck2', 'deck2 description',user_id))

        # for i in range(5):
        #     cur.execute(sql_card % (

        conn.commit()
        cur.close()

    else:
        print("User 'test_user' isn't found")

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
