from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
	GENDER_CHOICE = (
		("Male", "Male"),
		("Female", "Female"),
	)

	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	birth_day = models.DateField()
	gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
	nationality = models.CharField(max_length=25)
	phone_no = models.CharField(max_length=14, blank=True)
	email = models.EmailField()
	website = models.URLField(blank=True)
	address = models.CharField(max_length=100, blank=True)
	bio = models.TextField()
	picture = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=600)
	width_field = models.IntegerField(default=600)

	def __unicode__(self):
		return self.first_name

class WorkExperience(models.Model):
	personal_info = models.ForeignKey(PersonalInfo)
	company_name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=20)
	joining_year = models.DateField(null=True, blank=True)
	job_description = models.TextField()

	def __unicode__(self):
		return self.personal_info.first_name

class Education(models.Model):
	personal_info = models.ForeignKey(PersonalInfo)
	institute_name = models.CharField(max_length=50, blank=False)
	subject = models.CharField(max_length=40)
	year = models.DateField(null=True, blank=True)
	description = models.TextField()

	def __unicode__(self):
		return self.personal_info.first_name


class Skills(models.Model):
	personal_info = models.ForeignKey(PersonalInfo)
	language_skills = models.CharField(max_length=200, blank=True, help_text="Sparate languages by comma")
	other_skills = models.CharField(max_length=200, blank=True, help_text="Sparate Skills by comma")

	def __unicode__(self):
		return self.personal_info.first_name
		