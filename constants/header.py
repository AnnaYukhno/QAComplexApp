class HeaderConsts:
    """Stores constants related to header"""

    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_BUTTON_TEXT = 'Sign In'
    SIGN_OUT_BUTTON_XPATH = ".//button[@class='btn btn-sm btn-secondary']"
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_IN_USERNAME_FIELD_XPATH = ".// input[@placeholder = 'Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"

    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    MY_PROFILE_BUTTON_XPATH = ".//a[@href='/profile/{username}']"

    CHAT_BUTTON_XPATH = './/span[@data-original-title="Chat"]'
