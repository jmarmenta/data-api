from backend.database import Dbclient
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# path to sql documents
sql_directory_path = "./sql"


app = FastAPI()

# Home URL
@app.get("/")
async def hello():
    return JSONResponse("Welcome to the DVD Rental DB example.")

# Get customer names with sqlalchemy
@app.get("/customer-names")
async def get_customer_names():
    db_client = Dbclient()
    customer_names_query_path = f"{sql_directory_path}/customer_names.sql"
    with open(customer_names_query_path) as f:
        query = f.read()
        result = db_client.execute_query(query=query)

        list_result = []

        for row in result:
            list_result.append(row._asdict())

        return list_result
        

# Get customer names with pandas
@app.get("/customer-names-pandas")
async def get_customer_names_with_pandas(): 
    
    customer_names_query_path_pandas = f"{sql_directory_path}/customer_names.sql"

    with open(customer_names_query_path_pandas) as f:
        query = f.read()
        db_connection_str = os.environ['DB_CONNECTION_STRING']
        data = pd.read_sql_query(query, db_connection_str)
        json_output = data.to_dict(orient="records")
        return json_output

# Get customer names from may 2005
@app.get("/customers-2005")
async def get_customers_from_2005():

    customer_names_2005_query_path = f"{sql_directory_path}/customers_in_may2005.sql"

    with open(customer_names_2005_query_path) as f:
        query = f.read()
        db_connection_str = os.environ['DB_CONNECTION_STRING']
        data = pd.read_sql_query(query, db_connection_str)
        json_output = data.to_dict(orient="records")
        return json_output
    
# Get movies released in `year`
@app.get("/movies-released")
async def get_movies_in_x_year(year: str):

    movies_in_2020_query_path = f"{sql_directory_path}/movies_released2020.sql"

    with open(movies_in_2020_query_path) as f:
        query = f.read()
        customed_year_query = query.replace("2020", year)
        db_connection_str = os.environ['DB_CONNECTION_STRING']
        data = pd.read_sql_query(customed_year_query, db_connection_str)
        json_output = data.to_dict(orient="records")
        return json_output

# Get top `n` rented movies 
@app.get("/top-rented-movies")
async def get_top_n_movies(top_n_movies: str):

    top_5_movies_query_path = f"{sql_directory_path}/top5_rented_movies.sql"

    with open(top_5_movies_query_path) as f:
        query = f.read()
        top_n_movies_query = query.replace('5',top_n_movies)
        db_connection_str = os.environ['DB_CONNECTION_STRING']
        data = pd.read_sql_query(top_n_movies_query, db_connection_str)
        json_output = data.to_dict(orient="records")
        return json_output

# Get the top category of movies rented
@app.get("/top-category")
async def get_top_category():

    top_category_query_path = f"{sql_directory_path}/topcategory.sql"

    with open(top_category_query_path) as f:
        query = f.read()
        db_connection_str = os.environ['DB_CONNECTION_STRING']
        data = pd.read_sql_query(query, db_connection_str)
        json_output = data.to_dict(orient="records")
        return json_output



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)