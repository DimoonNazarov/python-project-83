import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')





def add_site(site: dict) -> None:
    conn = psycopg2.connect(DATABASE_URL)
