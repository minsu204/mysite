from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    """
    Room Model Definition
    """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(
        max_length=180,
        default="",
    )

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        print(self.amenities.all())
        return self.amenities.count()


class Amenity(CommonModel):
    """
    Amenity Definition
    """

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


"""
Many To One
One to Many
Many to Many


보는 관점에 따라 다르다.

[room1, room2, room3] => User1 : Many To One
User1 => [room1, room2, room3] : One to Many
[Amenity1, Amenity2, Amenity3] => [room1, room2, room3] : Many to Many
room1 => [Amenity1, Amenity2, Amenity3]

"""
