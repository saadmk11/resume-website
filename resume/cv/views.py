# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import formset_factory
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
	workexperience_detail = WorkExperience.objects.filter(personal_info=personalinfo)
	education_detail = Education.objects.filter(personal_info=personalinfo)
	skills_detail = Skills.objects.filter(personal_info=personalinfo)
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
		WorkExperienceFormset = formset_factory(WorkExperienceForm, extra=3,
												max_num=3, validate_max=True,
												min_num=3, validate_min=True)

		EducationFormset = formset_factory(EducationForm, extra=4,
												max_num=4, validate_max=True,
												min_num=4, validate_min=True)

		title = "Create CV"
		personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None)
		workexperienceformset = WorkExperienceFormset(request.POST or None)
		educationformset = EducationFormset(request.POST or None)
		skillsform = SkillsForm(request.POST or None)

		if personalinfoform.is_valid() and workexperienceformset.is_valid() and educationformset.is_valid() and skillsform.is_valid():
			instance = personalinfoform.save(commit=False)
			instance.user = request.user
			instance.save()
			for form in workexperienceformset:
				workexperience = form.save(commit=False)
				workexperience.personal_info = instance
				workexperience.save()
			for form in educationformset:
				education = form.save(commit=False)
				education.personal_info = instance
				education.save()
			skills = skillsform.save(commit=False)
			skills.personal_info = instance
			skills.save()
			user = request.user
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
		user = get_object_or_404(User, username=username)
		instance = get_object_or_404(PersonalInfo, user=user)
		personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None, instance=instance)
		id = instance.id
		instance = get_object_or_404(WorkExperience, id=id)
		workexperienceform = WorkExperienceForm(request.POST or None, instance=instance)
		instance = get_object_or_404(Education, id=id)
		educationform = EducationForm(request.POST or None, instance=instance)
		instance = get_object_or_404(Skills, id=id)
		skillsform = SkillsForm(request.POST or None, instance=instance)

		if personalinfoform.is_valid() and workexperienceform.is_valid() and educationform.is_valid() and skillsform.is_valid():
			instance = personalinfoform.save(commit=False)
			instance.user = request.user
			instance.save()
			workexperience = workexperienceform.save(commit=False)
			workexperience.personal_info = instance
			workexperience.save()
			education = educationform.save(commit=False)
			education.personal_info = instance
			education.save()
			skills = skillsform.save(commit=False)
			skills.personal_info = instance
			skills.save()
			return redirect("home")

		context = {'personalinfoform': personalinfoform,
				   'workexperienceform': workexperienceform,
				   'educationform': educationform,
				   'skillsform': skillsform,
				   'title': title
					}

		return render(request, "cv/create.html", context)
