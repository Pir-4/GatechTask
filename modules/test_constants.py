BASE_URI = "http://dummy.restapiexample.com/"
API_REST_VERSION_URI = {1: "api/v1"}
AVAILABLE_IDS = range(1, 25)


class RestPoints:
    """ Storage Rest endpoints name """

    EMPLOYEE = "employee"
    CREATE = "create"


class ResponseMessages:
    """Storage REST response messages"""

    SUCCESS_STATUS = "success"
    ERROR_STATUS = "error"
    GET_SUCCESS_MSG = "Successfully! Record has been fetched."
    POST_SUCCESS_MSG = "Successfully! Record has been added."
    NOT_FOUND_MSG = "Not found record"
    ID_NOT_FOUND_ERR = "id is empty"


POST_PARAM_TYPES = {"id": "int",
                    "name": "name",
                    "salary": "salary",
                    "age": "age"}
CLOSE_PARAM_TYPES = {"int": ["int", "age", "salary"],
                     "age": ["int", "age", "salary"],
                     "salary": ["int", "age", "salary"],
                     "name": ["name", "str"],
                     "str": ["name", "str"]}
POST_PARAM_LIST = ["id", "name", "salary", "age"]

FIELD_MAP = {"id": "id",
             "name": "employee_name",
             "salary": "employee_salary",
             "age": "employee_age"}
MIN_AGE = 12
MAX_AGE = 150
