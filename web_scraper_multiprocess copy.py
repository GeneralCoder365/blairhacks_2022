import sys
import time
import json
# import builtins as __builtin__
import multiprocessing
from multiprocessing import Pool
# import threading
# from pathos.multiprocessing import ProcessingPool as Pool
# import dill
# import multiprocessing_on_dill as multiprocessing
from xml import dom

from bs4 import BeautifulSoup as bs
import requests

# import resource_finder
# import web_crawler_multiprocess
# import relevance_analyzer

summary_list = ["about", "summary", "mission", "overview", "about this course", "about this professional certificate", "about this opportunity", "about this specialization", "purpose", "our purpose", "description"]


# url = "https://www.coursera.org/learn/machine-learning"

def master_query_maker(tags, dom_queue):
    import resource_finder
    resource_finder.query_maker(tags, dom_queue)

def master_web_crawler(search_queries, dom_queue):
    import web_crawler_multiprocess
    web_crawler_multiprocess.master_urls_to_search(search_queries, dom_queue)

def overview_finder(url):
    text_list = []
    
    k = 1
    request = requests.get(url)
 
    Soup = bs(request.text, 'html.parser')
 
    # creating a list of all common heading tags
    wanted_tags = ["h1", "h2", "h3", "h4", "h5", "p"]
    for tags in Soup.find_all(wanted_tags):
        text_list.append(tags.text.strip())
            
    # print("text_list: ", text_list)
    for i in text_list:
        # for j in range(len(summary_list)):
        #     if i.lower() in summary_list[j]:
        if i.lower() in summary_list:
            # print("Header: " + i)
            # print("k: " + str(k)) 
            break
        k += 1
        
            
    # print(text_list)
    # print(text_list[-1])
    # print(len(text_list))
    # print(k)
    # print(text_list[k])
    try:
        if text_list[k].lower() == "applied learning project":
            # print(text_list[k + 1])
            return(text_list[k + 1])
        else:                  
            # print(text_list[k])
            return(text_list[k])
    except IndexError:
        return False

def other_info_finder(url): # for Coursera only
    t_list = []

    r_list = []
    
    s = 1
    u = 0
    request = requests.get(url)
 
    Soup = bs(request.text, 'html.parser')
    
    w_tags = ["h1", "h2", "h3", "span"]
    for tags in Soup.find_all(w_tags):
        t_list.append(tags.text.strip())
    
    for l in t_list:
        if "approx" in l.lower():
            t = l.split(" ")
            r_list.append(t[1])
            
    for x in t_list:
        if x.lower() == "offered by":
            break
        
        s += 1
    r_list.append(t_list[s])
    
    r = list(dict.fromkeys(r_list))
    
    # print(r)
    return r

# other_info_finder(url) 
# print(overview_finder("https://www.coursera.org/specializations/data-structures-algorithms"))

def tags_to_dict(str_tags):
    tags = dict(json.loads(str_tags))
    
    return tags

# ! used to solve AttributeError: Can't pickle local object 'master_results.<locals>.description_relevance_calculator'
# global description_relevance_calculator
def description_relevance_calculator(relevance_calculator, tags_to_compare_to, url):    
    description = str(overview_finder(url))
    # print("DESCRIPTION: ", description)

    if (description != False): # only include urls that we can pull descriptions from
        relevance_data = relevance_calculator(tags_to_compare_to, description)
        relevance = relevance_data[0]
        tags_frequency = relevance_data[1] # {'exam': 3, 'boobs': 2, 'favourite': 1}
        # tags_frequency_dict[urls_to_search[j]] = tags_frequency
        # print("current relevance: ", relevance)
        if (relevance == False):
            relevance = 0
        
        # print("RELEVANCE: ", relevance)
        
        return (url, description, relevance, tags_frequency)

    else:
        return False




