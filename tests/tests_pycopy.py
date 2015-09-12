# coding: utf-8

import json
import unittest
import urllib

import responses

import fake_api

from pycopy import Copy


# TODO: test with wrong SSL certificate


class CopyClientTestCase(unittest.TestCase):

    def setUp(self):
        # As every test is going to authenticate we need to add this callback
        # on setUp
        responses.add_callback(responses.POST,
                               'https://api.copy.com/auth_user',
                                callback=fake_api.auth_user,
                                content_type='application/json')

    def authenticate(self):
        'Helper to authenticate on API'

        username, password = fake_api.CORRECT_AUTH
        self.copy = Copy(username, password)

    def assert_request_headers(self, request, form_encoded=True):
        'Assert if every request header is correct'

        self.assertEqual(request.headers['X-Api-Version'], '1')
        self.assertEqual(request.headers['X-Client-Type'], 'api')
        self.assertEqual(request.headers['User-Agent'], 'pycopy/0.1.0-dev')

        if form_encoded:
            self.assertEqual(request.headers['Content-Type'],
                             'application/x-www-form-urlencoded')

    @responses.activate
    def test_authenticate_error(self):
        username, password = fake_api.WRONG_AUTH

        with self.assertRaises(ValueError) as exception_context:
            copy = Copy(username, password)
        self.assertEqual(exception_context.exception.message,
                         'Error while authenticating')

        call = responses.calls[0]
        self.assert_request_headers(call.request)

        expected_response = {'error': 'incorrect data', }
        self.assertEqual(expected_response, call.response.json())

    @responses.activate
    def test_authenticate_ok(self):
        username, password = fake_api.CORRECT_AUTH

        copy = Copy(username, password)

        call = responses.calls[0]
        self.assert_request_headers(call.request)

        expected_response = {'auth_token': 'xxx', }
        self.assertEqual(expected_response, call.response.json())

    @responses.activate
    def test_files_list_folder_exists(self):
        self.authenticate()

        responses.add_callback(responses.POST,
                               'https://api.copy.com/list_objects',
                               callback=fake_api.list_objects,
                               content_type='application/json')
        self.copy.files_list_folder('/test')

        call = responses.calls[1]
        self.assert_request_headers(call.request)

        expected_response = {'path': '/test', }
        self.assertEqual(expected_response, call.response.json())
