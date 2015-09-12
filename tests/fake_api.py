# coding: utf-8

import json
import urllib


CORRECT_AUTH = ('correct-user', 'correct-pass')
WRONG_AUTH = ('wrong-user', 'wrong-pass')


def _decode_body(body):
    return {key: urllib.unquote_plus(value)
            for key, value in [elem.split('=') for elem in body.split('&')]}


def _retrieve_body_data(body):
    decoded_body = _decode_body(body)
    assert 'data' in decoded_body

    return json.loads(decoded_body['data'])


def auth_user(request):
    'Create fake response for /auth_user'

    data = _retrieve_body_data(request.body)
    assert 'username' in data
    assert 'password' in data

    if (data['username'], data['password']) == CORRECT_AUTH:
        # TODO: fix this (put complete response)
        response = {'auth_token': 'xxx', }
    elif (data['username'], data['password']) == WRONG_AUTH:
        # TODO: fix this (put correct response)
        response = {'error': 'incorrect data', }
    else:
        raise ValueError('Incorrect auth for tests')

    headers = {'Content-Type': 'application/json'}
    return (200, headers, json.dumps(response))


def list_objects(request):
    'Create fake response for /list_objects'

    data = _retrieve_body_data(request.body)

    response = {'path': data['path'], }
    headers = {'Content-Type': 'application/json'}
    return (200, headers, json.dumps(response))
