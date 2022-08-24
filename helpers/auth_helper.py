import jwt
from const import (JWT_SECRET,
                   JWT_ALGORITHM)
from flask import request, abort


def auth_required(func):
    def wrapper(*args, **kwargs):
        _check_auth_in_header()

        token = _get_token_from_header()
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        _check_auth_in_header()

        token = _get_token_from_header()
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get("role")
            if role != "admin":
                abort(400)
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def _check_auth_in_header():
    if 'Authorization' not in request.headers:
        abort(401)


def _get_token_from_header():
    data = request.headers['Authorization']
    return data.split("Bearer ")[-1]
