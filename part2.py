'''
Read sentences, remove punctuations and word tokenization
'''
import nltk
import string
input_file = open('deserialized.txt', 'r')
sentence_file = open('sent_tokenize.txt', 'w')
word_output = open('word_tokenize.txt', 'w')

punct_set = set(string.punctuation)

raw_sentences = input_file.read()
# sentence tokenize
sentences = nltk.sent_tokenize(raw_sentences)

print("Number of Sentences:", len(nltk.sent_tokenize(raw_sentences)))

# Write sentences to the text file one below the other
print("\n\nTokenizing Sentences ...")
for single_sentence in sentences:
    full_sentence = ""
    for line in single_sentence.splitlines():
        full_sentence = full_sentence + line
        full_sentence = full_sentence + " "
    sentence_file.write(full_sentence)
print("Output of Sentence tokenization is in file sent_tokenize.txt")

# Read words and remove punctuation and write to word_tokenize.txt file
print("\n\nTokenizing Words.....")
with open('sent_tokenize.txt') as fp:
    for line in fp.readlines():
        punct_line = ''.join([c for c in line if c not in punct_set])
        word_output.write(' '.join(nltk.word_tokenize(punct_line.upper())))
print("Output of Word tokenization is in file word_tokenize.txt")


