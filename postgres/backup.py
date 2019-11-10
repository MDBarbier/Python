import psycopg2

conn = psycopg2.connect("dbname=gamemanager user=postgres password=spectrum host=riker")

cur = conn.cursor()

cur.execute("SELECT * FROM games;")


records = cur.fetchall()

print(records)

# Make the changes to the database persistent
#conn.commit()

cur.close()
conn.close()
