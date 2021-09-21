BASE_URI = "http://dummy.restapiexample.com/"
API_REST_VERSION_URI = {1: "api/v1"}
AVAILABLE_IDS = range(1, 25)


class RestPoints:
    """"""
    EMPLOYEE = "employee"
    CREATE = "create"


class ResponseMessages:
    """"""
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
POST_PARAM_LIST = ["id", "name", "salary", "age"]

MIN_AGE = 12
MAX_AGE = 150
