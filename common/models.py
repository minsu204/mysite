from django.db import models


# 여기에 작성하는 것은 DB에 안 넣을 예정
# 다른 model에서 재사용하기 위한 model
class CommonModel(models.Model):
    """
    Common Model definition
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    """
    아래 class Meta는 django에서 model을 config할 때 사용하는데,
    abstract = True로 하면 이 모델은 DB에 config하지 않는다.

    ※ abstract 는 이 model은 DB에서 실 데이터로 사용되지 않는다 라는 의미를 가짐
    """

    class Meta:
        abstract = True
