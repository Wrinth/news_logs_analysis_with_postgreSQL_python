#! /usr/bin/env python
# coding=utf-8

import psycopg2
import datetime


DBNAME = "news"


def get_most_popular_three_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT a.title, COUNT(l.path) as count \
            FROM log as l \
            INNER JOIN articles as a \
            on ('/article/' || a.slug) = l.path \
            WHERE l.path != '/' \
            GROUP BY l.path, a.title \
            ORDER BY COUNT(l.path) DESC \
            LIMIT 3")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_articles(data):
    articles_array = data
    for article in articles_array:
        print('"' + article[0] + '" - ' + str(article[1]) + ' views')


def get_most_popular_article_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT aut.name, COUNT(art.author) as count \
              FROM log as l \
              INNER JOIN articles as art \
              on ('/article/' || art.slug) = l.path \
              INNER JOIN authors as aut \
              on art.author = aut.id \
              WHERE l.path != '/' \
              GROUP BY art.author, aut.name \
              ORDER BY COUNT(art.author) DESC")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_authors(data):
    authors_array = data
    for author in authors_array:
        print(author[0] + ' - ' + str(author[1]) + ' views')


def get_days_with_requests_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("SELECT q1.date, ((q1.count * 100) / q2.count) as percentage \
              FROM (SELECT date(time) as date, COUNT(status) as count \
                    FROM log \
                    WHERE status LIKE '%4%' or status LIKE '%5%' \
                    GROUP BY date(time)) as q1,  \
                   (SELECT date(time) as date, COUNT(status) as count \
                    FROM log \
                    GROUP BY date(time)) as q2  \
              WHERE q1.date = q2.date and ((q1.count * 100) / q2.count) > 1")
    c.execute(query)
    return c.fetchall()
    db.close()


def display_error_days(data):
    error_days_array = data
    for error_day in error_days_array:
        day = error_day[0].day
        month = datetime.date(1900, error_day[0].month, 1).strftime('%B')
        year = error_day[0].year
        print(month + ' ' + str(day) + ', ' + str(year) +
              ' - ' + str(error_day[1]) + '% errors')


print "The most popular three articles of all time:"
display_articles(get_most_popular_three_articles())

print "\nThe most popular article authors of all time:"
display_authors(get_most_popular_article_authors())

print "\nDays with more than 1% of requests lead to errors:"
display_error_days(get_days_with_requests_errors())
