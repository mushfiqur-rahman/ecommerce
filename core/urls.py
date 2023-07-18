from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Ecommerce Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground', include('playground.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
