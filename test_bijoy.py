import re

import pytest

def test_Requisition_Doc(login_page):

    Profile= login_page.get_by_role('img', name='SABBIR')
    Profile.click()
    print("Profile Clicked Successfully")

    AdminButton=login_page.get_by_role("link", name="Admin panel icon Admin")
    AdminButton.click()
    print("Admin Panel Clicked Successfully")

    ContestsOption=login_page.get_by_text('Contests', exact=True)
    ContestsOption.click()
    print("Contests Clicked Successfully")

    Contest=login_page.get_by_role("link", name="Contest Create")
    Contest.click()
    print("Contest Create Clicked Successfully")

    # Filling the Contest Create Form
    Title=login_page.get_by_role("textbox", name="* Title")
    Title.click()
    Title.fill("Art Creativity Contest 2025")

    Category=login_page.get_by_role("combobox", name="* Category")
    Category.click()
    login_page.get_by_text("ART").wait_for()
    login_page.get_by_text("ART").click()

    
#     searchBar= login_page.locator('#navbar-search')
#     searchBar.fill("Requisition")
#     searchBar.click()
#     assert searchBar.input_value() == "Requisition"


#     SearchList=login_page.get_by_role("listitem").filter(has_text=re.compile(r"^Requisition List$"))
#     SearchList.click()

    
#     AddNewRequisitionButton=login_page.get_by_role("button", name="Add Requisition")
#     AddNewRequisitionButton.click()


#     # company=login_page.locator("//div[@data-fieldname='company']//div//div//div//div//div//input[@role='combobox']")
#     company=login_page.get_by_role('combobox').nth(1)
#     company.fill("")
#     company.click()
#     company.fill("Humaira Composite Textile Mills Ltd.")

#     costCenter=login_page.locator("//div[@data-fieldname='cost_center']//div//div//div//div//div//input[@role='combobox']")
#     costCenter.click()
#     costCenter.fill("Main - HCTML", timeout=5000)


#     # Dept =page.locator("//div[@data-fieldname='department']//div//div//div//div//div//input[@role='combobox']")

#     Metarial_Type=login_page.locator("//div[@data-fieldname='material_type']//div//div//div//div//div//input[@role='combobox']")
#     Metarial_Type.click()
#     Metarial_Type.fill("General", timeout=5000)

#     company.click()  # To close the dropdown
   


#     Req_type=login_page.locator("//div[@data-fieldname='requisition_type']//div//div//div//div//div//input[@role='combobox']")
#     Req_type.click()
#     Req_type.fill("Material Issue", timeout=5000)
    
#     company.click()  # To close the dropdown


#     TargetStore=login_page.locator("//body/div/div[@id='body']/div[@id='page-Material Request']/div/div/div/div/div/div/div/div/div/div/div/div[@id='material-request-__details']/div[@data-fieldname='warehouse_section']/div/span[1]//*[name()='svg']")
#     # TargetStore.scroll_into_view_if_needed()
#     TargetStore.click()

#     Store=login_page.locator("//div[@data-fieldname='set_warehouse']//div//div//div//div//div//input[@role='combobox']")
#     Store.click()
#     Store.fill("Work In Progress - HCTML", timeout=5000)

#     Collaps=login_page.locator('//div[normalize-space()="Warehouse and Location Details"]')
#     Collaps.click()


#     # row addition
#     AddProduct=login_page.get_by_role('button', name='Add Row')
#     AddProduct.click()
   

#     # open row and add item

#     AddItem=login_page.locator("//div[@data-toggle='tooltip']//a//*[name()='svg']")
#     AddItem.click()


#     item_code =  login_page.locator("//div[@data-fieldname='item_code']//div//div//div//div//div//input[@role='combobox']")
#     item_code.click()
#     item_code.fill("1401003", timeout=1000)
#     login_page.wait_for_timeout(500)


#     Qty=login_page.locator("//div[@data-fieldname='qty']//div//div//div//input[@type='text']")
#     Qty.click()
#     Qty.fill('10', timeout=1000)

#     # typed value select

#     Close=login_page.locator("//div[@id='material-request-__details']//span[2]//button[1]//*[name()='svg']")
#     Close.click()

