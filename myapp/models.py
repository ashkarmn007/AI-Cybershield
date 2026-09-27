from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class expert_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    status=models.CharField(max_length=100)
    certificate=models.FileField()
    certificate1 = models.FileField(null=True, blank=True)
    certificate2 = models.FileField(null=True, blank=True)


class user_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    image= models.CharField(max_length=400)


class complaint(models.Model):
    date= models.DateField()
    complaint= models.CharField(max_length=100)
    reply= models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    # user foreign key

class   rewview_rating(models.Model):
    date = models.DateField()
    rating = models.CharField(max_length=100)
    review=models.CharField(max_length=100)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)









class tips_table(models.Model):
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    video=models.FileField()
    details=models.CharField(max_length=500)
    date=models.DateField()

class video_table(models.Model):
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    video=models.FileField()
    title=models.CharField(max_length=100)
    date=models.DateField()


class doubt_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    EXPERT=models.ForeignKey(expert_table,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=500)
    reply=models.CharField(max_length=500)
    date=models.DateField()


class chat_table(models.Model):
    FROM=models.ForeignKey(User,on_delete=models.CASCADE,related_name="fromid")
    TO=models.ForeignKey(User,on_delete=models.CASCADE,related_name="toid")
    message=models.CharField(max_length=500)
    date=models.DateField()



class feedback_table(models.Model):
    feedback=models.CharField(max_length=500)
    rating=models.IntegerField()
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    date=models.DateField()


class PasswordResetOTP(models.Model):
    email = models.EmailField(max_length=254)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)  #





class uploadpost(models.Model):
    date = models.DateField()
    post = models.CharField(max_length=400)
    caption=models.CharField(max_length=500)
    LOGIN = models.ForeignKey(User, on_delete=models.CASCADE)


class like(models.Model):
    USERID = models.ForeignKey(User, on_delete=models.CASCADE)
    UPLOADPOST = models.ForeignKey(uploadpost, on_delete=models.CASCADE)
    like_dislike = models.CharField(max_length=100)






class comment(models.Model):
    comment = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=500)
    USERID = models.ForeignKey(User, on_delete=models.CASCADE)
    UPLOADPOST = models.ForeignKey(uploadpost, on_delete=models.CASCADE)



class User_Post(models.Model):
    date = models.DateField()
    post = models.CharField(max_length=400)
    caption=models.CharField(max_length=500)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)


class User_like(models.Model):
    USERID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    UPLOADPOST = models.ForeignKey(User_Post, on_delete=models.CASCADE)
    like_dislike = models.CharField(max_length=100)

class Post_comment(models.Model):
    comment = models.CharField(max_length=500)
    date = models.DateField()
    status = models.CharField(max_length=500)
    USERID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    UPLOADPOST = models.ForeignKey(User_Post, on_delete=models.CASCADE)


class PostNotification(models.Model):
    POST =models.ForeignKey(User_Post, on_delete=models.CASCADE)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateField()
    bottom= models.CharField(max_length=100)
    left= models.CharField(max_length=100)
    right=models.CharField(max_length=100)
    top=models.CharField(max_length=100)


class Request(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=100)
    FROM = models.ForeignKey(user_table, on_delete=models.CASCADE, related_name="frm")
    TO = models.ForeignKey(user_table, on_delete=models.CASCADE, related_name="touser")




class MaliciousApp(models.Model):
    package_name = models.CharField(max_length=255, unique=True)
    result = models.CharField(max_length=50)
    checked_at = models.DateTimeField(auto_now_add=True)


class PhishingLink(models.Model):
    url = models.URLField(unique=True)
    result = models.CharField(max_length=20)
    checked_at = models.DateTimeField(auto_now_add=True)




from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)




class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='choices',
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)



class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    total_score = models.IntegerField(default=0)  # calculated after attempt



class Answer(models.Model):
    attempt = models.ForeignKey(
        QuizAttempt, related_name='answers', on_delete=models.CASCADE
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(
        Choice, on_delete=models.SET_NULL, null=True
    )
    is_correct = models.BooleanField(default=False)




