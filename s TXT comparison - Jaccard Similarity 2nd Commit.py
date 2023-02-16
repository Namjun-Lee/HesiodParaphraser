import numpy as np
import spacy 


sent1 = "The Black Lives Matter (BLM) movement is a social and political movement that advocates for the rights and equality of Black individuals. The movement began in 2013 after the acquittal of Trayvon Martin's killer and gained momentum in the wake of police killings of Black Americans such as Michael Brown, Tamir Rice, and Freddie Gray. BLM protests have taken place across the United States and around the world, calling for an end to systemic racism and police brutality, as well as for economic and political justice for Black people. The movement has also pushed for reforms in areas such as education, housing, and healthcare. In addition to protests and demonstrations, BLM activists have also used social media, art, and other forms of cultural expression to raise awareness about the movement's goals and message."
sent2 = "The Black Lives Matter movement aims to promote the rights and equality of Black individuals by working to end systemic racism, police brutality and fighting for economic and political justice. It began in 2013 and gained momentum following the acquittal of Trayvon Martin's killer and the deaths of other Black Americans by police. Activists use various methods such as protests, social media, art and cultural expression to bring attention to the cause and also call for reforms in areas such as education, housing, and healthcare."
tokens1 = [t.lower() for t in sent1.split(sent1)]
tokens2 = [t.lower() for t in sent2.split(sent2)]

set1 = set(tokens1)
set2 = set(tokens2)
set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
print(set_intersection)
print(set.union)

print("Jaccard Coefficient: {}".format(len(set_intersection)/len(set_union)))


# load a spacy model
nlp_en = spacy.load('en_core_web_sm')

def preprocess(sentence):
    result = []
    tokens = nlp_en(sentence)
    for token in tokens:
        # remove determiners and punctuation or spaces 
        if token.pos_ in ['PUNT', 'SPACE', 'DET']:
            continue 
        else:
            # the lemma of pronouse is stored as '-PRON-' in spacy; we want the actual pronoun 
            if token.pos_ == 'PRON':
                result.append(token.text.lower())
            else:
                result.append(token.lemma_)
    return result

print('preprocessed sent1: {}'.format(preprocess(sent1)))
print('preprocessed sent1: {}'.format(preprocess(sent2)))

def jaccard_coefficient(sent1, sent2, preprocessor = preprocess):
    tokens1 = preprocessor(sent1)
    tokens2 = preprocessor(sent2)
    set1 = set(tokens1)
    set2 = set(tokens2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection)/len(union)

print(jaccard_coefficient(sent1, sent2))






