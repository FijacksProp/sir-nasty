from django.shortcuts import render, get_object_or_404, redirect
from .models import Logo, Product, Order, OrderItem
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from .cart import Cart
import requests
import json
import hmac
import hashlib

# Create your views here.

def home(request):
    logo = Logo.objects.first()  # Get the first logo, assuming one is uploaded
    context = {'logo': logo}
    return render(request, 'homepage.html', context)

def whitepaper(request):
    logo = Logo.objects.first()  # Get the first logo, assuming one is uploaded
    context = {'logo': logo}
    return render(request, 'whitepaper.html', context)

def shop(request):
    logo = Logo.objects.first()  # Get the first logo, assuming one is uploaded
    """
    Shop page - display all active products
    """
    # Get all active products
    all_products = Product.objects.filter(is_active=True)

    # Separate recommended products
    recommended_products = all_products.filter(is_recommended=True)
    other_products = all_products.filter(is_recommended=False)

    context = {
        'recommended_products': recommended_products,
        'other_products': other_products,
        'all_products': all_products,
        'logo': logo,
    }

    return render(request, 'shop.html', context)


def product_detail(request, slug):
    logo = Logo.objects.first()  # Get the first logo, assuming one is uploaded
    """
    Product detail page - display full product information
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)

    context = {
        'product': product,
        'logo': logo,
    }

    return render(request, 'product_detail.html', context)


def cart_detail(request):
    logo = Logo.objects.first()  # Get the first logo, assuming one is uploaded
    """
    Cart page - display cart contents
    """
    cart = Cart(request)
    
    # Calculate totals
    cart_items = []
    for item in cart:
        cart_items.append(item)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.get_total_price(),
        'logo': logo,
    }
    
    return render(request, 'cart.html', context)


@require_POST
def cart_add(request, product_id):
    """
    Add product to cart (AJAX endpoint)
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Get quantity from POST data (default 1)
    quantity = int(request.POST.get('quantity', 1))
    
    cart.add(product=product, quantity=quantity)
    
    # Return JSON response for AJAX
    return JsonResponse({
        'success': True,
        'cart_count': len(cart),
        'message': f'{product.name} added to cart'
    })


@require_POST
def cart_remove(request, product_id):
    """
    Remove product from cart
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    
    return redirect('cart_detail')


@require_POST
def cart_update(request, product_id):
    """
    Update product quantity in cart (AJAX endpoint)
    """
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    
    cart.update_quantity(product_id, quantity)
    
    # Return updated cart info
    return JsonResponse({
        'success': True,
        'cart_count': len(cart),
        'cart_total': str(cart.get_total_price())
    })


def checkout(request):
    logo = Logo.objects.first()
    """
    Checkout page with Paystack payment
    """
    cart = Cart(request)
    
    if len(cart) == 0:
        return redirect('shop')
    
    # Calculate total in kobo (Paystack uses smallest currency unit)
    # For NGN: multiply by 100 to get kobo
    total_amount = cart.get_total_price()
    total_kobo = int(total_amount * 100)
    
    # Get cart items
    cart_items = list(cart)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': total_amount,
        'total_kobo': total_kobo,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
        'logo': logo,
    }
    
    return render(request, 'checkout.html', context)


def initialize_payment(request):
    """
    Initialize Paystack payment (AJAX endpoint)
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart = Cart(request)
            
            # Calculate amount in kobo
            amount = int(cart.get_total_price() * 100)
            
            # Prepare Paystack request
            url = 'https://api.paystack.co/transaction/initialize'
            headers = {
                'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
                'Content-Type': 'application/json',
            }
            
            # Build cart items list for metadata
            cart_items = []
            for item in cart:
                cart_items.append({
                    'product': item['product'].name,
                    'quantity': item['quantity'],
                    'price': str(item['price'])
                })
            
            payload = {
                'email': data.get('email'),
                'amount': amount,
                'currency': 'NGN',
                'callback_url': request.build_absolute_uri('/payment-callback/'),
                'metadata': {
                    'full_name': data.get('full_name'),
                    'phone': data.get('phone'),
                    'address_line1': data.get('address_line1'),
                    'address_line2': data.get('address_line2', ''),
                    'city': data.get('city'),
                    'state': data.get('state'),
                    'postal_code': data.get('postal_code', ''),
                    'country': data.get('country', 'Nigeria'),
                    'cart_items': cart_items,
                }
            }
            
            # Make request to Paystack
            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()
            
            if response_data['status']:
                return JsonResponse({
                    'status': 'success',
                    'authorization_url': response_data['data']['authorization_url'],
                    'access_code': response_data['data']['access_code'],
                    'reference': response_data['data']['reference'],
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': response_data.get('message', 'Payment initialization failed')
                }, status=400)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def payment_callback(request):
    """
    Handle Paystack callback after payment
    """
    reference = request.GET.get('reference')
    
    if not reference:
        return redirect('shop')
    
    # Verify payment with Paystack
    url = f'https://api.paystack.co/transaction/verify/{reference}'
    headers = {
        'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
    }
    
    response = requests.get(url, headers=headers)
    response_data = response.json()
    
    if response_data['status'] and response_data['data']['status'] == 'success':
        # Payment successful
        cart = Cart(request)
        payment_data = response_data['data']
        metadata = payment_data.get('metadata', {})
        
        # Create order
        order = Order.objects.create(
            email=payment_data['customer']['email'],
            full_name=metadata.get('full_name', ''),
            phone=metadata.get('phone', ''),
            address_line1=metadata.get('address_line1', ''),
            address_line2=metadata.get('address_line2', ''),
            city=metadata.get('city', ''),
            state=metadata.get('state', ''),
            postal_code=metadata.get('postal_code', ''),
            country=metadata.get('country', 'Nigeria'),
            total_amount=payment_data['amount'] / 100,  # Convert from kobo to naira
            payment_status='paid',
            status='processing',
            paystack_reference=reference,
        )
        
        # Create order items
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )
        
        # Clear cart
        cart.clear()
        
        return redirect('payment_success', order_number=order.order_number)
    else:
        # Payment failed or was cancelled
        return redirect('payment_failed')


def payment_success(request, order_number):
    """
    Payment success page
    """
    logo = Logo.objects.first()
    order = get_object_or_404(Order, order_number=order_number)
    
    context = {
        'order': order,
        'items': order.items.all(),
        'logo': logo,
    }
    
    return render(request, 'payment_success.html', context)


def payment_failed(request):
    """
    Payment failed page
    """
    logo = Logo.objects.first()
    
    context = {
        'logo': logo,
    }
    
    return render(request, 'payment_failed.html', context)


@csrf_exempt
def paystack_webhook(request):
    """
    Handle Paystack webhooks for payment notifications
    """
    if request.method == 'POST':
        # Verify webhook signature
        signature = request.headers.get('x-paystack-signature')
        
        if signature:
            body = request.body
            hash_value = hmac.new(
                settings.PAYSTACK_SECRET_KEY.encode('utf-8'),
                body,
                hashlib.sha512
            ).hexdigest()
            
            if hash_value == signature:
                # Process webhook event
                event = json.loads(body)
                
                if event['event'] == 'charge.success':
                    # Payment successful - update order
                    reference = event['data']['reference']
                    try:
                        order = Order.objects.get(paystack_reference=reference)
                        order.payment_status = 'paid'
                        order.status = 'processing'
                        order.save()
                    except Order.DoesNotExist:
                        pass
                
                return JsonResponse({'status': 'success'})
        
        return JsonResponse({'error': 'Invalid signature'}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)