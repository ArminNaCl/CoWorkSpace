from django.urls import path
from account.views import UserList, ProfileList, ProfileDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='users_api_url'),
    path('profiles/', ProfileList.as_view(), name='profile_api_url'),
    path('profiles/<int:user_id>/',ProfileDetail.as_view(),name='profile-detail-url')
]
