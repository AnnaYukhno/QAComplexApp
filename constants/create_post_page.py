class CreatePostPageConsts:
    """Stores constants related to create post page"""

    TITLE_INPUT_XPATH = ".//input[@id='post-title']"
    BODY_TEXTAREA_XPATH = ".//textarea[@id='post-body']"
    UNIQUE_POST_CHECKBOX_XPATH = ".//input[@name='uniquePost']"
    PUBLIC_POST_OPTION_XPATH = ".//option[@value='All Users']"
    PRIVATE_POST_OPTION_XPATH = ".//option[@value='One Person']"
    GROUP_POST_OPTION_XPATH = ".//option[@value='Group Message']"
    SAVE_NEW_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
