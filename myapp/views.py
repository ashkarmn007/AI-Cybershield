import base64
import random
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt

from .sample import requestReview

# Create your views here.
from myapp.models import *


def login_get(request):
    return render(request,'login_index.html')

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    # print(username,password)
    user=authenticate(request,username=username,password=password)
    if user is not None:
        if user.groups.filter(name="admin").exists():
            login(request,user)
            return redirect('/myapp/admin_index1/')
        elif user.groups.filter(name="Expert").exists():
            uu=expert_table.objects.get(LOGIN=user.id)
            if uu.status == 'accepted':
                login(request,user)
                print(request.user)
                return redirect('/myapp/expert_index/')
            else:
                messages.warning(request, "Verification Pending")
                return redirect('/myapp/login_get/')
        else:
             messages.warning(request,"Invalid username or password")
             return redirect('/myapp/login_get/')

    return redirect('/myapp/login_get/')


def verify_expert(request):
    a=expert_table.objects.all()
    return render(request,'admin/verify.html',{'data':a})



def accept_expert(request,id):
    b=expert_table.objects.filter(id=id).update(status='accepted')
    return redirect('/myapp/verify_expert/')
def reject_expert(request,id):
    b=expert_table.objects.filter(id=id).update(status='rejected')
    return redirect('/myapp/verify_expert/')

def view_users(request):
    var=user_table.objects.all()
    return render(request,'admin/viewuser.html',{'data':var})
def change_password(request):
    return render(request,'admin/changepass.html')

def change_password_post(request):
    old=request.POST['old']
    new=request.POST['new']
    confirm=request.POST['confirm']
    print(old,new,confirm)
    user = request.user
    if not user.check_password(old):
        messages.error(request, "Old password is incorrect")
        return redirect('/myapp/changepass2/')
    if new != confirm:
        messages.error(request, "New passwords do not match")
        return redirect('/myapp/changepass2/')
    user.set_password(new)
    user.save()
    update_session_auth_hash(request, user)
    messages.success(request, "Your password was successfully updated")
    return redirect('/myapp/login_get/')

def view_complaint(request):
    var=complaint.objects.all()
    return render(request,'admin/complaint.html',{'data':var})

def sent_reply(request,id):
    var=complaint.objects.get(id=id)
    request.session['id']=id
    return render(request,'admin/sendreply.html')

def sent_reply_post(request):
    Reply=request.POST['Reply']
    print(Reply)
    var=complaint.objects.get(id=request.session['id'])
    var.reply=Reply
    var.status='Replied'
    var.save()
    return redirect('/myapp/view_complaint/')

def view_feedback(request):
    var=rewview_rating.objects.all()
    return render(request,'admin/feedback.html',{'data':var})

def forgot_pass(request):
    return render(request,'admin/forgot.html')

def forgot_pass_post(request):
    email=request.POST['email']
    print(email)
    return HttpResponse("ok")

def admin_index(request):
    return render(request,'admin/admin_index1.html')


# expert=========================================


def register_get(request):
    return render(request,'expert/register.html')
def register_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    qualification=request.POST['qualification']
    post=request.POST['post']
    c=request.FILES['certificate']


    username=request.POST['username']
    password=request.POST['password']

    ex2 = expert_table()

    fs=FileSystemStorage()
    path=fs.save(c.name,c)
    if 'certificate1' in request.FILES:
        c1 = request.FILES['certificate1']
        path1 = fs.save(c1.name,c1)
        ex2.certificate1 = path1

    if 'certificate2' in request.FILES:
        c2 = request.FILES['certificate2']
        path2=fs.save(c2.name,c2)
        ex2.certificate2 = path2


    if User.objects.filter(username=username).exists():
        messages.error(request,'Usernmae already existed....!!!!')
        return redirect('/myapp/register_get')
    if User.objects.filter(email=email).exists():
        messages.error(request,'Email already existed....!!!!')
        return redirect('/myapp/register_get')

    ex=User.objects.create(username=username, password=make_password(password), email=email,first_name=name)
    ex.save()
    ex.groups.add(Group.objects.get(name="Expert"))



    ex2.LOGIN=ex
    ex2.name=name
    ex2.email=email
    ex2.phone=phone
    ex2.place=place
    ex2.qualification=qualification
    ex2.post=post
    ex2.certificate=path
    # ex2.certificate1=path1
    # ex2.certificate2=path2


    ex2.status='pending'
    ex2.save()




    return redirect('/myapp/login_get/')
def add_new(request):
    return render(request,'expert/add new.html')

def add_new_post(request):
    title=request.POST['title']
    details=request.POST['details']
    video=request.FILES['video']
    print(title,details)
    fs=FileSystemStorage()
    path=fs.save(video.name,video)
    c=tips_table()
    c.EXPERT=expert_table.objects.get(LOGIN=request.user.id)
    c.title=title
    c.details=details
    c.video=path
    c.date=datetime.now().today()
    c.save()
    return redirect('/myapp/manage_view/')


def addvdo(request):

    return render(request,'expert/addvdo.html')

def addvdo_post(request):
    video=request.FILES['video']
    title=request.POST['title']

    fs=FileSystemStorage()
    path=fs.save(video.name,video)

    print(video,title)
    dv=video_table()

    expert = expert_table.objects.get(LOGIN_id=request.user.id)

    dv.EXPERT=expert
    dv.video=path
    dv.title=title
    dv.date=datetime.now().today()
    dv.save()
    return redirect('/myapp/video/')



def changepass2(request):
    return render(request,'expert/changepass2.html')

