# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:40:20 2024

@author: marku
"""

"""
Write a function which count number of lines and number of words in a text. 
All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b)
 Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count 
number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

Read the countries_data.json data file in data directory, create a function that creates a list of 
the ten most populated countries

"""

#1 done
text_dir = '../data/obama_speech.txt'
def count_lines(text_dir):
    f = open(text_dir)
    lines = f.readlines()
    f.close()
    return(len(lines))

def count_words(text_dir):
    import re
    f = open(text_dir)
    text = f.read()
    
    all_words_list = re.findall(r'\w+', text,re.I) #\w one word character + one or more times

    f.close()

    return(len(all_words_list))

list_of_dirs = ['../data/' + i for i in ['obama_speech.txt','michelle_obama_speech.txt','donald_speech.txt','melina_trump_speech.txt']]
for i in list_of_dirs:
    print(f'{i[i.rfind('/')+1:]} has {count_words(i)} words and {count_lines(i)} lines!')


#2 & 3  Doesn't work. I don't know why. 
# import json
# file_dir = '../data/countries_data.json'

# with open(file_dir, 'w', encoding='utf-8') as f:
#     country_dict = json.loads(file_dir)
# f = open('../data/countries_data_long.json')
# data = json.load(f)


#%%

"""

    Extract all incoming email addresses as a list from the email_exchange_big.txt file.
    Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]

    Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
    Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
    Find the 10 most repeated words in the romeo_and_juliet.txt
    Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

 """
import re
text_dir = '../data/email_exchanges.txt'
def get_email(text_dir):
    email_ident = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    f = open(text_dir)
    text = f.read()
    all_emails_list = re.findall(email_ident, text,re.I) #\w one word character + one or more times
    
    all_emails_set = set(all_emails_list)
    f.close()
    return(all_emails_set)
 

text_dir = '../data/obama_speech.txt'
list_of_dirs = ['../data/' + i for i in ['obama_speech.txt','michelle_obama_speech.txt','donald_speech.txt','melina_trump_speech.txt']]

def find_most_common_words(text_dir, n):
    f = open(text_dir)
    text = f.read()
   
    all_words_list = re.findall(r'\w+', text,re.I) #\w one word character + one or more times
    all_words_set = set(all_words_list)
    
    all_words_count = [(all_words_list.count(j), j) for i,j in enumerate(all_words_set)]
    
    all_words_count.sort(reverse = True)  
    f.close()
    return(all_words_count[:n])


#6 done 
for i in list_of_dirs:
    print(find_most_common_words(i, 10))
    
    
#7 done
# check similarity between texts

text_dir_1 = '../data/michelle_obama_speech.txt'
text_dir_2 = '../data/melina_trump_speech.txt'

def clean_text(text):
    filter_str = r'[^A-Za-z0-9 \n]'
    filter_str2 = r'[â€]'
    filter_1_text = re.sub(filter_str + '|'+filter_str2, '', text)
    filter_2_text = re.sub( r'\n', ' ', filter_1_text)
    # filter_3_text = re.sub( r'\'', '', filter_2_text)
    return(filter_2_text)

def remove_support_words(text):
    stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    for pat in stop_words:
        text = re.sub(pat, ' ', text,re.I)
    return(text)

def clean_get_most_common(text_dir,n):
    # for j, text in enumerate([text_dir]):
        
    text = f = open(text_dir)
    text = f.read()
    f.close()
    filtered_text = clean_text(text)
    rem_word_text = remove_support_words(filtered_text)  
    
    all_words_list = re.findall(r'\w+', rem_word_text,re.I) #\w one word character + one or more times
    all_words_set = set(all_words_list)
    
    all_words_count = [(all_words_list.count(j), j) for i,j in enumerate(all_words_set)]
    
    all_words_count.sort(reverse = True)         
       
    # exec(f'cleaned_text_{j} = rem_word_text')    

    return(all_words_count[:n])

print(clean_get_most_common(text_dir_1,5))
print(clean_get_most_common(text_dir_2,5))
# could do more to compare the two text files


#8 done
find_most_common_words('../data/romeo_and_juliet.txt',10)

#9 done

import csv
with open('../data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    Java_count = 0
    Javascript_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
        if 'JavaScript' in str(row) or 'javascript' in str(row) or 'Javascript' in str(row):
            Javascript_count += 1
        if 'Java' in str(row) and not 'javascript' in str(row) and not 'Javascript' in str(row) and not 'JavaScript' in str(row):
            Java_count += 1

    print(f'Number of lines:  {line_count}')
    print(f'Number of Javascript:  {Javascript_count}')
    print(f'Number of Java:  {Java_count}')
    

