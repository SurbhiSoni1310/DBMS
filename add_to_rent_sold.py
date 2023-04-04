import mysql.connector
import random
from names import name

# Connect to MySQL database
connection = mysql.connector.connect(host="localhost", database="big_alley", user="root", password="kuku")

# Create a cursor object to execute queries
my_cursor = connection.cursor()


def main():
    try:
        avail = "select house_no, street, agent_id, status, year_of_avail from available order by house_no"
        my_cursor.execute(avail)
        result = my_cursor.fetchall()
        count = 0
        count2 = 25
        for row in result:
            if count < 25:
                agent = row[2]
                house = row[0]
                street = row[1]
                sta = row[3]
                params = (house, street, agent)
                if sta == 'sale':
                    sql = 'UPDATE available set status = "sold" where house_no = %s and street = %s and agent_id = %s'
                    my_cursor.execute(sql, params)
                    sql = "update sold set year_of_sale = %s where house_no = %s and street = %s and agent_id = %s"
                    sale_ = random.randint(1990, 2023)
                    while sale_ < row[4]:
                        sale_ = random.randint(1990, 2023)
                    params = (sale_, house, street, agent)
                    my_cursor.execute(sql, params)
                    count += 1
            if count2 < 55 and count >= 5:
                agent = row[2]
                house = row[0]
                street = row[1]
                sta = row[3]
                params = (house, street, agent)
                if sta == "rent":
                    sql = "UPDATE available set status = 'rented' where house_no = %s and street = %s and agent_id = %s"
                    my_cursor.execute(sql, params)
                    sql = "update rent set year_of_rent = %s, rented_to = %s where house_no = %s and street = %s " \
                          "and agent_id = %s"
                    rent = random.randint(1990, 2023)
                    while rent < row[4]:
                        rent = random.randint(1990, 2023)
                    rented = random.choice(name)
                    params = (rent, rented, house, street, agent)
                    my_cursor.execute(sql, params)
                    count2 += 1

        connection.commit()
        my_cursor.close()
        connection.close()

    except Exception as e:
        # Actions to take if an exception occurs
        print(f"An exception occurred: {e}")


if __name__ == '__main__':
    main()

