import datetime
import json
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from voteApp.models import *



#---------------------------




def login(request):
    return  render(request,"index.html")


def loginverify(request):
    try:
        uname=request.POST['Name']
        pwd=request.POST['Password']
        res=login_table.objects.get(username=uname,password=pwd)
        if res.type=="admin":
            return redirect('/homeadmin')
        elif res.type=="election_cordinator":
            return redirect('/elcodhome')
        else:
            return HttpResponse('''<script>alert("invalid username or password");window.location="/"<script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location="/"<script>''')





def logout(request):
    return render(request, "index.html")
def addstudent(request):
    return  render(request,"admin/add new student.html")

def addnewstudent(request):
    sname = request.POST['textfield']
    ssname = request.POST['textfield8']
    dobb = request.POST['textfield2']
    simage= request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(simage.name, simage)
    phone= request.POST['textfield4']
    semail= request.POST['textfield5']
    uname= request.POST['textfield6']
    pwd= request.POST['textfield7']
    gen=request.POST['Gender']

    ob=login_table()
    ob.username=uname
    ob.password=pwd
    ob.type='student'
    ob.save()
    sob=student_table()
    sob.Fname=sname
    sob.Lname=ssname
    sob.DOB=dobb
    sob.image=fp
    sob.phone_no=phone
    sob.Email=semail
    sob.gender=gen
    sob.LOGIN=ob
    sob.save()




    return HttpResponse('''<script>alert("Successfully Registered");window.location="/student"</script>''')
def homeadmin(request):
    return render(request, "admin/adminindex.html")
def addcourse(request):
    return render(request, "admin/add-course.html")
def addnewcourse(request):
    cname = request.POST['textfield']
    dname = request.POST['textfield2']
    cob=course_table()
    cob.course=cname
    cob.description=dname
    cob.save()
    return HttpResponse('''<script>alert("Successfully Added");window.location="/managecourse"</script>''')

def addnew(request):
    return render(request, "admin/add-new.html")
def addnewelectioncoo(request):
    cname = request.POST['textfield']
    dDOB = request.POST['textfield2']
    iImage = request.FILES['file']
    ff=FileSystemStorage()
    fsave=ff.save(iImage.name,iImage)
    pphoneno = request.POST['textfield4']
    zemail=request.POST['textfield5']
    un=request.POST['textfield6']
    pwd=request.POST['textfield7']
    ob=login_table()
    ob.username=un
    ob.password=pwd
    ob.type='election_cordinator'
    ob.save()
    mob=electioncoordinator_table()
    mob.name=cname
    mob.DOB=dDOB
    mob.image=fsave
    mob.LOGIN=ob
    mob.phone_no=pphoneno
    mob.Email=zemail
    mob.save()
    return HttpResponse('''<script>alert("Successfully Added");window.location="/manageele"</script>''')

def complaint(request):
    ob=complaint_table.objects.all()
    return render(request, "admin/complaint.html",{"val":ob})
def searchcomplaint(request):
    date=request.POST['textfield']
    ob=complaint_table.objects.filter(date=date)
    return render(request, "admin/complaint.html", {'val': ob})
def managecourse(request):
    ob=course_table.objects.all()
    return render(request, "admin/managecourse.html",{'val':ob})


def searchcourse(request):
    course=request.POST['textfield']
    ob=course_table.objects.filter(course__istartswith=course)
    return render(request, "admin/managecourse.html",{'val':ob})



def deletecourse(request,id):
    ob1 = course_table.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/managecourse"</script>''')
def electioncod(request):
    return render(request,"admin/election-coordinator.html")
def deleteelcod(request,id):
    ob1 = login_table.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/manageele"</script>''')

def deleteelectiondate(request,id):
    ob1 = electiondate_table.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/electiondate"</script>''')


def newelection(request):
    return render(request,"admin/NewelectionDate.html")

def newelectiondate(request):
    cpost = request.POST['textfield']
    cdate = request.POST['textfield2']
    cdetails = request.POST['textfield3']
    celecdate = request.POST['textfield4']
    eob=electiondate_table()
    eob.post=cpost
    eob.date=cdate
    eob.details=cdetails
    eob.election_date=celecdate
    eob.save()
    return HttpResponse('''<script>alert("Successfully Added");window.location="/electiondate"</script>''')


def viewfeedback(request):
    ob = Feedback_table.objects.all()
    return render(request, "admin/VIEW FEEDBACK.html", {'val': ob})

def manageele(request):
    ob = electioncoordinator_table.objects.all()
    return render(request, "admin/manage-staff.html", {'val': ob})

def searchmanageele(request):
    name=request.POST['textfield']
    ob=electioncoordinator_table.objects.filter(name__istartswith=name)
    return render(request, "admin/manage-staff.html", {'val':ob})

