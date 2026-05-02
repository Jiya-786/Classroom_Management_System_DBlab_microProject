import mysql.connector
from datetime import datetime

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    conn.autocommit = False
    return conn


# -------------------------------
# INITIALIZE DATABASE + TABLES
# -------------------------------
def initialize_database(cursor):
    # Ensure database exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS classroom_db;")
    
    cursor.execute("USE classroom_db;")

    print("Connected to Jiya's Classroom Management System.")

    # DEBUG: show tables immediately
    cursor.execute("SHOW TABLES;")
    print("DEBUG Tables after creation:", cursor.fetchall())


# -------------------------------
# UTIL FUNCTIONS
# -------------------------------
def get_all_tables(cursor):
    cursor.execute("SHOW TABLES;")
    return [table[0] for table in cursor.fetchall()]


def get_table_columns(cursor, table_name):
    cursor.execute(f"DESCRIBE {table_name};")
    return cursor.fetchall()


# -------------------------------
# CRUD OPERATIONS
# -------------------------------
def create_record(cursor, table_name, columns):
    values = []
    insert_cols = []

    for col in columns:
        field, dtype, is_nullable, key, default, extra = col

        if "auto_increment" in extra.lower():
            continue

        user_input = input(f"Enter value for {field} ({dtype}): ")
        insert_cols.append(field)

        if user_input == "" and is_nullable == "YES":
            values.append("NULL")
        elif "char" in dtype or "text" in dtype:
            values.append(f"'{user_input}'")
        elif "date" in dtype:
            date_value = datetime.strptime(user_input, "%Y-%m-%d")
            values.append(f"'{date_value.strftime('%Y-%m-%d')}'")
        else:
            values.append(user_input)

    query = f"INSERT INTO {table_name} ({', '.join(insert_cols)}) VALUES ({', '.join(values)});"
    cursor.execute(query)
    print("Record inserted successfully.")


def retrieve_records(cursor, table_name):
    condition = input("Enter WHERE condition (or press enter to fetch all): ")
    query = f"SELECT * FROM {table_name}"

    if condition.strip():
        query += f" WHERE {condition}"

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("No records found.")
    else:
        for row in rows:
            print(row)


def update_record(cursor, table_name):
    set_clause = input("Enter SET clause (e.g., name='John', age=30): ")
    condition = input("Enter WHERE clause (e.g., id=2): ")

    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition};"
    cursor.execute(query)
    print("Record(s) updated successfully.")


def delete_record(cursor, table_name):
    condition = input("Enter WHERE clause for deletion (e.g., id=2): ")

    query = f"DELETE FROM {table_name} WHERE {condition};"
    cursor.execute(query)
    print("Record(s) deleted successfully.")
    
def get_student_dashboard(cursor):
    query = """
    SELECT U.name, S.major, S.GPA, S.enrollmentDate
    FROM Users U
    JOIN Students S ON U.userID = S.studentID;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n--- Official Student Dashboard ---")
    for row in results:
        print(f"Name: {row[0]} | Major: {row[1]} | GPA: {row[2]} | Joined: {row[3]}")
        
def get_course_stats(cursor):
    query = """
    SELECT C.title, COUNT(E.studentID) AS TotalStudents
    FROM Courses C
    LEFT JOIN Enrollments E ON C.courseID = E.courseID
    GROUP BY C.title;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n--- Course Enrollment Statistics ---")
    for row in results:
        print(f"Course: {row[0]} | Total Enrolled: {row[1]}")
        
def check_hardware_inventory(cursor):
    query = """
    SELECT SB.brand, SB.serialNo, C.roomID, C.floor
    FROM SmartBoards SB
    JOIN Classrooms C ON SB.roomID = C.roomID;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n--- SmartBoard Location Report ---")
    for row in results:
        print(f"Brand: {row[0]} | SN: {row[1]} | Room: {row[2]} (Floor {row[3]})")


# -------------------------------
# MAIN LOOP
# -------------------------------
def main():
    conn = connect()
    cursor = conn.cursor()

    try:
        # Step 1: Initialize DB + tables
        initialize_database(cursor)
        conn.commit()

        # DEBUG: confirm DB
        cursor.execute("SELECT DATABASE();")
        print("Current DB:", cursor.fetchone())

        # Refresh cursor (important)
        cursor.close()
        cursor = conn.cursor()

        while True:
            operation = input("\nEnter operation (Create / Retrieve / Update / Delete / Report / Exit): ").strip().lower()

            if operation == 'exit':
                print("Exiting...")
                break

            # Handle Reports separately as they don't need a table name or a commit
            if operation == 'report':
                print("\n1. Student Dashboard\n2. Enrollment Stats\n3. Hardware Inventory")
                choice = input("Select report number: ")
                if choice == '1': 
                    get_student_dashboard(cursor)
                elif choice == '2': 
                    get_course_stats(cursor)
                elif choice == '3': 
                    check_hardware_inventory(cursor)
                else:
                    print("Invalid choice.")
                continue # Go back to the start of the while loop

            tables = get_all_tables(cursor)

            print("\nAvailable Tables:")
            for t in tables:
                print("-", t)

            table_name = input("\nEnter table name: ").strip()

            if table_name not in tables:
                print("Invalid table name.")
                continue

            columns = get_table_columns(cursor, table_name)

            if operation == 'create':
                create_record(cursor, table_name, columns)
            elif operation == 'retrieve':
                retrieve_records(cursor, table_name)
            elif operation == 'update':
                update_record(cursor, table_name)
            elif operation == 'delete':
                delete_record(cursor, table_name)
            else:
                print("Invalid operation.")
                continue

            commit_choice = input("Commit changes? (yes/no): ").strip().lower()
            if commit_choice == 'yes':
                conn.commit()
            else:
                conn.rollback()

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
