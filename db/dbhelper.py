import sqlite3

DB_FILE = './db/database.db'


# 创建数据库中的表
def create_tables():
    f_name = 'db/store-schema.sql'
    with open(f_name, 'r', encoding='utf-8') as f:
        sql = f.read()
        # 创建数据库链接
        conn = sqlite3.connect(DB_FILE)
        try:
            conn.executescript(sql)
            print('数据库初始化成功')
        except Exception as e:
            print('数据库初始化失败')
            print(e)
        finally:
            # 关闭数据库链接
            conn.close()

# 数据库的商品表插入数据
def load_data():
    f_name = 'db/store-dataload.sql'
    with open(f_name, 'r', encoding='utf-8') as f:
        sql = f.read()
        # 创建数据库链接
        conn = sqlite3.connect(DB_FILE)
        try:
            conn.executescript(sql)
            print('数据库初始化成功')
        except Exception as e:
            print('数据库初始化失败')
            print(e)
        finally:
            # 关闭数据库链接
            conn.close()