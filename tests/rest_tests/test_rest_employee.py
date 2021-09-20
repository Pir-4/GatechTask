import pytest
from http import HTTPStatus
from modules.rest_funcs.employee_rest import EmployeeRest


@pytest.fixture()
def rest_employee(request):
    return EmployeeRest.create_by_version(request.param)


@pytest.mark.parametrize('rest_employee', [1], indirect=True)
def test_create_positive(rest_employee):
    """"""
    rest_employee.create({"name": "test", "salary": "123", "age": "23"})
    t=1