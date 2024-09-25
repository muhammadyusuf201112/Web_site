# root/urls.py
from django.contrib import admin
from django.urls import path
from apps.views import index, product
from django.conf import settings
from django.conf.urls.static import static
from apps import views
# from apps.views import con

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Using 'home' for index
    path('payment/', views.payment_view, name='payment_view'),
    path('product/<int:id>/', product, name='pro'), 
    path('contact/', views.con, name='con'),
      # Keep 'id' consistent in the view and URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
