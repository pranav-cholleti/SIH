
import nltk
import pandas as pd
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
qsns=["Whether your skin remains oily throughout the year in \
comparison to others?",\
"Are your body-hairs & skin shiny, even when no oil or moisturizer is used?",\
'Are you considered attractive among your friends?',\
'Do  even  mild  or  trivial  injuries  on  your  body  make you upset?',\
"Among  your  family  members,  is  your  complexion\
considered fairer?"]
weight=[120,120,40,40,40]
answer=['p','p','p','p','n']
sid=SentimentIntensityAnalyzer()
vata_score=0

i=-1
name=""
def get_response(user_input):
    if(i==-1):
        i+=1
        name=user_input
        s=f"Hi {name}"
        return json.dumps(s)

    elif(i==len(qsns)):
       i+=1
       return json.dumps(vata_score)
    else:
        i+=1
        ans=user_input
        ss=sid.polarity_scores(ans)
        if (answer[i]=='p'):
            vata_score=vata_score+ss['pos']*weight[i]
        else:
            vata_score=vata_score+ss['neg']*weight[i]
        
        return json.dumps(qsns[i-1])
    

