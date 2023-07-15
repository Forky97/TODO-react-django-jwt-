from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView,RegistrationApiView
from rest_framework_simplejwt.views import TokenBlacklistView,TokenVerifyView,TokenRefreshView


urlpatterns = [
    path('notes/', views.NotesRetriew.as_view(), name="notes"),
    path('notes/create/', views.NoteCreate.as_view(), name="create-note"),
    path('notes/update/<int:pk>/', views.NoteChangeOne.as_view(), name="update-note"),
    path('notes/delete/<int:pk>/', views.NoteDeleteOne.as_view(), name="delete-note"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('notes/<int:pk>/', views.NoteGetOne.as_view(), name="note"),
    path('register/', views.RegistrationApiView.as_view(), name='register'),

]
