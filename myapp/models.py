from django.db import models

# Create your models here.
# python manage.py makemigrations (it will generate script of models file)
# python manage.py migrate        (it will execute script)

class User(models.Model):
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now=True)

class Chairman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    contact_no=models.CharField(max_length=15)
    pic=models.FileField(upload_to='media/images/',default='media/defaultpic.png')

class Members(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    house_no=models.CharField(max_length=10)
    block_no=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    contact_no=models.CharField(max_length=15)
    family_members=models.CharField(max_length=15)
    vehicle_details=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=5)
    job_description=models.CharField(max_length=30)
    job_address=models.TextField()
    pic=models.FileField(upload_to='media/images/',default='media/defaultpic.png')