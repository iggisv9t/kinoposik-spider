### Kinopoisk spider

- It traverse kinopoisk.ru through recoommendation links starting from top250 movies (https://www.kinopoisk.ru/top/ - ./data/startlinks.txt)
- Don't forget to create db (see comments in ./kinopoisk/pipelines.py) or change pipline as you need, and change proxy settings in middleware.py and like_spider.py (request parameter "meta")
