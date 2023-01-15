from tools import Tools


# Takes all processing
class Builder:
    def __init__(self, tools: Tools):
        self.tools = tools

    def build(self, text):
        # Tokenize
        tokenized_text = self.tools.preprocessor.tokenize(text)
        # Extract tags
        tagged_text = self.tools.morph_tagger.get_tags(tokenized_text)
        return tagged_text

# print(Builder(tools=Tools()).build(["Привет", "Привет как дела я полил цветы"]))
