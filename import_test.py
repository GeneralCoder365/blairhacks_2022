# import hmni
# import nltk
# import selenium
import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import multiprocessing

# import relevance_analyzer
# import resource_finder
# import web_crawler_multiprocess

def relevance():
    import relevance_analyzer

def master_web_crawler(search_queries, dom_queue):
    import web_crawler_multiprocess
    output = web_crawler_multiprocess.master_urls_to_search(search_queries, dom_queue)
    
    dom_queue.put(output)

search_queries = [{'search_query': 'computer science ', 'skill_interest': 'computer science', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'cs ', 'skill_interest': 'cs', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'math ', 'skill_interest': 'math', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'machine learning ', 'skill_interest': 'machine learning', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'probability ', 'skill_interest': 'probability', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}]

if __name__ == '__main__':
    dom_queue = multiprocessing.Queue()
    relevance_process = multiprocessing.Process(target=relevance)
    relevance_process.start()
    relevance_process.join()
    relevance_process.terminate()
    dom_process = multiprocessing.Process(target=master_web_crawler, args=(search_queries, dom_queue))
    dom_process.start()
    dom_process.join()
    final_result = dom_queue.get()
    dom_process.terminate()
    dom_queue.close()
    print("master_urls_to_search: ", final_result)