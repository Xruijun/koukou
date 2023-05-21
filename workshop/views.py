from django.shortcuts import render
from workshop.models import user_list
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


# Create your views here.
def register(request):
    return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # get获得name属性，不是id属性
    username = request.POST.get("username")
    password = request.POST.get("password")

    obj = user_list.objects.get(username)
    if username == obj['name'] and password == obj['password']:
        user_id = obj.id
        return render(request, 'workshop.html', {"user_id": user_id})
    return render(request, 'login.html', {"error_msg": "*用户名或密码错误"})


def workshop(request):
    return render(request, 'workshop.html')


@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        fs = FileSystemStorage(location="./media/temp")
        filename = fs.save(file.name, file)
        print(filename)
    if request.method == 'POST' and request.POST.get('X'):
        x = request.POST.get('X')
        y = request.POST.get('Y')
        pointlist = [x,y,1]
    return render(request, 'upload.html')


def author(request):
    usr = "shabi"
    introduction = "woshishabi"
    return render(request, 'author.html', {'username': usr, 'introduction': introduction})
