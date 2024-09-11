import os
from pathlib import Path

import requests
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

    page.wait_for_selector('a:has-text("Products & Services")')
    page.hover('a:has-text("Products & Services")')

    # list_config_selector='div:has-text("List of configurators ")'
    list_config_selector='div.primary-label.truncate[title="List of configurators"]'
    page.wait_for_selector(list_config_selector)
    page.click(list_config_selector)

    drive_tech_selector='div:has-text("Drive technology")'
    page.wait_for_selector(drive_tech_selector)
    page.click(drive_tech_selector)

    # drive_tech_selector='div.configuratorLabels'
    product_config_selector='a:has-text("Siemens Product Configurator")'
    page.wait_for_selector(product_config_selector)
    page.click(product_config_selector)

    searchbar=page.locator('input.spc-input')
    searchbar.fill("1LE1") 

    # Wait for the element to be visible
    page.wait_for_selector('p.text-main-on-light.font-bold')
    # Locate the element by its text content
    element = page.locator('text=Innomotics Low Voltage Motors')
    # Click the element
    element.click()

    page.wait_for_selector('span.spc-skeleton--normal:text("Next")')
    # Use a more specific selector like class and text together
    next_button = page.locator('span.spc-skeleton--normal:text("Next")')

    # Check if the element with the text "Configuration complete" is visible
    while not page.locator('#cdk-overlay-3 >> text="Configuration complete"').is_visible():

        # Click the button next
        next_button.click()
        div_selector = "#cdk-overlay-1"
        page.wait_for_selector(div_selector)

        if page.is_visible('spc-menu-item:nth-child(1)'):
            # Click the first menu item
            first_menu_item = page.locator('spc-menu-item:nth-child(1)')
            first_menu_item.click()
            
        else:
            # Fill the input field with '1.3'
            page.click(div_selector)
            input_selector = f'spc-label:has-text("Power demand") ~ input'

            # Wait for the input field to be visible
            page.wait_for_selector(input_selector)

            # Fill the input field with the value '0.13'
            page.fill(input_selector, '0.13')
            
        page.wait_for_timeout(3000)  # Wait for 3 seconds

    # <button _ngcontent-ng-c1927417756="" spc-button="" spcistextwithiconbutton="" appcompleteconfigurationtip="" spcdark="" spcbuttontype="primary" class="btn summary-action-button primary text-with-icon-btn dark"><spc-icon _ngcontent-ng-c1927417756="" icon="sieportal-technical-data" size="20" class="icon-sieportal-technical-data" style="font-size: 20px; line-height: 20px;"></spc-icon><app-ui-label _ngcontent-ng-c1927417756="" key="com.siemens.spice.ccm.configurator.overview.card.your.configuration" class="font-siemens-black"><span class="spc-skeleton--normal" style="max-width: 250px;">Results &amp; Documents</span></app-ui-label></button>
    results_and_docs_selector='button.btn.summary-action-button.primary.text-with-icon-btn.dark'
    page.wait_for_selector(results_and_docs_selector)
    page.click(results_and_docs_selector)

    # <span class="spc-skeleton--normal" style="max-width: 100px;">Data sheet (PDF)</span>
    pdf_selector='span:has-text("Data sheet (PDF)")'
    page.wait_for_selector(pdf_selector)
    page.click(pdf_selector)
    page.wait_for_timeout(5000)  # Wait for 10 seconds


    # <button _ngcontent-ng-c1927417756="" spc-button="" spcistextwithiconbutton="" spcdark="" spcbuttontype="secondary" class="btn summary-action-button secondary text-with-icon-btn dark ng-star-inserted"><!----><spc-icon _ngcontent-ng-c1927417756="" icon="sieportal-orderlist-add" size="16" class="icon-sieportal-orderlist-add ng-star-inserted" style="font-size: 16px; line-height: 16px;"></spc-icon><!----><app-ui-label _ngcontent-ng-c1927417756="" key="com.siemens.spice.ccm.add.to.cart.action" class="hidden lg:block font-siemens-black"><span class="spc-skeleton--normal" style="max-width: 250px;">Add to product list</span></app-ui-label></button>
    add_to_list_selector='button:has-text("Add to product list")'
    page.wait_for_selector(add_to_list_selector)
    page.click(add_to_list_selector)

    # page.wait_for_timeout(100000)  # Wait for 5 seconds
    page.click(results_and_docs_selector)

    # <spc-icon _ngcontent-ng-c3632254775="" icon="sieportal-orderlist" class="sidenav-link-icon icon-sieportal-orderlist" style="font-size: 24px; line-height: 24px;"><!----><spc-badge _ngcontent-ng-c3632254775="" badgetype="counter" class="badge-container self-start ng-star-inserted"><span class="badge-content badge-counter"> 1 <!----><!----></span></spc-badge><!----><!----></spc-icon>
    products_list_selector='spc-icon.icon-sieportal-orderlist'
    page.wait_for_selector(products_list_selector)
    page.click(products_list_selector)

    page.wait_for_timeout(10000)  # Wait for 10 seconds


