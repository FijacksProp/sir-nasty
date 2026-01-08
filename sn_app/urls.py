from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('whitepaper/', views.whitepaper, name='whitepaper'),
    
    # Shop pages
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Cart actions
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    
    # Checkout & Paystack Payment
    path('checkout/', views.checkout, name='checkout'),
    path('initialize-payment/', views.initialize_payment, name='initialize_payment'),
    path('payment-callback/', views.payment_callback, name='payment_callback'),
    path('payment-success/<str:order_number>/', views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('paystack-webhook/', views.paystack_webhook, name='paystack_webhook'),
]