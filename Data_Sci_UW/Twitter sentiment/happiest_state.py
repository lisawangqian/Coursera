import sys
import json



def parse(afinnfile):

    scores = {'word': {}, 'phrase': {} } # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        if ' ' in term:
            scores['phrase'][term] = int(score)  # Convert the score to an integer.
        else:
            scores['word'][term] = int(score)
    return scores

def cal_score(tweet, scores):
    global score
    score = 0

    if not "text" in tweet:
        return 0
    
    text = repr(tweet['text'])

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


def get_state(tweet, scores):
    if 'place' in tweet and tweet['place'] is not None:
        place = tweet['place']
        if place["country_code"] == "US" and place["place_type"] == "city":
            return place['full_name'][-2:]
    
    return ""




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    

    afinnfile = sent_file.readlines()
    outfile = tweet_file.readlines()

    scores = parse(afinnfile)
    states = {}
    for line in outfile:
        tweet = json.loads(line)
        state = get_state(tweet, scores)
        if not state == "":
            score = cal_score(tweet, scores)
            if not state in states:
                      states[state]=0
            states[state] += score
    
    state_max = ""
    score_max = 0
    for state in states:
        score = states[state]
        if score > score_max:
           score_max = score
           state_max = state
    print state_max
        

if __name__ == '__main__':
    main()
