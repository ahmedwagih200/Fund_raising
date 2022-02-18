from unicodedata import decimal
from django.db import models
from users.models import Users
from django.utils.text import slugify
class Project_data(models.Model):
  title = models.CharField(max_length=50)
  details = models.CharField(max_length=800)
  category = models.ForeignKey('Category',on_delete=models.CASCADE)
  target = models.IntegerField()
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateField()
  rating = models.IntegerField(null=True)
  reports = models.IntegerField(default=0,null=True)
  current_money = models.IntegerField(default=0,null=True)
  remain= models.IntegerField(default=0,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  featured = models.BooleanField(default=False,null=True)
  user = models.ForeignKey(Users,on_delete=models.CASCADE)
  img=models.ImageField(upload_to='images/',null=True)
  slug=models.SlugField(null=True) 
  def __str__(self):
    return self.title
  
 # def save(self,*args,**kwargs):
  #  self.slug=slugify(self.title)
   # super(Project_data,self).save(*args,**kwargs)
 

class Category(models.Model):
  id=models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)  
  
  def __str__(self):
        return self.name
  
class Project_pics(models.Model):
  project = models.ForeignKey(Project_data,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')
  
  def _str_(self):
    return self.project.title
  
class project_comments(models.Model):
  project = models.ForeignKey(Project_data,related_name='comments',on_delete=models.CASCADE)
  comment_user = models.ForeignKey(Users,on_delete=models.CASCADE)
  comment = models.TextField()
  
  def __str__(self):
    return self.comment

class project_tags(models.Model):
  project = models.ForeignKey('Project_data', on_delete=models.CASCADE)
  tag = models.CharField(max_length=50)  
  
  def _str_(self):
    return self.project.title + " - " + self.tag

# class project_comment_replies(models.Model):
#   comment = models.ForeignKey('Project_comments',related_name='replies',on_delete=models.CASCADE)
#   reply_user = models.ForeignKey('user.Profile',related_name='reply_user',on_delete=models.CASCADE)
#   reply = models.TextField()


class Report_project(models.Model):
  user = models.ForeignKey(Users,on_delete=models.CASCADE)
  project = models.ForeignKey(Project_data,related_name='project',on_delete=models.CASCADE)
  is_reported=models.BooleanField()
  
class Rate_project(models.Model):
  user = models.ForeignKey(Users,on_delete=models.CASCADE)
  project = models.ForeignKey(Project_data,related_name='pproject',on_delete=models.CASCADE)
  value = models.IntegerField( )

class Donate_project(models.Model):
  user = models.ForeignKey(Users,related_name='donate',on_delete=models.CASCADE)
  project = models.ForeignKey(Project_data,related_name='donate',on_delete=models.CASCADE)
  value = models.IntegerField()
  

class Report_comment(models.Model):
  user = models.ForeignKey(Users,on_delete=models.CASCADE)
  comment = models.ForeignKey(project_comments,on_delete=models.CASCADE)
