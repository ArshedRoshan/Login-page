from django.db import models

# Create your models here.

class abc:
    first=str
    last=str
    handle=str

a=abc()
b=abc()


a.first='Name1'
a.last='age'


b.first='Name2'
b.last='age'


list1=[a,b]

class photo:
    img=str
    title=str
    disc=str

ab=photo()
ac=photo()
ad=photo()

ab.img='canada.jpg'
ab.title='canada'
ab.disc='it is a beatiful place'

ac.img='canada.jpg'
ac.title='canada'
ac.disc='it is a beatiful place'

ad.img='canada.jpg'
ad.title='canada'
ad.disc='it is a beatiful place'

card1=[ab,ac,ad]