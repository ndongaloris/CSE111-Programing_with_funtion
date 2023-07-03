import random   

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words  = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = [ "drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    else:
        print("Cheese")
    verb = random.choice(verbs)
    return verb

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "adorable","adventurous","aggressive","agreeable","alert","alive","amused",
        "angry","annoyed","annoying","anxious","arrogant","ashamed","attractive",
        "average","awful","bad","beautiful","better","bewildered","black","bloody",
        "blue","blue-eyed"
    Return: a randomly chosen adjective.
    """
    adjectives = ["adorable","adventurous","aggressive","agreeable","alert","alive","amused",
                    "angry","annoyed","annoying","anxious","arrogant","ashamed","attractive",
                    "average","awful","bad","beautiful","better","bewildered","black","bloody",
                    "blue","blue-eyed"]
    adjective = random.choice(adjectives)
    return adjective

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "accordingly","additionally","also","anyway","besides","certainly","always",
        "usually","often","sometimes","rarely","tomorrow","tonight","yesterday",
        "now","well","fast","straight","hard","loudly","proudly","lots","somewhat",
        "barely","very","behind","above","nearby"
    Return: a randomly chosen adverb.
    """
    adverbs = ["accordingly","additionally","also","anyway","besides","certainly","always",
                "usually","often","sometimes","rarely","tomorrow","tonight","yesterday",
                "now","well","fast","straight","hard","loudly","proudly","lots","somewhat",
                "barely","very","behind","above","nearby"]
    adverb = random.choice(adverbs)
    return adverb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions  = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    get_preposition()
    get_determiner(quantity)
    get_noun(quantity)
    propositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
    return propositional_phrase

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()
    sentence = f"{determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} "\
               f"{determiner} {adjective} {noun} {prepositional_phrase_2}.".capitalize()
    return sentence

def main():
    i = 0 
    while i < 6: 
        quantities = [1,2]
        tenses = ["past", "present", "future"]
        quantity = random.choice(quantities)
        tense = random.choice(tenses)
        sentence = make_sentence(quantity, tense)
        print(sentence)
        i += 1
    return tense, quantity

main()