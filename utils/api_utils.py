import json
from urllib.parse import urljoin

import requests

requests.packages.urllib3.disable_warnings()


def raise_http_error(response):
    status_code = response.status_code
    message = response.text
    request = response.request
    request_msg = "\n-url: {}\n-headers: {},\n-body: {}".format(request.url, request.headers, request.body)
    response_msg = "\n-code: {},\n-text: {}".format(status_code, message)
    raise Exception("\nREQUEST: {}\n\nRESPONSE: {}".format(request_msg, response_msg))


def get_app_url(context):
    return context.env_config["api_url"]


def get_joined_url(context, url):
    return urljoin(get_app_url(context), url)


def requests_get(context, url, headers=None):
    request_url, headers = create_request(context, url, headers)
    return requests.get(request_url, headers=headers)


def requests_post(context, url, data, headers=None):
    request_url, headers = create_request(context, url, headers)
    return requests.post(request_url, data=json.dumps(data), headers=headers)


def requests_delete(context, url, headers=None):
    request_url, headers = create_request(context, url, headers)
    return requests.delete(request_url, headers=headers)


def create_request(context, url, headers):
    request_url = get_joined_url(context, url)
    if "no_auth" not in context:
        context.no_auth = False
    if headers is None:
        if not context.no_auth:
            headers = {
                "Content-type": "application/json",
                "Accept": "application/json",
                "X-API-Key": "special-key",
            }
        elif context.no_auth:
            headers = {"Content-type": "application/json", "Accept": "text/plain"}
    return request_url, headers


def requests_put(context, url, data, headers=None):
    request_url, headers = create_request(context, url, headers)
    return requests.put(request_url, data=json.dumps(data), headers=headers)