#     # save button================================
#     SaveButton=login_page.get_by_role("button", name="Save")
#     SaveButton.click()
    
#     SubmitButton=login_page.get_by_role("button", name="Submit")
#     SubmitButton.click()
#     YesButton=login_page.locator('//button[normalize-space()="Yes"]')
#     YesButton.click()
     
#      # wait until save completed
#     login_page.wait_for_load_state("networkidle")
#     # get document id from URL
#     url = login_page.url
#     doc_id = url.split("/")[-1]


#     # store globally (pytest)
#     import pytest
#     pytest.requisition_id = doc_id
  
#     login_page.screenshot(path="after_login.png", full_page=True)
#     print("Saved Requisition ID:", doc_id) 


# second test to access the draft requisition created in the first test===================
# def test_Requisition_To_Stock_transaction(login_page):
#     searchBar= login_page.locator('#navbar-search')
#     searchBar.fill("Requisition")
#     searchBar.click()
    

#     SearchList=login_page.get_by_role("listitem").filter(has_text=re.compile(r"^Requisition List$"))
#     SearchList.click()

#     SearchId=login_page.get_by_role("textbox", name="ID")
#     searchBar.fill("")
#     SearchId.fill(pytest.requisition_id)


#     SelectID=login_page.get_by_role('link', name=pytest.requisition_id)
#     SelectID.click()
    

#     Create=login_page.get_by_role('button', name='Create')
#     Create.click()

#     ProcessingButton=login_page.get_by_role('link', name='Processing')
#     ProcessingButton.click()

#     print(" Requisition Draft Processed Successfully")

    # login_page.wait_for_timeout(2000)


# # third test to create multiple DD from the requisition===================
# def test_Requisition_To_multiple_DD_create(login_page):
#     searchBar= login_page.locator('#navbar-search')
#     searchBar.fill("Requisition")
#     searchBar.click()
    

#     SearchList=login_page.get_by_role("listitem").filter(has_text=re.compile(r"^Requisition List$"))
#     SearchList.click()

#     SearchId=login_page.get_by_role("textbox", name="ID")
#     searchBar.fill("")
#     # SearchId.fill(pytest.requisition_id)
#     SearchId.fill("MR-HCTML-2025-00040")


#     SelectID=login_page.get_by_role('link', name="MR-HCTML-2025-00040")
#     # SelectID=login_page.get_by_role('link', name=pytest.requisition_id)
#     SelectID.click()   



#     AddItem=login_page.locator("//div[@data-toggle='tooltip']//a//*[name()='svg']")
#     AddItem.click()

#     DD_Button=login_page.get_by_role('button', name='Delivery Decision')
#     DD_Button.click()
#     print(" Delivery Decision Created Successfully")
    
#     # open DD popup and select multiple DDs
#     AddProduct=login_page.get_by_role('button', name='Add Row')
#     AddProduct.click()


  

#     DD_table=login_page.locator("//div[@role='dialog']//div//div//div//div//div//div//div//div//div//form//div[@data-fieldtype='Table']//div//div//div//div//div//div//div//div[@data-fieldname='delivery_decision']")

    
#     DD_table.dblclick(force=True)
#     DD_table.wait_for_timeout(2000)
#     # DD_table.wait_for(state="visible")
#     DD_table.select_option("From Own Company")
     
    

#     # DD_table.fill("From Own Company")

#     login_page.wait_for_timeout(5000)
    
#     FromCompany=login_page.get_by_role('combobox', name='From Company').nth(1)
#     FromCompany.click()
#     FromCompany.fill("Humaira Composite Textile Mills Ltd.")

#     ToStore=login_page.get_by_role('combobox', name='From Store').nth(1)
#     ToStore.click()
#     ToStore.fill("Work In Progress - HCTML")

#     Qty=login_page.get_by_role('textbox', name='Quantity').nth(1)
#     Qty.click()
#     Qty.fill("5")

#     DD_save=login_page.get_by_role('button', name='Save').nth(1)
#     DD_save.click()
#     print(" Multiple Delivery Decision Saved Successfully")
