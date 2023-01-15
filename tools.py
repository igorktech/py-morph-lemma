from tagger import Tagger
from preprocessing import Preprocessing


# Tools stores all intruments
class Tools():
    def __init__(self):
        self.preprocessor = Preprocessing()
        self.morph_tagger = Tagger()
