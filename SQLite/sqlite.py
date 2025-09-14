import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

## Create a Table
cursor.execute('''
Create table if not exists employees(
        id Integer Primary key,
        name test not null,
        age integer,
        department text)
''')

### Insert the data
cursor.execute('''
    Insert into employees(name,age,department)
    values('Sahil',27,'AI Engineer')''')

### Commit the changes -> After changes just commit it
connection.commit()

### Fetch
cursor.execute('Select * from employees')
rows = cursor.fetchall()

for row in rows:
    print(row)

### update the data
cursor.execute(''' 
update employees set age=28 where name='Sahil'
''')
connection.commit()

cursor.execute('Select * from employees')
rows = cursor.fetchall()

for row in rows:
    print(row)

### Delete the data
cursor.execute(''' 
delete from employees where name='Sahil'
''')
connection.commit()

### Permanently Close the connection
connection.close()