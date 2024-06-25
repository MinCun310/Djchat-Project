import jwt
from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser


user = get_user_model()


@database_sync_to_async
def get_user(scope):
    token = scope['token']
    user_id = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])['user_id']

    try:
        return user.objects.get(id=user_id)
    except user.DoesNotExist:
        return AnonymousUser()


def get_access_token(cookieStr):
    cookie_dict = {}
    for cookie in cookieStr.split('; '):
        if cookie.split('=')[0] == 'access_token':
            cookie_dict[cookie.split('=')[0]] = cookie.split('=')[1]
    return cookie_dict


class JWTAuthMiddleWare:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Lấy headers và chuyển sang dictionary
        headers_dict = dict(scope['headers'])
        print('headers_dict:::', headers_dict)
        # Trong headers lấy cookies và cho convert sang string
        cookies_str = headers_dict.get(b"cookie", b"").decode()
        print('cookies_str:::', cookies_str)
        # convert sang dict và lấy access token
        # cookie_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split('; ')}
        cookie_dict = get_access_token(cookies_str)
        print('cookie_dict:::', cookie_dict)
        # Lấy access token
        access_token = cookie_dict.get('access_token')
        scope['token'] = access_token
        scope['user'] = await get_user(scope)
        return await self.app(scope, receive, send)