def changepass2_post(request):
    old=request.POST['old']
    new=request.POST['new']
    confirm=request.POST['confirm']
    print(old,new,confirm)
    user=request.user
    if not user.check_password(old):
        messages.error(request,"Old password is incorrect")
        return redirect('/myapp/changepass2/')
    if new!=confirm:
        messages.error(request,"New passwords do not match")
        return redirect('/myapp/changepass2/')
    user.set_password(new)
    user.save()
    update_session_auth_hash(request,user)
    messages.success(request,"Your password was successfully updated")
    return redirect('/myapp/expert_index/')


def doubts(request):
    return render(request,'expert/doubts.html')


def edit_profile(request):
    y=expert_table.objects.get(LOGIN__id=request.user.id)
    return render(request,'expert/editprofile.html',{'data':y})


# def edit_profile_post(request):
#     name=request.POST['name']
#     email=request.POST['email']
#     phone=request.POST['phone']
#     place=request.POST['place']
#     qualification=request.POST['qualification']
#     post=request.POST['post']
#     ob=expert_table.objects.get(LOGIN__id=request.user.id)
#     ob.name=name
#     ob.email=email
#     ob.phone=phone
#     ob.place=place
#     ob.qualification=qualification
#     ob.post=post
#     ob.save()
#     return redirect('/myapp/expert_index/')


def edit_profile_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    qualification = request.POST['qualification']
    post = request.POST['post']

    ob = expert_table.objects.get(LOGIN__id=request.user.id)

    ob.name = name
    ob.email = email
    ob.phone = phone
    ob.place = place
    ob.qualification = qualification
    ob.post = post

    # handle file updates
    from django.core.files.storage import FileSystemStorage
    fs = FileSystemStorage()

    if 'certificate' in request.FILES:
        c = request.FILES['certificate']
        ob.certificate = fs.save(c.name, c)

    if 'certificate1' in request.FILES:
        c1 = request.FILES['certificate1']
        ob.certificate1 = fs.save(c1.name, c1)

    if 'certificate2' in request.FILES:
        c2 = request.FILES['certificate2']
        ob.certificate2 = fs.save(c2.name, c2)

    ob.save()

    return redirect('/myapp/expert_index/')

def deletecert1(request,id):
    d=expert_table.objects.get(id=id)
    d.certificate1.delete()
    return redirect('/myapp/profile')

def deletecert2(request,id):
    d=expert_table.objects.get(id=id)
    d.certificate2.delete()
    return redirect('/myapp/profile')

def edittip (request,id):
    f=tips_table.objects.get(id=id)
    request.session['tid']=id
    return render(request,'expert/edittip.html',{'data':f})
def edittip_post(request):
    title=request.POST['title']
    details=request.POST['details']
    c = tips_table.objects.get(id=request.session['tid'])
    if 'video' in request.FILES:
        video=request.FILES['video']
        fs=FileSystemStorage()
        path=fs.save(video.name,video)
        c.video = path
        c.save()
    print(title,details)

    c.EXPERT = expert_table.objects.get(LOGIN=request.user.id)
    c.title = title
    c.details = details

    c.date = datetime.now().today()
    c.save()
    return redirect('/myapp/manage_view/')


def manage_view(request):
    q=tips_table.objects.filter(EXPERT__LOGIN_id=request.user.id)
    return render(request,'expert/manage&view.html',{'data':q})

def profile(request):
    ob = expert_table.objects.get(LOGIN__id=request.user.id)
    return render(request,'expert/profile.html',{'data':ob})


def send_reply(request):
    return render(request,'expert/sendreply.html')
def send_reply_post(request):
    reply=request.POST['reply']
    print(reply)
    return HttpResponse("ok")

def video(request):
    d=video_table.objects.filter(EXPERT__LOGIN_id=request.user.id)
    return render(request,'expert/video.html',{'data':d})

def expert_view_users(request):
    var=user_table.objects.all()

    return render(request,'expert/viewuser.html',{'data':var})
def expert_index(request):
    return render(request,'expert/index.html')


def delete_tips(request,id):
    tips_table.objects.get(id=id).delete()
    return redirect('/myapp/manage_view/')


def delete_vdo(request,id):
     video_table.objects.get(id=id).delete()
     return redirect('/myapp/video/')



# user

def user_login(request):
    username=request.POST['username']
    password=request.POST['password']
    print(username,password)
    user=authenticate(request,username=username,password=password)
    if user is not None:
        if user.groups.filter(name="User").exists():
           return JsonResponse({'status':'ok','lid':str(user.id),'type':'User'})
        else:
            return JsonResponse({'status': 'not ok',})
    return JsonResponse({'status': 'not ok', })

def registration(request):
    print(request.POST,"***********************")
    name = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['Phone']
    place = request.POST['Place']
    post = request.POST['Post']
    username = request.POST['Username']
    password = request.POST['Password']
    image =request.POST['image']

    date = datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(image)
    fh = open(
        r"D:\\project\\aicybershield\\media\\user\\" + date + ".jpg",
        "wb")
    # fh = open(r"D:\\PROJECT\\cybercrime_prevention\\media\\user\\" + date + ".jpg", "wb")
    path = "/media/user/" + date + ".jpg"
    fh.write(a)
    fh.close()

    var=User.objects.filter(username=username)
    if var.exists():
        return JsonResponse({"status":'not ok'})

    print(name, email, phone, place, post, username, password)
    ex = User.objects.create(username=username, password=make_password(password), email=email, first_name=name)
    ex.save()
    ex.groups.add(Group.objects.get(name="User"))

    ob=user_table()
    ob.name = name
    ob.email = email
    ob.phone = phone
    ob.place = place
    ob.post = post
    ob.image = path
    ob.LOGIN = ex

    ob.save()
    return JsonResponse({'status': "ok"})









