import re
from itertools import combinations

import relevance_analyzer

def tag_cleaner(tag):
    tag = str(tag).lower()
    tag = re.sub(r'[^a-zA-Z0-9 -]', '', tag)
    
    return tag
# print(tag_cleaner("in-person")) # this works, so still outputs in-person

def tags_cleaner(tags_array):
    # tags_array is a list of tags.
    # This function cleans the tags and returns a list of cleaned tags.
    
    cleaned_text_tags = [tag_cleaner(tag) for tag in tags_array]
    
    for a, b in combinations(cleaned_text_tags, 2):
        if (a == b):
            cleaned_text_tags.remove(a)
        elif (relevance_analyzer.relevance_calculator(a,b) > 0.7):
            cleaned_text_tags.remove(a)
    
    return cleaned_text_tags

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


def database_lister_query_maker(tags):
    # tags is a dictionary with keys: skills, interests, languages, past experience, type of opportunity, in-person/online, location,
    # and the values are lists of the tags.
    
    skills = tags_cleaner(tags["skills"])
    interests = tags_cleaner(tags["interests"])
    languages = tags_cleaner(tags["languages"])
    past_experience = tags_cleaner(tags["past_experience"])
    type_of_opportunity = tags["type_of_opportunity"]
    in_person_online = tags["in_person_online"]
    location = tags["location"]
    
    search_queries = []
    skills_query = ""
    interests_query = ""
    languages_query = ""
    past_experience_query = ""
    location_query = ""
    
    if (len(skills) > 0):
        skills_query = ' '.join(skills[:5]) # ! This is a hack to make sure the query is not too long, so only gets first <= 5 skills
    if (len(interests) > 0):
        interests_query = ' '.join(interests[:5]) # ! This is a hack to make sure the query is not too long, so only gets first <= 5 interests
    if (len(languages) > 0):
        languages_query = ' '.join(languages[:5]) # ! This is a hack to make sure the query is not too long, so only gets first <= 5 languages
    if (len(past_experience) > 0):
        past_experience_query = ' '.join(past_experience[:5]) # ! This is a hack to make sure the query is not too long, so only gets first <= 5 past_experience
    if (len(location) > 0):
        location_query = str(location[0] + " " + location[1] + " " + location[2]) # city + state + country
    
    for i in range(len(in_person_online)):
        for j in range(len(type_of_opportunity)):
            search_query = ""
            
            if (skills_query != ""):
                search_query += str(skills_query + " ")
            if (interests_query != ""):
                search_query += str(interests_query + " ")
            if (languages_query != ""):
                search_query += str(languages_query + " ")
            if (past_experience_query != ""):
                search_query += str(past_experience_query + " ")
            
            if (in_person_online[i] == "online"):
                search_query += "online"
            elif (in_person_online[i] == "in-person"):
                if (location_query != ""):
                    search_query += str(location_query)
            
            search_queries.append(search_query)
    
    return search_queries