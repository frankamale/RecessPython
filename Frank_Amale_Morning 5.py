#Assignment
# 
# Context manager to open and close a file

class FileManager:
    def __init__(self, filename, mode):
        self.file_path = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


file_path = "example.txt"

with FileManager(file_path, "w") as file:
    file.write("Opened my file")



# Context manager for managing a database connection
import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

db_file = "Junior.db"

# Opening the database connection using the context manager
with DatabaseManager(db_file) as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    connection.commit()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

# Database connection is automatically closed outside the context manager

# multithreading example to run processes for a given amount of time
import threading
import time

def long_function(name, duration):
    print(f"Thread {name} started")
    time.sleep(duration)
    print(f"Thread {name} completed")

# Function arguments: (name, duration)
functions = [("Function 1", 5), ("Function 2", 3), ("Function 3", 2)]

# Create and start threads for each function
threads = []
for func in functions:
    thread = threading.Thread(target=long_function, args=func)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()


# Multiprocessing example to run processes for a given amount of time
import multiprocessing
import time

def long_running_function(name, duration):
    print(f"Process {name} started")
    time.sleep(duration)
    print(f"Process {name} completed")

# Function arguments: (name, duration)
functions = [("Function 1", 5), ("Function 2", 3), ("Function 3", 2)]

# Create and start processes for each function
processes = []
for func in functions:
    process = multiprocessing.Process(target=long_running_function, args=func)
    process.start()
    processes.append(process)

# Wait for all processes to complete
for process in processes:
    process.join()
