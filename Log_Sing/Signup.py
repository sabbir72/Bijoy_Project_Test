import re

from conftest import signup_page
import pytest

def test_signup_Doc(signup_page):
   Create_acc= signup_page.get_by_role('link', name='Create an account')
   Create_acc.click()

   Firs_Name= signup_page.get_by_role('textbox', name='First Name')
   Firs_Name.fill("Sabbir")
   Last_Nmae=signup_page.get_by_role('textbox', name='Last Name')
   Last_Nmae.fill("Hossain")

   Email_phone = signup_page.get_by_role('textbox', name='Email/Phone')
   Email_phone.fill("01531-969932")
   Email_phone.press("Tab")   # validation trigger

   Validation_text = signup_page.get_by_text(
        "Email/Phone is invalid",
        exact=True
    )

   if Validation_text.is_visible():
        print("❌ Validation Failed: Email/Phone is invalid")
   else:
        print("✅ Successfully passed")

   signup_page.screenshot(path="Signup_page.png", full_page=True)

def test_signup_All_fields_check(signup_page):
   Create_acc= signup_page.get_by_role('link', name='Create an account')
   Create_acc.click()

   Firs_Name= signup_page.get_by_role('textbox', name='First Name')
   Firs_Name.fill("Sabbir")
   Last_Nmae=signup_page.get_by_role('textbox', name='Last Name')
   Last_Nmae.fill("Hossain")

   Email_Number=signup_page.get_by_role('textbox', name='Email/Phone')
   Email_Number.fill("01531969932")

   Password=signup_page.get_by_label("Password", exact=True)
   Password.fill("Test@809672")

   Con_pass=signup_page.get_by_role('textbox', name='Confirm Password')
   Con_pass.fill("Test@809672")


   Submit_Btn=signup_page.locator('button[type="submit"]')
   Submit_Btn.click()

   
   PopUp=signup_page.get_by_text("Account created successfully. Verify your email/phone to continue.", exact=True)
   if PopUp.is_visible():
      print("✅ Signup Successful: Account created successfully popup is visible")
   else:
      print("❌  popup is not visible")   

  