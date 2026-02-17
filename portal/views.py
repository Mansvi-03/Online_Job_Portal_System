from django.shortcuts import render, redirect
from .models import Job,Candidate, Application,Company

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        role = request.POST.get("role")

        request.session['email'] = email
        request.session['role'] = role  

        if role == "candidate":
            return redirect('user_home')
        elif role == "company":
            return redirect('company')
        elif role == "admin":
            return redirect('admin_home')

    return render(request, 'portal/Login.html')


def register(request):
    if request.method == "POST":
        role = request.POST.get("role")

        if role == "candidate":
            return redirect('user_home')
        elif role == "company":
            return redirect('company')

    return render(request, 'portal/Register.html')

def admin_home(request):
    return render(request, 'portal/Admin_home.html')

def user_home(request):
    return render(request, 'portal/User.html')

def find_jobs(request):
    jobs = None

    if request.method == "POST":
        city = request.POST.get('city')
        jobs = Job.objects.filter(location__icontains=city)

    return render(request, 'portal/Find_jobs.html', {'jobs': jobs})

def profile(request):
    return render(request, 'portal/Profile.html')

def applied_jobs(request):
    # if request.session.get('role') != 'candidate':
    #     return redirect('login')

    email = request.session.get('email')

    candidate = Candidate.objects.filter(email=email).first()

    if not candidate:
        return render(request, 'portal/Applied_jobs.html', {
            'applications': []
        })

    applications = Application.objects.filter(candidate=candidate)

    return render(request, 'portal/Applied_jobs.html', {
        'applications': applications
    })


def help_page(request):
    return render(request, 'portal/Help.html')

def company(request):
    return render(request, 'portal/Company.html')

def post_job(request):
    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        salary = request.POST.get('salary')

        # get logged-in company using session email
        company_email = request.session.get('email')

        company = Company.objects.filter(email=company_email).first()

        if not company:
            return redirect('login')

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary
        )

        return redirect('company')

    return render(request, 'portal/Post_job.html')


def view_applications(request):
    
    company_email = request.session.get('email')

    if not company_email:
        return redirect('login')

    company = Company.objects.filter(email=company_email).first()

    if not company:
        return redirect('login')

    jobs = Job.objects.filter(company=company)

    applications = Application.objects.filter(job__in=jobs)

    return render(request, 'portal/View_applications.html', {
        'applications': applications
    })




def schedule_interview(request):
    return render(request, 'portal/Schedule_interview.html')

def logout(request):
    return redirect('login')

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    # GET EMAIL FROM SESSION
    email = request.session.get('email')

    candidate = Candidate.objects.filter(email=email).first()

    # If not logged in properly, show message instead of redirect
    if not candidate:
        return render(request, 'portal/Apply_job.html', {
            'job': job,
            'error': 'Please login first'
        })

    if request.method == "POST":
        resume = request.FILES.get('resume')
        experience = request.POST.get('experience')

        Application.objects.create(
            candidate=candidate,
            job=job,
            resume=resume,
            experience=experience
        )

        return redirect('applied_jobs')

    return render(request, 'portal/Apply_job.html', {'job': job})



