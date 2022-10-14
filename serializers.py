from rest_framework import serializers
from main.models import User, Tag, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("title",)


class TaskSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "date_of_creation",
            "date_of_change",
            "date_due",
            "state",
            "priority",
            "executor",
            "tag",
        )
