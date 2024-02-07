from django.db import models
class Link:
    linkname:str
    link:str
    productid:int
class Image:
    productId:int
    image:str
    name:str
    des:str
    cate:int
    gen:int
    links:list

class user:
    fname:str
    lname:str
    uname:str
    mail:str
    phone:int
    gen:str
    pas:int
    cpas:int
class designer:
    fname:str
    lname:str
    uname:str
    mail:str
    phone:int
    gen:str
    qual:str
    work:str
    pas:int
    cpas:int
    id:int

class profiles:
    fname = str
    lname = str

    
class homeo:
    fname:str
    lname:str
    uname:str
    mail:str
    phone:int




