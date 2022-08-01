from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, 'dotenv'))

class Config:
    ARPANSA_API_URL = environ.get('ARPANSA_API_URL')
    LOCATIONIQ_API_URL = environ.get('LOCATIONIQ_API_URL')
    LOCATIONIQ_API_KEY = environ.get('LOCATIONIQ_API_KEY')
