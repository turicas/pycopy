# coding: utf-8

import json

import requests


__version__ = '0.1.0-dev'
USER_AGENT = 'pycopy/{}'.format(__version__)
BASE_URL = 'https://api.copy.com'
AUTH_URL = BASE_URL + '/auth_user'  # TODO: should use /rest
OBJECTS_URL = BASE_URL + '/list_objects'  # TODO: should use /rest
DOWNLOAD_URL = BASE_URL + '/download_object'  # TODO: should use /rest


class Copy(object):
    """Base class to access Copy.com API"""

    def __init__(self, username, password):
        self.session = requests.session()
        self.session.headers.update({'X-Client-Type': 'api',
                                     'X-Api-Version': '1',
                                     'User-Agent': USER_AGENT, })
        self.authenticate(username, password)

    def _get(self, url, *args, **kwargs):
        return self.session.get(url, *args, **kwargs)

    def _post(self, url, data, *args, **kwargs):
        return self.session.post(url, {'data': json.dumps(data), }, *args,
                                 **kwargs)

    def authenticate(self, username, password):
        response = self._post(AUTH_URL,
                              {'username': username, 'password': password, })
        json_response = response.json()
        if 'auth_token' not in json_response:
            raise ValueError("Error while authenticating")

        self.user_data = json_response
        self.auth_token = json_response['auth_token']
        self.session.headers.update({'X-Authorization': self.auth_token, })

    def files_list_folder(self, path, recursive=False):
        response = self._post(OBJECTS_URL, {'path': path, })
        # TODO: implement recursive=True
        return response

    def files_download(self, path):
        object_url = BASE_URL + '/rest/meta/copy/' + path
        # TODO: '/copy' may not be needed
        response = copy.session.get(object_url)
        url = response.json()['url']
        # or: self.user_data['user_id']
        # https://copy.com/web/users/user-{user_id}/copy/{path}
        return self._get(url)

    def get(self, path):
        response = self._post(DOWNLOAD_URL, {'path': path})

    def put_object(self, path, fobj):
        object_url = BASE_URL + '/rest/meta/copy/' + path
        response = copy.session.post(object_url, files={'file': fobj})
        # TODO: change filename when sending
        return response.json()
