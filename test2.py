# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     context = browser.new_context(storage_state="auth.json")
#     page = context.new_page()

#     page.goto("https://preview.beejoyi.com/")


#     print("👉 আপনি সফলভাবে লগইন করেছেন এবং auth.json ফাইল থেকে স্টোরেজ স্টেট লোড করেছেন।")
#     page.wait_for_timeout(5000)  # কিছু সময় অপেক্ষা করুন যাতে আপনি পেজটি দেখতে পারেন
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")

    page = context.new_page()
    page.goto("https://preview.beejoyi.com/competitions")

    print("✅ auth0.json থেকে session load হয়েছে")
    page.wait_for_timeout(5000)

    browser.close()
