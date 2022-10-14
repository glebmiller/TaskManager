from django.shortcuts import render
from rest_framework import viewsets
from main.models import User, Task, Tag
from serializers import UserSerializer, TaskSerializer, TagSerializer
import django_filters


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("username",)


class TaskFilter(django_filters.FilterSet):

    tag__title = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Task
        fields = (
            "state",
            "tag__title",
            "executor__username",
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("executor").order_by("id")
    serializer_class = TaskSerializer
    filterset_class = TaskFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
