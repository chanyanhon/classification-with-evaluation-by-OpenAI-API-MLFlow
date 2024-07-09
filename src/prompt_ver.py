
#! /usr/bin/env python

# second batch 
# ride on v3 which have consistent label output & best perforamnce)
# v3
def prompt_v3(input):
    prompt = f"""
    Perform the following actions on the given text delimited by \
    triple backticks:
    - analyse and report the sentiment in strictly a single word \
    out of [Positive, Negative, Neutral].

    Text to analyse: ```{input}```
    """
    return prompt

# v3.1 
def prompt_v3_1(input):
    prompt = f"""
    Perform the following actions on the given text delimited by \
    triple backticks:
    - Below is the data from Reddit discussion forum
    - analyse and report the sentiment in strictly a single word \
    out of [Positive, Negative, Neutral].

    Text to analyse: ```{input}```
    """
    return prompt

# v3.2
# weak on recall metrics on positive labelled  
# GPT: write a prompt template that can classify sentiment into [Postive, Negative, Neutral]
# v3.2 > v3.0 > v3.1
def prompt_v3_2(input):
    prompt = f"""
    Text: ```{input}```

    Options:
    - Positive
    - Negative
    - Neutral

    Instructions: Determine the sentiment of the text and choose the appropriate option that best represents its sentiment.

    """
    return prompt
