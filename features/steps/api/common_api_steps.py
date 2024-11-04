import requests
from behave import *

requests.packages.urllib3.disable_warnings()


@step("the user is told the get pet request was not found")
def verify_request_status_not_found(context):
    assert context.response.status_code == 404, "Expected status code 404, current " + str(
        context.response.status_code
    )
    assert context.response.reason == "Not Found", "Expected reason Not Found, current " + context.response.reason


@step("the user is told the request to create was successful")
@step("the user is told the get pet request was successful")
@step("the user is told the request to update was successful")
@step("the user is told the request to delete was successful")
def create_entity_response(context):
    assert context.response.status_code == 200, f"Expected status code 200, current {context.response.status_code}"
    assert context.response.reason == "OK", f"Expected reason OK, current {context.response.reason}"
