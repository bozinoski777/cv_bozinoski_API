from django.db import models

class Education(models.Model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Languages(models.Model):
  language = models.CharField(max_length=50)
  proficiency = models.CharField(max_length=50)
  comment = models.CharField(max_length=50)

class Organizations(models.Model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  description = models.CharField(max_length=50)

class ProfessionalExperience(models.Model):
  timespan = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  description = models.CharField(max_length=50)

class Skills(models.Model):
  skill = models.CharField(max_length=50)
  description = models.CharField(max_length=50)

class CodingProjects(models.Model):
  title = models.CharField(max_length=50)
  tagline = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  live_demo = models.CharField(max_length=50)
  repository = models.CharField(max_length=50)

class Cv(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  mobile = models.CharField(max_length=50)
  birthday = models.CharField(max_length=50)
  citizenship = models.CharField(max_length=50)
  github = models.CharField(max_length=50)
  linkedin = models.CharField(max_length=50)
  introduction = models.CharField(max_length=50)

