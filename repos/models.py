from django.db import models

# Create your models here.
class RepoModel(models.Model):
   photo = models.URLField()
   project_title = models.CharField(max_length=150)
   project_description = models.TextField()
   tags = models.CharField(max_length=255)
   github_url = models.URLField()

   class Meta:
      db_table = 'repo_model'