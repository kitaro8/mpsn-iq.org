from django.urls import path
from .views import combined_list_view, PostListView, Post2ListView, MagValueView, MagValue2View,  PostDetailView, PostDetailView2, PostListView3, PostListView4, PostListView5, PostListView6, PostListView2, PostUpdateView, PostDeleteView, Post2UpdateView, Post2DeleteView, UserPostListView, UserPost2ListView
from . import views

urlpatterns = [

    path('', combined_list_view, name='testdb-home'),
    # path('', home, name='testdb-home'),

    # path('', PostListView.as_view(), name='testdb-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    
    path('post/new/', views.upload, name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('mag_value/<int:pk>/', views.MagValueView.as_view(), name='mag_value'),
    path('post/<int:pk>/Update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('phase/<int:pk>/', views.PostDetailView2.as_view(), name='post_phase'),


    # path('/', Post2ListView.as_view(), name='testdb-home2'),
    path('user/<str:username>', UserPost2ListView.as_view(), name='user_posts'),

    path('post2/new/', views.upload2, name='post_create2'),
    path('post2/<int:pk>/', views.Post2DetailView.as_view(), name='post2_detail'),
    path('mag_value2/<int:pk>/', views.MagValue2View.as_view(), name='mag2_value'),
    path('post2/<int:pk>/Update', Post2UpdateView.as_view(), name='post2_update'),
    path('post2/<int:pk>/delete', Post2DeleteView.as_view(), name='post2_delete'),
    path('phase2/<int:pk>/', views.Post2DetailView2.as_view(), name='post2_phase'),

    
    path('search/', PostListView3.as_view(), name='search'),
    # path('results', views.search_posts, name='search_results'),
    path('search/focal', views.search_focal, name='search_focal'),
    
    path('focal/new/', views.upload_focal, name='focal_create'),
    path('focal/', PostListView2.as_view(), name='focal'),

    path('report/new/', views.upload_report, name='report_create'),
    path('report/', PostListView4.as_view(), name='report'),

    path('paper/new/', views.upload_paper, name='paper_create'),
    path('paper/', PostListView5.as_view(), name='paper'),
    
    path('seismic/', PostListView6.as_view(), name='testdb-seismic'),
    path("contact/", views.contact, name="contact"),
    path('about/', views.about, name='testdb-about'),
    path('publications/', views.publications, name='publications'),
    path('search_results/', views.search_results, name='search_results'),

    
]
