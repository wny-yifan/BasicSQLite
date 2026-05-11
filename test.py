import sqlite3

DATABASE = "cars.db"

def print_all_cars():
    speed = input("What speed: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = 'select car_name, top_speed from car where top_speed > ?;'
        cursor.execute(sql, (speed,))
        results = cursor.fetchall()
        # print them nicely
        for car in results:
            print(f"Car: {car[0]} Top speed: {car[1]}" )

# db = sqlite3.connect('cars.db')
# cursor = db.cursor()
# sql = 'SELECT * FROM car;'
# cursor.execute(sql)
# results = cursor.fetchall()
# # print them nicely
# for car in results:
#     print(f"Car: {car[1]} Top speed: {car[2]}" )


# # close the db connection
# db.close()

if __name__ == "__main__":
    print("This is the main module.")
    print_all_cars()