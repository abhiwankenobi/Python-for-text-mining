import glob
from utils_4b import load_root, get_talks

def map_languages_to_paths():
    file_list = glob.glob("../Data/ted-talks/XML_releases/xml/*.xml")
    return {file.split("/")[-1].split("_")[-1].rsplit("-",1)[0]:file for file in file_list}

def find_coverage(path_dict, condition="most"):
    languages = []
    no_talks = []
    for language, path in path_dict.items():
        no_talks.append(len(get_talks(load_root(path))))
        languages.append(language)
    dic_language={}
    if condition=="most":
        for i, j in enumerate(no_talks):
            if j == max(no_talks):
                dic_language[languages[i]]=j
        return dic_language
    else:
        for i, j in enumerate(no_talks):
            if j == min(no_talks):
                dic_language[languages[i]]=j 

def get_id_title_dict(en_path):
    dic_id_title = {}
    for talk in get_talks(load_root(en_path)):
        dic_id_title[talk.find('head').find('talkid').text] = talk.find('head').find('title').text
    return dic_id_title

def Map_talks_to_languages(path_dict):
    talks_to_languages = {}
    for language, path in path_dict.items():
        for talk_id in [talk.find('head').find('talkid').text for talk in get_talks(load_root(path))]:
            if talk_id not in talks_to_languages:
                talks_to_languages[talk_id] = [language]
            elif language not in talks_to_languages[talk_id]:
                talks_to_languages[talk_id].append(language)
    return talks_to_languages

def map_nlang_to_talks(talk_id_to_languages):
    talk_ids, no_langs = [], []
    for talk_id in talk_id_to_languages:
        talk_ids.append(talk_id)
        no_langs.append(len(talk_id_to_languages[talk_id]))
    nlang_to_talks = {}
    for no_lang in no_langs:
        if no_lang not in nlang_to_talks:
            indexs = [index for index, nn_lang in enumerate(no_langs) if nn_lang==no_lang]
            nlang_to_talks[no_lang] = [talk_ids[index] for index in indexs]
    return nlang_to_talks

def find_top_coverage(path_dict, condition="most"):
    talks_to_languages = Map_talks_to_languages(path_dict)
    nlang_to_talks = map_nlang_to_talks(talks_to_languages)
    dic_id_title = get_id_title_dict(path_dict['en'])
    if condition=="most":
        talk_ids = nlang_to_talks[max(nlang_to_talks.keys())]
    else:
        talk_ids = nlang_to_talks[min(nlang_to_talks.keys())]
    return {dic_id_title[talk_id]:talks_to_languages[talk_id] for talk_id in talk_ids}

def main():
    path_dict = map_languages_to_paths()
    print(f"\n The mapping of languages to paths : {path_dict}")
    
    find_coverage_least = find_coverage(path_dict, condition="least")
    print(f"\n Least coverage: {find_coverage_least}")
    
    find_coverage_most = find_coverage(path_dict, condition="most")
    print(f"\n Most coverage: {find_coverage_most}")
    
    id_title_dict = get_id_title_dict(path_dict['en'])
    print(f"\n The id title dict for 'en': {id_title_dict}")
    
    talks_to_languages = Map_talks_to_languages(path_dict)
    print(f"\n The mapping of talks to languages: {talks_to_languages}")
    
    nlang_to_talks = map_nlang_to_talks(talks_to_languages)
    print(f"\n Mapping of no. of languages to talks: {nlang_to_talks}")

    top_coverage_most = find_top_coverage(path_dict, condition="most")
    print(f"\n Top most coverage: {top_coverage_most}")

    top_coverage_least = find_top_coverage(path_dict, condition="least")
    print(f"\n Top least coverage: {top_coverage_least}")


if __name__ == "__main__":
    main()

