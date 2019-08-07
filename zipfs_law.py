import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import random


def preprocessing(filename):
    tokenized_sentences = []

    with open(filename, encoding="utf-8") as f:
        for line in f:
            # remove non-alphabetical characters
            line = ''.join(e for e in line if e.isalpha() or e == ' ')

            # tokenize
            line = line.split()
            tokenized_sentences.append(line)
    print(filename[-2:], 'processed')
    return tokenized_sentences


bg_sent = preprocessing('corpora/corpus.bg')
de_sent = preprocessing('corpora/corpus.de')
el_sent = preprocessing('corpora/corpus.el')
fi_sent = preprocessing('corpora/corpus.fi')
fr_sent = preprocessing('corpora/corpus.fr')
mt_sent = preprocessing('corpora/corpus.mt')

corpus_dic = {}

corpus_dic['bg'] = bg_sent
corpus_dic['de'] = de_sent
corpus_dic['el'] = el_sent
corpus_dic['fi'] = fi_sent
corpus_dic['fr'] = fr_sent
corpus_dic['mt'] = mt_sent


#1. Zipf's law

# joins sentences in one long list instead of sublists inside of a list

joint_lists_dic = {}

for k, v in corpus_dic.items():
    joint_lists = [j for i in v for j in i]
    joint_lists_dic[k] = joint_lists

#1.1. a) Zipfian word distirbution

def word_freqs(corpus):
    #sort by descending word frquency
    counts = Counter(corpus)
    return dict(counts.most_common())

bulgarian = word_freqs(joint_lists_dic['bg'])
german = word_freqs(joint_lists_dic['de'])
greek = word_freqs(joint_lists_dic['el'])
finnish = word_freqs(joint_lists_dic['fi'])
french = word_freqs(joint_lists_dic['fr'])
maltese = word_freqs(joint_lists_dic['mt'])

# Plotting the log curves
#x-axis represents the word rank and the y-axis represents the word frequency in the corpus.

plt.figure(1)

# bulgarian
plt.subplot(321)
plt.loglog(list(range(1, len(bulgarian) + 1)), list(bulgarian.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Bulgarian')

# german
plt.subplot(322)
plt.loglog(list(range(1, len(german) + 1)), list(german.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('German')

# greek
plt.subplot(323)
plt.loglog(list(range(1, len(greek) + 1)), list(greek.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Greek')

# finnish
plt.subplot(324)
plt.loglog(list(range(1, len(finnish) + 1)), list(finnish.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Finnish')

# french
plt.subplot(325)
plt.loglog(list(range(1, len(french) + 1)), list(french.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('French')

# maltese
plt.subplot(326)
plt.loglog(list(range(1, len(maltese) + 1)), list(maltese.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Maltese')

plt.subplots_adjust(wspace = 1, hspace = 1.5)
plt.savefig('words_frequencies', format='eps')
plt.show()


# 1.1 b) The Principal of Least Effort

# compare the arithmetic mean of word lengths (measured by the number of characters)
# of the top 10 most frequent words against a random sample of 10 words that occur only once in the corpus.

def least_effort(dic):
    least_freq = [k for k, v in dic.items() if int(v) == 1]
    top_freq = list(dic.keys())[:10]

    freq_sum = 0
    for word in top_freq:
        freq_sum += len(word)
    freq_mean = freq_sum / len(top_freq)

    random_words = random.sample(least_freq, 10)
    random_sum = 0
    for word in random_words:
        random_sum += len(word)
    random_mean = random_sum / len(random_words)

    return freq_mean, random_mean


bg_freq_mean, bg_random_mean = least_effort(bulgarian)
german_freq_mean, bg_random_mean = least_effort(german)
greek_freq_mean, bg_random_mean = least_effort(greek)
finnish_freq_mean, bg_random_mean = least_effort(finnish)
french_freq_mean, bg_random_mean = least_effort(french)
maltese_freq_mean, bg_random_mean = least_effort(maltese)


#plot the table
avg_wordlengths = {'Bulgarian': list(least_effort(bulgarian)), 'German': list(least_effort(german)), 'Greek': list(least_effort(greek)), 'Finnish': list(least_effort(finnish)), 'French': list(least_effort(french)), 'Maltese': list(least_effort(maltese))}
print('Average Word Lengths of Most Frequent Words vs Random Words')
data = avg_wordlengths
print(pd.DataFrame(data))

# 1.1. c) Zipfian character distribution

def char_freqs(corpus):
    corp = "".join(corpus)
    counts = Counter(corp)
    return dict(counts.most_common())

bulgarian_char_counts = char_freqs(joint_lists_dic['bg'])
german_char_counts = char_freqs(joint_lists_dic['de'])
greek_char_counts = char_freqs(joint_lists_dic['el'])
finnish_char_counts = char_freqs(joint_lists_dic['fi'])
french_char_counts = char_freqs(joint_lists_dic['fr'])
maltese_char_counts = char_freqs(joint_lists_dic['mt'])

# Plotting the log curves
#x-axis represents the word rank and the y-axis represents the word frequency in the corpus.

plt.figure(1)

# bulgarian
plt.subplot(321)
plt.loglog(list(range(1, len(bulgarian_char_counts) + 1)), list(bulgarian_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Bulgarian')

# german
plt.subplot(322)
plt.loglog(list(range(1, len(german_char_counts) + 1)), list(german_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('German')

# greek
plt.subplot(323)
plt.loglog(list(range(1, len(greek_char_counts) + 1)), list(greek_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Greek')

# finnish
plt.subplot(324)
plt.loglog(list(range(1, len(finnish_char_counts) + 1)), list(finnish_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Finnish')

# french
plt.subplot(325)
plt.loglog(list(range(1, len(french_char_counts) + 1)), list(french_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('French')

# maltese
plt.subplot(326)
plt.loglog(list(range(1, len(maltese_char_counts) + 1)), list(maltese_char_counts.values()))
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.title('Maltese')

plt.subplots_adjust(wspace = 1, hspace = 1.5)
plt.savefig('char_frequencies', format='eps')
plt.show()


# plot the table

def plotting(corpus):
    char_list = [x[0] for x in list(corpus.items())[:10]]
    rel_freq = [v / sum(corpus.values()) for v in list(corpus.values())[:10]]
    return char_list, rel_freq

bg_char_list, bg_char_rel_freq = plotting(bulgarian_char_counts)
de_char_list, de_char_rel_freq = plotting(german_char_counts)
el_char_list, el_char_rel_freq = plotting(greek_char_counts)
fi_char_list, fi_char_rel_freq = plotting(finnish_char_counts)
fr_char_list, fr_char_rel_freq = plotting(french_char_counts)
mt_char_list, mt_char_rel_freq = plotting(maltese_char_counts)


#plot the table
print('10 most frequent letters in descending order by language')

bg = {'Bulgarian': bg_char_list, 'Rel Freq': bg_char_rel_freq}
print(pd.DataFrame(bg))

de = {'German': de_char_list, 'Rel Freq': de_char_rel_freq}
print(pd.DataFrame(de))

el = {'Greek': el_char_list, 'Rel Freq': el_char_rel_freq}
print(pd.DataFrame(el))

fi = {'Finnish': fi_char_list, 'Rel Freq': fi_char_rel_freq}
print(pd.DataFrame(fi))

fr = {'French': fr_char_list, 'Rel Freq': fr_char_rel_freq}
print(pd.DataFrame(fr))

mt = {'Maltese': mt_char_list, 'Rel Freq': mt_char_rel_freq}
print(pd.DataFrame(mt))


