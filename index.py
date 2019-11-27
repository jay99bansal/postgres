#!/usr/bin/python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import psycopg2


conn = psycopg2.connect(database="stIndex", host="localhost", port="9432")
print("Opened database successfully")

cur = conn.cursor()

try:
    c = 0
    while True:
        cur.execute("drop index spatioTemporal"+str(s)+";")
        c = c+1
        conn.commit()
except:
    pass


valid = []
data = []
st = 1
cur.execute("select * from testST")
rows = cur.fetchall()
for row in rows:
    data.append([row[0],str(row[1]),str(row[2])])
    valid.append(str(row[1]))
    valid.append(str(row[2]))

valid = sorted(list(set(valid)))
print(valid)

for i in valid:
    cur.execute("delete from testST")
    conn.commit()
    for j in data:
        if i>=j[1] and i<j[2]:
            cur.execute("insert into testST values ('"+str(j[0])+"','"+str(j[1])+"','"+str(j[2])+"')")
    conn.commit()

    cur.execute("select * from testST")
    rows = cur.fetchall()
    for row in rows:
        print(str(row[0]),str(row[1]),str(row[2]))

    cur.execute("create index spatioTemporal"+str(st)+" on testST using gist(coordinate);")
    conn.commit()
    st = st+1
    print("-----------------")

cur.execute("delete from testST")
conn.commit()

for i in data:
    cur.execute("insert into testST values ('"+str(i[0])+"','"+str(i[1])+"','"+str(i[2])+"')")
conn.commit()
conn.close()

'''data=[['(1,1)', '2017-06-21', '9999-12-31'], ['(1,2)', '2017-05-03', '2018-10-08'], ['(1,1)', '2014-03-07', '2014-07-07'], ['(3,4)', '2017-05-03', '2018-10-08'], ['(2,7)', '2018-10-08', '9999-12-31'], ['(1,3)', '2014-07-07', '2017-05-03'], ['(7,8)', '2014-07-07', '9999-12-31'], ['(5,6)', '2017-06-21', '2019-01-01'], ['(3,4)', '2019-01-01', '9999-12-31'], ['(1,4)', '2014-03-07', '2019-01-01'], ['(7,10)', '2019-01-01', '9999-12-31'], ['(5,6)', '2014-07-07', '2018-10-08']]
for i in data:
    cur.execute("insert into testST values ('"+str(i[0])+"','"+str(i[1])+"','"+str(i[2])+"')")
conn.commit()
conn.close()'''
