

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     page.goto("https://preview.beejoyi.com/sign-in")

#     print("👉 নিজে হাতে login করুন (Cloudflare verify হলে অপেক্ষা করুন)")
#     page.wait_for_timeout(20000)  # আপনি হাতে login করবেন

#     context.storage_state(path="auth.json")
#     browser.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context()
    page = context.new_page()

    page.goto("https://preview.beejoyi.com/sign-in")

    print("👉 নিজে হাতে login করুন")
    print("👉 Cloudflare pass হলে site fully load হতে দিন")
    print("👉 সব শেষ হলে terminal এ ENTER চাপুন")

    input()   # 👈 সবচেয়ে গুরুত্বপূর্ণ line

    context.storage_state(path="auth.json")
    print("✅ auth.json saved")

    browser.close()
