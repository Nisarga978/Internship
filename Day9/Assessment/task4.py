class DatabaseConnection:

    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")

conn = DatabaseConnection()
conn.__enter__()          
print("Performing Query...")
conn.__exit__(None, None, None)   
