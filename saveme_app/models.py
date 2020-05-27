from django.db import models


# Create your models here.


class User(models.Model):
    userEmail = models.CharField(max_length=25, unique=True, default='')
    userName = models.CharField(max_length=10, default='')
    userPw = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.userEmail


class Shelter(models.Model):
    status = models.CharField(max_length=3, default='', help_text='공고상태입력')
    species = models.CharField(max_length=5, default='', help_text='종')
    breed = models.CharField(max_length=20, default='', help_text='품종')
    date = models.DateTimeField(auto_now_add=True)
    # date = models.DateField(auto_now_add=True)
    area = models.CharField(max_length=20, default='', help_text='지역')
    spot = models.CharField(max_length=30, default='', help_text='발견 장소')
    gender = models.CharField(max_length=3, default='', help_text="성별")
    neuter = models.BooleanField(default=False, help_text='중성화 여부')
    pattern = models.CharField(max_length=10, default='', help_text='털 색')
    age = models.CharField(max_length=10, default='', help_text='나이')
    weight = models.CharField(max_length=5, default='', help_text='몸무게')
    notice_number = models.CharField(max_length=20, default='', help_text='공고번호')
    feature = models.CharField(max_length=30, default='', help_text='특이사항')
    protection_center = models.CharField(max_length=20, default='', help_text='보호센터')
    department_in_charge = models.CharField(max_length=20, default='', help_text='담당부서')
    protection_center_phone = models.CharField(max_length=11, default='', help_text='보호센터 전화번호')
    protection_center_address = models.CharField(max_length=30, default='', help_text='보호센터 주소')


class Missing(models.Model):
    status = models.CharField(max_length=3, default='', help_text='실종상태입력 (실종,보호,목격,완료)')
    date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=10, default='', help_text='시')
    district = models.CharField(max_length=10, default='', help_text='구')
    detailLocation = models.CharField(max_length=30, default='', help_text='상세주소')
    phone = models.CharField(max_length=11, default='', help_text='작성자 핸드폰번호')
    species = models.CharField(max_length=5, default='', help_text='동물 종')
    breed = models.CharField(max_length=50, default='', help_text='동물 품종')
    gender = models.CharField(max_length=3, default='', help_text='성별')
    neuter = models.BooleanField(default=False, help_text='중성화여부')
    age = models.CharField(max_length=10, default='', help_text='나이')
    weight = models.CharField(max_length=20, default='', help_text='몸무게')
    pattern = models.CharField(max_length=10, default='', help_text='털 색')
    feature = models.CharField(max_length=30, default='', help_text='특징')
    etc = models.CharField(max_length=30, default='', help_text='기타')
    # blank : 해당 속성이 비어도 되는지 나타내는 것
    # null : 해당 속성에 null 이 들어가도 되는지 나타내는 것
    # upload_to 인자를 함께 넣어 경로를 따로 지정할 수 있다. 하지만 MEDIA_ROOT 경로와 합쳐진다.
    image1 = models.ImageField(upload_to='missingBoard/images', blank=True, null=True, help_text='사진1')
    image2 = models.ImageField(upload_to='missingBoard/images', blank=True, null=True, help_text='사진2')
    image3 = models.ImageField(upload_to='missingBoard/images', blank=True, null=True, help_text='사진3')


class Community(models.Model):
    user_id = models.CharField(max_length=100, default='', help_text='작성자 uid')
    user_name = models.CharField(max_length=10, default='', help_text='작성자 이름')
    community_category = models.CharField(max_length=20, default='', help_text='글 카테고리')
    community_date = models.DateTimeField(auto_now_add=True, help_text='작성한 날짜')
    community_title = models.CharField(max_length=20, default='', help_text='글 제목')
    community_content = models.CharField(max_length=100, default='', help_text='글 내용')
    img1 = models.ImageField(upload_to='communityBoard/images', blank=True, null=True, help_text='사진1')
    img2 = models.ImageField(upload_to='communityBoard/images', blank=True, null=True, help_text='사진2')
    img3 = models.ImageField(upload_to='communityBoard/images', blank=True, null=True, help_text='사진3')


class NewsData(models.Model):
    title = models.CharField(max_length=200, help_text="뉴스 제목")
    link = models.URLField(null=True, default="", help_text="뉴스 링크")

    def __str__(self):
        return self.title
