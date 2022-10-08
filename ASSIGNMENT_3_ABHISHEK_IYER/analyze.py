from utils import get_paths
from utils import get_basic_stats

book_list = get_paths("Data/books") # changed the path from ../Data as I have included the Data folder 
                                           # with Books folder in the submission document 
print(book_list,"\n")

book2stats = {}

for book in book_list:
    stats = get_basic_stats("Data/books/" + book) # changed the path from ../Data as I have included the Data folder 
                                           # with Books folder in the submission document 
    print(stats)
    book2stats[book[:-4]] = stats
    with open(f"top_30_{book}", "w",encoding="utf-8") as f:
        f.write("\n".join(stats["top_30_tokens"]))
print("\n", 'book2stats')
print(book2stats,"\n")

stats2book_with_highest_value = {}
stats2book_with_highest_value['num_sents'] = max(book2stats.keys(), key=lambda x: book2stats[x]['num_sents'])
stats2book_with_highest_value['num_tokens'] = max(book2stats.keys(), key=lambda x: book2stats[x]['num_tokens'])
stats2book_with_highest_value['vocab_size '] = max(book2stats.keys(), key=lambda x: book2stats[x]['vocab_size'])
num_chapters_or_acts = {}

for book in book2stats:
    stat = book2stats[book].get('num_chapters_or_acts')
    if stat:
        num_chapters_or_acts[book] = stat
stats2book_with_highest_value['num_chapters_or_acts'] = max(num_chapters_or_acts, key=num_chapters_or_acts.get)

print("\n", "stats2book_with_highest_value")
print(stats2book_with_highest_value)
