# import os
from time import sleep
import sys
import multiprocessing

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

# ! NEED TO FORMAT SEARCH QUERIES FOR EACH DATABASE!!!

def typist(element, text):
    # Deletes anything currently in the field
    element.send_keys(keys.CONTROL,"a")
    element.send_keys(keys.DELETE)
    sleep(0.5)

    # random_speeds = [round(random.uniform(0.07, 0.3),2) for i in range(10)]

    for character in text:
        element.send_keys(character)
        # sleep(random_speeds[random.randint(0, (len(random_speeds) - 1))])

def google_searcher(search_query, slave_queue):
    try:
        print("GOOGLE 0")
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        print("GOOGLE 1")
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS GOOGLE
        browser.execute_script("window.open('https://www.google.com/', 'googletab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to Google tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(1)

        # Search for the query
        search_input_field = browser.find_element(By.CSS_SELECTOR, 'input[aria-label = "Search"]')
        typist(search_input_field, search_query)
        
        sleep(0.5)
        
        # searches for the query
        search_input_field.send_keys(keys.ENTER)
        
        sleep(1)
        
        result_tags = list(browser.find_elements(By.XPATH, "//div[@class = 'yuRUbf']//a"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        # return result_urls
        slave_queue.put(result_urls)
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "fetus deletus"
# print(google_searcher(search_query))

def coursera_searcher(search_query, slave_queue):
    try:
        print("COURSERA 0")
        # print("COURSERA SEARCH QUERY: '" + search_query + "'")
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        # options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        print("COURSERA 1")
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS COURSERA
        browser.execute_script("window.open('https://www.coursera.org/', 'courseratab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to Coursera tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(1)

        # Searches for search field button
        search_field_button = browser.find_element(By.XPATH, "//button[@aria-label = 'Search Coursera']")
        search_field_button.click()
        
        
        sleep(0.5)
        
        # Search for the query
        search_input_field = browser.find_element(By.XPATH, "//input[@type = 'text']") # '//input[@aria-label = "What do you want to learn?"]')
        typist(search_input_field, search_query)
        
        sleep(0.5)
        
        # searches for the query
        search_input_field.send_keys(keys.ENTER)
        
        sleep(2)
        
        result_tags = list(browser.find_elements(By.XPATH, "//a[@data-click-key = 'search.search.click.search_card']"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        # return result_urls
        slave_queue.put(result_urls)
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "computer science"
# print(coursera_searcher(search_query))

def oer_commons_searcher(search_query, slave_queue):
    try:
        print("OER COMMONS 0")
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        print("OER COMMONS 0")
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS OER COMMONS
        search_query = 'https://www.oercommons.org/search?f.search=' + search_query
        # "window.open('https://www.coursera.org/', 'courseratab');"
        browser.execute_script(f"""
                               var search_query = arguments[0];
                               window.open(search_query, 'oercommonstab');
                               """, search_query)

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to OER Commons tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(2)
        
        result_tags = list(browser.find_elements(By.XPATH, "//article[@class = 'js-index-item index-item clearfix']//a[@class = 'item-link js-item-link']"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append((result_tags[i].get_attribute('href') + '/view#summary-tab'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        # return result_urls
        slave_queue.put(result_urls)
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "data structures"
# print(oer_commons_searcher(search_query))

def volunteer_match_searcher(search_query, in_person_online, slave_queue):
    try:
        # in_person_online = "all" # can be in-person, online, or all
        # location = "Rockville%2C+MD%2C+USA"
        if (in_person_online != "online"):
            location = in_person_online
        
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS VOLUNTEER MATCH
        if (in_person_online != "online"):
            search_query = 'https://www.volunteermatch.org/search/?l=' + location + '&k=' + search_query
        else:
            search_query = 'https://www.volunteermatch.org/search/?v=true&k=' + search_query
        
        browser.execute_script(f"""
                               var search_query = arguments[0];
                               window.open(search_query, 'oercommonstab');
                               """, search_query)

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to OER Commons tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(2)
        
        result_tags = list(browser.find_elements(By.XPATH, "//li[@class = 'pub-srp-opps__opp pub-srp-opps__opp--ao']//div//h3//a"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        slave_queue.put(result_urls)
        
        # return result_urls
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "music"
# print(volunteer_match_searcher(search_query))

def points_of_light_searcher(search_query, in_person_online, slave_queue):
    try:
        # in_person_online = "all" # can be in-person, online, or all
        if (in_person_online != "online"):
            location = in_person_online
        
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS POINTS OF LIGHT
        if (in_person_online != "online"):
            browser.execute_script("window.open('https://engage.pointsoflight.org/search/i/', 'pointsoflighttab');")
        else:
            browser.execute_script("window.open('https://engage.pointsoflight.org/search/i/Remote+Volunteer+Opportunities', 'pointsoflighttab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to Points of Light tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(2)
        
        keyword_input_field = browser.find_element(By.XPATH, "//input[@placeholder = 'Keyword']")
        typist(keyword_input_field, search_query)
        
        sleep(0.5)
        
        location_input_field = browser.find_element(By.XPATH, "//input[@name = 'location']")
        typist(location_input_field, location)
        
        sleep(0.5)
        
        # searches for the query
        location_input_field.send_keys(keys.ENTER)
        
        sleep(2)
        
        
        result_tags = list(browser.find_elements(By.XPATH, "//a[@data-gtm = 'view-opportunity-from-search']"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        slave_queue.put(result_urls)
        
        # return result_urls
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "shelter"
# print(points_of_light_searcher(search_query))

# https://application.aausports.org/clublocator/
def aau_searcher(sport, location, slave_queue): # ! USA ONLY! and only returns the page of results since no sub-links for each result
    try:
        # sport = "Baseball"
        # location = "20852" # zip code
        
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS AAU SPORTS
        browser.execute_script("window.open('https://application.aausports.org/clublocator/', 'aautab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to AAU Sports tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(2)
        
        # sports list = ['Archery', 'Badminton', 'Baseball', "Basketball - Women's", 'Basketball-Boys', 'Basketball-Girls', "Basketball-Men's", 'Baton Twirling', 'Bowling', 
                    # 'Cheerleading', 'Chess', 'Cornhole', 'Cricket', 'Dance', 'Diving', 'Esports', 'Fencing', 'Field Hockey', 'Football - Flag, 7v7', 'Football Cheer', 
                    # 'Football Tackle', 'Futsal', "Girls & Women's Flag Football", 'Golf', 'Gymnastics', 'Gymnastics - Acrobatic', 'Hockey - Collegiate', 'Hockey - Ice', 
                    # 'Hockey - Inline', 'Hockey - Junior A Hockey', 'Jiu Jitsu', 'Judo', 'Jump Rope', 'Karate', 'Kung-Fu', 'Lacrosse', 'Paddle Board', 'Pickleball', 
                    # 'Powerlifting', 'Rhythmic Gymnastics', 'Skateboarding', 'Soccer', 'Softball', 'Special Needs', 'Sport Stacking', 'Surfing', 'Swimming', 'Table Tennis', 
                    # 'Taekwondo', 'Target Shooting', 'Team Handball', 'Tennis', 'Track and Field', 'Trampoline - Tumbling', 'Volleyball', 'Water Polo', 'Weightlifting', 
                    # 'Wrestling']
        
        sport_options = browser.find_element(By.XPATH, "//select[@id = 'sport1']")
        sport_option = browser.find_element(By.XPATH, "//select[@id = 'sport1']//option[contains(text(), '{s}')]".format(s=sport))
        sport_option.click()
        
        sleep(0.5)
        
        location_input_field = browser.find_element(By.XPATH, "//input[@id = 'search1']")
        typist(location_input_field, location)
        
        sleep(0.5)
        
        # searches for the query
        search_button = browser.find_element(By.XPATH, "//input[@id = 'button1']")
        search_button.click()
        
        sleep(2)
        
        
        result_page = [str(browser.current_url)] # converts to array since .extend is done at the end and this is only one url
        
        browser.quit()
        
        slave_queue.put(result_page)
        
        # return result_page
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "Baseball"
# print(aau_searcher(search_query))

def tutoring_searcher(slave_queue):
    url = ['https://www.skooli.com/for_tutors'] # need to have as array since .extend is done at the end and this is only one url
    
    slave_queue.put(url)

# https://studentsupportaccelerator.com/database/tutoring?f%5B0%5D=type_of_service%3ATutoring%20Program
def student_support_accelerator_searcher(grade_level, search_query, slave_queue):
    try:
        # grade_level = "12" # pre, k, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, post
        
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known
        # options.add_experimental_option("detach", True)

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS STUDENT SUPPORT ACCELERATOR
        browser.execute_script("window.open('https://studentsupportaccelerator.com/database/tutoring?f%5B0%5D=type_of_service%3ATutoring%20Program', 'ssatab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to Student Support Accelerator tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(2)
        
        grade_level_label = "grade-levels-"
        if (grade_level == "pre"):
            grade_level_label += "1"
        elif (grade_level == "k"):
            grade_level_label += "2"
        elif (grade_level == "post"):
            grade_level_label += "15"
        else:
            grade_level_label += str(int(grade_level) + 2)
        
        grade_level_checkbox = browser.find_element(By.XPATH, "//div[@class = 'facets-widget-checkbox']//ul[@data-drupal-facet-id = 'grade_levels']//input[@id = '{g}']".format(g=grade_level_label))
        browser.execute_script("arguments[0].click();", grade_level_checkbox)
        
        sleep(0.5)
        
        keyword_input_field = browser.find_element(By.XPATH, "//input[@data-drupal-selector = 'edit-keyword']")
        typist(keyword_input_field, search_query)
        
        sleep(0.5)
        
        # searches for the query
        keyword_input_field.send_keys(keys.ENTER)
        
        sleep(2)
        
        result_tags = list(browser.find_elements(By.XPATH, "//div[@class = 'lead']//a"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        slave_queue.put(result_urls)
        
        # return result_urls
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "math virtual"
# print(student_support_accelerator_searcher(search_query))

def indeed_searcher(search_query, in_person_online, slave_queue):
    try:
        if (in_person_online == "online"):
            location = "rockville md"
        else:
            location = in_person_online
        
        # browser = webdriver.Firefox()
        # makes chrome fullscreen
        options = Options()
        options.headless = True
        # options.add_argument("--kiosk")
        options.add_argument("window-size=1920,1080") # ! effectively maximizes window since headless doesn't have a fullscreen ability since no window size is known

        browser = webdriver.Chrome(options=options)
        
        browser.implicitly_wait(5) # ! make headless when ready
        
        # Remove navigator.webdriver Flag using JavaScript
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # OPENS INDEED
        browser.execute_script("window.open('https://www.indeed.com/', 'indeedtab');")

        # Switches to original blank tab and closes it
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        sleep(1)

        # Switches back to Indeed tab
        browser.switch_to.window(browser.window_handles[0])
        
        sleep(1)

        # Search for the query
        search_input_field = browser.find_element(By.CSS_SELECTOR, 'input[id = "text-input-what"]')
        typist(search_input_field, search_query)
        
        sleep(0.5)
        
        location_input_field = browser.find_element(By.CSS_SELECTOR, 'input[id = "text-input-where"]')
        typist(location_input_field, location)
        
        sleep(0.5)
        
        # searches for the query
        search_input_field.send_keys(keys.ENTER)
        
        sleep(2)
        
        if (in_person_online == "online"):
            remote_filter = browser.find_element(By.XPATH, "//button[@id = 'filter-remotejob']")
            browser.execute_script("arguments[0].click();", remote_filter)
            
            remote_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Remote')]")
            browser.execute_script("arguments[0].click();", remote_button)
            
            sleep(1)
        
        result_tags = list(browser.find_elements(By.XPATH, "//button[@id = 'mosaic-provider-jobcards']/a"))
        # print(result_tags)
        
        result_urls = []
        for i in range(len(result_tags)):
            result_urls.append(result_tags[i].get_attribute('href'))
        # print(result_urls)
        
        browser.quit()
        
        result_urls = result_urls[:5]
        
        slave_queue.put(result_urls)
        
        # return result_urls
        
    
    except  Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

# search_query = "computer science"
# print(indeed_searcher(search_query))

def databases_to_search_analyzer(search_dict, sub_queue):
    print("Starting Database Search Analyzer")
    print("RECEIVED SEARCH DICT: ", search_dict)
    
    # types of opportunities: Courses, Volunteer, Sports, Tutoring (if tutoring, expand to Getting Tutored and Tutoring), Internships
    
    # search_dict = {
        # "search_query" = str,
        # "skill_interest" = str,
        # "type_of_opportunity" = str, # "courses", "volunteer", "sports", "getting_tutored", "tutoring", "internships"
        # "in_person_online" = str, # "in person", "online", "all"
        # "location" = str, # ! only if in_person_online != "online"
        # "sport" = str, # ! only if type_of_opportunity == "sport"
        # "grade_level" = str
    # }
    urls_to_search_dict = {}
    
    google_search_query = ""
    if "search_query" in search_dict:
        search_query = search_dict["search_query"]
        google_search_query += search_query + " "
    if "skill_interest" in search_dict:
        skill_interest = search_dict["skill_interest"]
        urls_to_search_dict["skill_interest"] = skill_interest
    if "type_of_opportunity" in search_dict:
        type_of_opportunity = search_dict["type_of_opportunity"]
        google_search_query += type_of_opportunity + " "
        urls_to_search_dict["type_of_opportunity"] = type_of_opportunity
    if "in_person_online" in search_dict:
        in_person_online = search_dict["in_person_online"]
        google_search_query += in_person_online + " "
        urls_to_search_dict["in_person_online"] = in_person_online
    if "location" in search_dict:
        location = search_dict["location"]
        google_search_query += location + " "
    if "sport" in search_dict:
        sport = search_dict["sport"]
        google_search_query += sport + " "
    if "grade_level" in search_dict:
        grade_level = search_dict["grade_level"]
        google_search_query += grade_level + " "
    google_search_query = str(google_search_query)
    
    urls_to_search = []
    
    slave_queue = multiprocessing.Queue()
    slave_processes = []
    
    google_search_process = multiprocessing.Process(target=google_searcher, args=(google_search_query, slave_queue))
    slave_processes.append(google_search_process)
    # google_search_process.start()
    # google_results = google_searcher(google_search_query)[:5]
    
    if (type_of_opportunity == 'courses'):
        coursera_search_process = multiprocessing.Process(target=coursera_searcher, args=(search_query, slave_queue))
        slave_processes.append(coursera_search_process)
        # coursera_search_process.start()
        # coursera_results = coursera_searcher(search_query)[:5]
        # print(coursera_results)
        # if (len(coursera_results) > 0):
        #     urls_to_search.extend(coursera_results)
        
        oer_commons_search_process = multiprocessing.Process(target=oer_commons_searcher, args=(search_query, slave_queue))
        slave_processes.append(oer_commons_search_process)
        # oer_commons_search_process.start()
        # oer_commons_results = oer_commons_searcher(search_query)[:5]
        # if (len(oer_commons_results) > 0):
        #     urls_to_search.extend(oer_commons_results)
        
    elif (type_of_opportunity == 'volunteer'):
        # basically if not only online, then pass location in place of in_person_online, else pass in place of in_person_online
        if (in_person_online != "online"):
            volunteer_match_location = location.replace(' ', '%2C+')
            volunteer_match_search_process = multiprocessing.Process(target=volunteer_match_searcher, args=(search_query, volunteer_match_location, slave_queue))
            slave_processes.append(volunteer_match_search_process)
            # volunteer_match_results = volunteer_match_searcher(search_query, volunteer_match_location)[:5]
            points_of_light_search_process = multiprocessing.Process(target=points_of_light_searcher, args=(search_query, location, slave_queue))
            slave_processes.append(points_of_light_search_process)
            # points_of_light_results = points_of_light_searcher(search_query, location)[:5]
        else:
            volunteer_match_search_process = multiprocessing.Process(target=volunteer_match_searcher, args=(search_query, in_person_online, slave_queue))
            slave_processes.append(volunteer_match_search_process)
            # volunteer_match_results = volunteer_match_searcher(search_query, in_person_online)[:5]
            points_of_light_search_process = multiprocessing.Process(target=points_of_light_searcher, args=(search_query, in_person_online, slave_queue))
            slave_processes.append(points_of_light_search_process)
            # points_of_light_results = points_of_light_searcher(search_query, in_person_online)[:5]
        
        # if (len(volunteer_match_results) > 0):
        #     urls_to_search.extend(volunteer_match_results)
        # if (len(points_of_light_results) > 0):
        #     urls_to_search.extend(points_of_light_results)
        
        
    elif ((type_of_opportunity == 'sports') and ("USA" in location)):
        zipcode = location.split("USA ")[1]
        aau_search_process = multiprocessing.Process(target=aau_searcher, args=(sport, zipcode, slave_queue))
        slave_processes.append(aau_search_process)
        # aau_results = aau_searcher(sport, zipcode)
        # urls_to_search.append(aau_results)

    elif (type_of_opportunity == 'tutoring'):
        tutoring_search_process = multiprocessing.Process(target=tutoring_searcher, args=(slave_queue))
        slave_processes.append(tutoring_search_process)

    elif (type_of_opportunity == 'getting tutored'):
        student_support_accelerator_search_process = multiprocessing.Process(target=student_support_accelerator_searcher, args=(grade_level, search_query, slave_queue))
        slave_processes.append(student_support_accelerator_search_process)
        # student_support_accelerator_results = student_support_accelerator_searcher(grade_level, search_query)[:5]
        # if (len(student_support_accelerator_results) > 0):
        #     urls_to_search.extend(student_support_accelerator_results)
        
    elif (type_of_opportunity == 'internships'):
        if (in_person_online != "online"):
            indeed_search_process = multiprocessing.Process(target=indeed_searcher, args=(search_query, location, slave_queue))
            slave_processes.append(indeed_search_process)
            # indeed_results = indeed_searcher(search_query, location)[:5]
        else:
            indeed_search_process = multiprocessing.Process(target=indeed_searcher, args=(search_query, in_person_online, slave_queue))
            slave_processes.append(indeed_search_process)
            # indeed_results = indeed_searcher(search_query, in_person_online)[:5]
        
        # urls_to_search.extend(indeed_results)
    
    print("SLAVE PROCESSES: ", slave_processes)
    
    # google_search_process.join()
    
    # if (type_of_opportunity == 'courses'):
    #     coursera_search_process.join()
    #     oer_commons_search_process.join()
    
    # slave_processes[0].start()
    # slave_processes[1].start()
    # slave_processes[0].join()
    # slave_processes[1].join()
    for slv_process in slave_processes:
        slv_process.start()
        print("SLAVE PROCESS STARTED")
    for slv_process in slave_processes:
        print("SLAVE PROCESS FINISHING")
    #     # ! WORKING UP TO HERE BUT DEVTOOLS NOT SHOWING
    #     # ! NOT PRINTING GOOGLE 0, 1 or COURSERA 0, 1 or OER COMMONS 0, 1
        slv_process.join()
        print("SLAVE PROCESS FINISHED")
    
    # google_results = slave_queue.get() # gets the result from the slave_queue
    
    # if (len(google_results) > 0):
    #     urls_to_search.extend(google_results)
    
    for i in range(slave_queue.qsize()):
        result = slave_queue.get()
        # print("RESULT: ", result)
        if (len(result) > 0):
            urls_to_search.extend(result)
    
    # slave_processes[0].terminate()
    # slave_processes[1].terminate()
    for slv_process in slave_processes:
        slv_process.terminate()
    
    slave_queue.close()
    
    # ! REMOVING DUPLICATE URLS TO SEARCH
    urls_to_search = list(set(urls_to_search))
    
    urls_to_search_dict["urls_to_search"] = urls_to_search
    
    print("SLAVE PROCESS OUTPUT: ", urls_to_search_dict)
    
    # return urls_to_search_dict
    sub_queue.put(urls_to_search_dict)

def master_urls_to_search(search_queries, dom_queue):
    print("SEARCH QUERIES: ", search_queries)
    
    # if __name__ == '__main__':
    print("TESTING 1")
    urls_to_search = []
    sub_queue = multiprocessing.Queue()
    sub_processes = []
    for i in range(len(search_queries)):
        search_dict = search_queries[i]
        print("SEARCH DICT ", (i + 1), ": ", search_dict)
        # if __name__ == '__main__':
        databases_search_process = multiprocessing.Process(target=databases_to_search_analyzer, args=(search_dict, sub_queue))
        sub_processes.append(databases_search_process)
    
    print("FINISHED ADDING TO SUB_QUEUE")
    
    # sub_processes[0].start()
    # sub_processes[1].start()
    # sub_processes[0].join()
    # sub_processes[1].join()
    
    for s in range(len(sub_processes)):
        sub_processes[s].start()
        print("STARTED A SUB_PROCESS")
    
    for u in range(len(sub_processes)):
        print("FINISHING A SUB_PROCESS")
        sub_processes[u].join()
        print("FINISHED A SUB_PROCESS")
    
    # for s_process in sub_processes:
    #     s_process.start()
    #     print("STARTED A SUB_PROCESS")
    
    # for s_process in sub_processes:
    #     print("FINISHING A SUB_PROCESS")
    # #     # ! WORKING UP TO HERE
    # #     # ! NEVER SHOWS DEVTOOLS STUFF WHEN JOINING SUBPROCESSES
    #     s_process.join()
    #     print("FINISHED A SUB_PROCESS")

    print("TESTING 2")
    print("SUB_QUEUE SIZE = ", int(sub_queue.qsize()))
    
    for j in range(sub_queue.qsize()):
        search_process_result = sub_queue.get()
        # print("MASTER QUEUE RESULT: ", search_process_result)
        if (len(search_process_result) > 0):
            urls_to_search.append(search_process_result)
    
    # sub_processes[0].terminate()
    # sub_processes[1].terminate()
    # for s_process in sub_processes:
    #     s_process.terminate()
    for b in range(len(sub_processes)):
        sub_processes[b].terminate()
    
    print("TESTING 3")
    
    sub_queue.close()
            # urls_to_search.append(databases_to_search_analyzer(search_dict))
    
    print("TESTING 4")
    
    # wait = os.wait()
    # print("Child process with number %d exited" % (wait[0]))
    # print("Parent process with number %d exiting after child has executed its process" % (os.getpid()))
    
    print("URLS TO SEARCH: ", urls_to_search)

    # return urls_to_search
    dom_queue.put(urls_to_search)
    print("WEB CRAWLER DONE")

# search_queries = [{'search_query': 'computer science ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
# {'search_query': 'cs ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
# {'search_query': 'math ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
# {'search_query': 'machine learning ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
# {'search_query': 'probability ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}]
# ! 2:17 without multiprocessing, 25 secs with multiprocessing

# search_queries = [{'search_query': 'computer science ', 'skill_interest': 'computer science', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}]
# ! 35 secs without multiprocessing, 13 secs with multiprocessing


# if __name__ == '__main__':
#     dom_queue = multiprocessing.Queue()
#     dom_process = multiprocessing.Process(target=master_urls_to_search, args=(search_queries, dom_queue))
#     dom_process.start()
#     dom_process.join()
#     final_result = dom_queue.get()
#     dom_process.terminate()
#     dom_queue.close()
#     print("master_urls_to_search: ", final_result)

# print("master_urls_to_search: ", master_urls_to_search(search_queries))
