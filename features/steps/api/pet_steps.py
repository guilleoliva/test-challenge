from behave import *
from faker import Faker

from features.steps.api.common_api_steps import create_entity_response
from utils.api_utils import requests_delete, requests_get, requests_post, requests_put


@step("A request to create a new pet through Petstore's API")
def create_pet(context):
    faker = Faker()
    context.pet_id = faker.pyint()
    context.category_name = "Dog"
    context.pet_name = faker.first_name()
    context.data = {
        "url": "/v2/pet",
        "json": {
            "id": context.pet_id,
            "category": {"id": 0, "name": context.category_name},
            "name": context.pet_name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "Black"}],
            "status": "available",
        },
    }


@step("the request is made to create a pet")
def send_new_pet_request(context):
    url = context.data["url"]
    context.response = requests_post(context, url, context.data["json"], headers=None)


@step("the pet is created")
@step("the user verifies that all the pet information is correct")
def verify_pet_created(context):
    pet_created = context.response.json()
    assert pet_created["id"] == context.pet_id, (
        "The pet ID doesn't match, expected " + context.pet_id + " current " + pet_created["id"]
    )
    assert pet_created["name"] == context.pet_name, (
        "pet name doesn't match, expected " + context.context.pet_name + " current " + pet_created["name"]
    )
    assert pet_created["category"]["name"] == context.category_name, (
        "pet category name doesn't match, expected "
        + context.category_name
        + " current "
        + pet_created["category"]["name"]
    )


@step("the user wants to get the recently created pet")
@step("the user wants to get the recently deleted pet")
def get_pet_by_id(context):
    url = "v2/pet/{}".format(context.pet_id)
    context.response = requests_get(context, url)


@step("The pet is removed to keep the application clean")
@step("the request is made to Delete a pet through Petstore's API")
def remove_pet_clean_application(context):
    context.response = requests_delete(context, "v2/pet/{}".format(context.pet_id), headers=None)
    create_entity_response(context)


@step("A request to update a pet through Petstore's API")
def update_pet(context):
    faker = Faker()
    context.category_name = "Cat"
    context.pet_name = faker.first_name()
    context.data = {
        "url": "/v2/pet",
        "json": {
            "id": context.pet_id,
            "category": {"id": 0, "name": context.category_name},
            "name": context.pet_name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "Black"}],
            "status": "available",
        },
    }


@step("the request is made to update a pet through Petstore's API")
def send_update_pet_request(context):
    url = context.data["url"]
    context.response = requests_put(context, url, context.data["json"], headers=None)
