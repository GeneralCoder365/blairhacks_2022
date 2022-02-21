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

# ! CONVERT NICO'S DICT STRINGS TO DICT USING JSON.LOAD

def database_lister_query_maker(tags, dom_queue):
    # if __name__ == '__main__':
    
    # tags is a dictionary with keys: skills, interests, languages, past experience, type of opportunity, in-person/online, location,
    # and the values are lists of the tags.
    
    search_queries = []
    skills_interests_exists = []
    if "skills" in tags:
        skills = tags_cleaner(tags["skills"])
        # print("skills: ", skills)
        skills_interests_exists.append("skills")
    if "interests" in tags:
        interests = tags_cleaner(tags["interests"])
        # print("interests: ", interests)
        skills_interests_exists.append("interests")
    if "languages" in tags:
        languages = tags_cleaner(tags["languages"])
        if (len(languages) > 0):
            languages_query = ' '.join(languages[:3]) # ! This is a hack to make sure the query is not too long, so only gets first <= 3 languages
    if "type_of_opportunity" in tags:
        type_of_opportunity = tags["type_of_opportunity"]
    if "in_person_online" in tags:
        in_person_online = tags["in_person_online"]
    if "location" in tags:
        location = tags["location"]
    if "sport" in tags:
        sport = tags["sport"]
    if "grade_level" in tags:
        grade_level = str(tags["grade_level"])
    
    # ! WILL USE ML TO GENERATE A COMPOSITE ARRAY OF SKILLS AND INTERESTS WHERE IF THERE IS A SIMILAR INTEREST AND SKILL, THEN THE SKILL TAKES PRECEDENCE, ELSE BOTH ARE ADDED
    skills_interests_list = []
    skills_interests_query = ""
    if (("skills" in skills_interests_exists) and ("interests" in skills_interests_exists)):
        skills_interests_list = skills + interests
        skills_interests_list = tags_cleaner(skills_interests_list[:6])
        skills_interests_query = ' '.join(skills_interests_list)
    elif ("skills" in skills_interests_exists):
        skills_interests_list = skills[:5]
        skills_interests_query = ' '.join(skills)
    elif ("interests" in skills_interests_exists):
        skills_interests_list = interests[:5]
        skills_interests_query = ' '.join(interests)
    
    for i in range(len(type_of_opportunity)):
        search_dict = {}
        if (type_of_opportunity[i] == "sports"):
            search_dict["sport"] = sport
            search_dict["location"] = location
            search_dict["type_of_opportunity"] = type_of_opportunity[i]
            search_queries.append(search_dict)
        else:
            if (len(skills_interests_list) == 0):
                skills_interests_list = [""] # make it non-empty so that code still works
            for j in range(len(skills_interests_list)):
                search_dict = {}
                search_query = ""
                search_query = skills_interests_list[j] + " "
                # print("skill/interest: ", skills_interests_list[j])
                # print("current search query: ", search_query)
                
                if ("grade_level" in locals()): # if the variable exists
                    search_dict["grade_level"] = grade_level
                
                search_dict["search_query"] = search_query
                search_dict["skill_interest"] = skills_interests_list[j]
                search_dict["type_of_opportunity"] = type_of_opportunity[i]
                search_dict["in_person_online"] = in_person_online
                
                if (in_person_online != "online"):
                    search_dict["location"] = str(location)
                
                # print("search_dict: ", search_dict)
        
                search_queries.append(search_dict)
                # print("current_search_queries: ", search_queries)
    
    # return search_queries
    
    dom_queue.put(search_queries)

# tags = {
#     "skills": ["computer science", "cs", "math"],
#     "interests": ["machine learning", "probability"],
#     "type_of_opportunity": ["courses"],
#     "in_person_online": "all",
#     "location": "Rockville MD USA"
# }

# print(database_lister_query_maker(tags))