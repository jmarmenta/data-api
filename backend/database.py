from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()


class Dbclient:
    def __init__(self):
        self.db_string = os.environ['DB_CONNECTION_STRING']
        self.engine = create_engine(self.db_string)
        self.connection = self.engine.connect()
        

    def execute_query(self, query: str):
        return self.connection.execute(text(query))

    
    def close_connection(self):
        self.connection.close()