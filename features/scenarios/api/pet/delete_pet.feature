@API @PET @AUREUM
Feature: [API] Delete a Pet

  Background:
    Given A request to create a new pet through Petstore's API
    When the request is made to create a pet
    Then the user is told the request to create was successful

  @SR-010 @SMOKE
  Scenario: Delete a Pet
    When the request is made to Delete a pet through Petstore's API
    Then the user is told the request to delete was successful
    When the user wants to get the recently deleted pet
    Then the user is told the get pet request was not found

