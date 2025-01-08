from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
# Create your views here.

# def home(request):
#     return render(request, "myapp/index.html")

# def about(request):
#     return render(request,"myapp/aboutpage.html")


# def contect(request):
#     return render(request,"myapp/contactpage.html")

# def profile(request):
#     return render(request,"myapp/profilepage.html")


"""
get() : fetch single record from  model it will return an object

            syntax : Model.objects.get(filedname = value..)
            e.g. User.objects.get(email = email)
"""

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/index.html",context)
    else:
        if request.POST:
            print("----->>button clicked")
            email = request.POST['email']
            password = request.POST['password']
            print("-----> email",email)
            print("-----> password",password)
            # print("=======>>> uid :: ",uid)
            # print("-------> email",uid.role)
            # print("-------> password",uid.password)
            try:
                uid = User.objects.get(email = email)
                if uid.password == password:
                    if uid.role == "Chairman":
                        cid = Chairman.objects.get(user_id = uid)
                        print("welcome chairman")
                        context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
                        # store email in session
                        request.session['email'] = email
                        return render(request,"myapp/index.html",context)
                    else:
                        print("Welcome member")
                else:
                    e_msg = "invalid password"
                    return render(request,"myapp/login.html",{'e_msg' : e_msg})

            except Exception as e:
                print("Error: ",e)
                e_msg = "invalid email"
                return render(request,"myapp/login.html",{'e_msg' : e_msg})

        else:
            print("-------> only page is refresh")
        return render(request,"myapp/login.html")

def index(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
            'uid' : uid,
            'cid' : cid
        }
        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")


def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
            'uid' : uid,
            'cid' : cid
        }
        return render(request,"myapp/profile.html",context)
    else:
        return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def notfound(request):
    print("not found page")
    return render(request,"myapp/page404.html")

def change_password(request):
    if request.POST:
        currentPassword = request.POST['currentpassword']
        newPassword = request.POST['newpassword']

        uid = User.objects.get(email = request.session['email'])

        if uid.password == currentPassword:
            uid.password = newPassword
            uid.save() # update
            del request.session['email']
            s_msg = "Successfully password Reset"
            return render (request, "myapp/login.html",{'s_msg' : s_msg})
        else:
            e_msg = "invalid password"
            del request.session['email'] #logout logic
            return render(request,"myapp/login.html",{'e_msg' : e_msg})
    else:
        return render(request,"myapp/login.html")
    
def change_profil_details(request):
    if request.POST:
        currentFname = request.POST['currentFname']
        fname = Chairman.objects.get(email = request.session)

def update_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            cid.firstname = request.POST['firstname']
            cid.lastname = request.POST['lastname']
            cid.contact_no = request.POST['contactno']
            print("----->>> inside the profile pic ")
            if "pic" in request.FILES:
                cid.pic = request.FILES['pic']
                cid.save() # update
                print("-------->>> working")
            
            cid.save()
            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/profile.html",context)
        else:
            return render(request,"myapp/profile.html",context)

def add_member(request):
    
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            contact_no=request.POST['contact_no']
            email=request.POST['email']

            l1=["CN1354","SV1R53G1","A1D65FA4","3X51V5AD45","A1C5SF45","A1C5S31F5"]
            password=email[3:6]+random.choice(l1)+contact_no[3:6]

            user_id=User.objects.create(email=email,password=password,role="member")

            m_id=Members.objects.create(user_id=user_id,
                                        house_no=request.POST['house_no'],
                                        block_no=request.POST['block_no'],
                                        firstname=request.POST['firstname'],
                                        lastname=request.POST['lastname'],
                                        contact_no=contact_no,
                                        family_members=request.POST['family_members'],
                                        vehicle_details=request.POST['vehicle_details'],
                                        blood_group=request.POST['blood_group'],
                                        job_description=request.POST['job_description'],
                                        job_address=request.POST['job_address'],
                                        pic=request.POST['pic'])