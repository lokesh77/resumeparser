from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from perficient import resume_parser
from .models import Resume, UploadResumeModelForm
from django.contrib import messages
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import os


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


@login_required
def homepage(request):
    if request.method == 'POST':
        Resume.objects.all().delete()
        file_form = UploadResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')
        resumes_data = []
        if file_form.is_valid():
            for file in files:
                try:
                    # saving the file
                    resume = Resume(resume=file)
                    resume.save()

                    # extracting resume entities
                    parser = resume_parser.ResumeParser(
                        os.path.join(settings.MEDIA_ROOT, resume.resume.name))
                    data = parser.get_extracted_data()
                    resumes_data.append(data)
                    resume.name = data.get('name')
                    resume.email = data.get('email')
                    resume.mobile_number = data.get('mobile_number')
                    resume.education = get_education(data.get('education'))
                    resume.educations = get_educations(data.get('educations'))
                    resume.skills = ', '.join(data.get('skills'))
                    resume.experience = ', '.join(data.get('experience'))
                    resume.experiences = data.get('experiences')
                    resume.save()
                except IntegrityError:
                    messages.warning(
                        request, 'Duplicate resume found:', file.name)
                    return redirect('homepage')
            resumes = Resume.objects.all()
            messages.success(request, 'Resumes uploaded!')

            return render(request, 'resumeparser/parser.html', {'resumes': resumes})
    else:
        form = UploadResumeModelForm()
    return render(request, 'resumeparser/parser.html', {'form': form})


def get_education(education):
    '''
    Helper function to display the education in human readable format
    '''
    education_string = ''
    for edu in education:
        education_string += edu[0]
    return education_string.rstrip(', ')


def get_educations(educations):
    '''
    Helper function to display the year in human readable format
    '''
    education_year = ''
    for edus in educations:
        education_year += ' (' + str(edus[1]) + '),'
    return education_year.rstrip(', ')
    print(education_year)
