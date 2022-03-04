from http import client
from django.shortcuts import redirect, render
from projects.models import Project
from .models import Slider, Project , Testimonial , Client , Contact
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def project_index(request):
    sliders = Slider.objects.all()[0:3]
    testimonials = Testimonial.objects.all()[0:3]
    projects = Project.objects.all()
    clients = Client.objects.all()
    context = {
        'projects': projects,
        'sliders':sliders,
        'testimonials': testimonials,
        'clients':clients,
        'page_title': "Home"
        }
    return render(request, 'home/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'page_title': "Details"
    }
    return render(request, 'details/project_detail.html', context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        comment = request.POST['comment']
        Contact.objects.create(first_name=fname, last_name=lname, email=email, message=comment)
        send_mail(f"{fname} {lname} sent Contact Message.", comment ,"sabbirahmedfarhan45@gmail.com", [email], fail_silently=True)
        return redirect('contact')
    return render(request, 'contact.html', {'page_title': "Contact"})

def project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'page_title': "Project"
    }
    return render(request, 'project_list.html', context)