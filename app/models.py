from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=20)
    #                   문자열 길이
    def __str__(self):  # 오버라이딩
        return self.address


