import mysql.connector
import datetime


def connect():
    global connection, cursor
    try:
        connection = mysql.connector.connect(host='localhost', database='AXON_DATA', user='root',
                                             password='Passwordxyz!', port='3308')
        cursor = connection.cursor(buffered=True)
        print("MySQL connection is opened")
        # use config file to do all this password shit

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
        exit()


def disconnect():
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def insert_attendee(name: str, email: str, phone: str, company: str):
    if company == '':
        company = None
    mysql_insert_query = "INSERT INTO ATTENDEE(NAME, EMAIL, PHONE, COMPANY) VALUES (%s,%s,%s,%s);"
    values = (name, email, phone, company)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    lastid = cursor.lastrowid
    disconnect()
    return lastid


def insert_booth(name: str):
    mysql_insert_query = "INSERT INTO BOOTH(NAME) VALUES (%s);"
    values = (name,)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    lastid = cursor.lastrowid
    disconnect()
    return lastid


def insert_event(name: str, location: str, zipcode: int):
    mysql_insert_query = "INSERT INTO EVENT(NAME, LOCATION, ZIPCODE) VALUES (%s,%s,%s);"
    values = (name, location, zipcode)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    lastid = cursor.lastrowid
    disconnect()
    return lastid


def register_badge(attendeeid: int, badgeid: int):
    mysql_insert_query = "INSERT INTO CURRENT_BADGE_ASSIGNMENTS (ATTENDEE_ID, BADGE_ID) VALUES(%s, %s) ON DUPLICATE " \
                         "KEY UPDATE ATTENDEE_ID = %s; "
    values = (attendeeid, badgeid, attendeeid)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()


def unregister(badgeid: int):
    mysql_insert_query = "UPDATE CURRENT_BADGE_ASSIGNMENTS SET ATTENDEE_ID = NULL, UPDATED = CURRENT_TIMESTAMP WHERE " \
                         "BADGE_ID = %s; "
    values = (badgeid,)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()


def scanaction(badgeid: int, boothid: int):
    mysql_insert_query = "INSERT INTO BOOTH_INTERACTION (ATTENDEE_ID, EVENT_ID, BOOTH_ID) VALUES ((SELECT ATTENDEE_ID " \
                         "FROM CURRENT_BADGE_ASSIGNMENTS WHERE BADGE_ID = %s), (SELECT EVENT_ID FROM CURRENT_EVENT " \
                         "LIMIT 1), %s) "
    values = (badgeid, boothid)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()
    # func name is temp


def unregisterall():
    mysql_insert_query = "UPDATE CURRENT_BADGE_ASSIGNMENTS SET ATTENDEE_ID = NULL, UPDATED = CURRENT_TIMESTAMP;"
    connect()
    cursor.execute(mysql_insert_query)
    connection.commit()
    disconnect()


def setEvent(badgeId: int):
    mysql_insert_query = "UPDATE CURRENT_EVENT SET EVENT_ID = %s;"
    values = (badgeId,)
    connect()
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    disconnect()


def getAllEventsMenu():
    mysql_insert_query = "SELECT ID, NAME FROM EVENT;"
    connect()
    cursor.execute(mysql_insert_query)
    connection.commit()
    a = []
    for i in cursor:
        a.append(str(i))
        print("Yer" + str(i))
    disconnect()
    print(a)
    return a


def getAllEvents(sqlVars: []):
    values = ()
    if sqlVars[2]:
        mysql_insert_query = "SELECT * FROM EVENT WHERE 1=1 "
    else:
        mysql_insert_query = "SELECT * FROM EVENT WHERE CREATED > %s AND CREATED < %s "
        startDate = datetime.datetime.strptime(sqlVars[0], "%m/%d/%y")
        endDate = datetime.datetime.strptime(sqlVars[1], "%m/%d/%y")
        values = (startDate, endDate)
    if sqlVars[3] != "Select An Option":
        if sqlVars[3] != "Current Event" and sqlVars[3] != "All Events":
            mysql_insert_query += "AND ID = " + str(sqlVars[3]).split(" ")[0].replace("(", "").replace(",", "")
        elif sqlVars[3] != "All Events":
            mysql_insert_query += "AND ID = (SELECT EVENT_ID FROM CURRENT_EVENT LIMIT 1);"
    connect()
    print(mysql_insert_query)
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    a = []
    for i in cursor:
        a.append(str(i))
    disconnect()
    return a


def getAllAttendees(sqlVars: []):
    values = ()
    if sqlVars[2]:
        mysql_insert_query = "SELECT * FROM ATTENDEE "
    else:
        mysql_insert_query = "SELECT * FROM ATTENDEE WHERE CREATED > %s AND CREATED < %s "
        startDate = datetime.datetime.strptime(sqlVars[0], "%m/%d/%y")
        endDate = datetime.datetime.strptime(sqlVars[1], "%m/%d/%y")
        values = (startDate, endDate)
    connect()
    print(mysql_insert_query)
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    a = []
    for i in cursor:
        a.append(str(i))
    disconnect()
    return a


def getAllBooths(sqlVars: []):
    values = ()
    if sqlVars[2]:
        mysql_insert_query = "SELECT * FROM BOOTH "
    else:
        mysql_insert_query = "SELECT * FROM BOOTH WHERE CREATED > %s AND CREATED < %s "
        startDate = datetime.datetime.strptime(sqlVars[0], "%m/%d/%y")
        endDate = datetime.datetime.strptime(sqlVars[1], "%m/%d/%y")
        values = (startDate, endDate)
    connect()
    print(mysql_insert_query)
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    a = []
    for i in cursor:
        a.append(str(i))
    disconnect()
    return a


def getAllInteractions(sqlVars: []):
    values = ()
    if sqlVars[2]:
        mysql_insert_query = "SELECT A.NAME, A.EMAIL, A.PHONE, A.COMPANY, B.NAME, B.ID, E.NAME, E.ID FROM " \
                             "BOOTH_INTERACTION BI JOIN ATTENDEE A on BI.ATTENDEE_ID = A.ID JOIN BOOTH B on B.ID = " \
                             "BI.BOOTH_ID JOIN EVENT E on E.ID = BI.EVENT_ID WHERE 1=1 "
    else:
        mysql_insert_query = "SELECT A.NAME, A.EMAIL, A.PHONE, A.COMPANY, B.NAME, B.ID, E.NAME, E.ID FROM " \
                             "BOOTH_INTERACTION BI JOIN ATTENDEE A on BI.ATTENDEE_ID = A.ID JOIN BOOTH B on B.ID = " \
                             "BI.BOOTH_ID JOIN EVENT E on E.ID = BI.EVENT_ID WHERE BI.CREATED > %s AND BI.CREATED < %s "
        startDate = datetime.datetime.strptime(sqlVars[0], "%m/%d/%y")
        endDate = datetime.datetime.strptime(sqlVars[1], "%m/%d/%y")
        values = (startDate, endDate)
    if sqlVars[3] != "Select An Option":
        if sqlVars[3] != "Current Event" and sqlVars[3] != "All Events":
            mysql_insert_query += "AND BI.EVENT_ID = " + str(sqlVars[3]).split(" ")[0].replace("(", "").replace(",", "")
        elif sqlVars[3] != "All Events":
            mysql_insert_query += "AND BI.EVENT_ID = (SELECT EVENT_ID FROM CURRENT_EVENT LIMIT 1);"
    connect()
    print(mysql_insert_query)
    cursor.execute(mysql_insert_query, values)
    connection.commit()
    a = []
    for i in cursor:
        a.append(str(i))
    disconnect()
    return a
