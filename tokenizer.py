import string
import re


class Tokenizer:
    def __init__(self, pattern=None, flags=re.UNICODE | re.MULTILINE | re.DOTALL, split_by=[' '],
                 punctuations=string.punctuation, split_token='<SPLIT>'):

        self._regexp = None
        self._pattern = getattr(pattern, "pattern", pattern)
        self._flags = flags
        self._split_by = split_by
        self._split_token = split_token
        self._punctuations = punctuations

    def _check_regexp(self):
        if self._regexp is None:
            self._regexp = re.compile(self._pattern, self._flags)

    def tokenize(self, sentence):

        if self._pattern is not None:
            self._check_regexp()
            return self._regexp.findall(sentence)

        work_sentence = str(sentence)
        for punctuation in self._punctuations:
            work_sentence = work_sentence.replace(punctuation, " " + punctuation + " ")
        for delimiter in self._split_by:
            work_sentence = work_sentence.replace(delimiter, self._split_token)
        tokens = [x.strip() for x in work_sentence.split(self._split_token) if x != '']
        return tokens
