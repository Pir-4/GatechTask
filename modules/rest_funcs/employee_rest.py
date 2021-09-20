import json
from base_rest import BaseRestApi
from modules import test_constants


class EmployeeRest:

    @staticmethod
    def create_by_version(cls, api_version=1):
        """"""
        rest_version_url = test_constants.BASE_URI
        rest_version_url += test_constants.API_REST_VERSION_URI[api_version]
        return cls(rest_version_url)

    def __init__(self, base_url):
        """"""
        self._base_rest = BaseRestApi(base_url)

    def get(self, emp_id, expected_error=False):
        """"""
        result = self._base_rest.request("GET", test_constants.RestPoints.EMPLOYEE, emp_id)
        if expected_error:
            return result["status_code"], result
        return result["status_code"], json.loads(result["text"])

    def create(self, employee, expected_error=False):
        """"""
        result = self._base_rest.request("POST", test_constants.RestPoints.CREATE, params=employee)
        if expected_error:
            return result["status_code"], result
        return result["status_code"], json.loads(result["text"])