# global master_results
def master_results(all_urls_to_search, dom_queue):
    import relevance_analyzer
    
    # top_queue = multiprocessing.Queue()
    
    
    # https://towardsdatascience.com/parallelism-with-python-part-1-196f0458ca14
    search_results = {}
        
    for i in range(len(all_urls_to_search)):
        i_urls_to_search = all_urls_to_search[i]
        if "type_of_opportunity" in i_urls_to_search:
            type_of_opportunity = i_urls_to_search["type_of_opportunity"]
        if "skill_interest" in i_urls_to_search:
            skill_interest = i_urls_to_search["skill_interest"]
        if "in_person_online" in i_urls_to_search:
            in_person_online = i_urls_to_search["in_person_online"]
        urls_to_search = i_urls_to_search["urls_to_search"]
        
        tags_to_compare_to = [skill_interest, type_of_opportunity, in_person_online]
        relevance_ratings_dict = {}
        tags_frequency_dict = {}
        all_description_dict = {}
        
        # top_threads = []
        
        # for j in range(len(urls_to_search)):
        #     description_relevance_thread = threading.Thread(target=description_relevance_calculator, args=(relevance_analyzer.result_relevance_calculator, tags_to_compare_to, urls_to_search[j], top_queue))
        #     top_threads.append(description_relevance_thread)
        
        with Pool() as top_pool: # not specifying Pool(processes=__) so using max number of cores on computer
            top_pool = top_pool.starmap_async(description_relevance_calculator, [(relevance_analyzer.result_relevance_calculator, tags_to_compare_to, urls_to_search[j]) for j in range(len(urls_to_search))]).get()
            
        print(top_pool)
        # # print("TOP_THREADS: ", top_threads)
        
        
        # for t_thread in top_threads:
        #     t_thread.start()
        # print("FINISHED STARTING TOP_THREADS")
        # for t_thread in top_threads:
        #     print("FINISHING TOP_THREAD")
        #     t_thread.join()
        #     print("FINISHED TOP_THREAD")
        
        # if (len(urls_to_search) == top_queue.qsize()):
        #     print("GOOODDDDD!!!")
        
        # for k in range(top_queue.qsize()):
        #     description_relevance_data = top_queue.get()
            # (url, description, relevance, tags_frequency)
        for description_relevance_data in top_pool:
            if (description_relevance_data != False):
                url = description_relevance_data[0]
                description = description_relevance_data[1]
                relevance = description_relevance_data[2]
                tags_frequency = description_relevance_data[3]
                
                all_description_dict[url] = description
                tags_frequency_dict[url] = tags_frequency
                relevance_ratings_dict[url] = relevance
        

        # sorts in descending order
        relevance_ratings_dict = dict(sorted(relevance_ratings_dict.items(), key=lambda x:x[1], reverse=True))
        # print("RELEVANCE_RATINGS_DICT: ", relevance_ratings_dict)
        
        # print("sorted relevance_ratings_dict: ", relevance_ratings_dict)
        
        relevance_ratings_dict = dict(list(relevance_ratings_dict.items())[0: 5])
        
        # print("processed relevance_ratings_dict: ", relevance_ratings_dict)
        
        resource_data_dict = {}
        for a in relevance_ratings_dict.keys():
            resource_data_dict[a] = [all_description_dict[a], tags_frequency_dict[a]]
        # print("resource_data_dict: ", resource_data_dict)
        
        url_dict = {}
        if (type_of_opportunity == "sports"):
            url_dict["sport"] = i_urls_to_search["sport"]
            url_dict["type_of_opportunity"] = i_urls_to_search["type_of_opportunity"]
        else:
            url_dict["skill_interest"] = skill_interest
            url_dict["type_of_opportunity"] = type_of_opportunity
            url_dict["in_person_online"] = in_person_online
        url_dict["resource_data_dict"] = resource_data_dict
        
        # print("url_dict: ", url_dict)
        
        search_results[i] = url_dict
    
    # top_queue.close()
    
    search_results = json.dumps(search_results)
    
    dom_queue.put(search_results)

