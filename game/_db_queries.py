import sqlite3, math
from Table import Table

con = sqlite3.connect('test.db')
c = con.cursor()

def createMaterialsTabel():
    c.execute('''CREATE TABLE materials (id integer, name text, damage integer, defense integer, durability integer, weapon integer, armour integer)''')

def addMaterials():
    c.execute("INSERT INTO materials VALUES (0, 'Rusty', 1, 2, 2, 1, 1)")
    c.execute("INSERT INTO materials VALUES (1, 'Bronze', 1, 2, 2, 1, 1)")
    c.execute("INSERT INTO materials VALUES (2, 'Iron', 3, 4, 3, 1, 1)")
    c.execute("INSERT INTO materials VALUES (3, 'Silver', 5, 2, 1, 1, 1)")
    c.execute("INSERT INTO materials VALUES (4, 'Mythril', 3, 5, 3, 1, 1)")
    c.execute("INSERT INTO materials VALUES (5, 'Mysterious alloy', 5, 6, 2, 1, 1)")
    c.execute("INSERT INTO materials VALUES (6, 'Dragon scales', 4, 7, 4, 1, 1)")
    c.execute("INSERT INTO materials VALUES (7, 'leather', 0, 2, 15, 0, 1)")


def createWeaponsBlueprintTable():
    c.execute('''
        CREATE TABLE weaponBlueprints
        (
            id integer,
            name text,
            damage integer,
            durability integer
        )
    ''')

def createWeaponsTable():
    c.execute('''
        CREATE TABLE weapons
        (
            weaponBlueprintId integer,
            materialId integer,
            foreign key (weaponBlueprintId) references weaponBlueprints,
            foreign key (materialId) references materials
        )
    ''')

def showTable(tableName):
    headers = c.execute("PRAGMA table_info(" + tableName + ")").fetchall()
    contents = c.execute('''
        SELECT * 
        FROM ''' + tableName ).fetchall()

    sanitizedHeaders = ['' for i in range(len(headers))]
    for index, header in enumerate(headers):
        sanitizedHeaders[index] = header[1]


    rows = [sanitizedHeaders]
    for content in contents:
        rows.append(content)
    
    table = Table(rows, tableName)
    table.print()

def showTableNames():
    cursor = c.execute('''
        SELECT name 
        FROM sqlite_master
        WHERE type = "table"
    ''')

    table = Table(cursor.fetchall(), "Table Names")
    table.print()
    
    


showTableNames()
showTable('materials')
showTable('weapons')
showTable('weaponBlueprints')


con.commit()

con.close()
