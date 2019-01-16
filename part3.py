'''
Counting and Comparing
'''


from nltk.corpus import stopwords
from collections import Counter
from nltk.collocations import BigramCollocationFinder
import matplotlib.pyplot as plt
import string


word_output = open('word_tokenize.txt', 'r')
words = word_output.read()
word_list = words.split()

# Print uniques types
list_of_tokens = list(Counter(word_list).values())
print("Answer 1 : All unique unigram tokens",len(list_of_tokens))

# Print number of unique tokens
print("Answer 2 : All unigram tokens",len(word_list))

# Plot rank frequency
x = [i for i in range(1, len(list_of_tokens) + 1)]
y = list(reversed(sorted(list_of_tokens)))

plt.xscale('log')
plt.yscale('log')
plt.title('Zipf Law - Rank Frequency Plot')
plt.xlabel('Frequency')
plt.ylabel('Rank')
plt.plot(x, y, color='red')
plt.show()

# Print most common 20 words
print("Answer 3 : Twenty Most common words")
for key,item in Counter(word_list).most_common(20):
    print(key)

# Remove punctuation frm stopwords
stop_words = ' '.join(stopwords.words('english'))
punct_set = set(string.punctuation)
sent = ""
# Remove stop words from words list
for sw in stop_words:
    if sw not in punct_set:
        sent = sent + sw
sent = sent.upper().split()

filtered_sentence = []
for word in word_list:
    if not word in sent:
        filtered_sentence.append(word)

print("Number of tokens before removing stopwords", len(word_list))
print("Answer 4 : Removing stopwords",len(filtered_sentence))

print("Answer 5 : Twenty Most common words after stopwords")
for key,item in Counter(filtered_sentence).most_common(20):
    print(key)

#calculate bigram frequency count

finder = BigramCollocationFinder.from_words(word_list)

# calculate unigram probabilies
unigram_prob = {}
unigram_freq = dict(Counter(word_list).items())

for u_k, u_v in Counter(word_list).items():
    unigram_prob[u_k] = u_v/len(word_list)

# calculate bigram probabilities
bigram_prob = {}
finder = BigramCollocationFinder.from_words(word_list)
bigram_freq = dict(finder.ngram_fd.items())
for b_k, b_v in finder.ngram_fd.items():
    bigram_prob[b_k] = b_v/unigram_prob[b_k[0]]

# calculate pmi values
pmi_values = {}
for b_k, b_v in finder.ngram_fd.items():
    pmi_values[b_k] = b_v/(unigram_prob[b_k[0]] * unigram_prob[b_k[1]])

# Computer bigram probabilities and pmi values after threshold
bigram_threshold = {}
for thr_k , thr_v in finder.ngram_fd.items():
    if int(thr_v) > 100:
        bigram_threshold[thr_k] = bigram_prob[thr_k]

pmi_threshold = {}
for p_k, p_v in bigram_threshold.items():
    pmi_threshold[p_k] = p_v/(unigram_prob[p_k[0]] * unigram_prob[p_k[1]])

# Display first 10 outputs: PMI Values, Frequency Count of bigram, Frequency Count of unigram
counter = 0
threshold_data = [(key, pmi_threshold[key]) for key in sorted(pmi_threshold, key=pmi_threshold.get, reverse=True)]
for key,value in threshold_data:
    counter = counter + 1
    if counter == 11:
        break
    print(key, "=", value, "\t\t", key, '=', bigram_freq[key], '\t', key[0], '=', unigram_freq[key[0]], " ", key[1], "=", unigram_freq[key[1]])