def senddoubt(request):
    print(request.POST)
    eid = request.POST['eid']
    lid = request.POST['lid']
    doubt = request.POST['doubt']
    # k=user_table.objects.get(LOGIN__id=lid)
    # print(k,"kkkkkkkkkkkkk")
    ob=doubt_table()
    ob.EXPERT = expert_table.objects.get(id=eid)
    ob.USER = user_table.objects.get(LOGIN=lid)
    ob.date = datetime.today()
    ob.doubt = doubt
    ob.save()
    return JsonResponse({'status': "ok"})


def viewvideo(request):
    v=video_table.objects.all()
    print(v,"ok")
    mdata=[]
    for i in v:
        data={'Title':i.title,'Date':i.date}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})

def viewexpert(request):
    v=expert_table.objects.all()
    print(v,"ok")
    mdata=[]
    for i in v:
        data={'id':i.id,"lid":i.LOGIN.id,'Name':i.name,'email':i.email,'Phone':str(i.phone),'Place':i.place,'Qualification':i.qualification,'Post':i.post}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def viewdoubt(request):
    lid=request.POST['lid']
    eid=request.POST['eid']
    v=doubt_table.objects.filter(EXPERT__id=eid,USER__LOGIN__id=lid)
    print(v,"ok")
    mdata=[]
    for i in v:
        data={'id':i.id,'Doubt':i.doubt,'Reply':i.reply,'Date':i.date}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def viewtip(request):
    g=tips_table.objects.all()
    print(g,"ok")
    mdata=[]
    for i in g:
        data={'id':i.id,'Title':i.title,'Details':i.details,'Date':i.date,'Video': request.build_absolute_uri(i.video.url)}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def change_passwordpost(request):
    current_password = request.POST['old']
    new_password = request.POST['new']
    confirm_password = request.POST['confirm']
    lid = request.POST['lid']  # This is assumed to be the User ID

    try:
        user = User.objects.get(id=lid)
    except User.DoesNotExist:
        return JsonResponse({"status": "not ok", "error": "User not found"})

    if not check_password(current_password, user.password):
        return JsonResponse({"status": "not ok", "error": "Incorrect current password"})

    if new_password != confirm_password:
        return JsonResponse({"status": "not ok", "error": "Passwords do not match"})

    user.set_password(new_password)
    user.save()
    return JsonResponse({"status": "ok"})


#
# def and_forget_password_post(request):
#     print(request.POST)
#     try:
#         print("1")
#         print(request.POST)
#         email = request.POST['textfield']
#         print(email)
#         s=user_table.objects.get(email=email)
#         # qry = "SELECT login.password FROM student  JOIN login ON login.L_id = student.L_id WHERE email=%s"
#         # s = selectone(qry, email)
#         print(s, "=============")
#         if s is None:
#             return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')
#
#             # return jsonify({'task': 'invalid email'})
#         else:
#             try:
#                 gmail = smtplib.SMTP('smtp.gmail.com', 587)
#                 gmail.ehlo()
#                 gmail.starttls()
#                 gmail.login('koyaottak@gmail.com', 'dzwh fzuv rpan vsdb')
#                 print("login=======")
#             except Exception as e:
#                 print("Couldn't setup email!!" + str(e))
#             msg = MIMEText("Your new password id : " + str(s.LOGIN.password))
#             print(msg)
#             msg['Subject'] = 'password'
#             msg['To'] = email
#             msg['From'] = 'koyaottak@gmail.com'
#
#             print("ok====")
#
#             try:
#                 gmail.send_message(msg)
#             except Exception as e:
#                 return JsonResponse({'status': "not"})
#             return JsonResponse({'status': "ok"})
#                 # return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')
#             # return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
#     except Exception as e:
#         print(e)
#         return JsonResponse({'status': "not"})
#         # return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')



def forgotpasswordflutter(request):
    email = request.POST['email']
    try:
        user = user_table.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Email not found'})

    otp = random.randint(100000, 999999)
    PasswordResetOTP.objects.create(email=email, otp=otp)

    send_mail('Your Verification Code',
              f'Your verification code is {otp}',
              settings.EMAIL_HOST_USER,
              [email],
              fail_silently=False)
    return JsonResponse({'status': 'ok', 'message': 'OTP sent'})


def verifyOtpflutterPost(request):
    email = request.POST['email']
    entered_otp = request.POST['entered_otp']
    otp_obj = PasswordResetOTP.objects.filter(email=email).latest('created_at')
    if otp_obj.otp == entered_otp:
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})


# def changePasswordflutter(request):
#     email = request.POST['email']
#     newpassword = request.POST['newPassword']
#     confirmPassword = request.POST['confirmPassword']
#     if newpassword == confirmPassword:
#         try:
#             user = user_table.objects.get(email=email)
#             user.set_password(confirmPassword)
#             user.save()
#             return JsonResponse({'status': 'ok'})
#         except User.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'User not found'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})
#

from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

def changePasswordflutter(request):
    # Expecting POST
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    email = request.POST.get('email')
    newpassword = request.POST.get('newPassword')
    confirmPassword = request.POST.get('confirmPassword')

    if not all([email, newpassword, confirmPassword]):
        return JsonResponse({'status': 'error', 'message': 'Missing parameters'})

    if newpassword != confirmPassword:
        return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'})

    # Use set_password to properly hash the password
    user.set_password(newpassword)
    user.save()

    return JsonResponse({'status': 'ok', 'message': 'Password changed successfully'})

