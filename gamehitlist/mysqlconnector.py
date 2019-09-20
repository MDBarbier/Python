import mysql.connector
import passwords

try:
    mydb = mysql.connector.connect(
        host="den1.mysql6.gear.host",
        user="gamehitlist",
        passwd=passwords.databasePassword
    )

except:
    print("error connecting to database")

print(mydb)