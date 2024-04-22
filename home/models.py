from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

def validate_file_size(value):
    filesize = value.size
        
    max_size = 1024 * 1024 * 40 # 40MB
    if filesize > max_size:
        raise ValidationError("O tamanho máximo do arquivo que pode ser enviado é de 40MB")
    else:
        return value


class Setting(models.Model):
        
    about_us_text = models.TextField('Texto Sobre a V3L0Z', blank=True, null=True)
    about_us_image = models.ImageField('Imagem da Seção Sobre a V3L0Z', upload_to='home/images/logos', blank=True, null=True)
    projects_text = models.TextField('Texto da Seção de Projetos', blank=True, null=True)
    how_works_text = models.TextField('Texto da Seção de Como Funciona', blank=True, null=True)
    navbar_brand = models.FileField('Logo da Navbar', upload_to='home/images/logos', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'gif']), validate_file_size])
    navbar_brand_alt = models.CharField('Texto Alternativo da Logo da Navbar', max_length=100, blank=True, null=True)
    footer_brand = models.FileField('Logo do Rodapé', upload_to='home/images/logos', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'gif']), validate_file_size])
    promotional_video = models.FileField('Vídeo Promocional', upload_to='home/videos', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'm4v']), validate_file_size])
    video_thumbnail = models.ImageField('Thumbnail do Vídeo Promocional', upload_to='home/videos/thumb', blank=True, null=True)
    index_description = models.TextField('Descrição do Site', blank=True, null=True)
    metatags_image = models.ImageField('Imagem do Site', upload_to='home/images/logos', blank=True, null=True)
    
    def clean(self):
        if Setting.objects.count() > 0 and self.id != Setting.objects.first().id:
            raise ValidationError('Só pode haver uma instância de Configuração')
        super(Setting, self).clean()

    class Meta:
        verbose_name = "Configuração"
        verbose_name_plural = "Configurações"

    def __str__(self):
        return 'Configurações'
    

class Project(models.Model):
    
    name = models.CharField('Nome do Projeto', max_length=100)
    description = models.TextField('Descrição do Projeto', blank=True, null=True)
    image = models.ImageField('Imagem do Projeto', upload_to='home/images', blank=True, null=True)
    link = models.URLField('Link do Projeto', blank=True, null=True)
    unit = models.ForeignKey('home.Unit', verbose_name='Unidade', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.name


class User(AbstractUser):

    full_name = models.CharField('Nome do Dev', max_length=100)
    preferred_name = models.CharField('Cargo do Dev', max_length=100, blank=True, null=True)
    birthdate = models.TextField('Descrição do Dev', blank=True, null=True)
    picture = models.ImageField('Imagem do Dev', upload_to='home/images/devs', blank=True, null=True)
    gender = models.CharField('Gênero do Dev', max_length=100, blank=True, null=True)

    phone = models.CharField('Telefone do Dev', max_length=100, blank=True, null=True)
    linkedin = models.URLField('Linkedin do Dev', blank=True, null=True)
    github = models.URLField('Github do Dev', blank=True, null=True)

    role = models.CharField('Cargo do Dev', max_length=100, blank=True, null=True)
    unit = models.ForeignKey('home.Unit', verbose_name='Unidade', on_delete=models.CASCADE, blank=True, null=True)
    boss = models.ForeignKey('home.User', verbose_name='Chefe', on_delete=models.CASCADE, blank=True, null=True)
    admission_date = models.DateField('Data de Admissão', blank=True, null=True)
    resignation_date = models.DateField('Data de Saída', blank=True, null=True)
    
    def get_main_link(self):
        return self.socialmedia_set.filter(is_main=True).first()

    class Meta:
        verbose_name = "Dev"
        verbose_name_plural = "Devs"

    def __str__(self):
        return self.name


class Unit(models.Model):
    
    name = models.CharField('Nome da Unidade', max_length=100)
    local = models.CharField('Localização da Unidade', max_length=100, blank=True, null=True)
    description = models.TextField('Descrição da Unidade', blank=True, null=True)
    image = models.ImageField('Imagem da Unidade', upload_to='home/images/units', blank=True, null=True)
    link = models.URLField('Link da Unidade', blank=True, null=True)
    

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return self.name