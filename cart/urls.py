from django.urls import path
from.import views
urlpatterns =[
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('addcart/<int:id>/',views.addcart,name='addcart'),
    path('cart_decreament/<int:product_id>/', views.min_cart, name='cart_decreament'),
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),

    # path('addcart', views.addcart, name='addcart'),

]