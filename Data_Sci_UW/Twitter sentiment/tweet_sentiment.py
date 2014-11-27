import sys
import json



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
        if word in scores['word']:
           score += scores['word'][word]
    
    for phrase, phrase_score in scores['phrase'].iteritems():
        if phrase in text:
           score += phrase_score
           for word_in_phrase in phrase.split(' '):
              if word_in_phrase in scores['word']:
                 score -= scores['word'][word_in_phrase]
    return score


def senti_score(outfile, term_score):
    for line in outfile:
        tweet = json.loads(line)
        if not 'text' in tweet:
             print 0
        else:
             print '%d' % cal_score(tweet['text'], term_score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #lines(sent_file)
    #lines(tweet_file)

    afinnfile = sent_file.readlines()
    outfile = tweet_file.readlines()

    term_score = parse(afinnfile)
    senti_score(outfile, term_score)

  

if __name__ == '__main__':
    main()
