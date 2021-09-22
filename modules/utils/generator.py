import random
import sys
import string
from copy import copy
from modules.test_constants import POST_PARAM_LIST, POST_PARAM_TYPES, MIN_AGE, MAX_AGE, CLOSE_PARAM_TYPES


def get_bodies(number=5, excluded_params=None):
    """ Generate bodies for create cases

    :param number: number of bodies
    :type number: int
    :param excluded_params: parameter names witch excluded from generated body
    :type excluded_params: list
    :returns: valid bodies
    :rtype: list
    """
    bodies = []
    for _ in range(number):
        bodies.append(create_body(excluded_params))
    return bodies


def get_negative_post_bodies():
    """ Generate non valid bodies for create cases

    :returns: non valid bodies
    :rtype: list
    """
    bodies = [create_body()]  # body with id
    param_list = copy(POST_PARAM_LIST)
    param_list.remove("id")
    for param_name in param_list:
        bodies.append(create_body(excluded_params=["id", param_name]))
    for _ in range(5):
        bodies.append(create_body(excluded_params=["id"], is_bad_format=True))
    return bodies


def create_body(excluded_params=None, is_bad_format=False):
    """ Create body

    :param excluded_params: parameter names witch excluded from generated body
    :type excluded_params: list
    :param is_bad_format: generate body with non format parameters
    :type is_bad_format: bool
    :returns: body
    :rtype: dict
    """
    excluded_params = excluded_params or []
    excluded_params = excluded_params if isinstance(excluded_params, list) else [excluded_params]
    gen_funcs = {"int": lambda: random.randint(-sys.maxsize, sys.maxsize),
                 "age": lambda: random.randint(MIN_AGE, MAX_AGE),
                 "salary": lambda: random.randint(0, MAX_AGE),
                 "str": lambda: gen_string(),
                 "name": lambda: gen_string(allowed=["letters"], size=100, add_symbols=" "),
                 }
    body = {}
    for body_param in POST_PARAM_LIST:
        if body_param in excluded_params:
            continue
        param_format = POST_PARAM_TYPES[body_param]
        if is_bad_format:
            bad_formats = [item for item in POST_PARAM_TYPES.values() if item not in CLOSE_PARAM_TYPES[param_format]]
            param_format = random.choice(bad_formats)
        body[body_param] = gen_funcs[param_format]()
    return body


def gen_string(prefix="", allowed=None, size=None, postfix="", add_symbols=None):
    """ Generate string

    :param prefix: prefix of generated string
    :type prefix: str
    :param allowed: list of allowed symbols: letters, digits, punctuation
    :type allowed: list
    :param size: length of string
    :type size: int
    :param postfix: postfix of generated string
    :type postfix: str
    :param add_symbols: list of additional symbols
    :type add_symbols: list
    :returns:
    :rtype: str
    """
    symbols_dict = {"letters": string.ascii_letters, "digits": string.digits,
                    "punctuation": string.punctuation}
    allowed = allowed or ["letters", "digits", "punctuation"]
    symbols = []
    symbols += add_symbols or []
    for allow_key in allowed:
        symbols += symbols_dict[allow_key]
    size = size or random.randint(1, 50)
    result = prefix + "".join(random.choice(symbols) for _ in range(size)) + postfix
    return result
