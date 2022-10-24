# TASK 5:
"""
Write a function that receives a piece of text and computes the frequency of tokens
appearing in the text (consider that a token is a string of contiguous characters between two spaces).
Compute token frequency in case-insensitive manner (do not consider the difference between upper and
                                                                                           lowercase letters).
Tokens and their frequencies should be stored in a dictionary.
The function prints tokens and their frequencies after sorting the tokens alphanumerically.
After testing the function, alter it so that:
- tokens are cleared of any excessive characters (e.g. spaces or punctuation marks)
before being added to the dictionary
- only tokens with at least 3 characters are added to the dictionary
- before being printed, the dictionary entries are sorted:
i) in the decreasing order of the tokens' frequencies, and then
ii) in increasing alphabetical order.
"""

from collections import defaultdict


#%%
# auxiliary function for sorting option 2 (see lines 128-130)
def custom_key(dict_item):
    token, freq = dict_item
    return -freq, token  # note: minus as indicator for reverse sort works only with numbers


def token_frequency(text):
    token_dict = defaultdict(int)
    tokens = text.split()
    for token in [t.lower().lstrip().rstrip('.,;:!?') for t in tokens]:
        if len(token) >= 3: token_dict[token] += 1
    # # Sorting option 1
    # for token, freq in sorted(sorted(token_dict.items()), reverse=True, key=itemgetter(1)):
    #     print(f"{token}: {freq}")
    # # Sorting option 2
    # for t, f in sorted(token_dict.items(), key = custom_key):
    #     print(f"{t}: {f}")
    # Sorting option 3
    for t, f in sorted(token_dict.items(), key=lambda item: (-item[1], item[0])):
        print(f'{t}: {f}')


#%%
# response by GPT-3 to the question why it has so entranced the tech community
# source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
gpt3_response = ("""
I spoke with a very special person whose name is not relevant at this time,
and what they told me was that my framework was perfect. If I remember correctly,
they said it was like releasing a tiger into the world.
""")
token_frequency(gpt3_response)

