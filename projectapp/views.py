from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
import mysql.connector
import os
from django.conf import settings
from .models import Image,user,Link,designer,profiles,homeo
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 
from datetime import datetime
from django.contrib import messages;
import random
from django.utils.datastructures import MultiValueDictKeyError



def signup(request):
    #return render(request, "signup.html")
    if(request.method=="POST"):
        print("im in post request", request.POST)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        fname=request.POST['fn']
        lname=request.POST['ln']
        uname=request.POST['un']
        mail=request.POST['mail']
        phone=request.POST['pn']
        gender=request.POST['gender']
        p=request.POST['pw']
        conpass=request.POST['cpw']
        mycursor = conn.cursor()
        mycursor.execute("insert into users(fname,lname,uname,email,phone,gender,pwd,cpwd) values('"+fname+"','"+lname+"','"+uname+"','"+mail+"','"+phone+"','"+gender+"','"+p+"','"+conpass+"')")
        conn.commit()    
        return redirect('/homelogout',{"status":"you can login"})
    else:
        return render(request,'signup.html')
def login(request):
    print('hihello')
    if(request.method=="POST"):
        uname=request.POST['un']
        pwd=request.POST['pwd']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from customers where uname='"+uname+"' and pwd='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['uname']=uname
            return render(request,"homelogout.html")
        else:
            print('hi')
            messages.error(request, 'Invalid username or password.')
            return render(request,"login.html",{"status":"invalid credentials"})
    else:
        return render(request,'login.html')
    
def adminlogin(request):
    if(request.method=="POST"):
        uname=request.POST['un']
        pwd=request.POST['pwd']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from admin where uname='"+uname+"' and pwd='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            return render(request,"dashheader.html")
        else:
            return render(request,"adminlogin.html",{"status":"invalid credentials"})
    else:
        return render(request,'adminlogin.html') 
    

def userlogins(request):
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='registration'
    )
        mycursor=conn.cursor()
        mycursor.execute("select * from customers")
        result=mycursor.fetchall()
        images=[]
        if(result!=None):
            for x in result:
                u=user()
                u.fname=x[0]
                u.lname=x[1]
                u.uname=x[2]
                u.mail=x[3]
                u.phone=x[4]
                u.gen=x[5]
                u.pas=x[6]
                u.cpas=x[7]
                images.append(u)     
            return render(request, 'userlogins.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})



def profile(request):
    uname = ''
    

    if "uname" in request.session:
        uname = request.session["uname"]

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='registration'
    )

    mycursor = conn.cursor()
    

    mycursor.execute("SELECT fname, lname,uname, email, phone FROM designers WHERE uname='" + uname + "'")
    result = mycursor.fetchall()

    images = []

    for x in result:
        a = user()
        a.fname = x[0]
        a.lname = x[1]
        a.uname = x[2]
        
        
        # Check if 'x' tuple has enough elements before accessing
        if len(x) >= 4:
            a.mail = x[3]
        else:
            a.mail = ''  # Set a default value or handle the case as needed
        
        # Check if 'x' tuple has enough elements before accessing
        if len(x) >= 5:
            a.phone = x[4]
        else:
            a.phone = ''  # Set a default value or handle the case as needed

        images.append(a)

    conn.close()

    return render(request, 'profile.html', {"images": images, "MEDIA_URL": settings.MEDIA_URL})



