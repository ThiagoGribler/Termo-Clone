def word():
    from random import randint

    wordlist = ['adieu', 'odium', 'shade', 'resin', 'alert', 'haunt', 'orate', 'media', 'blind', 'route',
                'audio', 'pause', 'alien', 'canoe', 'plane', 'rouse', 'fraud', 'atone', 'raise', 'minor',
                'spate', 'odium', 'vapid', 'stint', 'augur', 'banal', 'assay', 'pique', 'berth', 'canon',
                'prate', 'plumb', 'taper', 'blase', 'fusty', 'preen', 'antic', 'beget', 'harry', 'clout']
    answear = wordlist[randint(0, len(wordlist))]
    return answear

def contains_number(string):
    return any(char.isdigit() for char in string)