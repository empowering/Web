from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add, name="add"),
    path("category", views.category, name="category"),
    path("category/<str:category_name>", views.categoryDetail, name="categoryDetail"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("detail/<int:list_id>", views.detail, name="detail"),
    path("detail/<int:list_id>/comment", views.comment, name='comment'),
    path("detail/<int:list_id>/bidding", views.bidding, name='bidding'),
    path("detail/<int:list_id>/like", views.post_like_toggle, name="like"),
    path('detail/<int:list_id>/delete',views.delete, name='delete'),
]
