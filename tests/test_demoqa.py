import allure

from utils.form.registration_form import RegistrationForm
from utils import users


def test_demoqa_complete_form():
    registration_form = RegistrationForm()
    # GIVEN
    with allure.step('Open registration form page'):
        registration_form.open()

    # WHEN
    with allure.step('Fill registration form'):
        registration_form.fill_form(users.user)

    # THEN
    with allure.step('Assert filled form'):
        registration_form.assert_registered_info(users.user)
