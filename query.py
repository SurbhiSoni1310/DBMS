import mysql.connector
from prettytable import PrettyTable

# Connect to MySQL database
connection = mysql.connector.connect(host="localhost", database="big_alley", user="root", password="kuku")

# Create a cursor object to execute queries
my_cursor = connection.cursor()


def print_table(result):
    columns = [desc[0] for desc in my_cursor.description]
    table = PrettyTable(columns)
    for row in result:
        table.add_row(list(row))
    print(table)


def main():
    try:
        # query 1
        print("List the houses in your city (for example Guwahati) that are built later than 2020 and are available "
              "for rent.")
        q1 = "select house_no, street, year_of_avail, status from available where year_of_avail > 2020 and status = " \
             "'rent'"
        my_cursor.execute(q1)
        result = my_cursor.fetchall()
        print_table(result)
        # query 2
        print("Find the addresses of the houses in your city costing between Rs.30,00,000 and Rs. 50,00,000")
        q2 = "select house_no, street, landmark, pincode, city, price from available natural join house where price " \
             "between " \
             "3000000 and 5000000 and status = 'sale'"
        my_cursor.execute(q2)
        result = my_cursor.fetchall()
        print_table(result)
        # query 3
        print("Find the addresses of the houses for rent in G.S.Road (you can use the name of another locality if "
              "your city is different) with at least 2 bedrooms and costing less than Rs.15,000 per month.")
        q3 = "select house_no, street, landmark, pincode, city, status, bhk, price from house natural join available " \
             "where status = 'rent' and price < 15000 and bhk >= 2 and landmark = 'Malviya Nagar Metro Station'"
        my_cursor.execute(q3)
        result = my_cursor.fetchall()
        print_table(result)
        # query 4
        print("Find the name of the agent who has sold the most property in the year 2023 by total amount in rupees.")
        # run this in cmd
        # create view sold_sum_2023 as select agent_id, sum(price) as sum_price from sold natural join available where
        # year_of_sale=2023 group by agent_id;
        q4 = "select agent_id as id, (select name from agent where agent_id = id) as name from sold_sum_2023 where " \
             "sum_price = (select max(sum_price) from sold_sum_2023)"
        my_cursor.execute(q4)
        result = my_cursor.fetchall()
        print_table(result)

        print("For each agent, compute the average selling price of properties sold in 2018, and the average time the "
              "property was on the market. Note that this suggests use of date attributes in your design.")
        q = "select agent_id as id, (select name from agent where agent_id = id) as name, avg(price) from sold " \
            "natural join available where year_of_sale = 2018 group by agent_id;"
        my_cursor.execute(q)
        result = my_cursor.fetchall()
        print_table(result)

        print("List the details of the most expensive houses and the houses with the highest rent, in the database.")
        q = "select house_no, street,landmark, city, pincode ,price from available natural join rent natural join " \
            "house where price = (select max(price) from available natural join rent)"
        my_cursor.execute(q)
        result = my_cursor.fetchall()
        print_table(result)

        print("Most expensive house for sale")
        q = "select house_no, street,landmark, city, pincode ,price from available natural join sold natural join " \
            "house where price = (select max(price) from available natural join sold)"
        my_cursor.execute(q)
        result = my_cursor.fetchall()
        print_table(result)

        connection.commit()
        my_cursor.close()
        connection.close()

    except Exception as e:
        print(f"An exception occurred: {e}")


if __name__ == '__main__':
    main()
