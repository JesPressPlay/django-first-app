from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    # Add another path object defining to URL pattern using `/date` prefix
    path(route='date', view=views.get_date, name='date'),
    # Adding another path for popular_course_list
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    path('course/<int:course_id>', views.course_details, name='course_details'),
]