# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)  # visible browser
#     context = browser.new_context()
#     page = context.new_page()

#     page.goto("https://beejoyi.vercel.app/sign-in")

#     # 🔴 এখানে তুমি manually:
#     # - email
#     # - password
#     # - Cloudflare CAPTCHA solve করবে

#     input("Login complete হলে Enter চাপো...")

#     # ✅ session + cookies save
#     context.storage_state(path="auth.json")

#     print("✅ Session saved successfully")

#     browser.close()



from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://beejoyi.vercel.app/sign-in")

    print("👉 Manually login + CAPTCHA solve করো")
    page.wait_for_url("**/dashboard**")

    context.storage_state(path="auth.json")
    print("✅ Session saved")

    browser.close()
