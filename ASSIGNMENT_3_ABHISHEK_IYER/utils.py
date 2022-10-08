from os import listdir
from os.path import isfile, join
import operator
from nltk.tokenize import sent_tokenize, word_tokenize

def get_paths(input_folder):
    return [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

def get_basic_stats(txt_path):
    with open(txt_path,encoding='utf-8') as f:
        text = f.read()
    stats = {}
    sentences = sent_tokenize(text)
    stats['num_sents'] = len(sentences)
    tokens = []
    for sent in sentences:
        tokens.extend(word_tokenize(sent))
    
    stats['num_tokens'] = len(tokens)
    stats['vocab_size'] = len(set(tokens))
    
    if "HuckFinn" in txt_path:
        stats['num_chapters_or_acts'] = text.count('CHAPTER')
    elif "AnnaKarenina" in txt_path:
        stats['num_chapters_or_acts'] = text.count('Chapter ')
    elif "Macbeth" in txt_path:
        stats['num_chapters_or_acts'] = text.count('ACT')
    counts = {}
    for token in set(tokens):
        counts[token] = tokens.count(token)
    stats['top_30_tokens'] = [token_freq[0] for token_freq in sorted(counts.items(), key=operator.itemgetter(1),reverse=True)][:30]
    return stats