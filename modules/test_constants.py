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
    SUCCESS_MSG = "Successfully! Record has been fetched."
    NOT_FOUND_MSG = "Not found record"
    ID_NOT_FOUND_ERR = "id is empty"
