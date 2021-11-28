from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Scholar

# Create your views here.
class ScholarshipIntro(TemplateView):
    template_name = 'scholarship/intro.html'

class Swire(TemplateView):
    template_name = 'scholarship/swire.html'

class Chevening(TemplateView):
    template_name = 'scholarship/chevening.html'

class PastScholarListView (ListView):
    template_name = 'scholarship/scholarList_past.html'
    model = Scholar
    def get_queryset(self):
        queryset = Scholar.objects.filter(status='past')
        return queryset

class CurrentScholarListView (ListView):
    template_name = 'scholarship/scholarList_past.html'
    model = Scholar
    def get_queryset(self):
        queryset = Scholar.objects.filter(status='current')
        return queryset

class ScholarDetailView (DetailView):
    template_name = 'scholarship/scholar_detail.html'
    model = Scholar
    def get_context_data(self, **kwargs):
        context = super(ScholarDetailView, self).get_context_data()
        context['scholar_list'] = Scholar.objects.all()
        return context

class News_Application(TemplateView):
    template_name = 'scholarship/news_application.html'

