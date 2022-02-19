from time import sleep
import sys

from selenium import webdriver
from bs4 import BeautifulSoup

def database_lister(type_of_opportunity):
    # types of opportunities: Courses, Volunteer, Sports, Tutoring (if tutoring, expand to Getting Tutored and Tutoring), Internships
    
    # Places to search in (Google), 
    # Education (Coursera, OER Commons), 
    # Volunteer (Points of Light, VolunteerMatch), 
    # Sports (Just stick to filters & Google, AAU Club Locator [US Only]),
    # Internships (Indeed)
    
    google_url = 'https://www.google.com/'
    education_urls = ['https://www.coursera.org/', 'https://www.oercommons.org/']
    # oer commons wants: "What are you looking for", "Subject", "Education Level"
    volunteer_urls = ['https://www.volunteermatch.org/', 'https://engage.pointsoflight.org/?utm_source=POLmenu&utm_medium=getinvolved&utm_campaign=DICE']
    # volunteer match wants: location (ex: Rockville, MD, USA)
        # then can select "All or Virtual Only", "Cause Areas", "Skills", "search by keyword" JUST USE THIS ONE!
    # points of light wants: "keywords", location (ex: Rockville, MD)
    sports_url = 'https://application.aausports.org/clublocator/' # wants "primary sport", "address or zip code", "search radius (miles)"
    tutoring_urls = ['https://studentsupportaccelerator.com/database/tutoring/', 'https://www.skooli.com/for_tutors']
    get_tutored_urls = ['https://www.skooli.com/database-tutors', 'https://www.teacheron.com/tutors']
    # teacheron wants: "subject/skill", "location" (have to select from generated list!)
    internship_url = 'https://www.indeed.com/' # wants "what", "where" then can choose "remote", "date posted", "salary estimate", "within n miles", "company", "experience level"
    
    urls_to_search = []
    urls_to_search.append(google_url)
    if (type_of_opportunity == 'courses'):
        urls_to_search.extend(education_urls)
    elif (type_of_opportunity == 'volunteer'):
        urls_to_search.extend(volunteer_urls)
    elif (type_of_opportunity == 'sports'):
        urls_to_search.append(sports_url)
    elif (type_of_opportunity == 'tutoring'):
        urls_to_search.extend(tutoring_urls)
    elif (type_of_opportunity == 'getting tutored'):
        urls_to_search.extend(get_tutored_urls)
    elif (type_of_opportunity == 'internships'):
        urls_to_search.append(internship_url)
    
    return urls_to_search

def google_searcher(search_query):
    try:
        browser = webdriver.Firefox()
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS TEMPORARY EMAIL SITE
        browser.execute_script("window.open('https://www.google.com/', 'googletab');")

        # Switches to original blank tab and closes it
        browser.switch_to_window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to the Temporary Email tab
        browser.switch_to_window(browser.window_handles[0])
        
        sleep(3)

        # Search for the query

    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

search_query = "fetus deletus"
print(google_searcher(search_query))