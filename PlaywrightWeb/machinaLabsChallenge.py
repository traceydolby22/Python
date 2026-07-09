from playwright.sync_api import Page, sync_playwright
import random
import string

def generate_email():
    """Generates a random email address for testing purposes."""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_string}@test.com"

def test_create_account_and_checkout():
    # starting a playwright instance
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without opening a browser window
        page = browser.new_page() # opens new page to navigate to url and interact with the website
        # Block Google Ads network requests
        page.route("**/*googleads*", lambda route: route.abort())
        # 2. Launch browser and navigate to the website
        page.goto("https://automationexercise.com/")

        # 3. Verify page loads 
        assert page.title() == "Automation Exercise"
        print("✅ Step 3: Home Page is visible")
        
        # 4. Click on the "Sign Up" button
        page.get_by_role("link", name="Signup").click()
        assert page.is_visible("text=New User Signup!")
        print("✅ Step 4: Sign Up page is visible")

        # 5. Fill sign up deets
        email = generate_email()
        page.fill("input[data-qa='signup-name']", "Test User") #data-qa specifies the input element must have qa attribute exacly equal to signup-name
        page.fill("input[data-qa='signup-email']", email) #data-qa specifies the input element must have qa attribute exacly equal to signup-email
        page.click("button[data-qa='signup-button']") 

        # 5b. Fill out account deets
        page.click("input#id_gender2")  # Select Mrs.
        page.fill("input[data-qa='password']", "T3st1ng!")
        page.select_option("select[data-qa='days']", "22")
        page.select_option("select[data-qa='months']", "8")
        page.select_option("select[data-qa='years']", "2021")
        page.fill("input[data-qa='first_name']", "Testing")
        page.fill("input[data-qa='last_name']", "User")
        page.fill("input[data-qa='address']", "123 Testing Street")
        page.select_option("select[data-qa='country']", "United States")
        page.fill("input[data-qa='state']", "California")
        page.fill("input[data-qa='city']", "Los Angeles")
        page.fill("input[data-qa='zipcode']", "90291")
        page.fill("input[data-qa='mobile_number']", "8012345679")
        page.click("button[data-qa='create-account']")
        print("✅ Step 5: Signup form filled out")
        
        # 6. Verify account created 
        page.wait_for_url("https://automationexercise.com/account_created")
        assert page.is_visible("text=Account Created!")
        print("✅ Step 6: Account creation successful")
        page.click("a[data-qa='continue-button']")

        # 7. verify logged in
        page.goto("https://automationexercise.com/")
        page.wait_for_url("https://automationexercise.com/")
        assert page.is_visible("text=Logged in as ")
        print("✅ Step 7: User is logged in")

        # 8. add product to cart
        page.goto("https://automationexercise.com/products")
        page.hover(".product-image-wrapper:first-child")  # Hover over the first product to reveal the orange overlay
        page.click(".product-image-wrapper:first-child .add-to-cart")  # Click the "Add to cart" button on the first product from the orange overlay
        page.click("button:has-text('Continue Shopping')")  # Click the "Continue Shopping" button on the pop-up
        print("✅ Step 8: Product added to cart")

        # 9. Click on the "Cart" button
        page.click("text=Cart")
        print("✅ Step 9: Cart button clicked")
        

        # 10. verify cart page
        assert page.is_visible("text=Shopping Cart")
        print("✅ Step 10: Cart page is visible")

        # 11. Click on the "Proceed To Checkout" button
        page.click("text=Proceed To Checkout")
        assert page.is_visible("text=Address Details")
        print("✅ Step 11: Checkout page is visible")

        # 12. Verify shipping details 
        assert page.is_visible("text= Your delivery address")
        assert page.is_visible("text= Review Your Order")
        print("✅ Step 12: Shipping details are visible, I can review order")

        # 13. Enter comment and Click Place order
        page.fill("textarea[name='message']", "Please deliver between 9 AM and 5 PM.")
        page.click("a:has-text('Place Order')")
        print("✅ Step 13: Comment added and Place Order button clicked")
         
         # 14. & 15. Enter payment deets, click pay and confirm order
        assert page.is_visible("text=Payment")
        page.fill("input[data-qa='name-on-card']", "Test User")
        page.fill("input[data-qa='card-number']", "4111111111111111")
        page.fill("input[data-qa='cvc']", "123")
        page.fill("input[data-qa='expiry-month']", "12")
        page.fill("input[data-qa='expiry-year']", "2029")
        page.click("button[data-qa='pay-button']")
        print("✅ Step 14: Place Order page is visible")

        # 16. verify order confirmation
        assert page.is_visible("text=Order Placed!")
        assert page.is_visible("text=Download Invoice")
        assert page.is_visible("text=Continue")
        print("✅ Step 16: Order confirmation is visible")

        # 17. Click on the "Delete Account" button
        page.click("text=Delete Account")
        print("✅ Step 17: Account delete button clicked")

        # 18. Verify account deletion
        assert page.is_visible("text=Account Deleted!")
        page.click("a[data-qa='continue-button']")
        print("✅ Step 18: Account deletion successful")

        browser.close()
        print("\n✅ All steps completed successfully!")

test_create_account_and_checkout()