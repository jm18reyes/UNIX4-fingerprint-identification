import mysql.connector as mariadb


mariadb_connection = mariadb.connect(host='localhost',user='ccesc',password='pass123',database='ccescdb')
c = mariadb_connection.cursor()

def Authenticate(pos):
    c.execute("SELECT count(*) FROM info WHERE posNum=%s", (pos,))
    count, = c.fetchone()
    if count != 0:
        return True
    else:
        return False

def AddUser(pos, name, snum, prog, email, pnum, hours):
    c.execute("INSERT INTO info VALUES(%s,%s,%s,%s,%s,%s,0,%s)", (pos, name, snum, prog, email, pnum, hours))
    mariadb_connection.commit()

def UpdateUser(pos, name, snum, prog, email, pnum):
    c.execute("UPDATE info SET name=%s,sNum=%s,program=%s,email=%s,phone=%s WHERE posNum=%s", (name, snum, prog, email, pnum, pos))
    mariadb_connection.commit()

def UserList():
    c.execute("SELECT name FROM info")
    record = c.fetchall()
    return record

def Name(pos):
    c.execute("SELECT name FROM info WHERE posNum=%s", (pos,))
    record = c.fetchone()
    return record

def Info(self, row):
    c.execute("SELECT * FROM info WHERE rowid=%s", (row,))
    record = c.fetchone()
    return record

def UpdateInfo(col, value, pos):
    query = str("UPDATE info SET "+col+"=%s WHERE posNum=%s")
    c.execute(query, (value,pos))
    mariadb_connection.commit()

def TimeList():
    c.execute("SELECT time FROM time")
    record = c.fetchall()
    return record

def AddSched(pos, time, date, backup):
    c.execute("INSERT INTO sched(posNum, timeid, dateid, backup) VALUES(%s, %s, %s, %s)", (pos, time, date, backup))
    mariadb_connection.commit()
    
def getSched(pos):
    c.execute("SELECT dateid FROM sched WHERE posNum=%s",(pos,))
    did,=c.fetchone()
    c.execute("SELECT timeid FROM sched WHERE posNum=%s",(pos,))
    tid,=c.fetchone()
    c.execute("SELECT date FROM date WHERE dateid=%s",(did,))
    det,=c.fetchone()
    c.execute("SELECT time FROM time WHERE timeid=%s",(tid,))
    taym,=c.fetchone()
    return det,taym
