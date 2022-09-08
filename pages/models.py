from django.db import models

# Create your models here.


class announcements(models.Model):

    picturename = models.CharField(blank=True, null=True, max_length=50, verbose_name='resim link')
    title = models.CharField(blank=True, null=True, max_length=50, verbose_name='başlık')
    text = models.TextField(blank=True, null=True, verbose_name='mesaj')
    postdate = models.DateField(blank=True,null=True, verbose_name='yayınlanma tarihi')
    column = models.IntegerField(null=False, verbose_name='sütun seçimi')



class teams(models.Model):
    teamname = models.CharField(null=False, max_length=50, verbose_name='takım adı')
    teamdescribtion = models.TextField(blank=True, null=True, verbose_name='takım açıklaması')
    teamlogo = models.CharField(blank=True, null=True, max_length=50, verbose_name='resim link')


class teammembers(models.Model):

    class roles(models.TextChoices):
        CAP =  "kaptan"
        SOF =  "yazılım"
        MEC =  "mekanik"
        ELE =  "elektronik"

    role = models.CharField(
        max_length=10,
        choices=roles.choices,
        default=roles.ELE,
        verbose_name='takımdaki rolü'
    )

    teamname = models.CharField(null=False, max_length=50, verbose_name='takım adı')
    image = models.CharField(blank=True,null=True, max_length=50, verbose_name='resim link')
    department = models.CharField(blank=True,null=True, max_length=50, verbose_name='bölüm')
    name = models.CharField(blank=True, null=True, max_length=50, verbose_name='İsim')
    github = models.CharField(blank=True,null=True, max_length=50, verbose_name='github')
    instagram = models.CharField(blank=True,null=True, max_length=50, verbose_name='insta') 
    email = models.EmailField(blank=True,null=True, verbose_name='email')
    linkedin = models.CharField(blank=True,null=True, max_length=50, verbose_name='linkedin')
    

class managers(models.Model):
    picture = models.CharField(blank=True,null=True, max_length=100, verbose_name='resim link')
    name = models.CharField(blank=True, null=True, max_length=50, verbose_name='İsim')
    role = models.CharField(blank=True, null=True, max_length=50, verbose_name='Görev')
    department = models.CharField(blank=True,null=True, max_length=50, verbose_name='bölüm')
    grade = models.CharField(blank=True,null=True, max_length=50, verbose_name='sınıf')
    email = models.EmailField(blank=True,null=True, verbose_name='email')
    linkedin = models.CharField(blank=True,null=True, max_length=200, verbose_name='linkedin')
    instagram = models.CharField(blank=True,null=True, max_length=200, verbose_name='insta')
    display = models.IntegerField(blank=False,null=False, verbose_name='gösterim sırası')


class sponsors(models.Model):
    
    class roles(models.TextChoices):
        Ana =  "ANA"
        gold = "ALTIN"
        silver = "GÜMÜŞ"
        

    level = models.CharField(
        max_length=10,
        choices=roles.choices,
        verbose_name='Sponsorluk seviyesi'
    )

    
    picture = models.CharField(blank=True,null=True, max_length=50, verbose_name='resim adı')
    name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Şirket adı')
    website = models.URLField(blank=True, null=True, verbose_name='Web sitesi')
    email = models.EmailField(blank=True,null=True, verbose_name='email')
    linkedin = models.CharField(blank=True,null=True, max_length=50, verbose_name='linkedin')
    instagram = models.CharField(blank=True,null=True, max_length=50, verbose_name='insta')
