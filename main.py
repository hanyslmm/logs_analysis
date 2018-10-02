import psycopg2
from datetime import datetime

#connect to news database
db = psycopg2.connect("dbname=news")
cu = db.cursor()


#query_1 to select the most popular three articles of all time
select = '''select path, count(*) from log
            group by path
            order by count(*) DESC'''
cu.execute(select)
query_1 = cu.fetchall()
db.close()
print ("Most Popular three articles:")
for i in range(1,4):
    #print("* {} __".format(query_1[i])
    article = query_1[i][0]
    views = query_1[i][1]
    print("{}- {} ___ {} views".format(i, article, views))
