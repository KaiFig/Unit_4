import sqlite3



#code for database handler
class database_worker: 
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

#password encryption

from passlib.hash import sha256_crypt

#create an object of the class CryptoConrtext
hasher = sha256_crypt.using(rounds=30000)

# this function receives the unsafe password and returns hashed
def encrpyt_password(user_password):
    return hasher.encrypt(user_password)
def check_password(hashed_password, user_password):
    return hasher.verify(user_password, hashed_password)

