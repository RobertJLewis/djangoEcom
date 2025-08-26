from django.urls import path
from . import models, views 


app_name = 'orders'
urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('checkout-cancelled/', views.checkout_cancelled, name='checkout_cancelled'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('checkout-start/', views.checkout_view, name='checkout_start'),
]