from django.contrib import admin
from .models import House

# Register your models here.

"""
django는 custom Data에 대한 관리 패널을 자동으로 생성해줌.
"""

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    '''
    list_display로 admin의 컬럼들을 조절할 수 있다.
    단, column 은 model의 property만 된다.
    '''

    fields = (
        "name",
        "address",
        ("price_per_night", "pets_allowed"),
    )

    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )

    list_filter = (
        "price_per_night",
        "pets_allowed",
    )

    search_fields = (
        "address",
    )

    list_display_links = (
        "name",
        "address",
    )

    list_editable = (
        "pets_allowed",
    )

    