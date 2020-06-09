from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from info.models import About, Experience, Project, CV


def homepage(request):
	template_name = "index.html"
	def get_context_data(**kwargs):
		context = {}
		context['About'] = About.objects.all()
		context['Experience'] = Experience.objects.order_by('date')
		context['Projects'] = Project.objects.all().order_by('-id')
		context['CV'] = CV.objects.all().first()
		return context

	return render(request ,'index.html', get_context_data())


def details(request, id):
	print(id)
	project = Project.objects.get(id=id)
	context = {'project' : project}
	return render(request , 'detail.html' , context)
