from django.urls import path
from . import views

urlpatterns = [
    path('rejestracja/', views.registerPage, name="register"),
    path('logowanie/', views.loginPage, name="login"),
    path('wylogowanie/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('profil_asystenta/', views.userPage, name = "profil_asystenta"),
    path('pacjenci/', views.pacjenci, name = "pacjenci"),
    path('pacjenci_asystent/', views.pacjenci_asystent, name = "pacjenci_asystent"),
    path('asystenci/<str:pk_test>/', views.asystenci, name = "asystenci"),
    path('aktualizuj_asystenta/<str:pk>/', views.aktualizujAsystenta, name="aktualizuj_asystenta"),
    path('pacjent_podglad/<str:pk_test>/', views.pacjent_podglad, name="pacjent_podglad"),

    path('dodaj_zgloszenie/', views.dodajZgloszenie, name = "dodaj_zgloszenie"),
    path('aktualizuj_zgloszenie/<str:pk>/', views.aktualizujZgloszenie, name = "aktualizuj_zgloszenie"),
    path('usun_zgloszenie/<str:pk>/', views.usunZgloszenie, name = "usun_zgloszenie"),

    path('aktualizuj_pacjenta/<str:pk>/', views.aktualizujPacjenta, name="aktualizuj_pacjenta"),
    path('usun_pacjenta/<str:pk>/', views.usunPacjenta, name="usun_pacjenta")
]