def master_scraper(tags, master_queue):
    # if __name__ == '__main__':
    
    try:
        dom_queue = multiprocessing.Queue()
        
        tags = tags_to_dict(tags)
        
        print("tags: ", tags)
        
        search_queries_process = multiprocessing.Process(target=master_query_maker, args=(tags, dom_queue))
        # search_queries_process = multiprocessing.Process(target=resource_finder.database_lister_query_maker, args=(tags, dom_queue))
        search_queries_process.start()
        search_queries_process.join()
        search_queries = dom_queue.get()
        search_queries_process.terminate()
        print("SEARCH QUERIES PROCESS IS ALIVE: ", search_queries_process.is_alive())
        # search_queries = resource_finder.database_lister_query_maker(tags)
        print("search_queries: ", search_queries)
        print("DOM_QUEUE SIZE = ", dom_queue.qsize())
        
        web_crawler_process = multiprocessing.Process(target=master_web_crawler, args=(search_queries, dom_queue))
        # web_crawler_process = multiprocessing.Process(target=web_crawler_multiprocess.master_urls_to_search, args=(search_queries, dom_queue))
        web_crawler_process.start()
        print("PREBOOB")
        web_crawler_process.join()
        print("BOOB")
        all_urls_to_search = dom_queue.get()
        print("POSTBOOB")
        web_crawler_process.terminate()
        print("WEB CRAWLER PROCESS IS ALIVE: ", web_crawler_process.is_alive())
        print("ENDBOOB")
        # all_urls_to_search = web_crawler_multiprocess.master_urls_to_search(search_queries, dom_queue)
        print("all_urls_to_search: ", all_urls_to_search)
        print("DOM_QUEUE SIZE = ", dom_queue.qsize())
        
        relevance_optimization_process = multiprocessing.Process(target=master_results, args=(all_urls_to_search, dom_queue))
        relevance_optimization_process.start()
        print("ZEBOOBOO")
        relevance_optimization_process.join()
        dom_results = dom_queue.get()
        print("GEEBOOBOO")
        relevance_optimization_process.terminate()
        print("RELEVANCE OPTIMIZATION PROCESS IS ALIVE: ", relevance_optimization_process.is_alive())
        print("DOM_RESULTS: ", dom_results)
        print("DOM_QUEUE SIZE = ", dom_queue.qsize())
        
        dom_queue.close()
        
        # return dom_results
        master_queue.put(dom_results)
        
    
    except Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Didn't work :(")

        return False

tags = '{"skills": ["computer science", "cs", "math"], "interests": ["machine learning", "probability"], "type_of_opportunity": ["courses"], "in_person_online": "all", "location": "Rockville MD USA"}'

# ! total runtime without multiprocessing/multithreading: 4 minutes and 25 seconds
# ! TOTAL RUNTIME WITH MULTIPROCESSING/MULTITHREADING: 1 minute and 58 seconds
if __name__ == '__main__':
    start_time = time.time()
    master_queue = multiprocessing.Queue()
    master_process = multiprocessing.Process(target=master_scraper, args=(tags, master_queue))
    master_process.start()
    master_process.join()
    # master_output = master_queue.get()
    master_process.terminate()
    master_queue.close()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

    # print("MASTER OUTPUT: ", master_output)

# if __name__ == '__main__':
#     dom_queue = multiprocessing.Queue()
        
#     tags = tags_to_dict(tags)
    
#     print("tags: ", tags)
    
#     search_queries_process = multiprocessing.Process(target=master_query_maker, args=(tags, dom_queue))
#     # search_queries_process = multiprocessing.Process(target=resource_finder.query_maker, args=(tags, dom_queue))
#     search_queries_process.start()
#     search_queries_process.join()
#     search_queries = dom_queue.get()
#     search_queries_process.terminate()
#     print("SEARCH QUERIES PROCESS IS ALIVE: ", search_queries_process.is_alive())
#     # search_queries = resource_finder.database_lister_query_maker(tags)
#     print("search_queries: ", search_queries)
#     print("DOM_QUEUE SIZE = ", dom_queue.qsize())
#     # print(dom_queue.get())
    
#     # search_queries = [{'search_query': 'computer science ', 'skill_interest': 'computer science', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
#     # {'search_query': 'cs ', 'skill_interest': 'cs', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
#     # {'search_query': 'math ', 'skill_interest': 'math', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
#     # {'search_query': 'machine learning ', 'skill_interest': 'machine learning', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
#     # {'search_query': 'probability ', 'skill_interest': 'probability', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}]
    
