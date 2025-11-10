# app/agents/bus_agent.py

import os
from langchain_groq import ChatGroq
from playwright.sync_api import sync_playwright

# Initialize the LLM to summarize the scraped data
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def get_bus_information(service_number: str):
    """
    Scrapes the APSRTC website for a specific bus service number.
    Note: APSRTC requires a specific "Service No.", not a general "Route No."
    """
    scraped_data = ""
    # This is the official tracking page for APSRTC services
    target_url = "https://www.apsrtconline.in/oprs-web/services/TrackService.do"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            print(f"Navigating to APSRTC website for service {service_number}...")
            page.goto(target_url, timeout=60000)
            
            # --- Interact with the APSRTC page ---
            # 1. Fill in the service number
            page.get_by_placeholder("Enter Service Number").fill(service_number)
            
            # 2. Click the "Search" button
            page.get_by_role("button", name="Search").click()
            
            # 3. Wait for the results to appear
            # We wait for the results container, which has one of two IDs
            page.wait_for_selector("#onwardTrip,#bookedTicket", timeout=15000)
            
            # Check if the bus was found
            results_div = page.locator("#onwardTrip,#bookedTicket")
            scraped_data = results_div.inner_text()
            
            if not scraped_data:
                scraped_data = "No information found for that service number."

            browser.close()
            print("Scraping successful.")

    except Exception as e:
        print(f"❌ Failed to scrape website. Error: {e}")
        # This error often happens if the service number is not valid or not running
        return f"No tracking information found for service '{service_number}'. This could be an invalid number, or the bus may not be running today."

    # --- Use the LLM to summarize the scraped data ---
    prompt = f"""
    Based on the following text scraped from the APSRTC bus tracking website for service '{service_number}', 
    summarize the current status of the bus.
    Be concise and list the key details like the Bus Registration No., Current Location, and ETA.
    
    Scraped Data:
    ---
    {scraped_data}
    ---
    """
    
    response = llm.invoke(prompt)
    return response.content