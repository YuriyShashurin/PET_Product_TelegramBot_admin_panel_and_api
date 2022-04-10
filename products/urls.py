from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.BotsViews.as_view(), name='dashboard'),
    path('bot/<int:pk>', views.ItemsView.as_view(), name='items'),
    path('create_bot/', views.CreateBotView.as_view(), name='create_bot')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
