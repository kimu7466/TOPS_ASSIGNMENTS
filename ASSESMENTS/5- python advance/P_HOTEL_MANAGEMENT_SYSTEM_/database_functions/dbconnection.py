import mysql.connector

def create_database():
    # print("func test")
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    my_cursor = con.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management_cwk")
    con.commit()
    con.close()

def create_cust_table():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hotel_management_cwk"
    )
    my_cursor = con.cursor()
    my_cursor.execute("""
                            CREATE TABLE IF NOT EXISTS customer_table(
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            ref VARCHAR(255) UNIQUE,
                            name VARCHAR(255),
                            mothers_name VARCHAR(255),
                            gender VARCHAR(255),
                            postal_code VARCHAR(255),
                            mobile VARCHAR(255),
                            email VARCHAR(255),
                            nationality VARCHAR(255),
                            id_proof VARCHAR(255),
                            id_number VARCHAR(255),
                            address VARCHAR(255)
                                                )
                                                """)
    con.commit()
    con.close()

def create_table_room():
    conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
    my_cursor = conn.cursor()
    query=("""  
                CREATE TABLE IF NOT EXISTS room_table (
                contact VARCHAR(45) NOT NULL,
                check_in VARCHAR(45) NULL,
                check_out VARCHAR(45) NULL,
                roomtype VARCHAR(45) NULL,
                room_number VARCHAR(45) NOT NULL,
                no_of_days VARCHAR(45) NULL,
                PRIMARY KEY (room_number, contact));
                                                        """)
    my_cursor.execute(query)
    conn.commit()
    conn.close()

def create_add_rooms():
    conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
    my_cursor = conn.cursor()
    query=("""  
                CREATE TABLE IF NOT EXISTS add_room(
                Floor VARCHAR(45) NOT NULL,
                RoomNo VARCHAR(45) UNIQUE NOT NULL,
                RoomType VARCHAR(45) NOT NULL,
                PRIMARY KEY ( RoomNo ));
                                                """)
    my_cursor.execute(query)
    conn.commit()
    conn.close()

