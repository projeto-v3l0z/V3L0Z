from django.views.generic import ListView
from .models import Project, Unit


class IndexView(ListView):
    template_name = 'home/index.html'
    model = Project
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["units"] = Unit.objects.all()
        return context
    
