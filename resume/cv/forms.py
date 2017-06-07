# import datetime
from django import forms
from .models import PersonalInfo, WorkExperience, Education, Skills
from django.forms.extras.widgets import SelectDateWidget


class PersonalInfoForm(forms.ModelForm):
    birth_day = forms.DateField(widget=SelectDateWidget(years=range(1960, 2018)))

    class Meta:
        model = PersonalInfo
        exclude = ["user", "height_field", "width_field"]


class WorkExperienceForm(forms.ModelForm):
    joining_year = forms.DateField(widget=SelectDateWidget(years=range(1960, 2018))) 

    class Meta:
        model = WorkExperience
        exclude = ["personal_info"]


class EducationForm(forms.ModelForm):
    year = forms.DateField(widget=SelectDateWidget(years=range(1960, 2018))) 

    class Meta:
        model = Education
        exclude = ["personal_info"]


class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        exclude = ["personal_info"]
