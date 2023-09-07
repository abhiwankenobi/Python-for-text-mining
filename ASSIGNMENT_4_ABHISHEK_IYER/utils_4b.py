from lxml import etree as et
import nltk
from datetime import datetime


def load_root(path):
    tree = et.parse(path)
    root = tree.getroot()
    return root


def get_talks(root):
    talks = root.findall('file')
    return talks


def find_length(input, length='longest'): 
    titles, ids, length_of_talks,indexs = [],[],[],[]
    for talk in input:
        content = talk.find('content')
        words = nltk.word_tokenize(content.text)
        length_of_talks.append(len(words))
    mean_word_count = sum(length_of_talks)/len(length_of_talks)
    if length=='shortest':
        count = min(length_of_talks)
    else:
        count = max(length_of_talks)
    for i, c in enumerate(length_of_talks):
        if c == count:
            indexs.append(i)   
    for index in indexs:
        title = input[index].find('head').find('title')
        titles.append(title)
        id = input[index].find('head').find('talkid')
        ids.append(id)
    return titles, ids, mean_word_count, count
    
    
def find_date(input, date='latest'):
    calenders,indexs,titles,ids = [],[],[],[]
    for talk in input:
        calender = talk.find('head').find('date').text
        calender = datetime.strptime(calender, '%Y/%m/%d')
        calenders.append(calender)
    if date=='latest':
        calender = max(calenders)
    else:
        calender = min(calender)
    for i, x in enumerate(calenders):
        if x == calender:
            indexs.append(i)
    for index in indexs:
        title = input[index].find('head').find('title')
        titles.append(title)
        id = input[index].find('head').find('talkid')
        ids.append(id)
    return titles, ids, datetime.strftime(calender, '%Y/%m/%d')
    

def find_speaker(input):
    output = {}
    for talk in input:
        speaker = talk.find('head').find('speaker').text
        if speaker in output:
            output[speaker].append((talk.find('head').find('title').text, talk.find('head').find('talkid').text))
        else:
            output[speaker] = [(talk.find('head').find('title').text, talk.find('head').find('talkid').text)]    
    return output


