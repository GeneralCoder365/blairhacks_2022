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
            
            search_queries.append([search_query, type_of_opportunity[j], in_person_online[i]])
    
    return search_queries