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

    cur.execute(
        '''CREATE TABLE Reviews (ReviewID int auto_increment NOT NULL PRIMARY KEY, AirBnBID VARCHAR(10) NOT NULL, _ReviewsPerMonth VARCHAR(10),_LastReview DATE,_NumberOfReviews VARCHAR(5));''')


# insert data
def insert_data(cur):
    # opening up file with data inside
    with open("AirBnBTest2.csv", 'r', encoding='utf-8') as r1:
        # skips first line the headers
        next(r1)
        # every line grabs data
        for line in r1:
            line = line.split(',')
            _ID = line.__getitem__(0)
            _reviewspermonth = line.__getitem__(1)
            _lastreview = line.__getitem__(2)
            _numberofreviews = line.__getitem__(3)
            # inserting into table
            cur.execute(
                'INSERT IGNORE INTO Reviews(AirBnBID,_ReviewsPerMonth, _LastReview, _NumberOfReviews) VALUES (%s,%s,%s,%s)',
               (_ID,_reviewspermonth,_lastreview,_numberofreviews))




# from the original code
# setups the database
cnx = make_connection()
cur = cnx.cursor()
setup_dp(cur)
insert_data(cur)
cur.close()
cnx.commit()
cnx.close()