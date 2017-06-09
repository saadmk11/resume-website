# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import formset_factory, BaseFormSet
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PersonalInfoForm, WorkExperienceForm, EducationForm, SkillsForm
from .models import *



# shows CV form the users from URL
def home(request, username=None):
	title = "Resume"
	if username is None:
		if not request.user.is_authenticated():
			return render(request, "cv/home.html", {})
		else:                          # Shows the logged in users CV in "/"
			user = request.user
	else:
		user = get_object_or_404(User, username=username)

	personalinfo = PersonalInfo.objects.filter(user=user)
	workexperience_detail = WorkExperience.objects.filter(user=user)
	education_detail = Education.objects.filter(user=user)
	skills_detail = Skills.objects.filter(user=user)
	can_update = request.user.groups.filter(name='new user').exists()


	context = {'personalinfo': personalinfo,
			   'workexperience_detail': workexperience_detail,
			   'education_detail': education_detail,
			   'skills_detail': skills_detail,
			   'title': title,
			   'can_update':can_update
				}

	return render(request, "cv/details.html", context)

# about page
def about(request):
	return render(request, "cv/about.html", {})


# creates new CV
@login_required()
def create(request):
	if not request.user.groups.filter(name='new user').exists():
		raise Http404
	else:
		class RequiredFormSet(BaseFormSet):
			def __init__(self, *args, **kwargs):
				super(RequiredFormSet, self).__init__(*args, **kwargs)
				for form in self.forms:
					self.forms[0].empty_permitted = False

		EducationFormset = formset_factory(EducationForm, extra=4, max_num=4, formset=RequiredFormSet)

		WorkExperienceFormset = formset_factory(WorkExperienceForm, extra=3, max_num=3, formset=RequiredFormSet)

		title = "Create CV"
		personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None)
		workexperienceformset = WorkExperienceFormset(request.POST or None, prefix='workexperience')
		educationformset = EducationFormset(request.POST or None, prefix='education')
		skillsform = SkillsForm(request.POST or None)

		if personalinfoform.is_valid() and workexperienceformset.is_valid() and educationformset.is_valid() and skillsform.is_valid():

			user = request.user
			personalinfo = personalinfoform.save(commit=False)
			personalinfo.user = user
			personalinfo.save()
			for form in workexperienceformset:
					workexperience = form.save(commit=False)
					workexperience.user = user
					if workexperience.company_name:
						workexperience.save()
			for form in educationformset:
					education = form.save(commit=False)
					education.user = user
					if education.institute_name:
						education.save()
			skills = skillsform.save(commit=False)
			skills.user = user
			skills.save()
			user.groups.clear()
			return redirect("home")

		context = {'personalinfoform': personalinfoform,
				   'workexperienceformset': workexperienceformset,
				   'educationformset': educationformset,
				   'skillsform': skillsform,
				   'title': title
					}

		return render(request, "cv/create.html", context)


# Updates CV
@login_required()
def update(request, username=None):
	if request.user.username != username:
		raise Http404
	else:
		title = "Update CV"
		
		class RequiredFormSet(BaseFormSet):
			def __init__(self, *args, **kwargs):
				instance = kwargs.pop('instance', None)
				super(RequiredFormSet, self).__init__(*args, **kwargs)
				for form in self.forms:
					self.forms[0].empty_permitted = False

		EducationFormset = formset_factory(EducationForm, extra=4, max_num=4, formset=RequiredFormSet)

		WorkExperienceFormset = formset_factory(WorkExperienceForm, extra=3, max_num=3, formset=RequiredFormSet)

		user = get_object_or_404(User, username=username)
		instance = get_object_or_404(PersonalInfo, user=user)
		personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None, instance=instance)
		instance = WorkExperience.objects.filter(user=user)
		workexperienceformset = WorkExperienceFormset(request.POST or None, instance=instance)
		instance = Education.objects.filter(user=user)
		educationformset = EducationFormset(request.POST or None, instance=instance)
		instance = Skills.objects.get(user=user)
		skillsform = SkillsForm(request.POST or None, instance=instance)

		if personalinfoform.is_valid() and workexperienceformset.is_valid() and educationformset.is_valid() and skillsform.is_valid():

			user = request.user
			personalinfo = personalinfoform.save(commit=False)
			personalinfo.user = user
			instance.save()
			for form in workexperienceformset:
					workexperience = form.save(commit=False)
					workexperience.user = user
					if workexperience.company_name:
						workexperience.save()
			for form in educationformset:
					education = form.save(commit=False)
					education.user = user
					if education.institute_name:
						education.save()
			skills = skillsform.save(commit=False)
			skills.user = user
			skills.save()
			user.groups.clear()
			return redirect("home")

		context = {'personalinfoform': personalinfoform,
				   'workexperienceformset': workexperienceformset,
				   'educationformset': educationformset,
				   'skillsform': skillsform,
				   'title': title
					}

		return render(request, "cv/create.html", context)