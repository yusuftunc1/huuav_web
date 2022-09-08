from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
from pages.models import teams

        


def login(request):

    team = teams.objects.all()

    content = {
        'teams': team
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #kullanıcı adı ve şifresi eşleşen bir kullanıcı varsa obje olarak döndürme
        user = auth.authenticate(username= username, password= password)
        #döndürülen objeyi kontrol etme
        if user is not None:
            #session oluşturma
            auth.login(request, user)
            #mesaj ekleme
            messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
            ### yetki kontrolu eklenecek
            return redirect('mainpage',)
        else:

            messages.add_message(request, messages.ERROR, 'Kullanıcı adı ve ya paralo yanlış')
            return redirect('login',)

    else:
        #eğer sayfa ilk kez açılıyorsa ve bir post değeri gönderilmediyse sayfa açılmalı
        return render(request, 'user/login.html', content)
    

def register(request):

    team = teams.objects.all()

    content = {
        'teams': team
    }
    
    if (request.method == 'POST'):
        
        #form değerlerini alma
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST["repassword"]

        #şifre kontol
        if password == repassword:
            #username kontrol
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, "Bu kullanıcı adı daha önce alınmış" )

                return redirect('register')
            else:
                #mail kontrol
                if User.objects.filter(email = email).exists():
                    
                    messages.add_message(request, messages.WARNING, "Bu mail daha önce alınmış")
                    return redirect('register')
                else:
                    #okey create user
                    user = User.objects.create_user(username= username, password= password, email= email)
                    user.save()
                    
                    messages.add_message(request, messages.SUCCESS, 'Kullanıcı oluşturuldu')
                    return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, "Paralolar eşleşmiyor")

            return redirect('register')

    else:
        return render(request, 'user/register.html' , content)



def logout(request):
    if request.method == 'POST':
        #session id silme
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturumunuz kapatıldı")
        return redirect('mainpage')

    return render(request, 'pages/index.html')