#     web_crawler_process = multiprocessing.Process(target=master_web_crawler, args=(search_queries, dom_queue))
#     # web_crawler_process = multiprocessing.Process(target=web_crawler_multiprocess.master_urls_to_search, args=(search_queries, dom_queue))
#     web_crawler_process.start()
#     print("PREBOOB")
#     web_crawler_process.join()
#     print("BOOB")
#     print("DOM_QUEUE SIZE = ", dom_queue.qsize())
#     all_urls_to_search = dom_queue.get()
#     print("POSTBOOB")
#     web_crawler_process.terminate()
#     print("WEB CRAWLER PROCESS IS ALIVE: ", web_crawler_process.is_alive())
#     print("ENDBOOB")
#     # all_urls_to_search = web_crawler_multiprocess.master_urls_to_search(search_queries, dom_queue)
#     print("all_urls_to_search: ", all_urls_to_search)
    
#     dom_queue.close()

# master_urls_to_search:  [{'type_of_opportunity': 'courses', 'in_person_online': 'all', 'urls_to_search': ['https://www.montgomerycollege.edu/academics/programs/computer-science-and-technologies/index.html', 'https://www.montgomeryschoolsmd.org/curriculum/computer-science/index.aspx', 'https://www.montgomeryschoolsmd.org/departments/onlinelearning/courses/computerscience.aspx', 'https://www.computerscience.org/online-degrees/maryland/', 'https://www.franklin.edu/colleges-near/bachelors-programs/maryland/rockville/computer-science-bachelors-degrees', 'https://www.coursera.org/learn/cs-programming-java', 'https://www.coursera.org/specializations/introduction-computer-science-programming', 'https://www.coursera.org/specializations/python', 'https://www.coursera.org/professional-certificates/google-it-support', 'https://www.coursera.org/specializations/data-structures-algorithms', 'https://www.oercommons.org/courseware/lesson/84461/view#summary-tab', 'https://www.oercommons.org/courses/computers-all-around/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/71695/view#summary-tab', 'https://www.oercommons.org/courses/free-online-computer-science-books/view#summary-tab', 'https://www.oercommons.org/courses/computation-and-visualization-in-the-earth-sciences/view#summary-tab']}, {'type_of_opportunity': 'courses', 'in_person_online': 'all', 'urls_to_search': ['https://www.montgomerycollege.edu/academics/programs/computer-science-and-technologies/index.html', 'https://www.montgomeryschoolsmd.org/curriculum/computer-science/index.aspx', 'https://coursebulletin.montgomeryschoolsmd.org/CourseLists/Index/163', 'https://www.computerscience.org/online-degrees/maryland/', 'https://www.franklin.edu/colleges-near/bachelors-programs/maryland/rockville/computer-science-bachelors-degrees', 'https://www.coursera.org/learn/html-css-javascript-for-web-developers', 'https://www.coursera.org/learn/duke-programming-web', 'https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript', 'https://www.coursera.org/learn/introcss', 'https://www.coursera.org/learn/website-coding', 
# 'https://www.oercommons.org/courses/cs-for-oregon-plan-version-1-0/view#summary-tab', 'https://www.oercommons.org/courses/cs-fundamentals-4-5-events-in-bounce/view#summary-tab', 'https://www.oercommons.org/courses/cs-fundamentals-1-2-learn-to-drag-and-drop/view#summary-tab', 'https://www.oercommons.org/courses/cs-fundamentals-2-10-the-right-app/view#summary-tab', 'https://www.oercommons.org/courses/cs-discoveries-2019-2020-web-development-lesson-2-2-websites-for-expression/view#summary-tab']}, {'type_of_opportunity': 'courses', 'in_person_online': 'all', 'urls_to_search': 
# ['https://www.montgomeryschoolsmd.org/curriculum/math/', 'https://www.montgomeryschoolsmd.org/curriculum/math/hs.aspx', 'https://www.mathnasium.com/rockville', 'https://www.montgomerycollege.edu/academics/stem/mathematics-statistics-data-science/index.html', 'https://www.montgomerycollege.edu/academics/programs/mathematics/index.html', 'https://www.coursera.org/specializations/algebra-elementary-to-advanced', 'https://www.coursera.org/learn/mathematical-thinking', 'https://www.coursera.org/specializations/mathematics-machine-learning', 'https://www.coursera.org/learn/introduction-to-calculus', 'https://www.coursera.org/learn/tsi-math-prep', 'https://www.oercommons.org/courseware/lesson/86384/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/65288/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/86570/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/1321/view#summary-tab', 'https://www.oercommons.org/authoring/29013-math-routines/view#summary-tab']}, {'type_of_opportunity': 'courses', 'in_person_online': 'all', 'urls_to_search': ['https://www.montgomerycollege.edu/academics/programs/data-science/index.html', 'https://www.icertglobal.com/course/Artificial-Intelligence-and-Deep-Learning-Certification-Training-Baltimore-MD/Classroom/82/178', 'https://www.glassdoor.com/Job/rockville-machine-learning-jobs-SRCH_IL.0,9_IC1153899_KO10,26.htm', 'https://www.onlc.com/training/python/rockville-md.htm', 'https://www.indeed.com/q-Machine-Learning-l-Rockville,-MD-jobs.html', 'https://www.coursera.org/learn/machine-learning', 'https://www.coursera.org/professional-certificates/ibm-machine-learning', 'https://www.coursera.org/specializations/deep-learning-healthcare', 'https://www.coursera.org/specializations/machine-learning', 'https://www.coursera.org/specializations/deep-learning', 'https://www.oercommons.org/authoring/56645-machine-learning/view#summary-tab', 'https://www.oercommons.org/courses/flashcard-machine/view#summary-tab', 'https://www.oercommons.org/courses/gitbook-machine-learning-in-action/view#summary-tab', 'https://www.oercommons.org/authoring/27895-artificial-intelligence-and-machine-learning/view#summary-tab', 'https://www.oercommons.org/courses/machine-learning-module-by-hunter-r-johnson/view#summary-tab']}, {'type_of_opportunity': 'courses', 'in_person_online': 'all', 'urls_to_search': ['https://www.montgomerycollege.edu/academics/stem/mathematics-statistics-data-science/index.html', 'https://www.montgomeryschoolsmd.org/departments/onlinelearning/courses/ap.aspx', 'https://coursebulletin.montgomeryschoolsmd.org/CourseDetails/Index/MAT2039', 'https://www.wyzant.com/Rockville_MD_statistics_tutors.aspx', 'https://academiccatalog.umd.edu/undergraduate/approved-courses/stat/', 'https://www.coursera.org/learn/introductiontoprobability', 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science', 'https://www.coursera.org/learn/stanford-statistics', 'https://www.coursera.org/specializations/statistical-inference-for-data-science-applications', 'https://www.coursera.org/specializations/probabilistic-graphical-models', 'https://www.oercommons.org/courseware/lesson/53607/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/4104/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/14210/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/4140/view#summary-tab', 'https://www.oercommons.org/courseware/lesson/4158/view#summary-tab']}]




