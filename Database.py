import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="scoredatabase"
)

mycursor = mydb.cursor()

mycursor.execute("create table scores(score_id int(100) primary key,highscore_name varchar (30)");




