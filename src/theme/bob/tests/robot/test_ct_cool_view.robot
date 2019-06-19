# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s theme.bob -t test_cool_view.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src theme.bob.testing.THEME_BOB_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/theme/bob/tests/robot/test_cool_view.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Cool View
  Given a logged-in site administrator
    and an add Cool View form
   When I type 'My Cool View' into the title field
    and I submit the form
   Then a Cool View with the title 'My Cool View' has been created

Scenario: As a site administrator I can view a Cool View
  Given a logged-in site administrator
    and a Cool View 'My Cool View'
   When I go to the Cool View view
   Then I can see the Cool View title 'My Cool View'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Cool View form
  Go To  ${PLONE_URL}/++add++Cool View

a Cool View 'My Cool View'
  Create content  type=Cool View  id=my-cool_view  title=My Cool View

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Cool View view
  Go To  ${PLONE_URL}/my-cool_view
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Cool View with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Cool View title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
