import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()

async def connection():
    try:
        conn = await asyncpg.connect(
            database="job_bot_db",
            port=5432,
            user="postgres",
            password= os.getenv("DB_PASSWORD"),
            host="localhost"
        )
        print("Connection Okey")
        return conn
    except Exception as error:
        print(f"Connection Error: {error}")
        
        

async def create_table():
    try:
        conn = await connection()
        await conn.execute("""
        create table if not exists users(
            user_id serial Primary key,
            username varchar(100),
            full_name varchar(100) not null,
            telegram_id varchar,
            created_at timestamp default now(),
            is_active boolean default true
        );
        
        create table if not exists cotegory(
            cotegory_id serial primary key,  
            cotegory_name varchar(100)
        );
            
        create table if not exists jobs(
            jobs_id serial primary key,
            title varchar(100) not null,
            discription text,
            salary int not null default(0),
            cotegory_id int references cotegory (cotegory_id)
        );
        
        create table if not exists applications(
            applications_id serial primary key,
            user_id int references users(user_id),
            jobs_id int references jobs(jobs_id),
            created_at timestamp default now()    
        );
                  
            """)
    except Exception as error:
        print(f"Connection Error: {error}")
    finally:
        await conn.close()
        print("Table created!")