from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        about_you=request.POST.get("about_you","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        skill=request.POST.get("skill","")
        project=request.POST.get("project","")
        previous_work=request.POST.get("previous_work","")

        profile = Profile(name=name,email=email,phone=phone,about_you=about_you,degree=degree,school=school,skill=skill,project=project,previous_work=previous_work)
        profile.save()
    return render(request,'index.html')

def resume(request,id):     #we are adding 'id' of the user which we want to download the pdf
    context={}              # so in our database many profile going to be saved so we only want to download a specifi profile so for that we need to pass the 'id' here 
    m = Profile.objects.get(pk=id)
    context['user_profile']=m               #now we can use the user_profile context in resume.html to extract the details of user
    template = loader.get_template('resume.html')    #it will load the template and save it inside a variable(this template will be empty )
    html = template.render(context)         #passing user data #now we have to pass the renderd tamplate to the pdfkit library which we have installed
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    config=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html,False,options,configuration=config)           #convert html (string) to a pdf document
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'    #pdf attachment      #making pdf downlodeble 
    filename = 'resume.pdf'
    return response

def list(request):
    context={}
    p= Profile.objects.all()
    context['profiles']=p
    return render(request,'list.html',context)

def download(request):
    return render(request,'download.html')