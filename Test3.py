# Lauren Atkinson and Harrison Dominique
# import to connect with mysql using python
#Ask how to link neighbourhoods and AirBnB

import pymysql as ps


# make the connection to the db

def make_connection():
    return ps.connect(host='database-1.cspat74yfn24.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='Lalastacks',
                      port=3306, autocommit=True)
# function creating the database
def setup_dp(cur):

    # Set up db
    cur.execute('DROP DATABASE IF EXISTS NYCAirBnBs');
    cur.execute('CREATE DATABASE NYCAirBnBs');
    cur.execute('USE NYCAirBnBs');

    # Drop Existing Tables
    cur.execute('DROP TABLE IF EXISTS AirBnB');
#    cur.execute('DROP TABLE IF EXISTS NeighbourhoodLocation');
    cur.execute('DROP TABLE IF EXISTS Reviews');
    cur.execute('DROP TABLE IF EXISTS AirBnBHost');
    cur.execute('DROP TABLE IF EXISTS Host');
    # Create Tables



    cur.execute(
        '''CREATE TABLE AirBnB(AirBnBID VARCHAR(10) NOT NULL PRIMARY KEY ,NBID VARCHAR(10), Name VARCHAR(100), Price VARCHAR(100), RoomType VARCHAR(25), RoomsAvailable VARCHAR(5), Longitude FLOAT, Latitude FLOAT);''')


# insert data
def insert_data(cur):
    # opening up file with data inside
    with open("AirBnBTest3.1.csv", 'r', encoding='utf-8') as r1:
        # skips first line the headers
        next(r1)
        # every line grabs data
        for line in r1:
            line = line.split(',')
            id = line.__getitem__(0)
            name = line.__getitem__(1)
            price = line.__getitem__(2)
            room_type = line.__getitem__(3)
            availability = line.__getitem__(4)
            longitude = line.__getitem__(5)
            latitude = line.__getitem__(6)
            NID = line.__getitem__(7)

            # inserting into table
            #search for the id


            cur.execute(
                'INSERT IGNORE INTO AirBnB(AirBnBID,NBID, Name, Price, RoomType, RoomsAvailable,Longitude, Latitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                (id, NID, name, price, room_type, availability, longitude, latitude))




# from the original code
# setups the database

cnx = make_connection()
cur = cnx.cursor()
setup_dp(cur)
insert_data(cur)
cur.close()
cnx.commit()
cnx.close()