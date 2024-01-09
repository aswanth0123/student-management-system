from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from hashlib import md5


''' 
        -------------------normal functions---------------------


'''


def time():
    time=Batch_times.objects.all()
    return time

def course():
    course=Course.objects.all()
    return course
def students():
    std=student.objects.all()
    return std
def staff():
    staff=Staff.objects.all()
    return staff

def session_id(re):
    try:
        s_id=Staff.objects.get(emp_id=re.session['staff'])
    except:
        try:
            s_id=student.objects.get(addmission_no=re.session['staff'])
        except:
            s_id=re.session['admin']

    return s_id

def logout(re):
    re.session.flush()
    return redirect(login)




def login(re):
    if re.method=='POST':
        username=re.POST['username']
        password=re.POST['password']
        p1= md5(password.encode()).hexdigest()
        try:
            falculty=Staff.objects.get(emp_id=username,password=p1)
            re.session['staff']=username
            return redirect(staff_home)
        except:
            try:
                student_dtls=student.objects.get(addmission_no=username,password=p1)
                re.session['student']=username
                return redirect(student_home)
            except:
                if username=='admin' and password=='admin':
                    re.session['admin']=username
                    return redirect(admin_home)
                else:
                    messages.success(re,'invalid username and password')
                    return redirect(login)


    return render(re,'login.html')


''' 
        -------------------Admin side---------------------


'''


def admin_home(re):
    d=Staff.objects.filter(possition='faculty')
    return render(re,'project_admin/html/index.html',{'course':course(),'d':d,'student':students(),'staff':staff()})
 
def add_course(re):
    if re.method=='POST':
        c_name=re.POST['c_name']
        duration=re.POST['duration']
        discription=re.POST['discription']
        image=re.FILES['image']
        selected_options = re.POST.getlist('checkbox_option')
        instance, created = YourModel.objects.get_or_create(name='Instance Name')

        for label in selected_options:
                print(label)

                checkbox_value, _ = Course.objects.get_or_create(course_name=label)
                instance.time.add(checkbox_value)
        instance.save()


        try:
            course=Course.objects.create(course_name=c_name,duration=duration,discription=discription,image=image)
            course.save()
            messages.success(re,'Course added')
        except:
            messages.success(re,'Course already exists')
    
    return render(re,'project_admin/html/add_course.html',{'time':time()})

def admin_view_course(re,name):
    single_course=Course.objects.get(course_name=name)
    return render(re,'project_admin/html/admin_view_course.html',{'single_course':single_course})
def add_student(re):
    if re.method=='POST':
        add_no=re.POST['add_no']
        s_name=re.POST['name']
        fee=re.POST['fee']
        r_fee=re.POST['r_fee']        
        phno=re.POST['phno']
        date=re.POST['date']
        email=re.POST['email']
        uname=add_no
        password=s_name[0:4]+phno[0:4]
        subject = 'Registration details '
        message = 'ur account uname {}  and password {}'.format(uname,password)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        cur=re.POST['c_name']
        course_std=Course.objects.get(course_name=cur)
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)  
        o_password=md5(password.encode()).hexdigest()
        student1=student.objects.create(addmission_no=add_no,name=s_name,email=email,fee=fee,paid_fee=r_fee,phno=phno,password=o_password,course=course_std,doj=date)
        student1.save()
        messages.success(re,'student details added') 
        
    return render(re,'project_admin/html/add_student.html',{'course':course()})


def admin_view_students(re):
    return render(re,'project_admin/html/view_students.html',{'students':students()})


def add_staff(re):
    if re.method=='POST':
        emp_no=re.POST['emp_no']
        s_name=re.POST['name']
        salary=re.POST['salary']
        # r_fee=re.POST['r_fee']        
        phno=re.POST['phno']
        email=re.POST['email']
        uname=emp_no
        password=s_name[0:4]+phno[0:4]
        subject = 'Registration details '
        message = 'ur account uname {}  and password {}'.format(uname,password)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        pos=re.POST['position']
        date=re.POST['date']
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)  
        o_password=md5(password.encode()).hexdigest()
        student1=Staff.objects.create(emp_id=emp_no,name=s_name,email=email,salary=salary,password=o_password,doj=date,possition=pos)
        student1.save()
        messages.success(re,'Staff details added')
    return render(re,'project_admin/html/add_staff.html',{'course':course()})

def admin_view_staffs(re):
    faculty=Staff.objects.all()
    return render(re,'project_admin/html/admin_view_staffs.html',{'faculty':faculty})

def admin_filter_student_by_course(re):
    return render(re,'project_admin/html/filter_std_by_course.html',{'course':course(),'students':students()})
def admin_view_selecetd_course_std(re,id):
    cur=Course.objects.get(course_name=id)
    student_dtls=student.objects.filter(course=cur)
    return render(re,'project_admin/html/filter_by_course.html',{'students':student_dtls})

def admin_filter_student_by_date(re):
    if re.method=='POST':
        s_date=re.POST['s_date']
        e_date=re.POST['e_date']
        print(s_date,e_date)
        students=student.objects.filter(doj__gte=s_date,doj__lte=e_date)
        print(students)
     
        return render(re,'project_admin/html/filter_std_by_date.html',{'course':course(),'students':students})
    return render(re,'project_admin/html/filter_std_by_date.html',{'course':course()})

def admin_filter_student_by_name(re):
    if re.method=='POST':
        pass
    
    return render(re,'project_admin/html/filter_std_by_name.html',{'student':students()})

def add_fee(re):
    if re.method=='POST':
        pass

    return render(re,'project_admin/html/add_fee.html',{'course':course()})


def add_batch_times(req):
    if req.method=='POST':
        s_time=req.POST['s_time']
        e_time=req.POST['e_time']
        b_time=Batch_times.objects.create(start_time=s_time,end_time=e_time)
        b_time.save()
        messages.success(req,'Batch added')
    return render(req,'project_admin/html/add_batch_timings.html',{'course':course()})

def view_batch_details(req):
    batch=Batch_times.objects.all()
    return render(req,'project_admin/html/view_batch_details.html',{'batch':batch})

''' 
        -------------------student side---------------------


'''

def student_home(re):
    return render(re,'')

''' 
        -------------------staff side---------------------


'''
def staff_home(re):
    return render(re,'staff/faculty_home.html',{'staff':session_id(re)})

def staff_view_all_students(re):
    std_dtls=student.objects.filter(faculty=session_id(re))
    return render(re,'staff/view_all_students.html',{'std_dtls':std_dtls})
