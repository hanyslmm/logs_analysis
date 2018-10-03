#! /usr/bin/env python3
import psycopg2
import os
import time
from datetime import datetime

localtime = time.asctime(time.localtime(time.time()))
print('\nprogram execution time stamp:\n')
print(localtime)
print('_______________________________\n')

#connect to news database
db = psycopg2.connect("dbname=news")
cu = db.cursor()

    #Most popular three articles query
top_articles = '''
        select title, views from click_view
        limit 3;
        '''
    #Most popular three authors query
top_authors = '''
        select authors.name, sum(views)
        from authors join click_view
        on authors.id = click_view.author
        group by authors.name
        order by sum(views)
        desc;
        '''
    #On which days did more than 1% of requests lead to errors query
errors_day = '''
        select * from error_percent
        where percentage > .01;
        '''

#execute top three articles query
cu.execute(top_articles)
topviews = cu.fetchall()
print ("Most Popular three articles:\n")
for i in range(0,3):
    article = topviews[i][0]
    artviews = topviews[i][1]
    print("{}- {} ___ {} views".format(i+1, article, artviews))
print('\n_______________________________\n')

#execute top three authors query
cu.execute(top_authors)
authors = cu.fetchall()
print ("Most Popular three authors:\n")
for i in range(0,3):
    author = authors[i][0]
    autviews = authors[i][1]
    print("{}- {} ___ {} views".format(i+1, author, autviews))
print('\n_______________________________\n')

#execute server daily errors
cu.execute(errors_day)
derrors = cu.fetchall()
print("Days more than 1% of requests get errors:\n")
for derror in derrors:
    i = 1
    day = derror[0]
    percent = round((derror[1]*100), 3)
    print ('{}- {} ___ {}% error'.format(i, day, percent))
    i += 1
print('\n_______________________________\n')


db.close()
