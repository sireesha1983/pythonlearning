Feature: sample1

#@signin
#Scenario: Verify signin button
# Given I login with url
# When i click on sign in button
# And i enter e-mail
# And i click on continue button
# And i click on password
# Then I click on sign_in button
#
@search
#Scenario:Verify search button
#  When i click on sign in button
#  And i enter e-mail
#  And i click on continue button
#  And i click on password
#  And I click on sign_in button
#  Then i enter "books" in search button

#@addcart
#Scenario:Verify addcart
#  When i enter "books" in search button
#  And i click on search button
#  And i click on awardwinner
#  And i click on firstbook
#  And i click on add to cart button
#  And i click on cart
#  Then i click on delete button

#@selectvideo
#Scenario:Verify selectvideo
#  When i click on primevideo
#  And i click on categories
#  And i click on tv
#  And i click on firstvideo
#  Then i click on seasons


#
#@todaydeals
#Scenario: Verify cart
#  When i click on todays deals
#  And i click on first video
#  And i click on add to cart
#  Then i click on proceedcheckout

@buyagain
Scenario: Verify buyagain
  When i click on buyagain
  And i click on third item
  And i click on add to cart
  And i click on cart
  And i click on save for later
  Then i click on move to cart