import psycopg2
import os
import time
from datetime import datetime

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#connect to news database
db = psycopg2.connect("dbname=news")
cu = db.cursor()

    #Most popular three articles

query_1 = '''
        select title, views from click_view
        limit 3;
        '''
cu.execute(query_1)
topviews = cu.fetchall()
#print(topviews)
print ("Most Popular three articles:")
for i in range(0,3):
    #print("* {} __".format(query_1[i])
    article = topviews[i][0]
    views = topviews[i][1]
    print("{}- {} ___ {} views".format(i+1, article, views))
    f = open('hany.txt', 'w')
    f.write("{}- {} ___ {} views".format(i+1, article, views))
f.close()
db.close()
