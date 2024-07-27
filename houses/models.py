'''
[models.py 의 목적]
App에 있는 데이터의 정의나 설명을 작성하는 파일

[사용]
1. models.py에서 사용할 데이터를 정의한다.
2. admin.py에 만든 model을 등록 (아래에선 House Class)
3. admin 페이지에서 error 발생 시 마이그레이션 확인
'''


from django.db import models

# Create your models here.
class House(models.Model):

    """
    #############################################
    TextField는 User가 긴 Text를 사용할 수 있게 함.
    문자길이 제한 시 CharField 사용
    #############################################

    모델을 만들 땐 모델에 대한 설명을 두는게 좋음
    작업 후 settings.py 에 반드시 이를 바라보라 알려줘야 함.
    """

    """ Model Definition for Houses """
    name = models.CharField(
        max_length=140,
    ) 
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price($)",
        help_text="Positive Number Only",
    )
    
    description = models.TextField()    

    address = models.CharField(
        max_length=140,
    )
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=True,
        help_text="Does this house allow pets?"
    )

    def __str__(self) -> str:
        return self.name