from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Message(CommonModel):
    """Message Model Difinition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"


"""
related_name argument

이 오류는 이름이 같은게 원인이 아니다.
진짜 문제는 같은 이름을 가진 2개 이상의 모델이 같은 모델과 연결되어 있다는 것.
"""
