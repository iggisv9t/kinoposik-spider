# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class KinopoiskPipeline(object):
    def __init__(self):
# Don't forget to create db and table like this:
# CREATE TABLE all_data(movie_id TEXT, name TEXT, date TEXT, genre TEXT, country TEXT, director TEXT, like TEXT);
        self.conn = sqlite3.connect("./kinopoisk.db")

    def process_item(self, item, spider):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO all_data VALUES " +
                    "('{}', '{}', '{}', '{}', '{}', '{}', '{}');"\
                    .format(item['movie_id'], item['name'], item['date'],
                        item['genre'], item['country'], item['director'],
                        '|'.join(item['like'])))
        self.conn.commit()
        return item
