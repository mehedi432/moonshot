from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

# Main views
from .views import index, send_main

# customizing admin interface
admin.site.site_header = 'Moonshot Blog Admin'
admin.site.site_title = 'Moonshot Blog'
admin.site.index_title = 'Moonshot Blog Administration'

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'), #for chnaging admin login view
    path('admin/logout/', auth_views.LogoutView.as_view(template_name='admin/logout.html'), name='login'), #for chnaging admin login view

    path("accounts/", include("django.contrib.auth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('rosetta/', include('rosetta.urls')),
    
    path('', include('blog.urls')),
    path('', index, name='index'),
    path('send_mail', send_main, name='send_mail'),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)