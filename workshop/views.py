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
    if request.method == 'POST' and request.POST.get('X1'):
        pointlist = [[]for i in range(5)]
        x1 = request.POST.get('X1')
        y1 = request.POST.get('Y1')
        label1 = request.POST.get('label1')
        x2 = request.POST.get('X2')
        y2 = request.POST.get('Y2')
        label2 = request.POST.get('label2')
        x3 = request.POST.get('X3')
        y3 = request.POST.get('Y3')
        label3 = request.POST.get('label3')
        x4 = request.POST.get('X4')
        y4 = request.POST.get('Y4')
        label4 = request.POST.get('label4')
        x5 = request.POST.get('X5')
        y5 = request.POST.get('Y5')
        label5 = request.POST.get('label5')
        pointlist[0] = [x1,y1,label1]
        pointlist[1] = [x2, y2, label2]
        pointlist[2] = [x3, y3, label3]
        pointlist[3] = [x4, y4, label4]
        pointlist[4] = [x5, y5, label5]
        print(pointlist)
    return render(request, 'upload.html')


def author(request):
    usr = "shabi"
    introduction = "woshishabi"
    return render(request, 'author.html', {'username': usr, 'introduction': introduction})
