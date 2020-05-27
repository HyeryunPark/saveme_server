import requests
import xmltodict
import json


class abandonedPetsParsing():
    # public api settings
    ServiceKey = "oH2mHVrDj%2BzIKdU4ZAuRqENqjNoOpdhCEYtcBD42m7rbpJ%2F2O5H3nFVoN1i7vycmeGnsTYWPKyhZHfdlRYUQEw%3D%3D"
    # url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?ServiceKey={}".format(ServiceKey)
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey={}".format(
        ServiceKey) + "&bgnde=20200101&endde=20200416&numOfRows=5000"

    req = requests.get(url).content
    # xmltodict : It changes xml type into dictionary.
    xmlObject = xmltodict.parse(req)
    jsonString = json.dumps(xmlObject['response']['body'], ensure_ascii=False)
    jsonObject = json.loads(jsonString)

    allData = xmlObject['response']['body']['totalCount']

    def __str__(self):
        return self.allData

    # # allData = xmlObject['response']['body']['items']['item']
    # # return allData
    # for item in jsonObject['items']['item']:
    # # for item in jsonObject['totalCount']:
    #     print(item)
    #
    # return len(jsonObject['items']['item'])
    # # return len(jsonObject['totalCount'])


print(abandonedPetsParsing())
