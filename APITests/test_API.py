import requests
from requests.exceptions import HTTPError


class TestAPI:
    content_type = 'application/json; charset=utf-8'
    res_body_data = {"id": 1, "title": "Post 1"}

    def test_status_code(self):
        try:
            res = requests.get('https://my-json-server.typicode.com/typicode/demo/posts/1')
            res.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            assert res.status_code == 200, 'Status code is not matched'

    def test_content_type(self):
        try:
            res = requests.get('https://my-json-server.typicode.com/typicode/demo/posts/1')
            res.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            assert res.headers.get('content-type') == self.content_type

    def test_response_body_data(self):
        try:
            res = requests.get('https://my-json-server.typicode.com/typicode/demo/posts/1')
            res.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            assert res.json() == self.res_body_data, 'Response body data not matched'
            print(res.headers)


