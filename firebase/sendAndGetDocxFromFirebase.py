import pyrebase
from dbConfig import *

config = dbConfig

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()


# Функция upload_file загружает файл с именем file_name в хранилище Firebase Storage.
def upload_file(file_name):
    storage.child(file_name).put(file_name)


# Функция download_file скачивает файл с именем file_name из Firebase Storage.
def download_file(file_name):
    storage.child(file_name).download("", file_name)