def User_sendchat(request):
    print(request.POST,"lllllllllll")
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg=request.POST['message']

    from  datetime import datetime
    c=chat_table()
    c.FROM_id=FROM_id
    c.TO_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})


def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = chat_table.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.message, "from": i.FROM_id, "date": i.date, "to": i.TO_id})

    return JsonResponse({"status":"ok",'data':l})


def view_profile(request):
    if request.method == "POST":
        lid = request.POST.get("lid")
        try:
            user = user_table.objects.get(LOGIN__id=lid)
            return JsonResponse({
                "status": "ok",
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "place": user.place,
                "post": user.post,
            })
        except user_table.DoesNotExist:
            return JsonResponse({"status": "no", "message": "User not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})


def update_profile(request):
    if request.method == "POST":
        lid = request.POST.get("lid")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        place = request.POST.get("place")
        post = request.POST.get("post")

        try:
            user = user_table.objects.get(LOGIN__id=lid)
            user.name = name
            user.email = email
            user.phone = phone
            user.place = place
            user.post = post
            user.save()
            return JsonResponse({"status": "ok"})
        except user_table.DoesNotExist:
            return JsonResponse({"status": "no", "message": "User not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

def android_view_videos(request):
    videos = video_table.objects.all().order_by('-date')
    data = []
    for v in videos:
        data.append({
            "id": v.id,
            "title": v.title,
            "video":str(v.video.url),  # full path
            "date": v.date.strftime("%Y-%m-%d"),
            "expert": v.EXPERT.name,
        })
    print(data,'=============')
    return JsonResponse({"status": "ok", "data": data})

# from .feature_extraction import predict_link_fn
# def check_phishing(request):
#     link=request.POST['link']
#     res=predict_link_fn(link)
#     print(res,type(res[0]))
#     if res[0]=="1":
#         return JsonResponse({"task":"Normal"})
#     else:
#         return JsonResponse({"task":"Malicious"})



from django.http import JsonResponse
# from .phishing_detector import detect_phishing
from .phishingExtraction import getResult
# from .phishing_detector import getResult
from .models import PhishingLink

def check_phishing(request):
    link = request.POST.get('link')
    # result = detect_phishing(link)
    result=getResult(link)
    print(result,'igdcyu')
    if result == "Phishing Url":
        PhishingLink.objects.get_or_create(
            url=link,
            defaults={"result": result}
        )

    return JsonResponse({"task": result})





# from django.http import JsonResponse
# from .feature_extraction import predict_link_fn
# from .models import PhishingLink
#
# def check_phishing(request):
#     link = request.POST['link']
#     res = predict_link_fn(link)
#
#     print(res, type(res[0]))
#
#     if res[0] == "1":
#         result = "Normal"
#     else:
#         result = "This is Phishing"
#
#         # save only phishing links
#         PhishingLink.objects.get_or_create(
#             url=link,
#             defaults={"result": result}
#         )
#
#     return JsonResponse({"task": result})



# def check_apk(request):
#     link=request.POST['app_name']
#     res=requestReview(link)
#     return JsonResponse({"task":res})



from django.http import JsonResponse
from .models import MaliciousApp
from .sample import requestReview   # adjust path if needed

def check_apk(request):
    link = request.POST['app_name']
    res = requestReview(link)

    if res == "Malicious":
        MaliciousApp.objects.get_or_create(
            package_name=link,
            defaults={"result": res}
        )

    # 👇 unchanged response
    return JsonResponse({"task": res})


from .file_checking import file_checking_main
def file_checking_fn(request):
    print(request.FILES,"#######################")
    file=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(file.name,file)
    # res=file_checking_main(r"C:\Users\GAYATHRI\Pictures\regional 2025 projects\cyber shield\aicybershield\media/"+fn)
    res=file_checking_main(r"D:\project\aicybershield\media/"+fn)
    print(res)
    return JsonResponse({"task":res})


# import requests
# def check_credentials(request):
#     email=request.POST['email']
#     url = f"https://leakcheck.io/api/public?check={email}"
#     headers = {'User-Agent': 'Gmail-Breach-Checker'}
#     try:
#         response = requests.get(url, headers=headers, timeout=10)
#         print(response)
#         if response.status_code == 200:
#             data = response.json()
#             if data.get("found"):
#                 print(f"🔐 '{email}' was found in known data leaks.")
#             else:
#                 print(f"✅ '{email}' was not found in public breaches.")
#         else:
#             print(f"❌ Error: {response.status_code} - {response.text}")
#     except Exception as e:
#         print(f"❌ Request failed: {e}")

import requests

@csrf_exempt
def check_credentials(request):
    if request.method != "POST":
        return JsonResponse({'status': 'error', 'msg': 'Only POST method allowed'}, status=405)
    email = request.POST.get('email')
    if not email:
        return JsonResponse({'status': 'error', 'msg': 'Email is required'}, status=400)
    url = f"https://leakcheck.io/api/public?check={email}"
    headers = {'User-Agent': 'Gmail-Breach-Checker'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(data,"1234567890")
            if data.get("found"):
                return JsonResponse({
                    'status': 'ok',
                    'type': 'User',
                    'darkweb': 'yes'
                })
            else:
                return JsonResponse({
                    'status': 'warning',
                    'msg': 'This email was not found in known data breaches.'
                })
        else:
            return JsonResponse({
                'status': 'error',
                'msg': f"LeakCheck API Error: {response.status_code}"
            }, status=response.status_code)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'msg': f"Request failed: {str(e)}"
        }, status=500)












def expert_add_post(request):
    if request.method == 'POST':
        post = request.FILES['image']
        fs = FileSystemStorage()
        path = fs.save(post.name, post)
        caption = request.POST['caption']

        var = uploadpost()
        var.date = datetime.now().today().date()
        var.post = path
        var.caption = caption
        var.LOGIN = User.objects.get(id=request.user.id)
        var.save()
        return redirect('/myapp/expert_add_post/')
    return render(request,'expert/add_post.html')



from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import date
from .models import uploadpost, like, comment


def expert_view_post(request):
    posts = uploadpost.objects.filter(LOGIN=request.user).order_by('-date')

    liked_posts = set(
        like.objects.filter(USERID=request.user)
        .values_list('UPLOADPOST_id', flat=True)
    )

    return render(request, 'expert/view_post.html', {
        'posts': posts,
        'liked_posts': liked_posts
    })


def expert_view_others_post(request):
    posts = uploadpost.objects.exclude(LOGIN=request.user).order_by('-date')

    liked_posts = set(
        like.objects.filter(USERID=request.user)
        .values_list('UPLOADPOST_id', flat=True)
    )

    return render(request, 'expert/view_others_post.html', {
        'posts': posts,
        'liked_posts': liked_posts
    })


def toggle_like(request, post_id):
    post = uploadpost.objects.get(id=post_id)

    existing = like.objects.filter(
        USERID=request.user,
        UPLOADPOST=post
    )

    if existing.exists():
        existing.delete()   # dislike
        liked = False
    else:
        like.objects.create(
            USERID=request.user,
            UPLOADPOST=post,
            like_dislike="like"
        )
        liked = True

    count = like.objects.filter(UPLOADPOST=post).count()
    return JsonResponse({'liked': liked, 'count': count})


def add_comment(request, post_id):
    if request.method == "POST":
        post = uploadpost.objects.get(id=post_id)
        text = request.POST.get('comment')

        comment.objects.create(
            comment=text,
            date=date.today(),
            USERID=request.user,
            UPLOADPOST=post
        )
    return redirect(request.META.get('HTTP_REFERER'))


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def expert_change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect")
            return redirect("/myapp/expert_change_password/")

        if new_password != confirm_password:
            messages.error(request, "New password and Confirm password do not match")
            return redirect("/myapp/expert_change_password/")

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)

        messages.success(request, "Password changed successfully")
        return redirect("/myapp/expert_change_password/")

    return render(request, "expert/change_password.html")



def user_viewprofile(request):
    lid=request.POST['lid']
    data=user_table.objects.get(LOGIN_id=lid)

    return JsonResponse({'status': 'ok',
                         'name':data.name,
                         'email':data.email,
                         'phone':str(data.phone),
                         'image':data.image,
                         'post':data.post,
                         'place':data.place,
                         })

def user_viewprofileandeditprofile(request):
    lid =request.POST['lid']
    name =request.POST['name']
    email =request.POST['email']
    phone =request.POST['phone']
    post =request.POST['post']
    place =request.POST['place']
    image = request.POST['image']

    import datetime
    import base64



    obj=user_table.objects.get(LOGIN_id=lid)

    if len(image)>0 :

       date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
       a = base64.b64decode(image)
       fh = open("D:\\project\\aicybershield\\media\\user\\" + date + ".jpg", "wb")
       # fh = open("C:\\Users\\91815\\PycharmProjects\\cyber\\media\\" + date + ".jpg", "wb")
       path = "/media/user/" + date + ".jpg"
       fh.write(a)
       fh.close()
       obj.image = path

    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.post=post
    obj.place=place
    obj.save()

    return JsonResponse({'status': 'ok'})



def useraddpost(request):
    newpost=request.POST['newpost']
    caption=request.POST['caption']
    lid=request.POST['lid']
    import datetime
    import base64

    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.bmp'
    a = base64.b64decode(newpost)
    path = "/media/user/" + dt

    # with open( r"C:\\Users\GAYATHRI\\Downloads\\Telegram Desktop\\cybercrime_prevention\\cybercrime_prevention\\media\\post\\" + dt,
    #                 "wb") as f:
    #     f.write(a)
    #     f.close()

    # with open(r"D:\\project\\aicybershield\\media\\post\\" + dt, "wb") as f:
    with open(r"D:\\project\\aicybershield\\media\\post\\" + dt, "wb") as f:
        f.write(a)
        f.close()




    from datetime import datetime
    date = datetime.now().strftime('%Y-%m-%d')
    obj = User_Post()
    obj.post = path
    obj.caption = caption
    obj.date = date

    obj.USER = user_table.objects.get(LOGIN_id=lid)
    obj.save()

    u = user_table.objects.all()
    uids = []
    imgs = []

    import face_recognition

    # mediapth = r"C:\\Users\\josep\\OneDrive\\Pictures\\project\\web\\aicybershield\\aicybershield\\media\\user\\"
    mediapth = r"D:\\project\\aicybershield\\media\\user\\"

    for i in u:
        print(i.id, 'iddddddd', i.LOGIN_id)

        if str(i.LOGIN_id) == str(lid):
            pass
        else:
            uids.append(i.id)

            # print(mediapth + i.photo.replace("/media/", ""))
            try:
                ppp=mediapth + i.image.replace("/media/user/", "")
                print("ppp",ppp)
                picture_of_me = face_recognition.load_image_file(ppp)
                my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

                imgs.append(my_face_encoding)

                print("added")
            except Exception as e:

                print("errrrr",e)
                # pass
    #
    # unknownfacesimages = r"C:\\Users\\GAYATHRI\\Downloads\\Telegram Desktop\\cybercrime_prevention\\cybercrime_prevention\\media\\post\\" + dt
    unknownfacesimages = r"D:\\project\\aicybershield\\media\\post\\" + dt

    picture_of_me = face_recognition.load_image_file(unknownfacesimages)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)

    import cv2
    img = face_recognition.load_image_file(unknownfacesimages)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(img_rgb)

    from PIL import Image
    # Open an image
    imagenews = Image.open(unknownfacesimages)
    width, height = imagenews.size
    new_image = Image.new("RGB", (width, height))

    #
    def modify_pixel(pixel):
        return (pixel[0] ^ 124, pixel[1] ^ 178, pixel[2] ^ 167)


    m = 0
    for i in my_face_encoding:

        print(face_locations[m])
        top, right, bottom, left = face_locations[m]
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        s = face_recognition.compare_faces(imgs, i, tolerance=0.45)
        print(s)

        for i in range(len(s)):
            if s[i] == True:
                print(uids[i], 'uiiiiiiiiiiiiiiiiiii    ')

                p = PostNotification()
                p.POST = obj
                p.USER_id = uids[i]
                p.status = "pending"
                p.date = datetime.now().date()
                p.bottom = bottom
                p.left = left
                p.right = right
                p.top = top
                p.save()

                crop_img = img_rgb[top:bottom, left:right]

                for x in range(left, right):
                    for y in range(top, bottom):
                        pixel = imagenews.getpixel((x, y))
                        new_pixel = modify_pixel(pixel)
                        imagenews.putpixel((x, y), new_pixel)

        m = m + 1

    # imagenews.save(r"C:\\Users\GAYATHRI\\Downloads\\Telegram Desktop\\cybercrime_prevention\\cybercrime_prevention\\media\\user\\\\"+dt)
    imagenews.save(r"D:\\project\\aicybershield\\media\\user\\\\"+dt)


    return JsonResponse({"status": "ok"})









def user_viewownpost(request):
    lid=request.POST['lid']
    res=User_Post.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'date':i.date,'post':i.post,'caption':i.caption,'name':i.USER.name,'image':i.USER.image})
    return JsonResponse({'status': 'ok','data':l})



