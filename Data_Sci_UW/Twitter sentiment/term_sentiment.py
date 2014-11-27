import sys
import json


all_terms = {}


def lines(fp):
    print str(len(fp.readlines()))

def parse(afinnfile):

    scores = {'word': {}, 'phrase': {} } # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        if ' ' in term:
            scores['phrase'][term] = int(score)  # Convert the score to an integer.
        else:
            scores['word'][term] = int(score)
    return scores

def cal_score(text, scores):
    score = 0
    for word in text.split(' '):
        word = word.lower()
        if word in scores['word']:
           score += scores['word'][word]
    
    for phrase, phrase_score in scores['phrase'].iteritems():
        if phrase in text:
           score += phrase_score
           for word_in_phrase in phrase.split(' '):
              if word_in_phrase in scores['word']:
                 score -= scores['word'][word_in_phrase]
    return score


def scan_score(text, scores):
    text = repr(text)
    score = cal_score(text, scores)
    for word in text.split(' '):
        word = word.lower()
        if not word or word in scores['word']:
            continue
        elif not word in all_terms:
            all_terms[word] = {}
            all_terms[word]['count'] = 1.0
            all_terms[word]['value'] = float(score)
        else:
            all_terms[word]['count'] += 1.0
            all_terms[word]['value'] += float(score)
    
    return all_terms




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #lines(sent_file)
    #lines(tweet_file)

    afinnfile = sent_file.readlines()
    outfile = tweet_file.readlines()

    scores = parse(afinnfile)
    for line in outfile:
        tweet = json.loads(line)
        if 'text' in tweet:
            all_terms = scan_score (tweet['text'], scores)
    
    for term, score in all_terms.iteritems():
         print '%s %.3f' % (term, score['value'] / score['count'])

if __name__ == '__main__':
    main()
