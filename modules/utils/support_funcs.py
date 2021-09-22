from modules.test_constants import MIN_AGE, MAX_AGE, FIELD_MAP


def is_employee_valid(employee_body, raise_error=True):
    """"""
    checkers = [{"keys": ["salary", "employee_salary"],
                 "compare": lambda body, check_key: body[check_key] >= 0,
                 "message": "The salary can be less 0",
                 "is_required": True},
                {"keys": ["age", "employee_age"],
                 "compare": lambda body, check_key: body[check_key] >= MIN_AGE,
                 "message": f"An employee can't be younger {MIN_AGE}",
                 "is_required": True},
                {"keys": ["age", "employee_age"],
                 "compare": lambda body, check_key: body[check_key] <= MAX_AGE,
                 "message": f"An employee can't be older {MAX_AGE}",
                 "is_required": True},
                {"keys": ["profile_image"],
                 "compare": lambda body, check_key: body[check_key] is not None,
                 "message": "Profile image can't be None"},
                {"keys": ["name", "employee_name"],
                 "compare": lambda body, check_key: isinstance(body[check_key], str),
                 "message": "The employee name must be a string",
                 "is_required": True},
                # TODO add verify format of an employee_name by regexp
                {"keys": ["id"],
                 "compare": lambda body, check_key: isinstance(body[check_key], int),
                 "message": "The id must be int",
                 "is_required": True}
                ]

    error_messages = []
    if not isinstance(employee_body, dict):
        error_messages.append("Employee body must be a dict")
    else:
        for check_item in checkers:
            inter = set(check_item["keys"]).intersection(set(employee_body.keys()))
            if not inter and check_item.get("is_required", False):
                error_messages.append(F"Employee body doesn't contain keys {check_item['key']}")
                continue
            elif not inter and not check_item.get("is_required", False):
                continue

            if not check_item["compare"](employee_body, list(inter)[0]):
                error_messages.append(check_item["message"])

    if error_messages:
        print(error_messages)
        if raise_error:
            raise AssertionError(error_messages)
        return False
    return True


def equals(post_body, get_body, raise_error=True):
    """"""
    error_messages = []
    for field_name in post_body.keys():
        get_field_name = FIELD_MAP[field_name]
        if post_body[field_name] != get_body[get_field_name]:
            message = f"POST {field_name}: {post_body[field_name]}, GET {get_field_name}: {get_body[get_field_name]}"
            error_messages.append(message)
    if error_messages:
        message = "Bodies don't equal:\n" + "\n".join(error_messages)
        print(message)
        if raise_error:
            raise AssertionError(message)
        return False
    return True

