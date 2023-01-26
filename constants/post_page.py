class PostPageConsts:
    """Stores constants related to post page"""

    POST_CREATED_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    POST_CREATED_MESSAGE_TEXT = "New post successfully created."

    POST_SETTINGS_MESSAGE_XPATH = ".//div[@class='body-content']"
    UNIQUE_POST_TEXT = "Is this post unique? : yes"
    NON_UNIQUE_POST_TEXT = "Is this post unique? : no"
    PRIVACY_MESSAGE_XPATH = ".//div[@class='body-content']/p/i/u"
