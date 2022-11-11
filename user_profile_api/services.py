from rest_framework.response import Response
from user_profile_api import mocks
from requests.auth import HTTPDigestAuth
import requests, json
from user_profile_api.urls_services import URL_SEARCH_USER, URL_RECORD_USER

from users_admin.settings import BASE_URL, DEVICE_UUID, ENVIRONMENT, GATEWAY_USER, GATEWAY_PASSWORD

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
        record_url = f'{URL_SEARCH_USER}?format=json&devIndex={DEVICE_UUID}'
        full_url = f'{base_url}{record_url}'

        res = requests.post(full_url, headers=headers, data=payload, auth=HTTPDigestAuth(GATEWAY_USER, GATEWAY_PASSWORD))

        data = res.json()

        return Response(status=res.status_code, data=data)
    else:
        #return mocks.search_users_400()
        return mocks.search_users_200()

def record_user(request):
    headers = {
        'Content-Type': 'application/json'
    }
	
    first_name = request.validated_data["first_name"]
    last_name = request.validated_data["last_name"]
    full_name = f'{first_name} {last_name}'
   
    begin_time = request.validated_data["begin_time"]
    begin_time_final = begin_time.strftime("%Y-%m-%dT%H:%M:%S")
    end_time = request.validated_data["end_time"]
    end_time_final = end_time.strftime("%Y-%m-%dT%H:%M:%S")
	

    payload = json.dumps(
        {
            "UserInfo": [
                {
                    "employeeNo": "91",
                    "name": full_name,
                    "userType": str(request.validated_data["profile_type"]),
                    "Valid": {
                        "enable": request.validated_data["is_active"],
                        "beginTime": begin_time_final,
                        "endTime": end_time_final
                    }
                }
            ]
        }
    )

    if ENVIRONMENT == 'PROD':
        base_url = BASE_URL
        record_url = f'{URL_RECORD_USER}?format=json&devIndex={DEVICE_UUID}'
        full_url = f'{base_url}{record_url}'
        
        res = requests.post(full_url, headers=headers, data=payload, auth=HTTPDigestAuth(GATEWAY_USER, GATEWAY_PASSWORD))	
        data = res.json()
        print(request.validated_data)

        return Response(status=res.status_code, data=data)
    else:
        #return mocks.record_user_400()
        #return mocks.record_user_200_already_exist()
        return mocks.record_user_200()


