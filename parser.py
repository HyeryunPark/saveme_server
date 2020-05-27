# parser.py
import requests
from bs4 import BeautifulSoup
# 아래 4줄을 추가해 줍니다.
import os

# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saveme_project.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()
# NewsData를 import해옵니다.
from saveme_app.models import NewsData


def parse_blog():
    # HTTP GET Request
    req = requests.get('https://blog.naver.com/PostList.nhn?blogId=pawinhand&categoryNo=26&skinType=&skinId=&from=menu&userSelectMenu=true')
    # HTML 소스 가져오기
    html = req.text
    # html 을 python 객체로 파싱
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '#PostThumbnailAlbumViewArea > ul > li > a > div.area_text > strong'
    )
    print(my_titles)
    # my_url = soup.select(
    #     '#PostThumbnailAlbumViewArea > ul > li > a'
    # )
    data = {}
    for title in my_titles:
        data[title.text] = title.text
    return data


# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__ == '__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        NewsData(title=t, link=l).save()
