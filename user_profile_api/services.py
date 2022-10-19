from rest_framework.response import Response
from user_profile_api import mocks
from requests.auth import HTTPDigestAuth
import requests, json, utils

from users_admin.settings import BASE_URL, DEVICE_UUID, ENVIRONMENT, GATEWAY_USER

def search_users():
    headers = {
        'Content-Type': 'application/json'
    }    

    payload = json.dumps(
        {
            "UserInfoSearchCond": {
                "searchID": "0",
                "searchResultPosition": 0,
                "maxResults": 1
            }
        }
    )

    if ENVIRONMENT == 'PROD':
        base_url = BASE_URL
        record_url = f'/ISAPI/AccessControl/UserInfo/Search?format=json&devIndex={DEVICE_UUID}'
        full_url = f'{base_url}{record_url}'

        res = requests.post(full_url, headers=headers, data=payload, auth=HTTPDigestAuth(GATEWAY_USER, utils.get_secret('GATEWAY_PASSWORD')))

        data = res.json()

        return Response(status=res.status_code, data=data)
    else:
        #return mocks.search_users_400()
        return mocks.search_users_200()

def record_user():
    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps(
        {
            "UserInfo": [
                {
                    "employeeNo": "21",
                    "name": "Juan Perez",
                    "userType": "normal",
                    "Valid": {
                        "enable": True,
                        "beginTime": "2017-01-01T00:00:00",
                        "endTime": "2025-08-01T17:30:08"
                    }
                }
            ]
        }
    )

    if ENVIRONMENT == 'PROD':
        base_url = BASE_URL
        record_url = f'/ISAPI/AccessControl/UserInfo/Record?format=json&devIndex={DEVICE_UUID}'
        full_url = f'{base_url}{record_url}'

        res = requests.post(full_url, headers=headers, data=payload, auth=HTTPDigestAuth(GATEWAY_USER, utils.get_secret('GATEWAY_PASSWORD')))

        data = res.json()

        return Response(status=res.status_code, data=data)
    else:
        #return mocks.record_user_400()
        #return mocks.record_user_200_already_exist()
        return mocks.record_user_200()


