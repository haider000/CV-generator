from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
import pdfkit
from django.template import loader
import io


# Create your views here.
def home(request):
    return render(request,"pdf/home.html")

def new(request):
    return render(request,'pdf/new.html')
def accept(request):
    if request.method =="POST":
        name = request.POST.get("name","")
        career_objective = request.POST.get("career_objective","")
        address = request.POST.get("address","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        github = request.POST.get("github","")
        linkedin = request.POST.get("linkedin","")
        other_link = request.POST.get("other_link","")
        achievements = request.POST.get("achievements","")
        ug_course_name = request.POST.get("ug_course_name","")
        university = request.POST.get("university","")
        ug_percentage = request.POST.get("ug_percentage","")
        diploma_or_12th = request.POST.get("diploma_or_12th","")
        school_12th = request.POST.get("school_12th","")
        percentage_12th = request.POST.get("percentage_12th","")
        school_10th = request.POST.get("school_10th","")
        percentage_10th = request.POST.get("percentage_10th","")
        work_or_project = request.POST.get("work_or_project","")
        technical_skills = request.POST.get("technical_skills","")
        soft_skills = request.POST.get("soft_skills","")
        
      

       

        profile = Profile( name = name,career_objective = career_objective,address = address,email = email,phone = phone,github = github,linkedin = linkedin,other_link = other_link,achievements = achievements,ug_course_name = ug_course_name, university = university,ug_percentage = ug_percentage,diploma_or_12th = diploma_or_12th,school_12th = school_12th,percentage_12th = percentage_12th,school_10th = school_10th,percentage_10th = percentage_10th,work_or_project = work_or_project,technical_skills = technical_skills, soft_skills = soft_skills)
        profile.save()
        

    return render(request,"pdf/accepting_data_for_resume.html")


def resum(request,id):
    user = Profile.objects.get(pk=id)
    
    template = loader.get_template('pdf/resume_layout.html')
    
    html = template.render({"user":user})

    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")


    
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }


    pdf = pdfkit.from_string(html,False,options,configuration=config)

    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    
    
    return response

def layout(request,id):
    user = Profile.objects.get(pk=id)

    
    achievements_list = user.achievements.split(",,")
    technical_skills_list = user.technical_skills.split(",,")
    soft_skills_list = user.soft_skills.split(",,")
    print()
    print
    print()
    print()
    print()
    my_context = {
        'user':user,
        'achievements_list':achievements_list,
        'technical_skills_list':technical_skills_list,
        'soft_skills_list' : soft_skills_list,
    }
    return render(request,'pdf/resume_layout.html',my_context)
    
def resume(request):
    return render(request,'pdf/resume_layout.html')