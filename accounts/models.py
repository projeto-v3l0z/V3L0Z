from django.db import models
from django.contrib.auth.models import AbstractUser
from home.models import Unit

class User(AbstractUser):
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    full_name = models.CharField('Nome Completo do Dev', max_length=100, blank=True, null=True)
    preferred_name = models.CharField('Nome Preferencial do Dev', max_length=100, blank=True, null=True)
    birthdate = models.DateField('Data de Nascimento do Dev', blank=True, null=True)
    picture = models.ImageField('Imagem do Dev', upload_to='home/images/devs', blank=True, null=True)
    gender = models.CharField('Gênero do Dev', max_length=1, blank=True, null=True, choices= gender_choices)
    
    phone = models.CharField('Telefone do Dev', max_length=100, blank=True, null=True)
    linkedin = models.URLField('Linkedin do Dev', blank=True, null=True)
    github = models.URLField('Github do Dev', blank=True, null=True)

    role = models.CharField('Cargo do Dev', max_length=100, blank=True, null=True)
    boss = models.ForeignKey('self', verbose_name='Chefe', on_delete=models.CASCADE, blank=True, null=True)
    unit = models.ForeignKey('home.Unit', verbose_name='Unidade', on_delete=models.CASCADE, blank=True, null=True)
    admission_date = models.DateField('Data de Admissão', blank=True, null=True)
    resignation_date = models.DateField('Data de Saída', blank=True, null=True)

    class Meta:
            db_table = 'auth_user'
            verbose_name = "Usuário"
            verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            if self.unit:
                self.unit.devs.add(self)