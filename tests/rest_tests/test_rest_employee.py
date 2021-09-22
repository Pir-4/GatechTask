import pytest
from http import HTTPStatus
from modules.rest_funcs.employee_rest import EmployeeRest
from modules.test_constants import ResponseMessages, AVAILABLE_IDS
from modules.utils import support_funcs, generator


@pytest.fixture()
def rest_version_employee(request):
    """Init employee object by REST API version"""
    return EmployeeRest.create_by_version(request.param)


@pytest.mark.parametrize('rest_version_employee', [1], indirect=True)
@pytest.mark.parametrize('employee_id', AVAILABLE_IDS)
def test_get_positive(rest_version_employee, employee_id):
    """Verify positive get cases"""
    status_code, body = rest_version_employee.get(employee_id)
    assert status_code == HTTPStatus.OK
    assert support_funcs.is_employee_valid(body["data"])
    assert body["message"] == ResponseMessages.GET_SUCCESS_MSG
    assert body["status"] == ResponseMessages.SUCCESS_STATUS


@pytest.mark.parametrize('rest_version_employee', [1], indirect=True)
@pytest.mark.parametrize('employee_id', [0, -1, "lol", 1.0])
def test_get_negative(rest_version_employee, employee_id):
    """Verify negative get cases"""
    status_code, body = rest_version_employee.get(employee_id)
    assert status_code == HTTPStatus.BAD_REQUEST
    assert body["errors"] == ResponseMessages.ID_NOT_FOUND_ERR
    assert body["message"] == ResponseMessages.NOT_FOUND_MSG
    assert body["status"] == ResponseMessages.ERROR_STATUS


@pytest.mark.parametrize('rest_version_employee', [1], indirect=True)
@pytest.mark.parametrize('expected_body', generator.get_bodies(excluded_params=["id"]))
def test_create_positive(rest_version_employee, expected_body):
    """Verify positive post cases"""
    status_code, body = rest_version_employee.create(expected_body)
    assert status_code == HTTPStatus.OK
    assert support_funcs.is_employee_valid(body["data"])
    employee_id = body["data"].pop("id")
    assert body["data"] == expected_body
    assert body["message"] == ResponseMessages.POST_SUCCESS_MSG
    assert body["status"] == ResponseMessages.SUCCESS_STATUS

    status_code, body = rest_version_employee.get(employee_id)
    assert status_code == HTTPStatus.OK
    assert body["message"] == ResponseMessages.GET_SUCCESS_MSG
    assert body["status"] == ResponseMessages.SUCCESS_STATUS
    assert support_funcs.is_employee_valid(body["data"])
    assert employee_id == body["data"].pop("id")
    assert support_funcs.equals(expected_body, body["data"])


@pytest.mark.parametrize('rest_version_employee', [1], indirect=True)
@pytest.mark.parametrize('expected_body', generator.get_negative_post_bodies())
def test_create_negative(rest_version_employee, expected_body):
    """Verify negative post cases"""
    status_code, body = rest_version_employee.create(expected_body)
    assert status_code == HTTPStatus.BAD_REQUEST
    assert body["status"] == ResponseMessages.ERROR_STATUS
