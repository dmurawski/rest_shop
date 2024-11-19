from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   RetrieveModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .filters import ProductFilter
from .models import Cart, CartItem, Collection, OrderItem, Product, Review
from .pagination import DefaultPagination
from .serializers import (AddCartItemSerializer, CartItemSerializer,
                          CartSerializer, CollectionSerializer,
                          ProductSerializer, ReviewSerializer,
                          UpdateCartItemSerializer)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ["title", "description"]
    ordering_fields = ["unit_price", "last_update"]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(
                {
                    "error": "Product cant be deleted because it is associated with an order item",
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count("products"),
    ).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        collection = get_object_or_404(Collection, pk=kwargs["pk"])
        if collection.products.exists():
            return Response(
                {
                    "error": "Collections cant be deleted because it is associated with an product item",
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}


class CartViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
):
    queryset = Cart.objects.prefetch_related("items__product").all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}

    def get_queryset(self):
        return CartItem.objects.filter(
            cart_id=self.kwargs["cart_pk"],
        ).select_related("product")
