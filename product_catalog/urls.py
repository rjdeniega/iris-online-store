from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductCatalogView.as_view()),
    url(r'^stalls/(?P<stall_id>(\d+))/$', views.StallView.as_view()),
    url(r'^search/$', views.search),
    url(r'^cart/$', views.CartView.as_view()),
    url(r'^wish/(?P<product_id>(\d+))/$', views.WishList.as_view())
]