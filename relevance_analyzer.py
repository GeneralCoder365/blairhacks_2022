from calendar import c
import re
import sys
from collections import Counter
from nltk import regexp_tokenize
from stop_words import get_stop_words
from nltk.corpus import stopwords
# ! use once to download nltk data
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

stop_words = list(get_stop_words('en'))
nltk_stopwords = list(stopwords.words('english'))
stopwords_array = stop_words + nltk_stopwords

from fuzzywuzzy import fuzz
import hmni # ! downgraded scikit-learn from 1.0.2 to 0.23.1 because of some functions in the hmni module calling functions in scikit-learn that use old syntax
matcher = hmni.Matcher(model='latin')


from nltk.corpus import wordnet as wn
from itertools import product


def text_cleaner(description):
    description = str(description).lower()
    description = re.sub(r'[^a-zA-Z0-9 ]', '', description)
    # print(description)
    # print(type(description))
    description = description.split(" ")
    
    description = [word for word in description if not word in stopwords_array]
    
    return description

# print(description_cleaner("This is_. a test"))


def synonym_rater(word_1, word_2): # uses word-sense disambiguation
    try:
<<<<<<< HEAD
        try:
            word_1 = str(word_1)
            word_2 = str(word_2)
            sem1, sem2 = wn.synsets(word_1), wn.synsets(word_2)
        # except wn.SyntaxError:
        # except Exception:
        # nltk.corpus.reader.wordnet.WordNetError
        except (WordNetError, ValueError): # ValueError because sometimes a weird string instead of int gets passed for the synset reference
        # except nltk.corpus.reader.wordnet.WordNetError:
            # print("bob")
            return False
        # print(sem1)
        # checks if the strings are words, if not, then synonym score doesn't make sense
        if not sem1:
            # print("gob1")
            return False
        elif not sem2:
            # print("gob2")
            return False

        maxscore = 0
        for i,j in list(product(*[sem1,sem2])):
            try:
                score = i.wup_similarity(j) # Wu-Palmer Similarity, which is the best measure for synonyms
                # The Wu-Palmer Similarity measures the similarity between two words, but not the similarity between two synsets
                maxscore = score if maxscore < score else maxscore
            except (WordNetError, IndexError, AttributeError, ValueError) as e: # ValueError because sometimes a weird string instead of int gets passed for the similarity comparison
                # print("gob3")
                # print("GOOBGAB")
                pass
            except StopIteration:
                break
        maxscore = round(maxscore, 2)
        # print("raw score: ", maxscore)

        if (maxscore > 0.5):
            if (maxscore > 0.65):
                maxscore = 1.0
                
            return maxscore
        else:
            return 0.1 # ! not returning 0 because 0 = False in Python
    except Exception as e:
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Synonym rater didn't work :(")
=======
        sem1, sem2 = wn.synsets(word_1), wn.synsets(word_2)
    except wn.SyntaxError:
        return False
    # print(sem1)
    # checks if the strings are words, if not, then synonym score doesn't make sense
    if not sem1:
        return False
    elif not sem2:
        return False

    maxscore = 0
    for i,j in list(product(*[sem1,sem2])):
        score = i.wup_similarity(j) # Wu-Palmer Similarity, which is the best measure for synonyms
        # The Wu-Palmer Similarity measures the similarity between two words, but not the similarity between two synsets
        maxscore = score if maxscore < score else maxscore
    maxscore = round(maxscore, 2)
    # print("raw score: ", maxscore)

    if (maxscore > 0.5):
        if (maxscore > 0.65):
            maxscore = 1.0
            
        return maxscore
    else:
