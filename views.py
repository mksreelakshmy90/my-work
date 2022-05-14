from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import connection
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import get_user_model
User = get_user_model()
from login.models import User, Course
# from .models import Course
# Create your views here.
def signup(request):
 	return render(request, 'signup.html' )
 	# return HttpResponse("hihihi")

def insert(request):
	username = request.POST.get('username')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	pw1 = request.POST.get('password1')
	pw2=request.POST.get('password2')
	email = request.POST.get('email')
	course_id= request.POST.get('courses')
	qualification=request.POST.get('qualification')
	address=request.POST.get('address')
	pin=request.POST.get('pin')
	phone=request.POST.get('phone')
	cur = connection.cursor()
	# encr_pwd=pbkdf2_sha256.encrypt(pw1)

	user = User.objects.create_user(username, email, pw1)
	
	

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
	user.last_name = lastname
	user.first_name= firstname
	user.course_id=course_id
	user.is_superuser=0
	user.is_staff=1
	user.qualification=qualification
	user.address=address
	user.pin=pin
	user.phone=phone
	user.save()
	data=Course.objects.all()
	coursedetails = Course.objects.get(id=course_id)
	print(coursedetails.name)
	# for abc in coursename:
	# 	print(abc)

	print(data)
	context1= {
		
        'firstname': firstname,
        'lastname': lastname,
        'coursename':coursedetails.name,
        'coursefee':coursedetails.fee,
        # 'pendingfee':cc[0][1]-paidfee,
        'courseid': course_id,
        # 'userid':userid,

        }
	return render(request, 'userpage.html' , context1)
	# return HttpResponse("raw inserted")
# 	

def sell(request):
	coursename = Course.objects.get(id=1)
	print(coursename.name)
	# for aa in user:
	# 	print (aa.name)
	return HttpResponse("hgfhgf")







	#from anu all the below lines

	#from anu 26-28
# @user_passes_test(user_is_not_logged_in, login_url='/adminpage')
def index(request):
	return render(request, 'login.html')

@login_required(login_url='/')
def adminpage(request):
	return render(request, 'admin.html')

def logout_view(request):
	logout(request)
	return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def home_test(request):
	return render(request, 'test/home.html' )
	# return HttpResponse("haii")

def register(request):
	# return HttpResponse("register")
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = User.objects.create_user(username, 'ccc@thebeatles.com', password)
	user.last_name = username
	user.is_staff = 1
	user.course =1
	user.save()
	return HttpResponse("regiserd success fully")

def login1(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	# user = authenticate(request, username=username, password=password)
	user = authenticate(request, username=username, password=password)
	
	if user is not None:
		login(request,user)
		# return HttpResponse("success")
		response = redirect('/adminpage/')
		return response				
		# return render(request, 'index.html')
	else:
		return HttpResponse("fail")
		# response = redirect('/')
		# return response
		# return render(request, 'login.html')
	# return HttpResponse("login success fully")
