from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Internships,Extracurriculur,Mooc,Workshops,CustomUser
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
import io
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# Create your views here.

def index(request):
     return render(request, "website/index.html")


class SearchView(ListView):
    model=CustomUser
    template_name='studentslist.html'
  
    

@login_required
def dashboard(request):
     if(request.user.is_advisor==True):
       return render(request, "website/advisordashboard.html")
     else:
       return render(request, "website/dashboard.html")

@login_required
def certificates(request):
     return render(request, "website/certificates.html")

@login_required
def studentsList(request):
    students=CustomUser.objects.filter(is_advisor=False)
    return render(request, "website/studentslist.html",{'students':students})

@login_required
def uploads_view(request):
      mooc = Mooc.objects.filter(user=request.user)
      intern= Internships.objects.filter(user=request.user)
      workshops=Workshops.objects.filter(user=request.user)
      extras=Extracurriculur.objects.filter(user=request.user)
      return render(request, "website/uploads.html",{'mooc':mooc,'intern':intern,'workshops':workshops,'extras':extras})
    
    

@login_required    
def mooc(request):
      if request.method == "POST":
       
        user = request.user
        title=request.POST['title']
        type=request.POST['type']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        folder_id=request.user.batch.mooc_folder_url

        id =upload(request.FILES['files'].read(),request.user.admission_number,folder_id)
        url= "https://drive.google.com/file/d/{id}/preview".format(id=id)
        mooc = Mooc(user=user,course_title=title,course_type=type,start_date=start_date,end_date=end_date,file_url=url)
        mooc.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
      return render(request, "website/mooc.html")
    

@login_required    
def internship(request):
      if request.method == "POST":
       
        user = request.user
        name=request.POST['name']
        company=request.POST['company']
        days=request.POST['days']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        folder_id=request.user.batch.internship_folder_url
     
        id =upload(request.FILES['files'].read(),request.user.admission_number,folder_id)
        url= "https://drive.google.com/file/d/{id}/preview".format(id=id)
        intern = Internships(user=user,name=name,company=company,no_of_days=days,start_date=start_date,end_date=end_date,file_url=url)
        intern.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
        
        # check whether it's valid:
     

      return render(request, "website/internship.html")
    
    
@login_required    
def extrac(request):

      if request.method == "POST":
       
        user = request.user
        title=request.POST['title']
        organiser=request.POST['organiser']
        date=request.POST['date']
        level=request.POST['event_level']
        type=request.POST['event_type']
        position=request.POST['position']
        folder_id=request.user.batch.extracurriculur_folder_url
     
        id =upload(request.FILES['files'].read(),request.user.admission_number,folder_id)
        url= "https://drive.google.com/file/d/{id}/preview".format(id=id)
        extrac = Extracurriculur(user=user,event_title=title,event_organiser=organiser,event_date=date,event_level=level,event_type=type,event_position=position,file_url=url)
        extrac.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
      

      return render(request, "website/extras.html")
    
    
def workshops(request):
      if request.method == "POST":
       
        user = request.user
        name=request.POST['name']
        organiser=request.POST['organiser']
        date=request.POST['date']
        no_of_days=request.POST['days']
        folder_id=request.user.batch.workshop_folder_url
     
        id =upload(request.FILES['files'].read(),request.user.admission_number,folder_id)
        url= "https://drive.google.com/file/d/{id}/preview".format(id=id)
        workshops = Workshops(user=user,name=name,organiser=organiser,date=date,no_of_days=no_of_days,file_url=url)
        workshops.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
      return render(request, "website/workshops.html")


def upload(files,name,folder_id):


    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'website/credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': '{name}.pdf'.format(name=name),'parents':[folder_id],}
    media = MediaIoBaseUpload(io.BytesIO(files),mimetype=' application/pdf')

    file = service.files().create(body=file_metadata, media_body=media,fields='id').execute()
    return file.get("id")


    
