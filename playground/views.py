from django.db.models import F, Func, Q, Value
from django.db.models.aggregates import Count, Min
from django.db.models.functions import Concat
from django.shortcuts import render

from store.models import Collection, Customer, Order, OrderItem, Product
from django.core.mail import send_mail, mail_admins, BadHeaderError
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name="emails/hello.html",
            context={
                "name": "Damian",
            },
        )
        message.send(["test@email.com"])
    except BadHeaderError:
        pass
    return render(
        request,
        "hello.html",
        {"x": "x"},
    )
