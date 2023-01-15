from io import open
import pandas as pd
import json
import ast
import os

from data.data import POS_TAGS_TEXT

DATA_PATH = os.path.join(os.getcwd(),
                         os.path.join("data", "opencorpora_all.csv"))

OUTPUT_DIR = os.path.join(os.getcwd(),
                          os.path.join("data", "lemmas.json"))


class Lemmatizator():
    def __init__(self):
        # Here we save dict
        self.word_lemma_dict = {}
        self.len = 0
        pass

    # Create dict from table
    def load_corpus(self, data_path=DATA_PATH, encoding='utf-8', delimiter=","):
        # Load data from table
        df = pd.read_csv(data_path, encoding=encoding, delimiter=delimiter)
        # Extract columns
        sentences = df['sentence']
        tags = df['pos']
        lemmas = df['lemmas']

        for sent_idx, sentence in enumerate(sentences):
            for token_idx, token in enumerate(ast.literal_eval(sentence)):
                tag = ast.literal_eval(tags[sent_idx])[token_idx]
                if tag in POS_TAGS_TEXT:
                    # Change ё to е
                    form = token.lower().replace('Ё', 'Е').replace('ё', 'е')
                    lemma = ast.literal_eval(lemmas[sent_idx])[token_idx].lower()
                    # if lemma != form:
                    # If ok - add
                    if form not in self.word_lemma_dict:
                        self.word_lemma_dict[form] = lemma

        self.len = len(self.word_lemma_dict)

    # Save to json
    def save_to_json(self, data_path=OUTPUT_DIR):
        with open(data_path, "w", encoding='utf8') as fp:
            json.dump(self.word_lemma_dict, fp, ensure_ascii=False)
        print('saved')

    # Read from json
    def read_from_json(self, data_path=OUTPUT_DIR):
        with open(data_path, "r", encoding='utf8') as fp:
            # Load
            self.word_lemma_dict = json.load(fp)
        self.len = len(self.word_lemma_dict)
        print('loaded')

    # Search
    def lemmatize(self, word):
        if word in self.word_lemma_dict:
            return self.word_lemma_dict[word]
        return word

# lemmatizator = Lemmatizator()
# lemmatizator.load_corpus()
# lemmatizator.save_to_json()
