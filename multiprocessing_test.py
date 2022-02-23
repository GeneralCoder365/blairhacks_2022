import multiprocessing

import web_crawler_multiprocess

search_queries = [{'search_query': 'computer science ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'cs ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'math ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'machine learning ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}, 
{'search_query': 'probability ', 'type_of_opportunity': 'courses', 'in_person_online': 'all', 'location': 'Rockville MD USA'}]

if __name__ == '__main__':
    dom_queue = multiprocessing.Queue()
    dom_process = multiprocessing.Process(target=web_crawler_multiprocess.master_urls_to_search, args=(search_queries, dom_queue))
    dom_process.start()
    dom_process.join()
    final_result = dom_queue.get()
    dom_process.terminate()
    dom_queue.close()
    print("master_urls_to_search: ", final_result)
