import pyrebase
from dbConfig import dbConfig, Secret


firebaseConfig = dbConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def signup(username):
    secret = db.get(Secret)
    logins = []
    for i in secret.val():
        logins.append(i)
    if username not in logins:
        name = "Имя"
        surname = "Фамилия"
        date_of_birthday = "Дата рождения"
        phone_number = "Номер телефона"
        mail = "Почта"
        db.child(username).child(name).set(name)
        db.child(username).child(surname).set(surname)
        db.child(username).child(date_of_birthday).set(date_of_birthday)
        db.child(username).child(phone_number).set(phone_number)
        db.child(username).child(mail).set(mail)