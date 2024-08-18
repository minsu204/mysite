from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bookings",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="bookings",
    )
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        blank=True,
        null=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for : {self.user}"