# [{'skill_interest': 'computer science', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'resource_data_dict': {'https://www.coursera.org/specializations/python': ['No prior experience required.', {'courses': 1}], 'https://www.coursera.org/professional-certificates/google-it-support': ['This program includes over 100 hours of instruction and hundreds of practice-based assessments, which will help you simulate real-world IT support scenarios that are critical for success in the workplace.', {'courses': 8}], 'https://www.coursera.org/specializations/introduction-computer-science-programming': ['There are a range of activities included in this specialization that will enable learners to apply and develop their programming skills in a fun and engaging way. Learners will master the fundamentals of computer science by solving mathematical puzzles using interactive techniques, becoming a detective and solving crimes in an interactive sleuth application and apply computer science concepts to solve problems found in daily computer use.', {'courses': 20, 'computer science': 6}], 'https://www.coursera.org/specializations/data-structures-algorithms': ['The specialization contains two real-world projects: Big Networks and Genome Assembly. You will analyze both road networks and social networks and will learn how to compute the shortest route between New York and San Francisco 1000 times faster than the shortest path algorithms you learn in the standard Algorithms 101 course! Afterwards, you will learn how to assemble genomes from millions of short fragments of DNA and how assembly algorithms fuel recent developments in personalized medicine.', {'courses': 24, 'computer science': 4}], 'https://www.coursera.org/learn/cs-programming-java': ['The basis for education in the last millennium was â\x80\x9creading, writing, and arithmetic;â\x80\x9d now it is reading, writing, and computing. Learning to program is an essential part of the education of every student, not just in the sciences and engineering, but in the arts, social sciences, and humanities, as well. Beyond direct applications, it is the first step in understanding the nature of computer scienceâ\x80\x99s undeniable impact on the modern world.  This course covers the first half of our book Computer Science: An Interdisciplinary Approach (the second half is covered in our Coursera course Computer Science: Algorithms, Theory, and Machines). Our intent is to teach programming to those who need or want to learn it, in a scientific context.', {'courses': 38, 'computer science': 10}]}}, {'skill_interest': 'cs', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'resource_data_dict': {'https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript': ['Want to take the first steps to become a Cloud Application Developer? This course will lead you through the languages and tools you will need to develop your own Cloud Apps.', {'courses': 7, 'cs': 6}], 'https://www.coursera.org/learn/website-coding': ['In this course you will learn three key website programming and design languages: HTML, CSS and JavaScript. You will create a web page using basic elements to control layout and style.  Additionally, your web page will support interactivity.', {'cs': 11, 'courses': 10}], 'https://www.coursera.org/learn/html-css-javascript-for-web-developers': ['Do you realize that the only functionality of a web application that the user directly interacts with is through the web page? Implement it poorly and, to the user, the server-side becomes irrelevant! Todayâ\x80\x99s user expects a lot out of the web page: it has to load fast, expose 
# the desired service, and be comfortable to view on all devices: from a desktop computers to tablets and mobile phones.', {'courses': 18, 'cs': 6}], 'https://www.coursera.org/learn/duke-programming-web': ['Learn foundational programming concepts (e.g., functions, for loops, conditional statements) and how to solve problems like a programmer. In addition, learn basic web development as you build web pages using HTML, CSS, JavaScript. By the end of the course, will create a web page where others can upload their images and apply image filters that you create.', {'courses': 15, 'cs': 7}], 'https://www.coursera.org/learn/introcss': ['The web today is almost unrecognizable from the early days of white pages with lists of blue links.  Now, sites are designed with complex layouts, unique fonts, and customized color schemes.   This course will show you the basics of Cascading Style Sheets (CSS3).  The emphasis will be on learning how to write CSS rules, how to test code, and how to establish good programming habits.', {'courses': 14, 'cs': 14}]}}, {'skill_interest': 'math', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'resource_data_dict': {'https://www.coursera.org/learn/mathematical-thinking': ['Learn how to think the way mathematicians do â\x80\x93 a powerful cognitive process developed over thousands of years.', {'math': 2, 'courses': 3}], 'https://www.coursera.org/learn/introduction-to-calculus': ['The focus and themes of the Introduction to Calculus course address the most important foundations for applications of mathematics in science, engineering and commerce. The course emphasises the key ideas and historical motivation for calculus, while at the same time striking a balance between theory and application, leading to a mastery of key threshold concepts in foundational mathematics.', {'courses': 18, 'math': 11}], 'https://www.coursera.org/learn/tsi-math-prep': ['The purpose of this course is to review and practice key concepts in preparation for the math portion of the Texas Success Initiative Assessment 2.0 (TSI2).Â\xa0 The TSI2 is series of placement tests for learners enrolling in public universities in Texas.Â\xa0 This MOOC will cover the four main categories of the Mathematics portion:Â\xa0 Quantitative Reasoning, Algebraic Reasoning, Geometric & Spatial 
# Reasoning, and Probabilistic & Statistical Reasoning.Â', {'math': 7, 'courses': 19}], 'https://www.coursera.org/specializations/algebra-elementary-to-advanced': ['Instead of a single large project, there are many smaller applied and algebra problems throughout the modules of the courses. Practice problems with worked solutions are provided throughout the course to prepare students and allow them to be successful. Problems range in difficulty to allow students to be challenged as they apply the knowledge gained from the course.', {'courses': 11, 'math': 6}], 'https://www.coursera.org/specializations/mathematics-machine-learning': ['Through the assignments of this specialisation you will use the skills you have learned to produce mini-projects with Python on interactive notebooks, an easy to learn tool which will help you apply the knowledge to real world problems. For example, using linear algebra in order to calculate the page rank of a small simulated internet, applying multivariate calculus in order to train your own neural network, performing a non-linear least squares regression to fit a model to a data set, and using principal component analysis to determine the features of the MNIST digits data set.', {'courses': 22, 'math': 17}]}}, {'skill_interest': 'machine learning', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'resource_data_dict': {'https://www.coursera.org/specializations/deep-learning': ['By the end youâ\x80\x99ll be able to', {'courses': 1}], 'https://www.coursera.org/specializations/machine-learning': ['Learners will implement and apply predictive, classification, clustering, and information retrieval machine learning algorithms to real datasets throughout each course in the specialization. They will walk away with applied machine learning and Python programming experience.', {'machine learning': 7, 'courses': 13}], 'https://www.coursera.org/specializations/deep-learning-healthcare': ['Learners will be able to apply the theoretical concepts in autograded programming assignments that use training data we provide for use with different types of neural networking algorithms. The technology used is (among others) Jupyter Notebooks / PyTorch.', {'machine learning': 1, 'courses': 11}], 'https://www.coursera.org/professional-certificates/ibm-machine-learning': ['This Professional Certificate has a strong emphasis on developing the skills that help you advance a career in Machine Learning. All the courses include a series of hands-on labs and final projects that help you focus on a specific project that interests you. Throughout this Professional Certificate, you will gain exposure to a series of tools, libraries, cloud services, 
# datasets, algorithms, assignments and projects that will provide you with practical skills with applicability to Machine Learning jobs. These skills include:', {'courses': 25, 'machine learning': 4}], 'https://www.coursera.org/learn/machine-learning': ["Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI.", {'machine learning': 14, 'courses': 28}]}}, {'skill_interest': 'probability', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'resource_data_dict': {'https://www.coursera.org/specializations/probabilistic-graphical-models': ['Through various lectures, quizzes, programming assignments and exams, learners in this specialization will practice and master the fundamentals of probabilistic graphical models. This specialization has three five-week courses for a total of fifteen weeks.', {'courses': 13, 'probability': 
# 1}], 'https://www.coursera.org/learn/introductiontoprobability': ['This course will provide you with a basic, intuitive and practical introduction into Probability Theory. You will be able to learn how to apply Probability Theory in different scenarios and you will earn a "toolbox" of methods to deal with uncertainty in your daily life.', {'courses': 9, 'probability': 5}], 'https://www.coursera.org/specializations/statistical-inference-for-data-science-applications': ['Learners will practice new probability skills. including fundamental statistical analysis of data sets, by completing exercises in Jupyter Notebooks. In addition, learners will test their knowledge by completing benchmark quizzes throughout the courses.', {'courses': 11, 'probability': 4}], 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science': ['Understand the foundations of probability and its relationship to statistics and data science.Â\xa0 Weâ\x80\x99ll learn what it means to calculate a probability, independent and dependent outcomes, and conditional events.Â\xa0 Weâ\x80\x99ll study discrete and continuous random variables and see how this fits with data collection.Â\xa0 Weâ\x80\x99ll end the course with Gaussian (normal) random variables and the Central Limit Theorem and understand its fundamental importance for all of statistics and data science.', {'courses': 18, 'probability': 7}], 'https://www.coursera.org/learn/stanford-statistics': ['Stanford\'s "Introduction to Statistics" teaches you statistical thinking concepts 
# that are essential for learning from data and communicating insights. By the end of the course,Â\xa0you will be able to perform exploratory data analysis, understand key principles of sampling, and select appropriate tests of significance for multiple contexts. You will gain the foundational skills that prepare you to pursue more advanced topics in statistical thinking and machine learning.', {'courses': 11, 'probability': 3}]}}]