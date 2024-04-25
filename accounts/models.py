from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField('Nome do Dev', max_length=100, blank=True, null=True)
    preferred_name = models.CharField('Cargo do Dev', max_length=100, blank=True, null=True)
    birthdate = models.TextField('Descrição do Dev', blank=True, null=True)
    picture = models.ImageField('Imagem do Dev', upload_to='home/images/devs', blank=True, null=True)
    gender = models.CharField('Gênero do Dev', max_length=100, blank=True, null=True)

    phone = models.CharField('Telefone do Dev', max_length=100, blank=True, null=True)
    linkedin = models.URLField('Linkedin do Dev', blank=True, null=True)
    github = models.URLField('Github do Dev', blank=True, null=True)

    role = models.CharField('Cargo do Dev', max_length=100, blank=True, null=True)
    unit = models.ForeignKey('home.Unit', verbose_name='Unidade', on_delete=models.CASCADE, blank=True, null=True)
    admission_date = models.DateField('Data de Admissão', blank=True, null=True)
    resignation_date = models.DateField('Data de Saída', blank=True, null=True)

    class Meta:
            db_table = 'auth_user'
