from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="home"),
    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),
    path("account-settings/", views.account_settings_view, name="account_settings"),
]