def postremove(request):
    uid = request.POST['uid']
    re = User_Post.objects.filter(id=uid).delete()
    return JsonResponse({'status': 'ok'})


def user_viewcommentsandreply(request):
    pid=request.POST['pid']
    res=Post_comment.objects.filter(UPLOADPOST_id=pid,status='normal')
    l=[]
    for i in res:
        l.append({'id':i.id,'userid':i.USERID.name,'userphoto':i.USERID.image,'uploadpost':i.UPLOADPOST.id , 'comment':i.comment,'date':i.date})
    return JsonResponse({'status': 'ok','data':l})



def user_addcomment(request):
    lid = request.POST['lid']
    pid = request.POST['postid']

    comments=request.POST['comment']


    obj = Post_comment()
    obj.USERID = user_table.objects.get(LOGIN_id=lid)
    obj.UPLOADPOST_id = pid
    obj.comment = comments
    obj.status = "normal"
    obj.date = datetime.now().date()
    obj.save()
    return JsonResponse({'status': 'ok'})





def user_viewotherspost(request):
    res=User_Post.objects.all()
    l=[]
    lid=request.POST['lid']
    for i in res:
        liked='no'
        lcnt = User_like.objects.filter(UPLOADPOST_id=i.id)

        if User_like.objects.filter(USERID__LOGIN_id=lid,UPLOADPOST_id=i.id).exists():
            liked='yes'
        l.append({'id':i.id,'date':i.date,'post':i.post,'name':i.USER.name,'image':i.USER.image,'liked':liked, 'likes':str(len(lcnt))})
    return JsonResponse({'status': 'ok','data':l})