def designerlogins(request):
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='registration'
    )
        mycursor=conn.cursor()
        mycursor.execute("select * from designers")
        result=mycursor.fetchall()
        images=[]
        if(result!=None):
            for x in result:
                d=designer()
                d.fname=x[0]
                d.lname=x[1]
                d.uname=x[2]
                d.mail=x[3]
                d.phone=x[4]
                d.gen=x[5]
                d.qual=x[6]
                d.work=x[7]
                d.id=x[8]
                d.pas=x[9]
                d.cpas=x[10]
                images.append(d)     
            return render(request, 'designerlogins.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})
        
def designerform(request):
    if(request.method=="POST"):
        print("im in post request", request.POST)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        fname=request.POST['fn']
        lname=request.POST['ln']
        uname=request.POST['un']
        mail=request.POST['mail']
        phone=request.POST['pn']
        gender=request.POST['gender']
        qual=request.POST['ql']
        wk=request.POST['wk']
        p=request.POST['pwd']
        id=request.POST['id']
        conpass=request.POST['cpwd']
        mycursor = conn.cursor()
        mycursor.execute("insert into users(fname,lname,uname,email,phone,gender,qual,work,id,pwd,cpwd) values('"+fname+"','"+lname+"','"+uname+"','"+mail+"','"+phone+"','"+gender+"','"+qual+"','"+wk+"','"+id+"','"+p+"','"+conpass+"')")
        conn.commit()    
        return redirect('/homelogout',{"status":"you can login"})
    else:
        return render(request,'designerform.html')

    
def designlog(request):
    if(request.method=="POST"):
        uname=request.POST['un']
        pwd=request.POST['pwd']
        id=request.POST['id']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from designers  where uname='"+uname+"' and pwd='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['uname']=uname
            return render(request,"homelogout.html")
        else:
            return render(request,"login.html",{"status":"invalid credentials"})
    else:
        return render(request,'designlog.html')


def addplogin(request):
    if(request.method=="POST"):
        print(request.POST)
        uname=request.POST.get('un')
        pwd=request.POST.get('pwd')
        id=request.POST.get('id')
        if uname is None:
         return HttpResponse("Login Failed", status=400)


        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        # mycursor.execute("select * from combo where uname='"+uname+"' and id='"+id+"'and pwd='"+pwd+"'")
        mycursor.execute("select * from designers where uname=%s and id=%s and pwd=%s", (uname, id, pwd))

        result=mycursor.fetchone()
        if(result!=None):
            return render(request,"add_designer.html")
        else:
            return render(request,"addplogin.html",{"status":"invalid credentials"})
    else:
        return render(request,'addplogin.html') 
    
def addp(request):
    if(request.method=="POST"):
        uname=request.POST['un']
        id=request.POST['id']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        mycursor.execute("select * from users where uname='"+uname+"' and id='"+id+"'")
        result=mycursor.fetchone()
        if(result!=None):
            return render(request,"add_designer.html")
        else:
            return render(request,"add_designer.html",{"status":"invalid credentials"})
    else:
        return render(request,'designlog.html') 
def dashboard(request):
    return render(request, "dashboard.html")

def dummy(request):
    return render(request, "dummy.html")
def dashheader(request):
    return render(request, "dashheader.html")
def kaali(request):
    return render(request, "kaali.html")
# def homelogout(request):
#     if('uname' not in request.session):
#         return redirect('login')
#     return render(request, "homelogout.html")
def designer_admin(request):
    return render(request, "designer_admin.html")

def header(request):
    return render(request, "header.html")


def fullproduct(request,productId):
     if(request.method=="POST"):
        searchkey=request.POST['search']
        request.session["searchkey"]=searchkey
        return redirect('search')
     else:
        conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
        mycursor=conn.cursor()
        mycursor.execute("select * from products where  productid='"+str(productId+"'"))
        result=mycursor.fetchall()
        images=[]
        if(result!=None):
            for x in result:
                s=Image()
                s.productId=x[0]
                s.image=x[2]
                s.des=x[3]
                s.name=x[1]         
                mycursor1=conn.cursor()
                mycursor1.execute("select * from productslinks where productid="+str(s.productId))
                result1=mycursor1.fetchall()
                links=[]
                if(result1!=None):
                    for y in result1:
                        l=Link()
                        l.linkname=y[1]
                        l.link=y[2]
                        l.productid=y[3]
                        links.append(l)
                s.links=links
                images.append(s)
        return render(request, "fullproduct.html",{"images":images,"MEDIA_URL":settings.MEDIA_URL})
def extra(request):
    if(request.method=="POST"):
        searchkey=request.POST['search']
        request.session["searchkey"]=searchkey
        return redirect('search')
    else:
     return render(request, "extra.html")

def wedding(request):
    if('uname' not in request.session):
        return redirect('signup')
    else:
        conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=501 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'wedding.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})

def wedding_men(request):
    
    if('uname' not in request.session):
        return redirect('signup') 
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=501 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'wedding_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})



def handle_uploaded_file(uploaded_file):
    # Define the directory where you want to save the uploaded files
    upload_dir = 'media'
    
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # Generate a unique file name (you can modify this as needed)
    file_name = os.path.join(upload_dir, uploaded_file.name)
    
    # Open the destination file and save the uploaded file data into it
    with open(file_name, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    
    # Return the path to the saved file
    return file_name

def gridindex(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="registration"        
        )
    mycursor = conn.cursor()
    mycursor.execute("select * from products")
    result=mycursor.fetchall()
    products=[]
    
    if(result!=None):
        for x in result:
            p=Image()
            p.productId=x[0]
            p.name=x[1]
            p.image=x[2]
            p.des=x[3]
            p.links=x[4]
            p.cate=x[5]
            p.gen=x[6]
            products.append(p)
        return render(request,'gridindex.html',{"products":products,"MEDIA_URL":settings.MEDIA_URL})
    else:
        return render(request,'gridindex.html')
    
def griddesigner(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="registration"        
        )
    mycursor = conn.cursor()
    mycursor.execute("select * from products")
    result=mycursor.fetchall()
    products=[]
    
    if(result!=None):
        for x in result:
            p=Image()
            p.productId=x[0]
            p.name=x[1]
            p.image=x[2]
            p.des=x[3]
            p.links=x[4]
            p.cate=x[5]
            p.gen=x[6]
            products.append(p)
        return render(request,'griddesigner.html',{"products":products,"MEDIA_URL":settings.MEDIA_URL})
    else:
        return render(request,'griddesigner.html')    


def add(request):  
    if(request.method=="POST"):
        print(request.method)
        image =request.FILES['image']
        saved_file_path = handle_uploaded_file(image)
        s = saved_file_path.split("\\")
        if len(s) >= 2:
         print(s[1])
        else:
          print("Invalid file path format")

        print(s[1])
        name=request.POST['name']
        des=request.POST['des']
        cate=request.POST['cate']
        gen=request.POST['gen']
        links=str(request.POST['link']).split(',')
        print(links)
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
        mycursor = conn.cursor()
        print("insert into products(name,image,description,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','"+cate+"','"+gen+"')")
       
        # mycursor.execute( "insert into products(name,image,description,links,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','abc','"+cate+"','"+gen+"')")
        mycursor.execute("insert into products(name,image,description,links,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','abc','"+cate+"','"+gen+"')")

        conn.commit()
        #get new product id
        # select top 1 * from products order by desc
        pid=0
        mycursor.execute( "select * from products order by productid desc limit 1")
        result1=mycursor.fetchone()
        if(result1!=None):
            pid=result1[0]

        
        #end get new product id
        for x in links:
            lname=x.split('$')[0]
            link=x.split('$')[1]            
            mycursor.execute( "insert into productslinks(linkname,link,productId) values('"+lname+"','"+link+"','"+str(pid)+"')")
        conn.commit()
        return redirect('add')
    else:
        return render(request,'add.html')
    
def add_designer(request):  
    if(request.method=="POST"):
        print(request.method)
        image =request.FILES['image']
        saved_file_path = handle_uploaded_file(image)
        s = saved_file_path.split("\\")
        if len(s) >= 2:
         print(s[1])
        else:
          print("Invalid file path format")

        print(s[1])
        name=request.POST['name']
        des=request.POST['des']
        cate=request.POST['cate']
        gen=request.POST['gen']
        links=str(request.POST['link']).split(',')
        print(links)
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
        mycursor = conn.cursor()
        print("insert into products(name,image,description,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','"+cate+"','"+gen+"')")
       
        # mycursor.execute( "insert into products(name,image,description,links,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','abc','"+cate+"','"+gen+"')")
        mycursor.execute("insert into products(name,image,description,links,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','abc','"+cate+"','"+gen+"')")

        conn.commit()
        #get new product id
        # select top 1 * from products order by desc
        pid=0
        mycursor.execute( "select * from products order by productid desc limit 1")
        result1=mycursor.fetchone()
        if(result1!=None):
            pid=result1[0]

        
        #end get new product id
        for x in links:
            lname=x.split('$')[0]
            link=x.split('$')[1]            
            mycursor.execute( "insert into productslinks(linkname,link,productId) values('"+lname+"','"+link+"','"+str(pid)+"')")
        conn.commit()
        return redirect('add_designer')
    else:
        return render(request,'add_designer.html')    
# def add_designer(request): 
#     print(request.method) 
#     if(request.method=="POST"):
        
#         image =request.FILES['image']
#         saved_file_path = handle_uploaded_file(image)
#         s=saved_file_path.split("\\")
#         print(s[1])
#         name=request.POST['name']
#         des=request.POST['des']
#         cate=request.POST['cate']
#         gen=request.POST['gen']
#         links=str(request.POST['link']).split(',')
#         print(links)
        
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",    
#             password="",
#             database="registration"        
#             )
#         mycursor = conn.cursor()
#         print("insert into products(name,image,description,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','"+cate+"','"+gen+"')")
       
#         mycursor.execute( "insert into products(name,image,description,links,categoryId,gender) values('"+name+"','"+s[1]+"','"+des+"','abc','"+cate+"','"+gen+"')")
#         conn.commit()
#         #get new product id
#         # select top 1 * from products order by desc
#         pid=0
#         mycursor.execute( "select * from products order by productid desc limit 1")
#         result1=mycursor.fetchone()
#         if(result1!=None):
#             pid=result1[0]

        
#         #end get new product id
#         for x in links:
#             lname=x.split('$')[0]
#             link=x.split('$')[1]            
#             mycursor.execute( "insert into productslinks(linkname,link,productId) values('"+lname+"','"+link+"','"+str(pid)+"')")
#         conn.commit()
#         return redirect('add_designer')
#     else:
#         return render(request,'add_designer.html')

def edit(request,productId):  
      if(request.method=="POST"):
        print(request.method)
        
        image =request.FILES['image']
        saved_file_path = handle_uploaded_file(image)
        s=[]
        if('image' in request.FILES):
            image=request.FILES['image']
            saved_file_path=handle_uploaded_file(image)
            s=saved_file_path.split("\\")
        else:
           image='no file'
           saved_file_path="no"
        #print(s[1])
        name=request.POST['name']
        des=request.POST['des']
        cate=request.POST['cate']
        gen=request.POST['gen']
       
       
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
        mycursor=conn.cursor()
        mycursor.execute( "update products set name='"+name+"',image='"+s[1]+"',description='"+des+"',categoryId="+cate+",gender="+gen+" where productId="+productId)
        conn.commit()
        return redirect("add")
      else:
         conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
         mycursor=conn.cursor()
         mycursor.execute( "select * from products where productId='"+str(productId)+"'")
         result=mycursor.fetchone()
         images=[]
         if(result!=None): 
            i=Image()         
            i.productId=result[0]
            i.name=result[1]
            i.image=result[2]   
            i.des=result[3]
            i.links=result[4]
            i.cate=result[5]
            i.gen=result[6]
         return render(request,'edit.html',{"products":i,"MEDIA_URL":settings.MEDIA_URL})
    

def delete(request,productId):
    print('in delete')
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='registration'
    )
    mycursor = conn.cursor()
    mycursor.execute("delete from productslinks where productId='"+str(productId)+"'")
    mycursor.execute("delete from products where productId='"+str(productId)+"'")
    conn.commit()
    return redirect('gridindex')

def editdesigner(request,productId):  
      if(request.method=="POST"):
        
        image =request.FILES['image']
        saved_file_path = handle_uploaded_file(image)
        s=[]
        if('image' in request.FILES):
            image=request.FILES['image']
            saved_file_path=handle_uploaded_file(image)
            s=saved_file_path.split("\\")
        else:
           image='no file'
           saved_file_path="no"
        #print(s[1])
        name=request.POST['name']
        des=request.POST['des']
        cate=request.POST['cate']
        gen=request.POST['gen']
       
       
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
        mycursor=conn.cursor()
        mycursor.execute( "update products set name='"+name+"',image='"+s[1]+"',description='"+des+"',categoryId="+cate+",gender="+gen+" where productId="+productId)
        conn.commit()
        return redirect("add")
      else:
         conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
         mycursor=conn.cursor()
         mycursor.execute( "select * from products where productId='"+str(productId)+"'")
         result=mycursor.fetchone()
         images=[]
         if(result!=None): 
            i=Image()         
            i.productId=result[0]
            i.name=result[1]
            i.image=result[2]   
            i.des=result[3]
            i.links=result[4]
            i.cate=result[5]
            i.gen=result[6]
         return render(request,'editdesigner.html',{"products":i,"MEDIA_URL":settings.MEDIA_URL})
    

def deletedesigner(request,productId):
    print('in delete')
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='registration'
    )
    mycursor = conn.cursor()
    mycursor.execute("delete from productslinks where productId='"+str(productId)+"'")
    mycursor.execute("delete from products where productId='"+str(productId)+"'")
    conn.commit()
    return redirect('griddesigner')

