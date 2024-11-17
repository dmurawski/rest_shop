from django.db.models import F, Func, Q, Value
from django.db.models.aggregates import Count, Min
from django.db.models.functions import Concat
from django.shortcuts import render

from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):
    qs2 = Customer.objects.annotate(
        full_name=Concat("first_name", Value(" "), "last_name")
    )
    collection = Collection()
    collection.title = "xd"
    return render(
        request,
        "hello.html",
        {"x": "x", "orders": qs2},
    )
