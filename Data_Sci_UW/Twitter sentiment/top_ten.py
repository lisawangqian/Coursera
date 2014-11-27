import sys
import json
import math


tags ={}


def get_hashtag(tweet):
    if 'entities' in tweet:
        hashtag = tweet['entities']['hashtags']
        return hashtag

def all_tag(tag):
    tag_text = tag['text']
    if not tag_text in tags:
       tags[tag_text] = {'text': tag_text, 'count':1}
    else:
       tags[tag_text]['count']+=1
    
    return tags

def find_top_ten(tag, tags, top_ten):
    s = 0
    e = 9
    if top_ten[e]['count'] > tag['count']:
        return top_ten
    count = tag['count']
    while not s == e:
        i = (s+e)/2
        c_cnt = top_ten[i]['count']
        if count > c_cnt:
            e = i
        else:
            s = i+1
     
    newlst = top_ten[0:s]
    newlst.append(tag)
    newlst.extend(top_ten[s:9])
    return newlst

def main():
    
    tweet_file = open(sys.argv[1])
    
    outfile = tweet_file.readlines()

    
    top_ten = []

    for line in outfile:
        tweet = json.loads(line)
        hash_tag = get_hashtag(tweet)
        
        if not hash_tag: 
           continue
        for tag in hash_tag:
           tags = all_tag(tag)
    
    for i in range(10):
         top_ten.append({'text':'', 'count':0})
    
    for key, tag in tags.iteritems():
          top_ten = find_top_ten(tag, tags, top_ten)
    for tag in top_ten:
         print tag['text'], tag["count"]

if __name__ == '__main__':
    main()
