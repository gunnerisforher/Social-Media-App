from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
import uuid
import datetime
# Create your models here.
class MyAccountManger(BaseUserManager):
    def create_user(self, first_name, last_name , username , email, password = None):
        if not email:
            raise ValueError('Email Address is Mandatory!')
        
        if not username:
            raise ValueError('User must have a UserName!')


        user = self.model(
            email  = self.normalize_email(email),
            username  = username , 
            first_name  = first_name,
            last_name      = last_name,
        ) 

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_superuser(self, first_name , last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name= last_name,
            password = password,
        )

        user.is_admin = True
        user.is_active = True 
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
        
class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    
    #required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    objects = MyAccountManger()
    
    
    def __str__(self):
        return self.email
    
    
    
    def has_perm(self, perm , obj=None):
        return self.is_admin
    
    
    
    def has_module_perms(self, add_label):
        return True


class Profile(models.Model):
    pages = models.ManyToManyField('profiles.Page',blank=True)
    friends = models.ManyToManyField('Profile',blank=True)
    account = models.OneToOneField(Account , on_delete=models.CASCADE, blank=True , null=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    short_intro = models.CharField(max_length=150,null=True,blank=True)
    bio = models.TextField(max_length=300,blank=True,null=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    profile_image = models.ImageField(default='user-default.png', upload_to='profile_pics/%y/%m/%d')
    social_github = models.CharField(max_length=50,null=True,blank=True)
    social_twitter = models.CharField(max_length=50,null=True,blank=True)
    social_youtube = models.CharField(max_length=50,null=True,blank=True)
    social_website = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    skill = models.CharField(max_length=255,null=True,blank=True)
    language = models.CharField(max_length=50,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/user-default.png'
        return url
    
    class Meta:
        ordering = ['-created']


class FriendRequests(models.Model):
    sender = models.ForeignKey(Account,on_delete=models.CASCADE,null=True, blank=True)
    reciever = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender.username)