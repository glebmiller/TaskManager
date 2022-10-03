from django.db import models
from .user import User
from .tags import Tag

STATE_NEW = "new_task"
STATE_IN_DEVELOPMENT = "in_development"
STATE_IN_QA = "in_qa"
STATE_IN_CODE_REWIEV = "in_code_review"
STATE_READY_FOR_RELEASE = "ready_for_release"
STATE_RELEASED = "released"
STATE_ARCHIVED = "archived"

STATE_CHOICES = (
    (STATE_NEW, STATE_NEW),
    (STATE_IN_DEVELOPMENT, STATE_IN_DEVELOPMENT),
    (STATE_IN_QA, STATE_IN_QA),
    (STATE_IN_CODE_REWIEV, STATE_IN_CODE_REWIEV),
    (STATE_READY_FOR_RELEASE, STATE_READY_FOR_RELEASE),
    (STATE_RELEASED, STATE_RELEASED),
    (STATE_ARCHIVED, STATE_ARCHIVED),
)


TRANSITIONS = {
    STATE_NEW: [STATE_IN_DEVELOPMENT, STATE_ARCHIVED],
    STATE_IN_DEVELOPMENT: [STATE_IN_QA],
    STATE_IN_QA: [STATE_IN_DEVELOPMENT, STATE_IN_CODE_REWIEV],
    STATE_IN_CODE_REWIEV: [STATE_READY_FOR_RELEASE, STATE_IN_DEVELOPMENT],
    STATE_READY_FOR_RELEASE: [STATE_RELEASED],
    STATE_RELEASED: [STATE_ARCHIVED],
    STATE_ARCHIVED: [],
}


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = "high"
        MEDIUM = "medium"
        LOW = "low"

    class Meta:
        permissions = [
            # ("create_task", "Can create task"),
            # ("edit_task", "Can edit task"),
            # ("delete_task", "Can delete task"),
            ("change_status", "Can change status"),
            ("change_assigned", "Can change assigned"),
        ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date_of_creation = models.DateField()
    date_of_change = models.DateField()
    date_due = models.DateField()
    state = models.CharField(max_length=30, default=STATE_NEW, choices=STATE_CHOICES)
    priority = models.CharField(
        max_length=30, default=Priority.MEDIUM, choices=Priority.choices
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
