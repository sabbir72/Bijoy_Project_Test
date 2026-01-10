from dotenv import load_dotenv
import os
import pytest
from playwright.sync_api import Page

load_dotenv()

@pytest.fixture
def login_page(page:Page):

    page.goto(os.getenv("BASE_URL"))
    ClickSignIn= page.get_by_text('Sign In', exact=True)
    ClickSignIn.click()

    page.get_by_role('textbox', name='Email').fill(os.getenv("EMAIL"))
    page.get_by_role('textbox', name='Password').fill(os.getenv("PASSWORD"))
    page.get_by_role('button', name='Sign In').click()
    
    return page


    
@pytest.fixture
def signup_page(page:Page):

    page.goto(os.getenv("BASE_URL"))
    ClickSignIn= page.get_by_text('Sign In', exact=True)
    ClickSignIn.click()

    
    
    return page
