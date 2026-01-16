import re

import pytest

def test_Login_to_Create_Doc(signup_page_Demo):

    Profile= signup_page_Demo.get_by_role('img', name='SABBIR')
    Profile.click()

    AdminButton=signup_page_Demo.get_by_role("link", name="Admin panel icon Admin")
    AdminButton.click()
    
    signup_page_Demo.wait_for_timeout(1000) 


    ContestsOption=signup_page_Demo.get_by_text('Contests', exact=True)
    ContestsOption.click()
    print("Contests Clicked Successfully")

    Contest=signup_page_Demo.get_by_role("link", name="Contest Create")
    Contest.click()
    print("Contest Create Clicked Successfully")

    # Filling the Contest Create Form
    Title=signup_page_Demo.get_by_role("textbox", name="* Title")
    Title.click()
    Title.fill("Art Creativity Contest 2025")

    Category=signup_page_Demo.get_by_role("combobox", name="* Category")
    Category.click()
    # signup_page_Demo.get_by_text("ART").wait_for()
    signup_page_Demo.get_by_text("ART").click()
    
    Enrollment_Type=signup_page_Demo.get_by_role('combobox', name='Enrollment Type')
    Enrollment_Type.scroll_into_view_if_needed()
    Enrollment_Type.click()
    signup_page_Demo.get_by_text("FREE").click()
    


    signup_page_Demo.wait_for_timeout(5000)  # 1 second

    