import mysql.connector
import pandas as pd 
import requests
from pathlib import Path
import MySQLdb
from MySQLdb import Connection

__file__= "C:\\Users\\OOHIRO\\OneDrive - Lone Star College\\Osato U Drive\\LSC-AIR\WTAMU\\SUM_1_2021\\5310\\CIDM5310\\Final_Project\\"

mydb = mysql.connector.connect(
	host='localhost', 
	port=3306 ,
	user ='Seetos', 
	passwd = 'S!510', 
	db ='bidss'
)

mycursor = mydb.cursor()
script_location = Path(__file__).absolute().parent

response = requests.get("https://www.dallasopendata.com/resource/qv6i-rri7.csv?$where=upzdate>'2021-07-02'")
f = open(script_location/ 'crime2.txt', 'a')
f.write(response.text)
f.close()

sql =("INSERT INTO DallasCrime_2021(ServiceNumberID, ZipCode, VictimGender, VictimRace, VictimEthnicity, VictimAge, Type_location, VictimType, Division, NIBRSCrimeCategory, Month, Year, UpdateDate) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)")
val= (response.text)
mycursor.execute(sql, val)
mydb.commit()


mydb.close()

