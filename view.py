#! /usr/bin/env python3

import psycopg2

#connect to news database
db = psycopg2.connect("dbname=news")
cu = db.cursor()

#create views to enhance query usage

top_views = '''
    create or replace view click_view as
    select title, count(*) as views, author
    from log join articles
    on log.path = concat('/article/', articles.slug)
    group by title, author
    order by views desc;
    '''
daily_errors = '''
    create or replace view errors_view as
    select time::date, count(*) as errors
    from log
    where status != '200 OK'
    group by time::date
    order by time::date desc;
    '''
daily_request = '''
    create or replace view requests_view as
    select time::date, count(*) as requests
    from log
    group by time::date
    order by time::date desc;
    '''
error_percentage = '''
    create or replace view error_percent as
    select errors_view.time::date,
    cast(errors_view.errors as float) /
    cast(requests_view.requests as float)
    as percentage
    from errors_view
    inner join requests_view
    on errors_view.time::date = requests_view.time::date
    group by errors_view.time::date, errors_view.errors,
    requests_view.requests;
    '''
cu.execute(top_views)
cu.execute(daily_errors)
cu.execute(daily_request)
cu.execute(error_percentage)

db.commit()
db.close()
