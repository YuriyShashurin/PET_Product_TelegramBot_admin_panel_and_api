from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('all/', views.ItemsView.as_view()),
    path('<int:id>/', views.ItemView.as_view()),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.login_user, name='login')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)