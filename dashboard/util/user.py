from datetime import datetime
from datetime import timezone

from passlib.hash import sha256_crypt

from dashboard.app import rdb_users


class User:
    def __init__(self, username: str):
        self.__username = 'user:' + username
        self.__is_authenticated = False

    def exists(self) -> bool:
        """
        Checks if username already exists in database
        :return: boolean
        """
        return bool(rdb_users.exists(self.__username))

    def register(self, fullname: str, password: str) -> bool:
        """
        Register new user
        :param fullname:
        :param password:
        :return: boolean value according if registration was successful or not
        """

        if not self.exists():
            rdb_users.hset(
                name=self.__username,
                key='registerDate',
                value=datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d')
            )
            rdb_users.hset(
                name=self.__username,
                key='fullname',
                value=fullname
            )
            rdb_users.hset(
                name=self.__username,
                key='password',
                value=User.hash_password(password=password)
            )

            return True
        return False

    def login(self, password: str):
        """
        Check if user is authenticated to login
        :param password:
        :return:
        """
        if self.exists() and self.__check_password(password=password):
            return True
        return False

    def __check_password(self, password: str) -> bool:
        """
        Check if hashed password from matches raw password
        :param password:
        :return:
        """
        rdb_password = rdb_users.hget(name=self.__username, key='password')
        return sha256_crypt.verify(password, rdb_password)

    @staticmethod
    def hash_password(password: str) -> str:
        hashed_password = sha256_crypt.hash(password)
        return hashed_password


if __name__ == '__main__':
    user = User(username='sandermoller')
    print(user.exists())
    register_status = user.register(fullname='Sander Möller', password='mypass')
    print(register_status)
    print(user.exists())

    print(rdb_users.hgetall(name='user:sandermoller'))

    print(user.login(password='mypass'))



