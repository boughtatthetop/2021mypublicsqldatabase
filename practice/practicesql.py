import sqlite3
connect=sqlite3.connect('chinook (3).db', isolation_level=None)
c=connect.cursor()
query='''
        SELECT * FROM genres 
        '''
print(query)
print(c.execute(query).fetchall())


print('------------------------------------------------')
print(connect.execute(query).fetchall())

