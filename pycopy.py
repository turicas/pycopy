# coding: utf-8

import json

import requests


BASE_URL = 'https://api.copy.com'
AUTH_URL = BASE_URL + '/auth_user'
OBJECTS_URL = BASE_URL + '/list_objects'
DOWNLOAD_URL = BASE_URL + '/download_object'


class CopyClient(object):
    def __init__(self, username, password):
        self.session = requests.session()
        self.session.headers.update({'X-Client-Type': 'api',
                                     'X-Api-Version': '1'})
        self.authenticate(username, password)

    def _post(self, url, data):
        return self.session.post(url, {'data': json.dumps(data)})

    def authenticate(self, username, password):
        response = self._post(AUTH_URL, {'username': username,
                                         'password': password})
        json_response = response.json()
        if 'auth_token' not in json_response:
            raise ValueError()
        self.user_data = json_response
        self.auth_token = json_response['auth_token']
        self.session.headers.update({'X-Authorization': self.auth_token})

    def list_files(self, path='/'):
        response = self._post(OBJECTS_URL, {'path': path})
        return response

    def get(self, path):
        response = self._post(DOWNLOAD_URL, {'path': path})


    def put_object(self, path, fobj):
        object_url = BASE_URL + '/rest/meta/copy/' + path
        response = copy.session.post(object_url, files={'file': fobj})
        # TODO: change filename when sending
        return response.json()

    def get_object(self, path):
        object_url = BASE_URL + '/rest/meta/copy/' + path
        response = copy.session.get(object_url)
        url = response.json()['url']
        # or: self.user_data['user_id']
        # https://copy.com/web/users/user-{user_id}/copy/{path}
        return self.session.get(url)
