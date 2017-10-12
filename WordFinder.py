#TextMining Project: KeyWord Search
#This script will search through a given paper or papers for the occurences of several keywords
#it will then tell the user the most relevant paper based on the maximum number of occurences of a keyword or keywords
#Claire Kincaid
#April 18, 2016 (revised for MiniProject 5)
import doctest
import string
import random
import math
from random import randint
import requests



Knight_full_text = requests.get('http://www.gutenberg.org/files/55708/55708-8.txt').text
America_full_text = requests.get('http://www.gutenberg.org/files/55713/55713-0.txt').text
Wolf_full_text = requests.get('http://www.gutenberg.org/files/55720/55720-8.txt').text
#first remove all punctuation from the texts
s1 = Knight_full_text # do you just put the whole text here?
#out1 = s1.translate(string.punctuation)
s2 = America_full_text # Sample string
#out2 = s2.translate(string.punctuation)
s3 = Wolf_full_text
exclude = set(string.punctuation)
s1 = ''.join(ch for ch in s1 if ch not in exclude)
s2 = ''.join(ch for ch in s2 if ch not in exclude)
s3 = ''.join(ch for ch in s3 if ch not in exclude)

#make all letters lowercase
Knight_text = str.lower(s1)
America_text = str.lower(s2)
Wolf_text = str.lower(s3)
whole_text = Knight_text + America_text + Wolf_text
#print(whole_text)

word_list = whole_text.split(' ')

#make an index of all words in Herland & Crusoe
new_dict = {}
""" The following code creates a dictionary (new_dict) that contains all of the
words in both texts as keys and then the word that
follows the key word stored in a dictionary. If the word already exists in the
dictionary the code simply adds the following word in the list to the dictionary.
 """
for index,word in enumerate(word_list[:-1]):
     if word not in new_dict:
         new_dict[word] = [word_list[index + 1]]
     else:
         new_dict[word].append(word_list[index + 1])
#print(new_dict)

def quote(data,length_quote):
     """ This function generated a random sentence/quote from the dictionary
     created above. this code randomly chooses an index and then finds the key
     with that index in the dictionary and then randomly chooses a value of that
     key. That value is then added to a string and then becomes the next key.
     This process is repeted until the desired length of quote is reached.
     """
     new_string = ''
     num_words = 0
     x = random.choice(list(data.keys()))
     while num_words < length_quote:
         if num_words > 0:
             new_string += ' '
             #print(new_string)
         next_word = random.choice(data[x])
         new_string = new_string + next_word
         x = next_word
         num_words = num_words + 1
     new_string += '."'
     #print(new_string)
     return new_string



Knight_America_Wolf = quote(new_dict, 10000)
print(Knight_America_Wolf)



def make_data(data):
    """Takes a string, removes all punctuation, makes all letters lowercase and puts words of string into a list
    >>> make_data("I'm hilarious")
    ['im', 'hilarious']
    """
    listdata = data.split(data)
    return listdata

def word_count(data):
    """Takes a string, uses make_data to turn it into an analyzable list
    creates a dictionary that counts all words within that list
    >>> word_count("I'm hilarious")
    {'im': 1, 'hilarious': 1}
    """
    words = dict()
    for word in make_data(data):
        words[word] = words.get(word, 0) + 1
    return words

def word_find(data, keyword):
    """ Takes a string, uses word_count to create dict counting all words in string
    returns frequency of word specified as a keyword
    >>> word_find("I'm hilarious", "hilarious")
    1
    """
    hist = word_count(data)
    return hist.get(keyword, 0)

def multi_keywords_find(data, keywords):
    """ Takes a string data and a list of keywords and returns dict w/ word count of those words
    >>> multi_keywords_find("I'm hilarious", ['im', 'hilarious'])
    {'im': 1, 'hilarious': 1}
    """
    all_keywords = dict()
    for i in keywords:
        all_keywords[i] = (word_find(data, i))
    return all_keywords

def multi_paper_word_find(data, keyword):
    """takes string keyword, uses word_find to find the occurences of keyword in three datasets in a list
    returns dictionary of papers in order of highest occurences of word to lowest"""
    data_keyword = dict()
    for i in data:
        data_keyword[i] = word_find(i, keyword)
    return data_keyword

def relevance(data, keyword):
    data_keyword = multi_paper_word_find(data, keyword)
    most_relevant = max(data_keyword.get(data, 0))
    return most_relevant


keywords = ['kingdom', 'wild', 'cold', 'learning', 'war', 'violence', 'journey', 'love','hero','freedom','morning','people','interested','the']


print (multi_keywords_find(Knight_America_Wolf, keywords))
print (relevance(Knight_America_Wolf, keywords[1]))
