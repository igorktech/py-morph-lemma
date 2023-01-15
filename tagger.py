from lemmatizator import Lemmatizator
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
from data.data import POS_TAGS
import os

# Model path / name
# DATA_PATH = os.path.join(os.getcwd(),
#                          os.path.join("data", "morph_tagger"))

# My model name:
DATA_PATH = "igorktech/rubert-base-morph-tagging"

TOKENIZER = AutoTokenizer.from_pretrained(DATA_PATH)
MODEL = AutoModelForTokenClassification.from_pretrained(DATA_PATH, num_labels=len(POS_TAGS))


# Extracting tags
class Tagger():
    def __init__(self, model=MODEL, tokenizer=TOKENIZER):
        self.model = model
        self.tokenizer = tokenizer
        self.classifier = pipeline("token-classification", model=MODEL, tokenizer=TOKENIZER)
        self.lemmatizator = Lemmatizator()
        self.lemmatizator.read_from_json()

    #  API huggingface
    def get_tags(self, text):
        entities = []

        if isinstance(text[0], str):
            # For pipeline function join tokens
            string = " ".join([word for word in text])
            # Extrac entities
            i = 0
            for entity in self.classifier(string):
                if entity['word'][:2] == "##":
                    # Fix ## split
                    entities[i - 1][text[i - 1]]['lemma'] = self.lemmatizator.lemmatize(text[i - 1].lower())
                    i = i - 1

                else:
                    entities.append({text[i]: {'morph': entity['entity'],
                                               'lemma': self.lemmatizator.lemmatize(entity['word'].lower())}})
                i = i + 1
            return entities

        if isinstance(text[0], list):

            for sentence in text:
                string = " ".join([word for word in sentence])
                ent = []
                i = 0
                for entity in self.classifier(string):

                    if entity['word'][:2] == "##":

                        # Fix ## split
                        ent[i - 1][sentence[i - 1]]['lemma'] = self.lemmatizator.lemmatize(sentence[i - 1].lower())
                        i = i - 1

                    else:
                        ent.append({sentence[i]: {'morph': entity['entity'],
                                                  'lemma': self.lemmatizator.lemmatize(entity['word'].lower())}})
                    i = i + 1
                entities.append(ent)
            return entities

# print(Tagger().get_tags(["Привет", "как", "поживаешь"]))
# print(Tagger().get([["Привет", "как", "поживаешь"], ["Привет", "как", "дела"]]))
