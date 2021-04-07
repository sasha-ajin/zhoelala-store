from django.shortcuts import render
from .models import *
import json
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse


class Store(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/store.html'


def cart(request):
    if request.user.is_authenticated:
        customer_ = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer_, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items_quantity': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer_ = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer_, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items_quantity': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action, 'ID:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)