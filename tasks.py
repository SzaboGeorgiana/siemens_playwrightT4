import os
from pathlib import Path
from robocorp import browser
from robocorp.tasks import task
from RPA.Excel.Files import Files as Excel

FILE_NAME = "challenge.xlsx"
EXCEL_URL = f"https://rpachallenge.com/assets/downloadFiles/{FILE_NAME}"
OUTPUT_DIR = Path(os.getenv("ROBOT_ARTIFACTS", "output"))


@task
def my_task_4():

    # Navigate to Site
    page=browser.goto("https://sieportal.siemens.com/en-de/home")
    
    # agree cookies
    page.click('button:has-text("Accept All Cookies")')

    # Products & Services
    page.wait_for_selector('a:has-text("Products & Services")')
    page.hover('a:has-text("Products & Services")')

    # List of configurators 
    list_config_selector='div.primary-label.truncate[title="List of configurators"]'
    page.wait_for_selector(list_config_selector)
    page.click(list_config_selector)

    # Drive technology
    page.locator("div.topLevelNode", has_text="Drive technology").click()
    # drive_tech_selector='div:has-text("Drive technology")'
    # page.wait_for_selector(drive_tech_selector)
    # page.click(drive_tech_selector)

    # Siemens Product Configurator
    product_config_selector='a:has-text("Siemens Product Configurator")'
    page.wait_for_selector(product_config_selector)
    page.click(product_config_selector)

    # Search
    searchbar=page.locator('input.spc-input')
    searchbar.fill("1LE1") 

    # Innomotics Low Voltage Motors
    page.wait_for_selector('p.text-main-on-light.font-bold')
    element = page.locator('text=Innomotics Low Voltage Motors')
    element.click()

    # find Next button
    page.wait_for_selector('span.spc-skeleton--normal:text("Next")')
    next_button = page.locator('span.spc-skeleton--normal:text("Next")')

    # Check if the element with the text "Configuration complete" is visible
    while not page.locator('#cdk-overlay-3 >> text="Configuration complete"').is_visible():

        # Click the button next
        next_button.click()

        # Wait for the box under the Next button
        div_selector = "#cdk-overlay-1"
        page.wait_for_selector(div_selector)

        # Check if it is a menu
        if page.is_visible('spc-menu-item:nth-child(1)'):
            # Click the first menu item
            first_menu_item = page.locator('spc-menu-item:nth-child(1)')
            first_menu_item.click()
            
        else:
            #click on the div
            page.click(div_selector)

            # Fill the input field with '0.13'
            input_selector = f'spc-label:has-text("Power demand") ~ input'
            page.wait_for_selector(input_selector)
            page.fill(input_selector, '0.13')
            
        page.wait_for_timeout(3000)  # Wait for 3 seconds

    # Results & Documents
    results_and_docs_selector='button.btn.summary-action-button.primary.text-with-icon-btn.dark'
    page.wait_for_selector(results_and_docs_selector)
    page.click(results_and_docs_selector)

    # Data sheet (PDF)
    pdf_selector='span:has-text("Data sheet (PDF)")'
    page.wait_for_selector(pdf_selector)
    page.click(pdf_selector)
    page.wait_for_timeout(10000)  # Wait for 10 seconds

    # Add to product list 
    add_to_list_selector='button:has-text("Add to product list")'
    page.wait_for_selector(add_to_list_selector)
    page.click(add_to_list_selector)

    # Back
    page.click(results_and_docs_selector)

    # Products list
    products_list_selector='spc-icon.icon-sieportal-orderlist'
    page.wait_for_selector(products_list_selector)
    page.click(products_list_selector)

    page.wait_for_timeout(10000)  # Wait for 10 seconds


