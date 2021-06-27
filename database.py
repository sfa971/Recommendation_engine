import pymysql
import sqlalchemy
import pandas as pd
from sqlalchemy import  create_engine


#creating dataframe
books = pd.read_csv('https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv')

tags = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/tags.csv")

ratings = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")

books_tag = pd.read_csv('https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/book_tags.csv')

to_read = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/to_read.csv")


# Connect to the database
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="root", db="Good_book"))

# Insert whole DataFrame into MySQL
books.to_sql('books', con = engine, if_exists = 'append', chunksize = 1000)
ratings.to_sql('ratings', con = engine, if_exists = 'append', chunksize = 1000)
tags.to_sql('tags', con = engine, if_exists = 'append', chunksize = 1000)
to_read.to_sql('to_read', con = engine, if_exists = 'append', chunksize = 1000)
books_tag.to_sql('books_tag', con = engine, if_exists = 'append', chunksize = 1000)