def reply(request,id):
    request.session['oo']=id
    return render(request, "admin/reply.html")


def sendingreply(request):
    reply=request.POST['textfield']

    ob=complaint_table.objects.get(id=request.session['oo'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert("Reply Sent");window.location="/complaint"</script>''')




def result(request):
    ob = electiondate_table.objects.all()
    return render(request, "admin/result.html",{'val': ob})



def viewresult(request,id):
    # ob = student_table.objects.all()
    ob1 = result_table.objects.get(id=id)
    res_obj = result_table.objects.all()

    data = []
    n_id = []
    for i in res_obj:
        vote_cnt = 0
        if i.NOMINEES.id in n_id:
            pass
        else:
            n_id.append(i.NOMINEES.id)
            # for j in n_id:
            obb = result_table.objects.filter(NOMINEES__id=i.NOMINEES.id)
            for ij in obb:
                vote_cnt = vote_cnt + 1
            row = {"nom": i.NOMINEES.STUDENT.Fname + "" + i.NOMINEES.STUDENT.Lname, "vote": vote_cnt,
                   "date": "2024-04-05"}
            data.append(row)
            print(data, "Hhhhhhhhhhhhhhhhhhhhhhhhhhh")


    return render(request, "admin/viewresult.html",{'val': data})
def student(request):
    ob = student_table.objects.all()
    return render(request, "admin/student.html", {'val': ob})

def searchstudent(request):
    name=request.POST['textfield']
    ob=student_table.objects.filter(Fname__istartswith=name)
    return render(request, "admin/student.html",{'val':ob})


def deletestudent(request,id):
    ob1=login_table.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Successfully deleted");window.location="/student"</script>''')

def viewnom(request):
    ob = nominees_table.objects.all()
    return render(request, "admin/view-nominees.html", {'val': ob})

def searchviewnom(request):
    name=request.POST['textfield']
    ob=nominees_table.objects.filter(STUDENT__Fname__istartswith=name)
    return render(request, "admin/view-nominees.html",{'val':ob})


def elcodhome(request):
    return render(request, "staff/staff.html")
def viewnomec(request):
    ob=nominees_table.objects.all()
    return render(request, "staff/view-nominees-ec.html", {'val': ob})

def accept(request,id):
    ob=nominees_table.objects.get(id=id)
    ob.status='accepted'
    ob1 = student_table.objects.get(id=ob.STUDENT.id)
    email = ob1.Email
    print("##########", email)

    try:
        print("^^^^^^^^^^^")
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('kmadarsh16@gmail.com', 'jrxg cvnm dcvt saka')
        print("login=======")
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Your Nomination for "+ob.ELECTION_DATE.post+" is Accepted")
    print(msg)
    msg['Subject'] = 'E-Voting'
    msg['To'] = email
    msg['From'] = 'kmadarsh16@gmail.com'
    print("ok====")
    # try:
    gmail.send_message(msg)
    ob.save()
    # except Exception as e:
    #     return HttpResponse('''<script>alert('invalid email');window.location='/viewnomec'</script>''')
    return HttpResponse('''<script>alert('sended');window.location='/viewnomec'</script>''')




def reject(request,id):
    ob=nominees_table.objects.get(id=id)
    ob.status='rejected'
    ob1 = student_table.objects.get(id=ob.STUDENT.id)
    email = ob1.Email
    print("##########", email)

    try:
        print("^^^^^^^^^^^")
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('ashikmohammedd4@gmail.com', 'ijfm gqhu plce iezy')
        print("login=======")
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Your Nomination for " + ob.ELECTION_DATE.post + " is Rejected")
    print(msg)
    msg['Subject'] = 'E-Voting'
    msg['To'] = email
    msg['From'] = 'ashikmohammedd4@gmail.com'
    print("ok====")
    try:
        gmail.send_message(msg)
        ob.save()
    except Exception as e:
        return HttpResponse('''<script>alert('invalid email');window.location='/viewnomec'</script>''')

    return HttpResponse('''<script>alert("rejected");window.location="/viewnomec"</script>''')



def votres(request):
    ob = electiondate_table.objects.all()
    return render(request, "staff/voting-result-ec.html", {'val': ob})

def electioncoodviewresult(request,id):
    # ob = student_table.objects.all()
    ob1 = result_table.objects.get(id=id)
    res_obj = result_table.objects.all()

    data = []
    n_id = []
    for i in res_obj:
        vote_cnt = 0
        if i.NOMINEES.id in n_id:
            pass
        else:
            n_id.append(i.NOMINEES.id)
            # for j in n_id:
            obb = result_table.objects.filter(NOMINEES__id=i.NOMINEES.id)
            for ij in obb:
                vote_cnt = vote_cnt + 1
            row = {"nom": i.NOMINEES.STUDENT.Fname + "" + i.NOMINEES.STUDENT.Lname, "vote": vote_cnt,
                   "date": "2024-04-05"}
            data.append(row)
            print(data, "Hhhhhhhhhhhhhhhhhhhhhhhhhhh")


    return render(request, "staff/electioncoodviewresult.html", {'val': data})


def addeditstudent(request,id):
    ob=student_table.objects.get(id=id)
    request.session['eid']=id
    return render(request, "admin/add edit student.html", {'val': ob,"date":str(ob.DOB)})
def addeditstudentadd(request):
    try:
        sname = request.POST['textfield']
        ssname = request.POST['textfield8']
        dobb = request.POST['textfield2']
        image = request.FILES['image']
        fs=FileSystemStorage()
        fp=fs.save(image.name,image)
        phone = request.POST['textfield4']
        semail = request.POST['textfield5']
        gen = request.POST['Gender']

        sob=student_table.objects.get(id=request.session['eid'])


        sob.Fname = sname
        sob.Lname = ssname
        sob.DOB = dobb
        sob.image = fp
        sob.phone_no = phone
        sob.Email = semail
        sob.gender = gen
        sob.save()
    except:
        sname = request.POST['textfield']
        ssname = request.POST['textfield8']
        dobb = request.POST['textfield2']
        phone = request.POST['textfield4']
        semail = request.POST['textfield5']
        gen = request.POST['Gender']

        sob = student_table.objects.get(id=request.session['eid'])

        sob.Fname = sname
        sob.Lname = ssname
        sob.DOB = dobb
        sob.phone_no = phone
        sob.Email = semail
        sob.gender = gen
        sob.save()
    return HttpResponse('''<script>alert("Successfully Edited");window.location="/student"</script>''')




def sendnotification(request):
    return render(request,"admin/SEND NOTIFICATION.html")

def sendnotifications(request):
    cpost = request.POST['textfield']
    ob=notification_table()
    ob.Notification=cpost
    ob.date=datetime.datetime.today()
    ob.save()
    # cdate = request.POST['textfield2']
    # cdetails = request.POST['textfield3']
    # celecdate = request.POST['textfield4']
    # eob=electiondate_table()
    # eob.post=cpost
    # eob.date=cdate
    # eob.details=cdetails
    # eob.election_date=celecdate
    # eob.save()
    return HttpResponse('''<script>alert("Successfully Added");window.location="/sendnotification"</script>''')

def editelectiondate(request,id):
    ob = electiondate_table.objects.get(id=id)
    request.session['eid'] = id
    return render(request, "admin/editelectiondate.html",{"val":ob,"date":str(ob.date)})


def electiondate(request):
    ob = electiondate_table.objects.all()
    return render(request, "admin/electiondate.html", {'val': ob})
def searchdate(request):
    date=request.POST['textfield']
    ob=electiondate_table.objects.filter(date=date)
    return render(request, "admin/electiondate.html", {'val': ob})


def addeditelectiondate(request):
    cpost = request.POST['textfield']
    cdate = request.POST['textfield2']
    cdetails = request.POST['textfield3']
    celecdate = request.POST['textfield4']
    eob = electiondate_table(id=request.session['eid'])
    eob.post = cpost
    eob.date = cdate
    eob.details = cdetails
    eob.election_date = celecdate
    eob.save()
    return HttpResponse('''<script>alert("Successfully Edited");window.location="/electiondate"</script>''')
def editelectioncood(request,id):
    ob = electioncoordinator_table.objects.get(id=id)
    request.session['eid'] = id
    return render(request, "admin/editcoo.html",{"val":ob,"date":str(ob.DOB)})
def addeditelectioncood(request):
    try:
        cname = request.POST['textfield']
        dDOB = request.POST['textfield2']
        iImage = request.FILES['file']
        ff = FileSystemStorage()
        fsave = ff.save(iImage.name, iImage)
        pphoneno = request.POST['textfield4']
        zemail = request.POST['textfield5']

        mob = electioncoordinator_table.objects.get(id=request.session['eid'])
        mob.name = cname
        mob.DOB = dDOB
        mob.image = fsave
        mob.phone_no = pphoneno
        mob.Email = zemail
        mob.save()
        return HttpResponse('''<script>alert("Successfully Edited");window.location="/manageele"</script>''')
    except:
        cname = request.POST['textfield']
        dDOB = request.POST['textfield2']
        pphoneno = request.POST['textfield4']
        zemail = request.POST['textfield5']

        mob = electioncoordinator_table.objects.get(id=request.session['eid'])
        mob.name = cname
        mob.DOB = dDOB
        mob.phone_no = pphoneno
        mob.Email = zemail
        mob.save()
        return HttpResponse('''<script>alert("Successfully Edited");window.location="/manageele"</script>''')





#________________________________WEBSERVICE________________________________





def login_code(request):
        print(request.POST)
        un = request.POST['username']
        pwd = request.POST['password']
        print(un, pwd)
        try:
            ob = login_table.objects.get(username=un, password=pwd)

            if ob is None:
                data = {"task": "invalid"}
            else:
                print("in user function")
                data = {"task": "valid", "lid": ob.id, "type": ob.type}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        except:
            data = {"task": "invalid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)



import random

def registration(request):
    firstname = request.POST['Firstname']
    lastname = request.POST['Lastname']
    phone = request.POST['phone']
    gender = request.POST['Gender']
    rollno = request.POST['rollno']
    dob = request.POST['dob']
    image = request.FILES['image']
    fs=FileSystemStorage()
    fp=fs.save(image.name,image)
    email_id = request.POST['Email']
    username = request.POST['Username']
    password = request.POST['Password']

    lob = login_table()
    lob.username = username
    lob.password = password
    lob.type = 'student'
    lob.save()

    user_obj = student_table()
    user_obj.LOGIN=lob
    user_obj.Fname = firstname
    user_obj.RollNo = rollno
    user_obj.Lname = lastname
    user_obj.DOB = dob
    user_obj.gender = gender
    user_obj.image = fp
    user_obj.phone_no = phone
    user_obj.Email = email_id
    user_obj.save()

    # random_number = random.randint(1000, 9999)
    # makeimg(str(random_number),str(lob.id)+".png")
    # encryption(str(lob.id)+".png")
    # qry = student_table.objects.all()
    # res = selectall(qry)
    # result=[]
    # for i in qry:
    #     row = [i.id, r"C:\Users\JASMINE\OneDrive\Desktop\pg\e_voting\e_voting\media/"+str(i.image.url)]
    #     result.append(row)

    # enf(result)
    data = {"data": "ok","res":str(lob.id)+".png"}
    r = json.dumps(data)
    return HttpResponse(r)


def send_complaint_app(request):
    complaints = request.POST["com"]
    lid = request.POST["lid"]
    date = datetime.datetime.now()
    reply = "pending"
    complaint_obj = complaint_table()
    complaint_obj.complaint = complaints
    complaint_obj.date = date
    complaint_obj.reply = reply
    complaint_obj.STUDENT = student_table.objects.get(LOGIN__id=lid)
    complaint_obj.save()
    data = {'task':'success'}
    r = json.dumps(data)
    return HttpResponse(r)


def send_feedback_app(request):
    complaints = request.POST["feedback"]
    lid = request.POST["lid"]
    date = datetime.datetime.now()
    reply = "pending"
    complaint_obj = Feedback_table()
    complaint_obj.feedback = complaints
    complaint_obj.date = date
    complaint_obj.STUDENT = student_table.objects.get(LOGIN__id=lid)
    complaint_obj.save()
    data = {'task':'success'}
    r = json.dumps(data)
    return HttpResponse(r)



# def sendnomination(request):
#     u_id = request.POST["uid"]
#     eid = request.POST["eid"]
#     date = datetime.datetime.now()
#     ob=nominees_table.objects.filter(STUDENT__LOGIN__id=u_id,ELECTION_DATE__id=eid)
#
#     if len(ob)==0:
#
#         complaint_obj = nominees_table()
#         complaint_obj.status = 'pending'
#         complaint_obj.date = date
#         complaint_obj.ELECTION_DATE = electiondate_table.objects.get(id=eid)
#         complaint_obj.STUDENT = student_table.objects.get(LOGIN__id=u_id)
#         complaint_obj.save()
#         data = {'task': 'success'}
#         r = json.dumps(data)
#         return HttpResponse(r)
#     else:
#         data = {'task': 'not'}
#         r = json.dumps(data)
#         return HttpResponse(r)


import datetime
import json
from django.http import HttpResponse
from .models import nominees_table, electiondate_table, student_table

def sendnomination(request):
    u_id = request.POST["uid"]
    eid = request.POST["eid"]
    date = datetime.datetime.now()
    # Get the election date object
    try:
        election = electiondate_table.objects.get(id=eid)
    except electiondate_table.DoesNotExist:
        return HttpResponse(json.dumps({'task': 'invalid_election'}), content_type="application/json")

    # Check if election is within 5 days from now
    days_difference = (election.election_date - date.date()).days
    if days_difference > 5:
        return HttpResponse(json.dumps({'task': 'too_early'}), content_type="application/json")

    # Check if the user has already nominated for any post in this election
    existing_nomination = nominees_table.objects.filter(STUDENT__LOGIN__id=u_id, ELECTION_DATE__id=eid)
    if existing_nomination.exists():
        return HttpResponse(json.dumps({'task': 'already_nominated'}), content_type="application/json")

    # Save the nomination
    nomination_obj = nominees_table()
    nomination_obj.status = 'pending'
    nomination_obj.date = date
    nomination_obj.ELECTION_DATE = election
    nomination_obj.STUDENT = student_table.objects.get(LOGIN__id=u_id)
    nomination_obj.save()

    return HttpResponse(json.dumps({'task': 'success'}), content_type="application/json")




def face_verification_fn(request):
    # try:
        print(request.FILES)
        print(request.POST)
        img=request.FILES['image']
        lid = request.POST["lid"]
        fs=FileSystemStorage()
        fn=fs.save(img.name,img)

        print("##############",fn)
        print("=================================")
        print("=================================")
        print("=================================")
        print("=================================")
        # img=cv2.imread(r"C:\Users\JASMINE\OneDrive\Desktop\pg\e_voting\e_voting\media/"+str(fn))
        # img=cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
        # cv2.imwrite(r"C:\Users\JASMINE\OneDrive\Desktop\pg\e_voting\e_voting\media/"+str(fn),img)

        enf(r"E:\e_voting\media/"+str(fn))
        print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        obu=student_table.objects.get(LOGIN__id=lid)
        print(r"E:\e_voting\media/"+str(obu.image))
        print("***********************************************")
        print("***********************************************")
        print("***********************************************")
        print(obu.Fname,obu.Lname,"+++++++++++++")
        print(r"E:\e_voting\media/"+str(obu.image))
        res=rec_face_image(r"E:\e_voting\media/"+str(obu.image))
        print(res,"res================+++++++++")
        if len(res)>0:
            print("okkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            data = {'task': 'success'}
            r = json.dumps(data)
            return HttpResponse(r)
        else:
            print("naaaaa")
            data = {'task': 'invalid'}
            r = json.dumps(data)
            return HttpResponse(r)
    # except:
    #     print("naaaaa")
    #     data = {'task': 'invalid'}
    #     r = json.dumps(data)
    #     return HttpResponse(r)


# import os
# import json
# import cv2
# import numpy as np
# from PIL import Image
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from .models import student_table
# import face_recognition
#
# def face_verification_fn(request):
#     try:
#         print(request.FILES)
#         print(request.POST)
#
#         if 'image' not in request.FILES or 'lid' not in request.POST:
#             return HttpResponse(json.dumps({'task': 'invalid_request'}), content_type="application/json")
#
#         img = request.FILES['image']
#         lid = request.POST["lid"]
#
#         # Save uploaded file
#         fs = FileSystemStorage()
#         fn = fs.save(img.name, img)
#         image_path = os.path.join(fs.location, fn)
#
#         print(f"🖼️ Saved Image Path: {image_path}")
#
#         # ✅ Step 1: Open the image using PIL and convert to RGB
#         try:
#             with Image.open(image_path) as pil_img:
#                 print(f"Original Image Mode: {pil_img.mode}")  # Debug image format
#                 pil_img = pil_img.convert("RGB")  # Convert to RGB if not already
#                 pil_img.save(image_path, format="JPEG")  # Save in a known format
#         except Exception as e:
#             print("🚨 Error processing image with PIL:", e)
#             return HttpResponse(json.dumps({'task': 'image_processing_error'}), content_type="application/json")
#
#         # ✅ Step 2: Read the image using OpenCV
#         image = cv2.imread(image_path)
#
#         if image is None:
#             print("🚨 Error: Image not loaded properly (cv2.imread returned None)!")
#             return HttpResponse(json.dumps({'task': 'image_error'}), content_type="application/json")
#
#         print("📸 Image successfully loaded with OpenCV.")
#
#         # ✅ Step 3: Convert image to RGB
#         try:
#             image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         except Exception as e:
#             print(f"🚨 Error converting image to RGB: {e}")
#             return HttpResponse(json.dumps({'task': 'color_conversion_error'}), content_type="application/json")
#
#         print("🎨 Image converted to RGB format.")
#
#         # ✅ Step 4: Detect faces
#         face_locations = face_recognition.face_locations(image_rgb)
#
#         if not face_locations:
#             print("🚫 No face detected in the uploaded image!")
#             return HttpResponse(json.dumps({'task': 'no_face_detected'}), content_type="application/json")
#
#         print("✅ Face detected!")
#
#         # ✅ Step 5: Fetch user image from the database
#         obu = student_table.objects.get(LOGIN__id=lid)
#         user_image_path = os.path.join("E:/e_voting/media/", str(obu.image))
#
#         print(f"🔎 User Image Path: {user_image_path}")
#
#         # ✅ Step 6: Read stored user image
#         user_image = cv2.imread(user_image_path)
#
#         if user_image is None:
#             print("🚨 Error: User image not found or unreadable!")
#             return HttpResponse(json.dumps({'task': 'user_image_not_found'}), content_type="application/json")
#
#         print("✅ User image successfully loaded.")
#
#         # ✅ Step 7: Convert stored user image to RGB
#         try:
#             user_image_rgb = cv2.cvtColor(user_image, cv2.COLOR_BGR2RGB)
#         except Exception as e:
#             print(f"🚨 Error converting stored user image to RGB: {e}")
#             return HttpResponse(json.dumps({'task': 'user_color_conversion_error'}), content_type="application/json")
#
#         # ✅ Step 8: Encode faces
#         uploaded_encodings = face_recognition.face_encodings(image_rgb)
#         stored_encodings = face_recognition.face_encodings(user_image_rgb)
#
#         if not uploaded_encodings or not stored_encodings:
#             print("🚨 Face encoding failed! No encodings found.")
#             return HttpResponse(json.dumps({'task': 'face_encoding_failed'}), content_type="application/json")
#
#         print("✅ Face successfully encoded!")
#
#         # ✅ Step 9: Compare faces
#         results = face_recognition.compare_faces([stored_encodings[0]], uploaded_encodings[0])
#
#         if results[0]:
#             print("✅ Face Match Successful!")
#             return HttpResponse(json.dumps({'task': 'success'}), content_type="application/json")
#         else:
#             print("❌ Face Not Recognized!")
#             return HttpResponse(json.dumps({'task': 'invalid'}), content_type="application/json")
#
#     except Exception as e:
#         print(f"🚨 General Error: {e}")
#         return HttpResponse(json.dumps({'task': 'error', 'message': str(e)}), content_type="application/json")
#

def reply_app(request):
    print(request.POST,"kkkkkkkkkkkk")
    user_id = request.POST['lid']
    complaint_obj = complaint_table.objects.filter(STUDENT__LOGIN__id=user_id)
    print(complaint_obj,"llll")
    data = []
    for i in complaint_obj:
        row = {'Complaint': i.complaint,'id':i.id, 'Reply': i.reply, 'Date':str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def viewnotificationmmm(request):
    print(request.POST,"kkkkkkkkkkkk")

    complaint_obj = notification_table.objects.all()
    print(complaint_obj,"llll")
    data = []
    for i in complaint_obj:
        row = {'notification': i.Notification,'id':i.id, 'Date':str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def viewfeedbackk(request):
    print(request.POST,"kkkkkkkkkkkk")
    user_id = request.POST['lid']
    complaint_obj = Feedback_table.objects.filter(STUDENT__LOGIN__id=user_id)
    print(complaint_obj,"llll")
    data = []
    for i in complaint_obj:
        row = {'feedback': i.feedback,'id':i.id, 'Date':str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def viewnominee (request):
    # user_id = request.POST['lid']
    # print("OOOOOOOOOOOOOO", user_id)
    p_id = request.POST['pid']
    complaint_obj = nominees_table.objects.filter(status="accepted",ELECTION_DATE_id=p_id )
    data = []
    for i in complaint_obj:
        row = {'student': i.STUDENT.Fname+ " "+ i.STUDENT.Lname, 'electiondate': str(i.ELECTION_DATE.election_date), 'status': i.status, 'date': str(i.date),'id':i.id,'lid':i.STUDENT.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    print("^^^^^^^^^^^^^^^^^^^^", data)
    return HttpResponse(r)




def viewnomineeonly (request):
    # user_id = request.POST['lid']
    # print("OOOOOOOOOOOOOO", user_id)

    complaint_obj = nominees_table.objects.filter(status="accepted" )
    data = []
    for i in complaint_obj:
        row = {'student': i.STUDENT.Fname+ " "+ i.STUDENT.Lname, 'electiondate': str(i.ELECTION_DATE.election_date), 'status': i.status, 'date': str(i.date),'id':i.id,'lid':i.STUDENT.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    print("^^^^^^^^^^^^^^^^^^^^", data)
    return HttpResponse(r)

def viewelectiondate (request):
    # user_id = request.POST['lid']
    # print("OOOOOOOOOOOOOO", )
    complaint_obj = electiondate_table.objects.all()
    data = []
    for i in complaint_obj:
        row = {'electiondate': str(i.election_date), 'post': i.post, 'details': i.details,'id':i.id}
        data.append(row)
    r = json.dumps(data)
    print("^^^^^^^^^^^^^^^^^^^^", data)
    return HttpResponse(r)


def electipndat (request):
    # user_id = request.POST['lid']
    complaint_obj = electiondate_table.objects.all()
    data = []
    for i in complaint_obj:
        row = {'electiondate': str(i.election_date), 'post': i.post,'details': i.details, 'date': str(i.date),'id':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def viewpost (request):
    # user_id = request.POST['lid']
    complaint_obj = electiondate_table.objects.all()
    data = []
    for i in complaint_obj:
        row = {'post': i.post,'details': i.details,'id':i.id}
        data.append(row)
    r = json.dumps(data)
    print("%%%%%%%%%%%%%%", r)
    return HttpResponse(r)

def resultt(request):
    # lid = request.POST['lid']
    postid = request.POST['postid']
    res_obj = result_table.objects.filter(NOMINEES__ELECTION_DATE__id=postid)
    data =[]
    n_id = []
    for i in res_obj:
        vote_cnt = 0
        if i.NOMINEES.id in n_id:
            pass
        else:
            n_id.append(i.NOMINEES.id)
    # for j in n_id:
            obb=result_table.objects.filter(NOMINEES__id=i.NOMINEES.id)
            for ij in obb:
                vote_cnt=vote_cnt+1
            row={"nom":i.NOMINEES.STUDENT.Fname+""+i.NOMINEES.STUDENT.Lname,"vote":str(vote_cnt),"date":"2024-04-05"}
            data.append(row)
            print(data,"Hhhhhhhhhhhhhhhhhhhhhhhhhhh")


    # # for i in n_id:
    # #
    # #
    # # for i in res_obj:
    # #     row = {'student': i.NOMINEES.STUDENT.Fname+ " "+ i.NOMINEES.STUDENT.Lname,'electiondate': str(i.NOMINEES.ELECTION_DATE.election_date), 'vote': i.vote }
    # #     data.append(row)


    # data = []
    # data2 = []
    # with open(
    #         r'C:\Users\JASMINE\OneDrive\Desktop\pg\e_voting\e_voting\node_modules\.bin\build\contracts\Structreq.json') as file:
    #     contract_json = json.load(file)  # load contract info as JSON
    #     contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    # contract = web3.eth.contract(address='0xFfe2F173a85085b20182f768616372b59bC11873', abi=contract_abi)
    # blocknumber = web3.eth.get_block_number()
    # for i in range(blocknumber, 24, -1):
    #     try:
    #         a = web3.eth.get_transaction_by_block(i, 0)
    #         decoded_input = contract.decode_function_input(a['input'])
    #         if int(decoded_input[1]['postid']) == int(postid):
    #             data.append(decoded_input[1])
    #         print(data, "*********************", decoded_input[1]['charityid'])
    #     except Exception as e:
    #         print(e)
    #         pass
    #
    #
    # print(data, "==============================")
    # candid_lis=[]
    # v=0
    # for i in data:
    #     # if i.candid in candid_lis:
    #     #     v=v+1
    #     # else:
    #     candid_lis.append(i["candid"])

    # from collections import Counter
    #
    # # Count the occurrences of each element
    # element_counts = Counter(candid_lis)
    # print(element_counts,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # print(element_counts,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # print(element_counts,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # print(element_counts,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # print(element_counts,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
    # x1=[]
    # x2=[]
    # # Print the counts
    # try:
    #     for element, count in element_counts.items():
    #
    #             ob=student_table.objects.filter(id=element)
    #             print(ob,"hhhhhhhhhhhhhhhhhhhh")
    #             row={"nom":ob[0].Fname+ " "+ob[0].Lname,"vote":count}
    #             data2.append(row)
    # except:
    #     pass





    # for i in data:






    r = json.dumps(data)
    return HttpResponse(r)



import subprocess
def vote(request):
    u_id = request.POST["id"]
    lidd = request.POST["lid"]
    on=result_table.objects.filter(STUDENT__LOGIN__id=lidd)
    if len(on)==0:
        complaint_obj = result_table()
        complaint_obj.NOMINEES = nominees_table.objects.get(id=u_id)
        complaint_obj.vote='1'
        complaint_obj.STUDENT=student_table.objects.get(LOGIN__id=lidd)
        complaint_obj.save()

        nn=nominees_table.objects.get(id=u_id)
        kk=nn.STUDENT.id
        postid=nn.ELECTION_DATE.id
        # with open(
        #         r'E:\e_voting\node_modules\.bin\build\contracts\Structreq.json') as file:
        #     contract_json = json.load(file)  # load contract info as JSON
        #     contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        # contract = web3.eth.contract(address='0x7194B83b6D13743547bD2523766CbABf1ab894d1', abi=contract_abi)
        # blocknumber = web3.eth.get_block_number()
        # message2 = contract.functions.addreq(blocknumber + 1, str(postid), str(kk),
        #                                       str(datetime.datetime.now().strftime("%Y-%m-%d")),
        #                                       ).transact({"from":web3.eth.accounts[0]})
        data=str(postid)+"#"+str(kk)
        response = subprocess.run(
            [r'C:\Users\USER\AppData\Local\Programs\Python\Python36\python',
             r'D:\germany\Deep Fake\Deepfake\app\predict_vidio_fn.py'],  # Replace with your script or command
            input=data.encode('utf-8')
            # The input to be provided to the subprocess
            # Capture the error (if any)

        )
        data = {'task': 'success'}
        r = json.dumps(data)
        return HttpResponse(r)
    else:
        data = {'task': 'not'}
        r = json.dumps(data)
        return HttpResponse(r)




def forgot_password(request):
    print(request.POST)
    try:
        print("1")
        print(request.POST)

        email = request.POST['email']
        uname = request.POST['uname']
        print(email)
        s=student_table.objects.get(Email=email,LOGIN__username=uname)
        # qry = "SELECT `login`.`password` FROM `student`  JOIN `login` ON `login`.`L_id` = `student`.`L_id` WHERE email=%s"
        # s = selectone(qry, email)
        print(s, "=============")
        if s is None:
            data = {'task': 'invalid'}
            r = json.dumps(data)
            return HttpResponse(r)
            # return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')

            # return jsonify({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('ashikmohammedd4@gmail.com', 'Aswq12@@')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your new password id : " + str(s.LOGIN.password))
            print(msg)
            msg['Subject'] = 'OutPass'
            msg['To'] = email
            msg['From'] = 'ashikmohammedd4@gmail.com'
            print("ok====")
            try:
                gmail.send_message(msg)
            except Exception as e:
                data = {'task': 'invalid'}
                r = json.dumps(data)
                return HttpResponse(r)
                # return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')
            data = {'task': 'valid'}
            r = json.dumps(data)
            return HttpResponse(r)
            # return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
    except Exception as e:
        print(e)
        data = {'task': 'invalid'}
        r = json.dumps(data)
        return HttpResponse(r)
        # return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')

def cryptophotoupload(request):
    print(request.FILES,"pppppppppppp")
    file = request.FILES['image']
    lid = request.POST['lid']
    u_id=request.POST["nid"]
    postid=request.POST["pid"]
    ob=student_table.objects.get(LOGIN__id=lid)
    fss = FileSystemStorage()
    fn=fss.save(file.name, file)
    print(fn, "pppppppjjjjjjjjjjjjjjjjjjjjjjjjjjppppp")
    # res=decription(str(ob.id)+".png",fn)
    # print(res,"iiiiiiiiiiiiiiiiiiiiiiiii")
    # if res=="true":
    #     print("rrrrrrrrrrrr")


        #_________________________block chain_________________

    lidd = request.POST["lid"]
    on = result_table.objects.filter(STUDENT__LOGIN__id=lidd,NOMINEES__ELECTION_DATE__id=postid)
    if len(on) == 0:
        print("iiiiiiiiiiiiii")
        complaint_obj = result_table()
        complaint_obj.NOMINEES = nominees_table.objects.get(id=u_id)
        complaint_obj.vote = '1'
        complaint_obj.STUDENT = student_table.objects.get(LOGIN__id=lidd)
        complaint_obj.save()
        nn = nominees_table.objects.get(id=u_id)
        kk = nn.STUDENT.id
        postid = nn.ELECTION_DATE.id
        # with open(
        #         r'E:\e_voting\node_modules\.bin\build\contracts\Structreq.json') as file:
        #     contract_json = json.load(file)  # load contract info as JSON
        #     contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        # contract = web3.eth.contract(address='0x7194B83b6D13743547bD2523766CbABf1ab894d1', abi=contract_abi)
        # blocknumber = web3.eth.get_block_number()
        # message2 = contract.functions.addreq(blocknumber + 1, str(postid), str(kk),
        #                                      str(datetime.datetime.now().strftime("%Y-%m-%d")),
        #                                      ).transact({"from": web3.eth.accounts[0]})
        data = str(postid) + "-" + str(kk)
        response = subprocess.run(
            [r'C:\Users\orchid\AppData\Local\Programs\Python\Python310\python',
             r'E:\e_voting\voteApp\block.py'],  # Replace with your script or command
            input=data.encode('utf-8')
            # The input to be provided to the subprocess
            # Capture the error (if any)

        )
        data = {'task': 'success'}
        r = json.dumps(data)
        return HttpResponse(r)


    #---------------------------------------------
        img1=cv2.imread(r"E:\e_voting\media\img/"+str(ob.id)+".png")
        img2=cv2.imread(r"E:\e_voting\media\final/"+str(ob.id)+".png")
        print(type(img1),type(img2))
        print(str(img1))
        if str(img1)==str(img2):
            print("oooooooo")
            data = {'task': 'success'}
            r = json.dumps(data)
            return HttpResponse(r)
        else:
            print("5555555555")
            data = {'task': 'invalid'}
            r = json.dumps(data)
            return HttpResponse(r)


    else:
        print("999999999")
        data = {'task': 'not'}
        r = json.dumps(data)
        return HttpResponse(r)
    data = {'task': 'invalid'}
    r = json.dumps(data)
    return HttpResponse(r)




