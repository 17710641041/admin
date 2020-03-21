from __future__ import unicode_literals
from .users_views import (
    RegistHandle,
    loginHandle
)

urls = [
    # 从 /users/register 过来的请求，将调用 users_views 里面的 RegistHandle 类
    (r'register', RegistHandle),
    (r'login', loginHandle)
]
