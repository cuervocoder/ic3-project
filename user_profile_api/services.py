from rest_framework.response import Response
import requests
import utils

from users_admin.settings import BASE_URL, DEVICE_UUID, GATEWAY_USER

def record_user(self, request):
    """
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
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

    base_url = BASE_URL
    record_url = f"/ISAPI/AccessControl/UserInfo/Record?format=json&devIndex={DEVICE_UUID}"
    full_url = f"{base_url}{record_url}"

    res = requests.post(full_url, headers=headers, data=payload, auth={GATEWAY_USER, utils.get_secret("GATEWAY_PASSWORD")})

    print('This is the true http resonse: ', res.status_code)

    if res.status_code >= 300:
        return Response({"error": "Request failed"}, status = res.status_code)
    else:
        data = res.json()
        return Response({"status": "success", "data": data})
    """
