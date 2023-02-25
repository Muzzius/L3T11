import spacy


def list_nlp(list1):
    """
    A function to pass a list of strings through a spaCy language model
    :param list1: A list of strings
    :return: The list with modeled strings
    """
    for index, sentence in enumerate(list1):
        nlp_sentence = nlp(sentence)
        list1[index] = nlp_sentence
        print(list1)
    return list1


nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The old man the boat",
    "The complex houses married and single soldiers and their families.",
    "British Left Waffles on Falklands.",
    "The cotton clothing is made of grows in Mississippi. ",
    "The Inuit can fish in their new factory in town."
]

# Use the list_nlp function to model the strings in the gardenpathSentences list
list_nlp(gardenpathSentences)

# Print the tokens for each string in the gardenpathSentences list
for sentence in gardenpathSentences:
    print([(w.text, w.pos_) for w in sentence])

# Print the entities for each string in the gardenpathSentences list
for sentence in gardenpathSentences:
    print([(w, w.label_, w.label) for w in sentence.ents])
