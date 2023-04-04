import json
import mysql.connector


# Load JSON data from file
with open('addresses.json', 'r') as f:
   data = json.load(f)


# Connect to MySQL database
connection=mysql.connector.connect(host="localhost",database="big_alley",user="root",password="kuku")


# Create a cursor object to execute queries
mycursor = connection.cursor()

count = 1
# Iterate over the data and insert into MySQL table
for item in data:
    if count <= 75:
       sql = "INSERT INTO available (house_no,street,agent_id,status,price,year_of_avail) VALUES (%s, %s, %s,%s,%s,%s)"
       mycursor.execute(sql, (item['House Number'],item['Street'],item['Agent'],item['status'],item['price'],item['Year_of_Avail']))
    count +=1




# Commit changes to the database
connection.commit()


# Close the cursor and database connection
mycursor.close()
connection.close()


