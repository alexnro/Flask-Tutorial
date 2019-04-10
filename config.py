import os
from dotenv import load_dotenv
from mongoengine import connect

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #             mongodb://[new_user:123@192.168.2.50:27017
    MONGO_URI = "mongodb://localhost:27017/microblog"
    CLIENT = connect('microblog', host='mongodb://localhost:27017/microblog')
    POSTS_COLLECTION = CLIENT.posts
    USERS_COLLECTION = CLIENT.user
    FOLLOWERS_COLLECTION = CLIENT.followers
    # config["MONGO_URI"] = "mongodb://localhost:27017/microblog"

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 25
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
