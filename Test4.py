# Lauren Atkinson and Harrison Dominique
# import to connect with mysql using python

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
    cur.execute('DROP TABLE IF EXISTS NeighbourhoodLocation');
    cur.execute('DROP TABLE IF EXISTS Reviews');
    cur.execute('DROP TABLE IF EXISTS AirBnBHost');
    cur.execute('DROP TABLE IF EXISTS Host');

    cur.execute(
        '''CREATE TABLE AirBnBHost(AirBnBID VARCHAR(10) NOT Null REFERENCES AirBnB(AirBnBID), HostID VARCHAR(10) NOT Null REFERENCES Host(HostID) );''')

# insert data
def insert_data(cur):
    # opening up file with data inside
    with open("AirBnBTest4.csv", 'r') as r1:
        # skips first line the headers
        next(r1)
        # every line grabs data
        for line in r1:
            line = line.split(',')
            AirBnBID = line.__getitem__(0)
            HostID = line.__getitem__(1)

            # inserting into table
            cur.execute(
                'INSERT IGNORE INTO AirBnBHost(AirBnBID,HostID) VALUES (%s,%s)',
                (AirBnBID, HostID))


# from the original code
# setups the database

cnx = make_connection()
cur = cnx.cursor()
setup_dp(cur)
insert_data(cur)
cur.close()
cnx.commit()
cnx.close()