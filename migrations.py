from categories import categories

def create_accounts(c):
    c.execute("""CREATE TABLE accounts (acc_id 
    SERIAL, pc_accountid TEXT, name TEXT, nickname
    TEXT,acc_type TEXT, institution_id INTEGER,acc_group TEXT,
    user_id INTEGER)""")


def create_balances(c):
    c.execute("""CREATE TABLE balances (bal_id 
    SERIAL, acc_id INTEGER, balance NUMERIC, time
    )""")


def create_categories(c):
    c.execute("""CREATE TABLE categories (cat_id 
    SERIAL, category TEXT, cat_group TEXT)""")


def create_institutions(c):
    c.execute("""CREATE TABLE institutions (institution_id 
    SERIAL, institution TEXT)""")


def create_items(c):
    c.execute("""CREATE TABLE items (item_id 
    SERIAL, item TEXT, long_item TEXT)""")


def create_txs(c):
    c.execute("""CREATE TABLE txs (tx_id 
    SERIAL, acc_id INTEGER, item_id INTEGER,
    cat_id INTEGER, amount NUMERIC,is_credit TEXT, pc_catid
    INTEGER, pc_cat INTEGER,date TEXT,pc_txid NUMERIC)""")


def create_users(c):
    c.execute("""CREATE TABLE users (user_id 
    SERIAL, username TEXT NOT NULL, pwhash TEXT NOT
    NULL, pc_email TEXT)""")


def migrate_categories(c, categories):
    for i in categories:
        category = i[0]
        cat_group = i[1]
        c.executemany("""INSERT INTO categories (category, cat_group)
                    VALUES (?, ?)""",
                    [(category, cat_group),])

conn.commit()
conn.close()
