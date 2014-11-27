import sys
import json

all_terms = {}
total = 0

def scan_word(text):
    global total
    text = repr(text)
    
    for word in text.split(' '):
        word = word.lower()
        if not word: 
            continue
        elif not word in all_terms:
            all_terms[word] = {}
            all_terms[word]['count'] = 1.0
            total += 1.0
        else:
            all_terms[word]['count'] += 1.0
            total += 1.0
    
    return all_terms




def main():
    
    global total
    tweet_file = open(sys.argv[1])
    
    outfile = tweet_file.readlines()

    
    for line in outfile:
        tweet = json.loads(line)
        if 'text' in tweet:
            all_terms = scan_word(tweet['text'])
    
    for term, con in all_terms.iteritems():
         print '%s %.3f' % (term, con['count'] / total)

if __name__ == '__main__':
    main()
