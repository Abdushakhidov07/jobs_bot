from connection import connection


async def get_user(telegram_id):
    try:
        conn = await connection()
        users = await conn.fetchrow("""
        select * from users where telegram_id = $1                           
        """, str(telegram_id))
        return users
    except Exception as error:
        print(f"Error in get users: {error}")
    finally:
        await conn.close()
        
async def save_user(telegram_id, username, full_name):
    try:
        conn = await connection()
        await conn.execute("""
        INSERT INTO users(telegram_id, username, full_name) VALUES
        ($1, $2, $3)
        """, str(telegram_id), username, full_name)
        print("User saved")
    except Exception as error:
        print(f"Error in save users: {error}")
    finally:
        await conn.close()
        
        
        
        
async def save_category(category):
    try:
        conn = await connection()
        await conn.execute("""
        INSERT INTO cotegory(cotegory_name) VALUES
        ($1)
        """, category)
        print("category saved")
        return True
    except Exception as error:
        print(f"Error in save category: {error}")
        return False
    finally:
        await conn.close()