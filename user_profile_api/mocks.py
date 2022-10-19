from rest_framework import status
import json

class MockResponse:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data

def search_users_200():
    data = json.dumps(
        {
            "UserInfoSearch": {
                "searchID": "0",
                "responseStatusStrg": "MORE",
                "numOfMatches": 1,
                "totalMatches": 10,
                "UserInfo": [
                    {
                        "employeeNo": "1",
                        "name": "Hernan",
                        "userType": "normal",
                        "closeDelayEnabled": False,
                        "Valid": {
                            "enable": True,
                            "beginTime": "2000-01-01T00:00:00",
                            "endTime": "2037-12-31T23:59:59",
                            "timeType": "local"
                        },
                        "belongGroup": "",
                        "password": "",
                        "doorRight": "1",
                        "RightPlan": [
                            {
                                "doorNo": 1,
                                "planTemplateNo": "1"
                            }
                        ],
                        "maxOpenDoorTime": 0,
                        "openDoorTime": 0,
                        "roomNumber": 0,
                        "floorNumber": 0,
                        "localUIRight": True,
                        "gender": "unknown",
                        "numOfCard": 1,
                        "numOfFace": 1,
                        "PersonInfoExtends": [
                            {
                                "value": ""
                            }
                        ]
                    }
                ]
            }
        }        
    )

    return MockResponse(status_code=status.HTTP_200_OK, data=data)

def search_users_400():
    data = json.dumps(
        {
            "errorCode": 1610612737,
            "errorMsg": "Incorrect parameter.",
            "statusCode": 6,
            "statusString": "Content Error",
            "subStatusCode": "badParameters"
        }
    )

    return MockResponse(status_code=status.HTTP_400_BAD_REQUEST, data=data)

def record_user_200():
    data = json.dumps(
        {
            "UserInfoOutList": {
                "UserInfoOut": [
                    {
                        "employeeNo": "22",
                        "errorCode": 1,
                        "errorMsg": "Operation completed.",
                        "statusCode": 1,
                        "statusString": "OK",
                        "subStatusCode": "ok"
                    }
                ]
            }
        }        
    )

    return MockResponse(status_code=status.HTTP_200_OK, data=data)

def record_user_200_already_exist():
    data = json.dumps(
        {
            "UserInfoOutList": {
                "UserInfoOut": [
                    {
                        "employeeNo": "22",
                        "errorCode": 1610637344,
                        "errorMsg": "employeeNoAlreadyExist",
                        "statusCode": 6,
                        "statusString": "Content Error",
                        "subStatusCode": "employeeNoAlreadyExist"
                    }
                ]
            }
        }        
    )

    return MockResponse(status_code=status.HTTP_200_OK, data=data)

def record_user_400():
    data = json.dumps(
        {
            "errorCode": 1610612737,
            "errorMsg": "Incorrect parameter.",
            "statusCode": 6,
            "statusString": "Content Error",
            "subStatusCode": "badParameters"
        }        
    )
        
    return MockResponse(status_code=status.HTTP_400_BAD_REQUEST, data=data)