# def likes(request):
#     lid=request.POST['lid']
#     pid=request.POST['pid']
#     obj=User_like()
#     if User_like.objects.filter(USERID__LOGIN_id=lid,UPLOADPOST_id=pid).exists():
#         like.objects.filter(USERID__LOGIN_id=lid, UPLOADPOST_id=pid).delete()
#         return JsonResponse({'status': "ok"})
#
#     obj.USERID=user_table.objects.get(LOGIN_id=lid)
#     obj.UPLOADPOST_id=pid
#     obj.save()
#
#     return JsonResponse({'status':"ok"})



def likes(request):
    lid = request.POST['lid']
    pid = request.POST['pid']

    if User_like.objects.filter(USERID__LOGIN__id=lid, UPLOADPOST_id=pid).exists():
        User_like.objects.filter(USERID__LOGIN__id=lid, UPLOADPOST_id=pid).delete()
        return JsonResponse({'status': "ok"})

    obj = User_like()
    obj.USERID = user_table.objects.get(LOGIN__id=lid)
    obj.UPLOADPOST_id = pid
    obj.like_dislike = "like"   # IMPORTANT (field required)
    obj.save()

    return JsonResponse({'status': "ok"})


def user_viewothersusers(request):
    lid=request.POST['lid']
    res=user_table.objects.exclude(LOGIN=lid)
    l=[]
    for i in res:
           l.append({'id':i.id,'name':i.name,'image':i.image})
    print(l)
    return JsonResponse({'status': 'ok','data':l})


