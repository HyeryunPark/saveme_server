import requests
import xmltodict
import json


def abandonedPetsParsing():
    # public api settings
    ServiceKey = "oH2mHVrDj%2BzIKdU4ZAuRqENqjNoOpdhCEYtcBD42m7rbpJ%2F2O5H3nFVoN1i7vycmeGnsTYWPKyhZHfdlRYUQEw%3D%3D"
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?ServiceKey={}".format(
        ServiceKey)

    req = requests.get(url).content
    # xmltodict : It changes xml type into dictionary.
    xmlObject = xmltodict.parse(req)
    jsonString = json.dumps(xmlObject['response']['body'], ensure_ascii=False)
    jsonObject = json.loads(jsonString)

    # allData = xmlObject['response']['body']['items']['item']
    # return allData
    for item in jsonObject['items']['item']:
        print(item)

    return item


print(abandonedPetsParsing())
