from django.db import models

class Project_data(models.Model):
  title = models.CharField(max_length=50)
  details = models.CharField(max_length=800)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default='non categorized')
  target = models.IntegerField()
  start_date = models.DateField()
  end_date = models.DateField()
  rating = models.IntegerField()
  reports = models.IntegerField(default=0)
  current_money = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  cover = models.ImageField(upload_to='images/' ,null=True)
  featured = models.BooleanField(default=False)
#   user = models.ForeignKey('user.Profile',related_name='user',on_delete=models.CASCADE)

  def _str_(self):
    return self.title
  
class Category(models.Model):
    name = models.CharField(max_length=50)  
  
    def _str_(self):
        return self.name
  
  
class Project_pics(models.Model):
  project = models.ForeignKey('Project_data',on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')
  
  def _str_(self):
    return self.project.title
  
class project_comments(models.Model):
  project = models.ForeignKey('Project_data',related_name='comments',on_delete=models.CASCADE)
#   comment_user = models.ForeignKey('user.Profile',related_name='comment_user',on_delete=models.CASCADE)
  comment = models.TextField()
  
  def _str_(self):
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
#   user = models.ForeignKey('user.Profile', related_name='report_user',on_delete=models.CASCADE)
  project = models.ForeignKey('Project_data', related_name='reported_project',on_delete=models.CASCADE)
  is_reported=models.BooleanField()
  
class Rate_project(models.Model):
#   user = models.ForeignKey('user.Profile', related_name='rate_user',on_delete=models.CASCADE)
  project = models.ForeignKey('Project_data', related_name='rated_project',on_delete=models.CASCADE)
  value = models.IntegerField()

class Donate_project(models.Model):
#   user = models.ForeignKey('user.Profile', related_name='donate_user',on_delete=models.CASCADE)
  project = models.ForeignKey('Project_data', related_name='donated_project',on_delete=models.CASCADE)
  value = models.IntegerField()
  amount=models.IntegerField()

class Report_comment(models.Model):
#   user = models.ForeignKey('user.Profile', related_name='report_comment_user',on_delete=models.CASCADE)
  comment = models.ForeignKey('project_comments', related_name='comment_id',on_delete=models.CASCADE)
