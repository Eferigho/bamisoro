from django.urls import path
from .views import (
    my_profile_view,
    invites_received_view,
    invite_profile_list_view,
    ProfileListView,
    ProfileDetailView,
    send_invitation,
    remove_from_friends,
    accept_invitation,
    reject_invitation,
    search_from_friends,
)

app_name = 'profiles'
urlpatterns = [
    path('userprofile/', my_profile_view, name='my-profile'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('to-invite/', invite_profile_list_view, name='invite-profile-view'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('search-for-friends/', search_from_friends, name='search-for-friends'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),

    path('my-invite/accept/', accept_invitation, name='accept-invite'),
    path('my-invite/reject/', reject_invitation, name='reject-invite'),
]
