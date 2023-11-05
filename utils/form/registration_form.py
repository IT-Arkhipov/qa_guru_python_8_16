from os.path import dirname, abspath
import platform

from selene import browser, have, command
from selenium.webdriver import Keys
from utils.users import User


class RegistrationForm:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.phone_number = browser.element('#userNumber')
        self.birth_day = browser.element('#dateOfBirthInput')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.element('#hobbiesWrapper')

    def open(self):
        browser.open("/automation-practice-form")
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_form(self, user: User):
        self._fill_user_name(user.first_name, user.last_name)
        self._fill_email(user.email)
        self._select_gender(user.gender)
        self._fill_phone(user.phone)
        self._fill_birthday(user.date)
        self._select_subject(user.subject)
        self._select_hobby(user.hobby)
        self._upload_picture(user.file_name)
        self._fill_address(user.address)
        self._select_state(user.state)
        self._select_city(user.city)
        self._submit_form()

    def assert_registered_info(self, user: User):
        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.exact_texts(
            ' '.join((user.first_name, user.last_name)),
            user.email,
            user.gender,
            user.phone,
            user.checked_date,
            user.subject,
            user.hobby,
            user.file_name,
            user.address,
            ' '.join((user.state, user.city))
        ))

    def _fill_user_name(self, first_name: str, last_name: str):
        self.first_name.type(first_name)
        self.last_name.type(last_name)

    def _fill_email(self, email: str):
        self.user_email.type(email)

    def _select_gender(self, gender: str):
        self.gender.all('label').element_by(have.text(gender)).click()

    def _fill_phone(self, number: str):
        self.phone_number.type(number)

    def _fill_birthday(self, date: str):
        os_base = platform.system()
        if os_base == 'Darwin':
            self.birth_day.send_keys(Keys.COMMAND + 'a').send_keys(date).press_enter()
        else:
            self.birth_day.send_keys(Keys.CONTROL + 'a').send_keys(date).press_enter()

    def _select_subject(self, subject: str):
        self.subject.type(subject).press_enter()

    def _select_hobby(self, hobby: str):
        self.hobby.perform(command.js.scroll_into_view)
        self.hobby.all('label').element_by(have.text(hobby)).click()

    def _upload_picture(self, file_name: str):
        browser.element('#uploadPicture').send_keys(dirname(dirname(dirname(abspath(__file__)))) +
                                                    '/tests/img/' + file_name)

    def _fill_address(self, address: str):
        browser.element('#currentAddress').type(address)

    def _select_state(self, state: str):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.element('#react-select-3-input').type(state).press_enter()

    def _select_city(self, city: str):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def _submit_form(self):
        browser.element('footer').execute_script('element.remove()')
        browser.element('#submit').perform(command.js.click)
