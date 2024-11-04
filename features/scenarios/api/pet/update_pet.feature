@API @PET @AUREUM
Feature: [API] Update Pet

  Background:
    Given A request to create a new pet through Petstore's API
    When the request is made to create a pet
    Then the user is told the request to create was successful

  @SR-009 @SMOKE
  Scenario: Update a Pet
    And A request to update a pet through Petstore's API
    When the request is made to update a pet through Petstore's API
    Then the user is told the request to update was successful
    And the user verifies that all the pet information is correct
    And The pet is removed to keep the application clean

