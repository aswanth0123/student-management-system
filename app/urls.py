from django.urls import path
from .import views
urlpatterns = [
# basic urls
    path('',views.login),
    path('logout',views.logout),

# admin urls

    path('admin_home',views.admin_home),
    path('add_course',views.add_course),
    path('admin_view_course/<name>',views.admin_view_course),
    path('add_student',views.add_student),
    path('admin_view_students',views.admin_view_students),
    path('add_staff',views.add_staff),
    path('admin_view_staffs',views.admin_view_staffs),
    path('admin_filter_student_by_cource',views.admin_filter_student_by_course),
    path('view_selecetd_course_std/<id>',views.admin_view_selecetd_course_std),
    path('admin_filter_student_by_date',views.admin_filter_student_by_date),
    path('add_fee',views.add_fee),
    path('admin_filter_student_by_name',views.admin_filter_student_by_name),
    path('add_batch_times',views.add_batch_times),
    path('view_batch_details',views.view_batch_details),




# student urls

    path('student_home',views.student_home),
   



# staff urls

    path('staff_home',views.staff_home),
    path('staff_view_all_students',views.staff_view_all_students),

]