def user_sendfriendrequest(request):
    lid=request.POST['lid']
    uid=request.POST['uid']
    re=Request.objects.filter(TO=uid,FROM__LOGIN_id=lid)
    if re.exists():
        return JsonResponse({'status':'no'})
    else:
        r=Request()
        r.FROM = user_table.objects.get(LOGIN=lid)
        r.TO = user_table.objects.get(pk=uid)
        from datetime import datetime
        r.date = datetime.now().today()
        r.status = 'pending'
        r.save()
        return JsonResponse({'status': 'ok'})

def user_viewfriedrequest(requestS):
    lid=requestS.POST['lid']
    res = Request.objects.filter(TO__LOGIN_id=lid,status="pending")
    l = []
    for i in res:
        l.append({'id': i.id, 'name': i.FROM.name, 'image': i.FROM.image,'status': i.status })
    return JsonResponse({'status': 'ok', 'data': l})

def user_followback(request):
    lid = request.POST['lid']
    uid = request.POST['uid']
    re = Request.objects.filter(TO=uid, FROM__LOGIN_id=lid)
    if re.exists():
        return JsonResponse({'status': 'no'})
    else:
        re = Request.objects.filter(id=uid).update(status='accepted')
        return JsonResponse({'status': 'ok'})



def user_viewreject(request):
    rid=request.post['rid']
    var=request.objects.filter(id=rid).update(status='rejected')
    return JsonResponse({'status': 'ok'})

def user_remove(request):
    uid = request.POST['uid']
    re = Request.objects.filter(id=uid).delete()
    return JsonResponse({'status': 'ok'})


def viewfriends(request):
    lid = request.POST['lid']
    l = User.objects.get(id=lid)
    print(l, 'llll')
    uid = user_table.objects.get(LOGIN_id=l)
    print(uid, 'uuuu')

    roj = Request.objects.filter(FROM_id=uid,status='accepted') | Request.objects.filter(TO_id=uid,status='accepted')
    print(roj,'rrrrrrrr')
    user_data = []
    for user in roj:
        if user.TO.id == uid.id:
            user_data.append({
                "image": user.FROM.image,
                "id": user.id,
                "name": user.FROM.name,
                "ulid": user.FROM.LOGIN_id,
                "gender": user.FROM.name,
            })
        if user.FROM.id == uid.id:
            user_data.append({
                "image": user.TO.image,
                "id": user.id,
                "ulid": user.TO.LOGIN_id,
                "name": user.TO.name,
            })

    return JsonResponse({"status": "ok", 'data': user_data})

def user_viewapprovedrequest(req):
    lid=req.POST['lid']
    var=Request.objects.filter(status='accepted',FROM__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'date':i.date,'Status':i.status,'name':i.FROM.name})
    print(l)
    return JsonResponse({'status': 'ok','data':l})

def user_fromremovefromfriendlist(request):
    uid = request.POST['uid']
    print(uid)
    re = Request.objects.get(id=uid).delete()
    return JsonResponse({'status': 'ok'})


def user_viewnotification(request):
    lid= request.POST["lid"]
    res=PostNotification.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'date':i.date,'post':i.POST.post,'name':i.POST.USER.name,'image':i.POST.USER.image})
    return JsonResponse({'status': 'ok','data':l})

def reject_notification(request):
    lid= request.POST["nid"]
    res=PostNotification.objects.filter(id=lid).delete()
    return JsonResponse({'status': 'ok'})

from PIL import Image

def accept_notification(request):
    nid= request.POST["nid"]
    n=PostNotification.objects.get(id=nid).POST.post
    pid=PostNotification.objects.get(id=nid).POST.id
    print(n)
    bottom=int(PostNotification.objects.get(id=nid).bottom)
    left=int(PostNotification.objects.get(id=nid).left)
    right=int(PostNotification.objects.get(id=nid).right)
    top=int(PostNotification.objects.get(id=nid).top)
    postimage=PostNotification.objects.get(id=nid).POST.post
    postimage=postimage.replace("/media/user/","")
    # imagenews = Image.open(r"C:\\Users\\GAYATHRI\\Downloads\\Telegram Desktop\\cybercrime_prevention\\cybercrime_prevention\\media\\user\\" + postimage)
    imagenews = Image.open(r"D:\\project\\aicybershield\\media\\user\\" + postimage)
    width, height = imagenews.size
    new_image = Image.new("RGB", (width, height))
    def modify_pixel(pixel):
        return (pixel[0] ^ 124, pixel[1] ^ 178, pixel[2] ^ 167)
    for x in range(left, right):
        for y in range(top, bottom):
            pixel = imagenews.getpixel((x, y))
            new_pixel = modify_pixel(pixel)
            imagenews.putpixel((x, y), new_pixel)
    import datetime
    dates= datetime.datetime.now().strftime("%Y%m%d%H%M%f")+".bmp"
    p=User_Post.objects.get(id=pid)
    imagenews.save(r"D:\\project\\aicybershield\\media\\user\\\\" + dates)
    p.post="/media/user/"+ dates
    p.save()
    res=PostNotification.objects.filter(id=nid).delete()
    return JsonResponse({'status': 'ok'})






def user_viewreply(request):
    lid=request.POST['lid']
    r=complaint.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in r:
        l.append({'id':i.id,'date':i.date,'complaint':i.complaint,'reply':i.reply ,'status':i.status})

    return JsonResponse({'status': 'ok','data':l})

from datetime import datetime

