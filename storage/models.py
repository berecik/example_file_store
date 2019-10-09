import random
import sys
from hashlib import md5
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings


class File(models.Model):
    file = models.FileField(upload_to='files_valut')
    hash = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255, null=True)
    date_to = models.DateField(null=True)
    file_name = models.CharField(max_length=255, null=True)

    @staticmethod
    def __get_salt():
        return str(random.randint(-sys.maxsize - 1, sys.maxsize))

    @classmethod
    def generate_hash(cls):
        new_hash = md5(cls.__get_salt().encode()).hexdigest()
        if cls.objects.filter(hash=new_hash).count():
            return cls.generate_hash()
        return new_hash

    def set_password(self, password):
        salt = self.__get_salt()
        self.password = make_password(password, salt)

    def check_password(self, password):
        return check_password(password, self.password)

    def download_url(self):
        return "/{}/".format(self.hash)

    def save(self, password=None, **kwargs):
        if password and len(password):
            self.set_password(password)
        if not self.hash:
            self.hash = self.generate_hash()
        return super().save(**kwargs)
