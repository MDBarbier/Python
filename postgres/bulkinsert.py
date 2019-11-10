import psycopg2
import csv

#variables
dataFilePath = "C:\\Users\\matth\\Downloads\\games_list.csv"
postgresConnectionString = "dbname=gamemanager user=postgres password=spectrum host=riker"
gameDict = [] #will hold our DictReader
postgres_insert_query = ""

#Setup connection
conn = psycopg2.connect(postgresConnectionString)

#Get a cursor to interact with db connection
cur = conn.cursor()

#read the data from the csv
with open(dataFilePath, mode='r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row["Name"]}, {row["Genre"]}, {row["Category"]}')
            line_count += 1
            gameDict.append(row)

    print(f'Processed {line_count} lines.')    

print(f"There are {len(gameDict)} items in the dict")

try:
    for game in gameDict:
        postgres_insert_query = """ INSERT INTO games (name, genre, owned, category, store) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (game["Name"], game["Genre"], "true", game["Category"], game["Store"])
        cur.execute(postgres_insert_query, record_to_insert)
    
    conn.commit()

except (Exception, psycopg2.Error) as error :
    if(conn):
        print("Failed to insert record into table: ", error)

finally:
    #closing database connection.
    if(conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