>>>>>>> parent of d5b53a9 (successfully implemented web scraper multiprocess ended up also needing multithreading still getting weird errors occasionally when internally calling relevance calculator but doesn't break code need to continue testing)
        return 0.1 # ! not returning 0 because 0 = False in Python

# print(synonym_rater("fkodpoi", "test"))
# print(synonym_rater("boob", "test"))
# print(synonym_rater("exam", "test"))
# print(synonym_rater("test", "test"))
# print(synonym_rater("corn", "test"))
# print(synonym_rater("computer science", "python"))

def relevance_calculator(word_1, word_2):
    fuzzy_rating = round(((fuzz.ratio(word_1, word_2))/100), 2)
    hmni_rating = round((matcher.similarity(word_1, word_2)), 2)
    fuzzy_hmni_rating_weights = [0.2, 0.8]
    comp_rating = round(((fuzzy_hmni_rating_weights[0] * fuzzy_rating) + (fuzzy_hmni_rating_weights[1] * hmni_rating)), 2)
    # print("fuzzy_hmni_rating: ", comp_rating)
    
<<<<<<< HEAD
    if (" " in word_1):
        word_1 = word_1.split(" ")
    if (" " in word_2):
        word_2 = word_2.split(" ")
    
    synonym_rating = 0.
    try:
        if ((type(word_1) == str) and (type(word_2) == str)):
            synonym_rating = synonym_rater(word_1, word_2)
        elif ((type(word_1) == list) and (type(word_2 == str))):
            for i in word_1:
                temp_rating = synonym_rater(i, word_2)
                if (temp_rating != False):
                    if (temp_rating == 0.1): # ! Have to do this because 0 = False in Python
                        temp_rating = 0
                    synonym_rating += temp_rating
                    synonym_rating = round(synonym_rating, 2)
        elif ((type(word_1) == str) and (type(word_2 == list))):
            for i in word_2:
                temp_rating = synonym_rater(word_1, i)
                if (temp_rating != False):
                    if (temp_rating == 0.1): # ! Have to do this because 0 = False in Python
                        temp_rating = 0
                    synonym_rating += temp_rating
                    synonym_rating = round(synonym_rating, 2)
        else:
            for i in word_1:
                for j in word_2:
                    temp_rating = synonym_rater(i, j)
                    if (temp_rating != False):
                        if (temp_rating == 0.1): # ! Have to do this because 0 = False in Python
                            temp_rating = 0
                        synonym_rating += temp_rating
                        synonym_rating = round(synonym_rating, 2)
    except Exception as e:
        synonym_rating = False
        print("Error: " + str(e))
        print("Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        print("Block synonym rating didn't work")

    # print("SYNONYM_RATING: ", synonym_rating)
=======
    synonym_rating = synonym_rater(word_1, word_2)
>>>>>>> parent of d5b53a9 (successfully implemented web scraper multiprocess ended up also needing multithreading still getting weird errors occasionally when internally calling relevance calculator but doesn't break code need to continue testing)
    if (synonym_rating != False):
        synonym_rating = round(synonym_rating, 2)
        if (synonym_rating > 1.0):
            synonym_rating = 1.0
        if (synonym_rating == 0.1): # ! Have to do this because 0 = False in Python
            synonym_rating = 0
        
        # print("synonym_rating: ", synonym_rating)
        if (synonym_rating == 1.0):
            comp_rating = 1.0
        elif (synonym_rating == 0):
            comp_rating = 0
        else:
            comp_weights = [0.1, 0.9]
            comp_rating = round(((comp_weights[0] * comp_rating) + (comp_weights[1] * synonym_rating)), 2)
    else:
        comp_rating = round((comp_rating * 0.8), 2) # ! accounts for margin of error
    
    # print("comp_rating: ", comp_rating)
                
    if (comp_rating < 0.3):
        comp_rating = 0
    
    return comp_rating

def relevance_rater(tags, description):
    tags_frequency = []
    tags_prominence_iterator = 0
    
    word_relevance_ratings = [0] * len(description)
    
    for i in range(len(description)):
        for j in range(len(tags)):
            # print("word: ", description[i], "; tag: ", tags[j])
            comp_rating = relevance_calculator(description[i], tags[j])
            # ! https://towardsdatascience.com/in-10-minutes-web-scraping-with-beautiful-soup-and-selenium-for-data-professionals-8de169d36319
            if (comp_rating > word_relevance_ratings[i]):
                word_relevance_ratings[i] = comp_rating
                if ((tags_prominence_iterator < (len(tags_frequency) - 1)) or (tags_prominence_iterator == 0)):
                    tags_frequency.append(tags[j])
                    # tags_prominence_iterator += 1
                else:
                    # print("tags_frequency_length: ", len(tags_frequency))
                    # print("tags_prominence_iterator: ", tags_prominence_iterator)
                    tags_frequency[tags_prominence_iterator] = tags[j]
                    
                if (tags[j] == tags[-1]):
                    tags_prominence_iterator += 1
    
    divider = (len(description)**2)/len(tags) #["exam", "sits", "C"]: 0.36; ["exam", "boobs", "favourite"]: 0.54 for "This is_. a test. What if tits are the best things in the world?
        # "This is_. a test. What if tits are the best things in the world?" has significant words: ['test', 'tits', 'best', 'things', 'world']
    
    # NOTE: The Wu-Palmer Similarity measures "boobs" and "tits" to have a 1.0 similarity score!
    
    # ! TRYING JUST SUM BECAUSE A WEBSITE SHOULDN'T BE PENALIZED FOR HAVING A LONG DESCRIPTION
    description_fuzzy_hmni_synonym_rating = round(sum(word_relevance_ratings), 2)
    # description_fuzzy_hmni_synonym_rating = round((sum(word_relevance_ratings) / divider), 2)
    
    tags_frequency_dict = dict(Counter(tags_frequency))
    
    # print(word_relevance_ratings)
    return [description_fuzzy_hmni_synonym_rating, tags_frequency_dict]

def result_relevance_calculator(tags, description):
    description = text_cleaner(description)
    
    tags = [tag.lower() for tag in tags]
    # print(tags)
    # print(description)
    
    relevance_rating_data = relevance_rater(tags, description) # returns relevance rating and dictionary of prominent tags as keys and frequency as values

    return relevance_rating_data

def related_words_calculator(word_1, word_2):
    print()

# print(result_relevance_calculator(["exam", "boobs", "favourite"], "This is_. a test. What if tits are the best things in the world?"))