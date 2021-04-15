FEATURES1:  Trip

@login
Scenario: Verify login button
 Given I login with url
 When i click on log in button
 And i enter e-mail
 And i click on continue button
 And i click on password
 Then I click on sign_in button
