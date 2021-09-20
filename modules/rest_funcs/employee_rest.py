import json
from modules.rest_funcs.base_rest import BaseRestApi
from modules import test_constants


class EmployeeRest:
    """Provide Rest API for employee's end point"""

    @staticmethod
    def create_by_version(api_version=1):
        """ Create EmployeeRest

        :param api_version: api version: 1
        :type api_version: int
        :returns: EmployeeRest object with right version api url
        :rtype: EmployeeRest
        """
        rest_version_url = test_constants.BASE_URI
        rest_version_url += test_constants.API_REST_VERSION_URI[api_version]
        return EmployeeRest(rest_version_url)

    def __init__(self, base_url):
        """ Init class

        :param base_url: url of an information system
        :type base_url: str
        :returns: None
        """
        self._base_rest = BaseRestApi(base_url)

    def get(self, emp_id, expected_error=False):
        """ Get employee by id

        :param emp_id: employee id
        :type emp_id: int
        :param expected_error: True if expected an error else False
        :type expected_error: bool
        :returns: response status code, body response
        :rtype: int, dict
        """
        result = self._base_rest.request("GET", test_constants.RestPoints.EMPLOYEE, str(emp_id))
        if expected_error:
            return result["status_code"], result
        return result["status_code"], json.loads(result["text"])

    def create(self, employee, expected_error=False):
        """ Create employee

        :param employee: request body for creating an employee
        :type employee: dict
        :param expected_error: True if expected an error else False
        :type expected_error: bool
        :returns: response status code, body response
        :rtype: int, dict
        """
        result = self._base_rest.request("POST", test_constants.RestPoints.CREATE, params=employee)
        if expected_error:
            return result["status_code"], result
        return result["status_code"], json.loads(result["text"])
