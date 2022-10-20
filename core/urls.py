from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView, TemplateView

admin.site.site_header = 'NBI Ninja Backend administration'
admin.site.site_title = 'NBI Ninja Backend Admin'

urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/docs', permanent=True), name='index'),
    path('admin/', admin.site.urls),
    path("api/", include('apps.api.urls')),
    path("robots.txt", TemplateView.as_view(template_name="core/robots.txt", content_type="text/plain")),
    # add the robots.txt file
]
