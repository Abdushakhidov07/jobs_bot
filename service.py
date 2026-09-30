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
        
        
async def get_category():
    try:
        conn = await connection()
        users = await conn.fetch("""
        select * from cotegory                           
        """)
        return users
    except Exception as error:
        print(f"Error in get category: {error}")
    finally:
        await conn.close()
        
        
async def update_category_service(cat_id, category_name):
    try:
        conn = await connection()

        await conn.execute("""
            UPDATE cotegory
            SET cotegory_name = $1
            WHERE cotegory_id = $2
        """, category_name, int(cat_id))

        return True

    except Exception as error:
        print(f"Error in Update category: {error}")
        return False

    finally:
        await conn.close()
        
        
        
        
        
        
async def delete_category_service(cat_id):
    try:
        conn = await connection()
        await conn.execute("""
            DELETE FROM cotegory
            WHERE cotegory_id = $1
        """, int(cat_id))
        return True

    except Exception as error:
        print(f"Error in delete category: {error}")
        return False

    finally:
        await conn.close()