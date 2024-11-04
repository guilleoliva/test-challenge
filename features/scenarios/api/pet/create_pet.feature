@API @PET @AUREUM
Feature: [API] Create Pet

  @SR-007 @SMOKE
  Scenario: Create a new Pet
    Given A request to create a new pet through Petstore's API
    When the request is made to create a pet
    Then the user is told the request to create was successful
    And the pet is created
    And The pet is removed to keep the application clean


