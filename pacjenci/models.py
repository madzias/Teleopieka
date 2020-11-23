from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dom(models.Model):
    class Meta:
        verbose_name_plural = "Domy sąsiedzkie"

    nazwa = models.CharField(max_length=200, null=True)
    dzielnica = models.CharField(max_length=200, null=True)

    def __str__(self):
        return " - ".join([self.nazwa, self.dzielnica])

class Asystent(models.Model):
    class Meta:
        verbose_name_plural = "Asystenci"
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dom = models.ForeignKey(Dom, null=True, on_delete=models.SET_NULL)
    imie_i_nazwisko = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_dodania = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.imie_i_nazwisko

class Pacjent(models.Model):
    class Meta:
        verbose_name_plural = "Pacjenci"

    STATUS = (
        ('Lista rezerwowa', 'Lista rezerwowa'),
        ('Aktywny', 'Aktywny'),
        ('Zmarły', 'Zmarły'),
        ('Rezygnacja', 'Rezygnacja')
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    nr_IMEI = models.CharField(max_length=200, null=True)
    imie_i_nazwisko = models.CharField(max_length=200, null=True)
    dom = models.ForeignKey(Dom, null=True, on_delete=models.SET_NULL)
    data_dodania = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.imie_i_nazwisko

class Zgloszenie(models.Model):
    class Meta:
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"

    STATUS = (
        ('Nowe', 'Nowe'),
        ('W trakcie', 'W trakcie'),
        ('Rozwiązane', 'Rozwiązane')
    )
    RODZAJ = (
        ('Awaria', 'Awaria'),
        ('Rezygnacja', 'Rezygnacja'),
        ('Inne', 'Inne')
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    rodzaj = models.CharField(max_length=200, null=True, choices=RODZAJ)
    #asystent = models.ForeignKey(Asystent, null=True, on_delete=models.SET_NULL)
    pacjent = models.ForeignKey(Pacjent, null=True, on_delete=models.SET_NULL)
    opis = models.CharField(max_length=500, null=True)
    data_dodania = models.DateTimeField(auto_now_add=True, null=True)