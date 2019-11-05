from django.urls import path
from . import views

#app_name='tools'
urlpatterns = [
    #path('', views.index , name='index')
    path('', views.on_stock, name='on_stock'),
    path('all_issues/', views.all_issues, name='all_issues'),
    path('issue/', views.issue, name='issue'),
    path('<str:tool_name>', views.tool_det, name='tool_det'),
    path('issue/thanks/', views.thanks, name='thanks'),
    path('test/?id=4', views.test2, name='test2'),
    path('test/', views.test1, name='test1'),
    path('mv/', views.myview, name='mv'),
]
