from pprint import pprint
from utils_4b import *


path = '../Data/ted-talks/XML_releases/xml/ted_en-20160408.xml'
root = load_root(path)
talks = get_talks(root)

length='longest'
date='latest'


def main():
    titles, ids, mean_word_count, count = find_length(talks)
    print(f"The total number of talks given in english language are : {len(talks)}")  
    print(f"\nThe lenth of the talk is : {count}")
    for i in range(len(titles)):
        print(type(titles))
        print(f"The {length} talk is : {titles[i].text} and the talk id for the same is : {ids[i].text}")
    print(f"The mean word count is : {mean_word_count}")
    
    titles, ids, calender_date = find_date(talks)
    print(f"\nThe date of the talk is: {calender_date}")
    for i in range(len(titles)):
        print(f"{date} talk: {titles[i].text} (id: {ids[i].text})")

    speaker_data = find_speaker(talks)
    print("The following is the collection of speakers and their talks:")
    pprint(speaker_data)


if __name__ == "__main__":
    main()
