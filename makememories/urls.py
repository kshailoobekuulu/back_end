"""makememories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static

API_TITLE = 'Make Memories Api'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('companies.urls')),
    path('authentification/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include('posts.urls'), name='home'),
    path('docs/', include_docs_urls(title=API_TITLE)),
    path('schema/', schema_view)

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
