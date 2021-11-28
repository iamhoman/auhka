from django.urls import path
from .views import post_list, post_detail, post_create, post_delete, \
    post_like, post_comment

app_name = 'blog'

urlpatterns = [

    # post -- list, detail, create, delete
    path('list/', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('delete/<int:id>/', post_delete, name='post_delete'),

    # post -- CLS
    path ('like/<int:post_id>/', post_like, name='post_like'),
    path ('comment/<int:post_id>/', post_comment, name='post_comment'),
]
