import mariadb

try:
    conn = mariadb.connect(user = 'root', password='Sad1996.', host='127.0.0.1', port=3306)
    cursor = conn.cursor()
    # cursor.execute("CREATE SCHEMA bots")
    cursor.execute('USE bots')
    cursor.execute('CREATE TABLE gladiatus ('
                   'id integer auto_increment primary key,'
                   'log varchar(100) not null,'
                   'username varchar(100) not null,'
                   'date_inc date not null);'
                   )

except mariadb.Error as e:
    print(f'Error -> {e}')
