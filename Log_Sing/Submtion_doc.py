def test_signup_All_fields_check(Login_page):
   Create_acc=Login_page.get_by_text('Submissions', exact=True)
   Create_acc.click()

   SelectContent=Login_page.get_by_role('link', name='পাকিস্তানি হানাদার বাহিনীর নির্মমতা')
   SelectContent.click()

   Preview_btn=Login_page.get_by_text('Preview', exact=True)
   Preview_btn.click()


   Zoom_in=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(5)
   Zoom_in.click()
   Login_page.wait_for_timeout(2000)  # 1 second
   Zoom_out=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(4)
   Zoom_out.click()
   Login_page.wait_for_timeout(2000)  # 1 second   

   Right=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(3)
   Right.click()
   Login_page.wait_for_timeout(3000)  # 1 second
   Left=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(2)
   Left.click()
   Login_page.wait_for_timeout(2000)  # 1 second

   LeftSide=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(1)
   LeftSide.click()
   Login_page.wait_for_timeout(2000)  # 1 second
   rightSide=Login_page.locator('div.ant-image-preview-operations-operation > span.anticon > svg').nth(0)
   rightSide.click()
   Login_page.wait_for_timeout(2000)  # 1 second

   CloseBtn=Login_page.locator('.ant-image-preview-close')
   CloseBtn.click()

   Login_page.wait_for_timeout(3000)  # 1 second
   Login_page.screenshot(path="Submission_page.png")