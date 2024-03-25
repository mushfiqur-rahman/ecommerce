from django.views.generic import TemplateView
from django.urls import path

# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'))
]