def user_sendcomplaint(request):
    lid = request.POST['lid']
    date = datetime.now().date()
    complaints = request.POST['complaint']
    status = 'pending'

    obj = complaint()
    obj.USER = user_table.objects.get(LOGIN_id=lid)
    obj.date = date
    obj.complaint = complaints
    obj.reply = 'pending'
    obj.status = status
    obj.save()


    return JsonResponse ({'status':'ok'})


def user_review_rating(request):
    lid = request.POST['lid']
    rat = request.POST['rating']
    rev = request.POST['review']
    date = datetime.now().date()

    obj=rewview_rating()
    obj.USER=user_table.objects.get(LOGIN_id=lid)
    obj.date=date
    obj.rating=rat
    obj.review=rev
    obj.save()

    return JsonResponse ({'status':'ok'})









def question_list(request):
    questions = Question.objects.all()
    return render(request, 'admin/question_list.html', {'questions': questions})



def add_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        correct_option = request.POST.get('correct')  # 1,2,3,4

        question = Question.objects.create(question_text=question_text)

        for i in range(1, 5):
            Choice.objects.create(
                question=question,
                choice_text=request.POST.get(f'choice{i}'),
                is_correct=(str(i) == correct_option)
            )

        return redirect('/myapp/question_list/')

    return render(request, 'admin/add_question.html')




# --------------------
# User Quiz Views
# --------------------


# from django.shortcuts import get_list_or_404
# from django.http import JsonResponse
# from .models import Question, Choice
#
# def take_quiz_json(request):
#
#     if request.method != 'POST':
#         # Send questions and choices as JSON for frontend
#         questions = Question.objects.all()
#         data = []
#         for q in questions:
#             data.append({
#                 'id': q.id,
#                 'question_text': q.question_text,
#                 'choices': [
#                     {'id': c.id, 'choice_text': c.choice_text} for c in q.choices.all()
#                 ]
#             })
#         return JsonResponse({'questions': data})
#
#     # Handle submitted answers
#     submitted = request.POST  # or request.body if JSON is sent
#     questions = Question.objects.all()
#     total_score = 0
#     results = []
#
#     for q in questions:
#         selected_choice_id = submitted.get(str(q.id))  # POST key = question id
#         if selected_choice_id:
#             choice = Choice.objects.get(id=selected_choice_id)
#             correct = choice.is_correct
#             if correct:
#                 total_score += 1
#             results.append({
#                 'question_id': q.id,
#                 'selected_choice': selected_choice_id,
#                 'is_correct': correct
#             })
#         else:
#             results.append({
#                 'question_id': q.id,
#                 'selected_choice': None,
#                 'is_correct': False
#             })
#
#     return JsonResponse({
#         'total_score': total_score,
#         'total_questions': questions.count(),
#         'results': results
#     })



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Question, Choice, QuizAttempt, Answer

# ------------------------
# Get 10 quiz questions
# ------------------------
def take_quiz_json(request):
    """
    GET: Return up to 10 questions with choices
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'GET method required'}, status=400)

    questions = Question.objects.all()[:10]
    data = []
    for q in questions:
        data.append({
            'id': q.id,
            'question_text': q.question_text,
            'choices': [
                {'id': c.id, 'choice_text': c.choice_text} for c in q.choices.all()
            ]
        })

    return JsonResponse({'questions': data})


# ------------------------
# Submit quiz answers
# ------------------------


import json
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Question, Choice, QuizAttempt, Answer

def submit_quiz(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST request required'}, status=400)

    data = json.loads(request.body)  # JSON body is a dict
    lid = data.get('lid')  # <- use .get() on dict
    answers_data = data.get('answers', [])

    try:
        user = User.objects.get(id=lid)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'}, status=400)

    # Create QuizAttempt
    attempt = QuizAttempt.objects.create(user=user)

    total_score = 0
    results = []

    for ans in answers_data:
        question_id = ans.get('question_id')
        selected_choice_id = ans.get('selected_choice_id')

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            continue

        choice = None
        is_correct = False

        if selected_choice_id:
            try:
                choice = Choice.objects.get(id=selected_choice_id, question=question)
                is_correct = choice.is_correct
                if is_correct:
                    total_score += 1
            except Choice.DoesNotExist:
                choice = None
                is_correct = False

        # Save answer
        Answer.objects.create(
            attempt=attempt,
            question=question,
            selected_choice=choice,
            is_correct=is_correct
        )

        results.append({
            'question_id': question.id,
            'question_text': question.question_text,
            'selected_choice': choice.choice_text if choice else None,
            'is_correct': is_correct
        })

    # Update attempt total score and finished time
    attempt.total_score = total_score
    attempt.finished_at = timezone.now()
    attempt.save()

    return JsonResponse({
        'total_score': total_score,
        'total_questions': len(answers_data),
        'answers': results
    })




from django.shortcuts import render
from django.contrib.auth.models import User
from .models import QuizAttempt

def quiz_results_view(request):

    attempts = QuizAttempt.objects.select_related('user').prefetch_related('answers__question', 'answers__selected_choice').order_by('-started_at')
    return render(request, 'admin/quiz_results.html', {'attempts': attempts})



def expert_chat_to_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = user_table.objects.get(LOGIN=cid)
    print(qry.LOGIN.id,'login----------')

    return render(request, "expert/Chat.html", { 'name': qry.name, 'toid': cid})
    # return render(request, "shop/Chat.html", {'photo': qry.image, 'name': qry.name, 'toid': cid})


def chat_view(request):
    fromid = request.user.id
    toid = request.session["userid"]
    qry = user_table.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = chat_table.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid)).order_by('id')
    l = []
    print(qry.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})
    return JsonResponse({"data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.user.id
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = chat_table()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})