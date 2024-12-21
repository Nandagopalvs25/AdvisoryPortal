from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from .models import Internships, Extracurriculur, Mooc, Workshops, CustomUser, Student, Advisor, Department, Batch
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
import io
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import JsonResponse
from django.apps import apps
from django.template.loader import render_to_string


MODEL_MAP = {
    'moc': Mooc,
    'interns': Internships,
    'workshops': Workshops,
    'extrac': Extracurriculur
  
}


def index(request):
    return render(request, "website/index.html")


class SearchView(ListView):
    model = CustomUser
    template_name = 'studentslist.html'


@login_required
def dashboard(request):
    if (request.user.is_advisor == True):
        return render(request, "website/advisordashboard.html")
    else:
        return render(request, "website/dashboard.html")


@login_required
def certificates(request):
    return render(request, "website/certificates.html")


@login_required
def advisor_studentsList(request):
    advisor = Advisor.objects.get(user=request.user)
    print(advisor.department)
    batch_id = request.GET.get('batch')
    batches_in_department = Batch.objects.filter(department=advisor.department)
    students_in_department = Student.objects.filter(
        department=advisor.department)
    if (batch_id == "Choose batch..."):
        students_in_department = Student.objects.filter(
            department=advisor.department)
        html = render_to_string(
            'website/advisor_partial_studentslist.html',
            {'students': students_in_department})
        return JsonResponse({'html': html})
    
    elif (batch_id != None):
        students_in_department = Student.objects.filter(
            department=advisor.department).filter(batch=batch_id)
        html = render_to_string(
            'website/advisor_partial_studentslist.html',
            {'students': students_in_department})
        return JsonResponse({'html': html})

    return render(request, "website/advisor_studentslist.html", {'students': students_in_department, 'batches': batches_in_department})


@login_required
def student_uploads_view(request):
    mooc = Mooc.objects.filter(user=request.user)
    intern = Internships.objects.filter(user=request.user)
    workshops = Workshops.objects.filter(user=request.user)
    extras = Extracurriculur.objects.filter(user=request.user)
    return render(request, "website/student_uploaded_documents.html", {'mooc': mooc, 'intern': intern, 'workshops': workshops, 'extras': extras})


@login_required
def advisor_approval_view(request):
    department = Advisor.objects.get(user=request.user).department
    students = Student.objects.filter(department=department)
    student_user_ids = students.values_list('user_id', flat=True)
    internships = Internships.objects.filter(
        user_id__in=student_user_ids).filter(is_approved=False)
    moocs = Mooc.objects.filter(
        user_id__in=student_user_ids).filter(is_approved=False)
    extracurriculars = Extracurriculur.objects.filter(
        user_id__in=student_user_ids).filter(is_approved=False)
    workshops = Workshops.objects.filter(
        user_id__in=student_user_ids).filter(is_approved=False)
    context = {
        "department": department,
        "students": students,
        "internships": internships,
        "moocs": moocs,
        "extracurriculars": extracurriculars,
        "workshops": workshops,
    }
    return render(request, "website/advisor_approvals.html", context)


@login_required
def mooc(request):
    if request.method == "POST":

        user = request.user
        title = request.POST['title']
        type = request.POST['type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        student = Student.objects.get(user=user)
        folder_id = student.batch.gdrive_folder_url
        id = upload(request.FILES['files'].read(),
                    student.admission_number, folder_id)
        url = "https://drive.google.com/file/d/{id}/preview".format(id=id)
        mooc = Mooc(user=user, course_title=title, course_type=type,
                    start_date=start_date, end_date=end_date, file_url=url)
        mooc.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
    return render(request, "website/mooc.html")


@login_required
def internship(request):
    if request.method == "POST":

        user = request.user
        name = request.POST['name']
        company = request.POST['company']
        days = request.POST['days']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        student = Student.objects.get(user=user)
        folder_id = student.batch.gdrive_folder_url
        id = upload(request.FILES['files'].read(),
                    student.admission_number, folder_id)
        url = "https://drive.google.com/file/d/{id}/preview".format(id=id)
        intern = Internships(user=user, name=name, company=company, no_of_days=days,
                             start_date=start_date, end_date=end_date, file_url=url)
        intern.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")


    return render(request, "website/internship.html")


@login_required
def extrac(request):

    if request.method == "POST":

        user = request.user
        title = request.POST['title']
        organiser = request.POST['organiser']
        date = request.POST['date']
        level = request.POST['event_level']
        type = request.POST['event_type']
        position = request.POST['position']
        student = Student.objects.get(user=user)
        folder_id = student.batch.gdrive_folder_url
        id = upload(request.FILES['files'].read(),
                    student.admission_number, folder_id)
        url = "https://drive.google.com/file/d/{id}/preview".format(id=id)
        extrac = Extracurriculur(user=user, event_title=title, event_organiser=organiser, event_date=date,
                                 event_level=level, event_type=type, event_position=position, file_url=url)
        extrac.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")

    return render(request, "website/extras.html")


def workshops(request):
    if request.method == "POST":

        user = request.user
        name = request.POST['name']
        organiser = request.POST['organiser']
        date = request.POST['date']
        no_of_days = request.POST['days']
        student = Student.objects.get(user=user)
        folder_id = student.batch.gdrive_folder_url
        id = upload(request.FILES['files'].read(),
                    student.admission_number, folder_id)
        url = "https://drive.google.com/file/d/{id}/preview".format(id=id)
        workshops = Workshops(user=user, name=name, organiser=organiser,
                              date=date, no_of_days=no_of_days, file_url=url)
        workshops.save()

        messages.success(request, "Uploaded Succesfully.")
        return HttpResponseRedirect("/")
    return render(request, "website/workshops.html")


def upload(files, name, folder_id):

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'website/credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': '{name}.pdf'.format(
        name=name), 'parents': [folder_id], }
    media = MediaIoBaseUpload(io.BytesIO(files), mimetype=' application/pdf')

    file = service.files().create(body=file_metadata,
                                  media_body=media, fields='id').execute()
    return file.get("id")


@login_required
def delete(request, model_name, id):

    obj = get_object_or_404(MODEL_MAP.get(model_name), id=id)
    obj.delete()
    messages.success(request, "Deleted Succesfully.")
    return HttpResponseRedirect("/uploads/")