def loaddata(request):
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]
            s.links=x[4]
            images.append(s)
    return render(request,'loadimages.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})

def load_data(request):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='registration'
    )
    mycursor=conn.cursor()
    mycursor.execute("select * from products")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]
            s.links=x[4]
            images.append(s)
    print(images)       
    return render(request, 'load_data.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})

    
    
def logout(request):
    if("uname" in request.session):
        del request.session['uname']
    return redirect('home')

def session(request):
     if ('email' not in request.session):
        return redirect('home') 
     return render(request,"home")


def ethnic_men(request):
    if('uname' not in request.session):
        return redirect('signup')
    if(request.method=="POST"):
        searchkey=request.POST['search']
        request.session["searchkey"]=searchkey
        return redirect('search')
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=502 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'ethnic_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def ethnic_women(request):
    if('uname' not in request.session):
        return redirect('signup')
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=502 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'ethnic_women.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def workout_men(request):
    if('uname' not in request.session):
        return redirect('signup')
     
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=503 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'workout_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def workout_women(request):
    if('uname' not in request.session):
        return redirect('signup')
    
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=503 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'workout_women.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def party_men(request):
    if('uname' not in request.session):
        return redirect('signup')
     
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=504 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'party_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def party_women(request):
    if('uname' not in request.session):
        return redirect('signup')
     
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=504 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'party_women.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def formal_men(request):
    if('uname' not in request.session):
        return redirect('signup')
    
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=505 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'formal_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def formal_women(request):
    if('uname' not in request.session):
        return redirect('signup')
 
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=505 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'formal_women.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def casual_men(request):
    if('uname' not in request.session):
        return redirect('signup')
     
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=506 and gender=1")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'casual_men.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def casual_women(request):
    if('uname' not in request.session):
        return redirect('signup')
    
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
    mycursor=conn.cursor()
    mycursor.execute("select * from products where categoryId=506 and gender=2")
    result=mycursor.fetchall()
    images=[]
    if(result!=None):
        for x in result:
            s=Image()
            s.productId=x[0]
            s.image=x[2]
            s.des=x[3]
            s.name=x[1]         
            mycursor1=conn.cursor()
            mycursor1.execute("select * from productslinks where productid="+str(s.productId))
            result1=mycursor1.fetchall()
            links=[]
            if(result1!=None):
                for y in result1:
                    l=Link()
                    l.linkname=y[1]
                    l.link=y[2]
                    l.productid=y[3]
                    links.append(l)
            s.links=links
            images.append(s)
    return render(request,'casual_women.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})


def home(request):
    if(request.method=="POST"):
        searchkey=request.POST['search']
        request.session["searchkey"]=searchkey
        return redirect('search')
    else:
        return render(request, 'home.html')
    
def homelogout(request):
    if(request.method=="POST"):
        searchkey=request.POST['search']
        request.session["searchkey"]=searchkey
        return redirect('search')
    else:
        return render(request, 'homelogout.html')    
    
    
   
def search(request):
    searchkey=''
    if("searchkey" in request.session):
        searchkey=request.session["searchkey"]
        print(searchkey)
        conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="registration"
            )
        mycursor=conn.cursor()
        mycursor.execute("select * from products where name='"+searchkey+"'")
        result=mycursor.fetchall()
        images=[]
        if(result!=None):
            for x in result:
                s=Image()
                s.productId=x[0]
                s.image=x[2]
                s.des=x[3]
                s.name=x[1]         
                mycursor1=conn.cursor()
                mycursor1.execute("select * from productslinks where productid="+str(s.productId))
                result1=mycursor1.fetchall()
                links=[]
                if(result1!=None):
                    for y in result1:
                        l=Link()
                        l.linkname=y[1]
                        l.link=y[2]
                        l.productid=y[3]
                        links.append(l)
                s.links=links
                images.append(s)
        return render(request,'search.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})
    else:
        return render(request,'search.html')
    
def forgot_password(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registration"
        )
        mycursor = conn.cursor()
        # retrieve post details
        email = request.POST['email']
        mycursor.execute("SELECT pwd FROM users WHERE email='" + email + "'")
        result = mycursor.fetchone()
        pwd = str(result)
        if result is not None:
            # SMTP server configuration
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'akashbhalshankar474@gmail.com'
            # For App Password, enable 2-step verification, then create an app password
            smtp_password = 'ucpi whqg iocg jlkl'
            # Email content
            subject = 'Password recovery'
            body = 'This is a Password recovery email sent from StyleSphere. ' \
                   'Your password as per registration is: ' + pwd[2:len(pwd) - 3]
            sender_email = 'akashbhalshankar474@gmail.com'
            receiver_email = email
            # Create a message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            # Connect to SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            message = "Password sent to the given email ID"
            return redirect('login')
        else:
            message = "Please enter the correct email ID"
            return render(request, 'forgot_password.html', {'alert_message': message})
    else:
        return render(request, 'forgot_password.html')    
    
def kaali(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="registration"
        )
    if "email" in request.session:
        email = request.session['email']
        mycursor = conn.cursor()
        mycursor.execute("SELECT fname,lname,gender,email,address FROM users WHERE email=%s", (email,))
        result = mycursor.fetchone()
        if result:
            fname,lname,email,phone,gender = result
            customer = {
                'fname': fname,
                'lname': lname,
                'gender':gender,
                'email': email,
                'phone': phone
            }
        else:
            customer = None
    else:
        customer = None
    return render(request, 'kaali.html', {'customer':customer})

def editprofile(request,uname): 
      if request.method=="POST":
        print("hi")
        
        # image =request.FILES['image']
        # saved_file_path = handle_uploaded_file(image)
        # s=[]
        # if('image' in request.FILES):
        #     image=request.FILES['image']
        #     saved_file_path=handle_uploaded_file(image)
        #     s=saved_file_path.split("\\")
        # else:
        #    image='no file'
        #    saved_file_path="no"
        fname=request.POST['fname']
        lname=request.POST['lname']
        mail=request.POST['email']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
        mycursor=conn.cursor()
        mycursor.execute( "update users set fname='"+fname+"',lname='"+lname+"',email="+mail+" where uname="+uname)
        conn.commit()
        return redirect("profile")
      else:
         conn = mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",
            database="registration"        
            )
         mycursor=conn.cursor()
         mycursor.execute( "select * from users where uname='"+str(uname)+"'")
         result=mycursor.fetchone()
         images=[]
         if(result!=None): 
            j=user()         
            j.fname=result[0]
            j.lname=result[1]
            j.phone=result[2]   
            j.mail=result[3]
         return render(request,'editprofile.html',{"images":images,"MEDIA_URL":settings.MEDIA_URL})

