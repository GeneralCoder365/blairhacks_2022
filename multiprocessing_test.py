import multiprocessing

import web_crawler_multiprocess


if __name__ == '__main__':
    dom_queue = multiprocessing.Queue()
    dom_process = multiprocessing.Process(target=web_crawler_multiprocess.master_urls_to_search, args=(search_queries, dom_queue))
    dom_process.start()
    dom_process.join()
    final_result = dom_queue.get()
    dom_process.terminate()
    dom_queue.close()
    print("master_urls_to_search: ", final_result)
