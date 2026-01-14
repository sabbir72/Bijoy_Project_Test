import os
import re

from conftest import signup_page
import pytest

# def test_signup_Doc(signup_page):
#    Create_acc= signup_page.get_by_role('link', name='Create an account')
#    Create_acc.click()

#    Firs_Name= signup_page.get_by_role('textbox', name='First Name')
#    Firs_Name.fill("Sabbir")
#    Last_Nmae=signup_page.get_by_role('textbox', name='Last Name')
#    Last_Nmae.fill("Hossain")

#    Email_phone = signup_page.get_by_role('textbox', name='Email/Phone')
#    Email_phone.fill(os.getenv("NUMBER"))
#    Email_phone.press("Tab")   # validation trigger

#    Validation_text = signup_page.get_by_text("Email/Phone is invalid",exact=True)

#    if Validation_text.is_visible():
#         print("❌ Validation Failed: Email/Phone is invalid")
#    else:
#         print("✅ Successfully passed")

#    signup_page.screenshot(path="Signup_page.png", full_page=True)

   #  test cas 02 all fields check===================================================
   #  ===============================================================================


def test_signup_All_fields_check(signup_page):
   Create_acc= signup_page.get_by_role('link', name='Create an account')
   Create_acc.click()

   Firs_Name= signup_page.get_by_role('textbox', name='First Name')
   Firs_Name.fill("Sabbir")
   Last_Nmae=signup_page.get_by_role('textbox', name='Last Name')
   Last_Nmae.fill("Hossain")

   Email_Number=signup_page.get_by_role('textbox', name='Email/Phone')
   Email_Number.fill(os.getenv("NUMBER"))

   Password=signup_page.get_by_label("Password", exact=True)
   Password.fill(os.getenv("PASSWORD"))

   Con_pass=signup_page.get_by_role('textbox', name='Confirm Password')
   Con_pass.fill(os.getenv("PASSWORD"))

   Submit_Btn=signup_page.locator('button[type="submit"]')
   Submit_Btn.click()
   # signup_page.wait_for_load_state("networkidle")
    
   signup_page.wait_for_timeout(5000)

   PopUp_sms=signup_page.locator('.ant-notification-notice-message')
   PopUp_sms.is_visible()
   
   print("✅ Signup Successful: ",PopUp_sms.inner_text())
   
   signup_page.screenshot(path="Signup_page2.png", full_page=True)

    

  