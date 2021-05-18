from django.urls import path,include
from gstoreapp import views
urlpatterns = [
    path('latest-products/',views.LatestProductsList.as_view()),
    path(r'latest-products/<str:query>/',views.userSearch),
    path(r'latest-products/<str:categories>/<str:query>/',views.getSelectedCategory),
    path(r'products/<str:categoryslug>/<slug:productslug>/',views.viewProduct.as_view()),
    path(r'category/',views.getCategory),
    
   
]
