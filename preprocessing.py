from tokenizer import Tokenizer

tokenizer = Tokenizer(pattern=r'\w+')


# Simple Preprocessing class
class Preprocessing:
    def __init__(self, tokenizer=tokenizer):
        self.tokenizer = tokenizer

    def tokenize(self, sentence):
        # проверяем тип
        if isinstance(sentence, str):
            return self.tokenizer.tokenize(sentence)

        if isinstance(sentence, list):
            return [self.tokenizer.tokenize(sent) for sent in sentence]


print(Preprocessing(tokenizer).tokenize(["привет как дела", " , привет не надо"]))
