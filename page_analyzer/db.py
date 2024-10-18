import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import NamedTupleCursor

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def add_site(site: dict) -> None:
    try:
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            q_insert = """
            INSERT INTO urls (name , created_at)
            VALUES (%s, %s);"""
            cur.execute(q_insert, (site['url'], site['created_at']))

            conn.commit()
    except Exception as e:
        print(f"Error adding site: {e}")
    finally:
        conn.close()


def get_all_urls() -> dict:
    try:
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            q_select = """
            SELECT DISTINCT ON (urls.id)
            urls.id as id,
            urls.name as name,
            url_checks.created_at as last_check,
            url_checks.status_code as status_code
            FROM urls
            LEFT JOIN url_checks on urls.id = url_checks.url_id
            AND url_checks.id = (SELECT MAX(id)
                                        FROM url_checks
                                        WHERE url_id = urls.id)
                        ORDER BY urls.id DESC;"""
            cur.execute(q_select)
            urls = cur.fetchall()
    except Exception as e:
        print(f"Error fetching URLs: {e}")
        urls = []
    finally:
        conn.close()
    return urls


def get_urls_by_id(id_: int)-> dict:
    try:
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            q_select = "select * from urls where id =(%s);"
            cur.execute(q_select, (id_,))
            urls = cur.fetchone()

    except Exception as e:
        print("error in get_urls_by_id")
        urls_list = []
    finally:
        conn.close()
    return urls


def get_checks_by_id(id_: int) -> dict:

    conn  = psycopg2.connect(DATABASE_URL)
    with  conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        q_select = """
        SELECT * from url_checks
        WHERE url_id = (%s)
        order by id DESC;"""
        cur.execute(q_select,[id_] )
        checks = cur.fetchall()
    conn.close()
    return checks