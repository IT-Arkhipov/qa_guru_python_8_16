from selene import browser, be, have


class SignIn:

    @staticmethod
    def desktop_sign_in():
        browser.element("a[href='/login']").click()
        browser.element('.auth-form-header>h1').should(be.visible).should(have.text('Sign in to GitHub'))

    @staticmethod
    def mobile_sign_in():
        browser.element('div.flex-column').element('.Button-content').click()
        browser.element("a[href='/login']").should(be.visible).click()
        browser.element('.auth-form-header>h1').should(be.visible).should(have.text('Sign in to GitHub'))


sign_in = SignIn()
