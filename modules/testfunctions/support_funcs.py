import re


def is_employee_valid(employee_body, raise_error=True):
    """"""
    checkers = [{"compare": lambda body: body["employee_salary"] >= 0,
                 "message": "The salary can be less 0"},
                {"compare": lambda body: body["employee_age"] >= 12,
                "message": "An employee can't be younger 12"},
                {"compare": lambda body: body["employee_age"] <= 150,
                 "message": "An employee can't be older 150"},
                {"compare": lambda body: body["profile_image"] is not None,
                 "message": "Profile image can't be None"},
                {"compare": lambda body: isinstance(body["employee_name"], str),
                 "message": "The employee name must be a string"}
                # TODO add verify format of an employee_name by regexp
                ]

    is_valid = True
    for check_item in checkers:
        if not check_item["compare"](employee_body):
            print(check_item["message"])
            is_valid = False
            if raise_error:
                raise ValueError(check_item["message"])
    return is_valid
