#import mysql.connector


def connect():
    """global connection, cursor
    try:
        connection = mysql.connector.connect(host='localhost', database='AXON_DATA', user='root',
                                             password='Passwordxyz!', port='3308')
        cursor = connection.cursor()
        print("MySQL connection is opened")
        # use config file to do all this password shit

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
        exit()"""


def disconnect():
    """if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")"""


def insert_attendee(name: str, email: str, phone: str, company: str):
    """if company == '':
        company = None
    mysql_insert_query = "INSERT INTO ATTENDEE(NAME, EMAIL, PHONE, COMPANY) VALUES (%s,%s,%s,%s);"
    values = (name, email, phone, company)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    lastid = cursor.lastrowid
    disconnect()
    return lastid"""


def insert_booth(name: str):
    """mysql_insert_query = "INSERT INTO BOOTH(NAME) VALUES (%s);"
    values = (name,)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()"""


def insert_event(name: str, location: str, zipcode: int):
    """mysql_insert_query = "INSERT INTO EVENT(NAME, LOCATION, ZIPCODE) VALUES (%s,%s,%s);"
    values = (name, location, zipcode)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()"""


def register_badge(attendeeid: int, badgeid: int):
    """mysql_insert_query = "INSERT INTO CURRENT_BADGE_ASSIGNMENTS (ATTENDEE_ID, BADGE_ID) VALUES(%s, %s) ON DUPLICATE KEY UPDATE ATTENDEE_ID = %s;"
    values = (attendeeid, badgeid, attendeeid)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()"""


def new_attendee(name: str, email: str, phone: str, company: str):
    insert_attendee(name, email, phone, company)
    # add email format checking here or frontend? + checking by email


def new_booth(name: str):
    insert_booth(name)
    # check if booth already exists by name?


def new_event(name: str, location: str, zipcode: int):
    insert_event(name, location, zipcode)


def register(attendeeid: int, badgeid: int):
    register_badge(attendeeid, badgeid)
    # return error if lookup (not implemented) is wrong


def unregister(badgeid: int):
    """mysql_insert_query = "UPDATE CURRENT_BADGE_ASSIGNMENTS SET ATTENDEE_ID = NULL, UPDATED = CURRENT_TIMESTAMP WHERE BADGE_ID = %s;"
    values = (badgeid,)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()"""


def scanaction(attendeeid: int, eventid: int, boothid: int):
    """mysql_insert_query = "INSERT INTO BOOTH_INTERACTION (ATTENDEE_ID, EVENT_ID, BOOTH_ID) VALUES (%s, %s, %s);"
    values = (attendeeid, eventid, boothid)
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    # func name is temp"""


def unregisterall():
    """mysql_insert_query = "UPDATE CURRENT_BADGE_ASSIGNMENTS SET ATTENDEE_ID = NULL, UPDATED = CURRENT_TIMESTAMP;"
    connect()
    cursor.execute(mysql_insert_query)
    connection.commit()
    disconnect()"""