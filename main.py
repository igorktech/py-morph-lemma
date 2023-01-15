from tools import Tools
from builder import Builder


# Function for input text processing
def call_builder(builder, list_of_text):
    # Text analysis
    list = builder.build(list_of_text)
    print(list)
    result = []

    for sent in list:
        constructed = ""
        # Get dict for each token
        for word in sent:
            # Construc specific stirng
            for key, value in word.items():
                constructed = constructed + f" {key}" \
                              + '{' + f"{value['lemma']}={value['morph']}" + '}'
        result.append(constructed)
    return result


def parse_txt():
    my_file = open('./data/text.txt', 'r')
    # read text file
    data = my_file.read()
    builder = Builder(Tools())
    [print(line) for line in call_builder(builder, data.split('\n'))]


def app_loop():
    input_text = []
    new_input = ' '
    # Initializing builder
    builder = Builder(Tools())
    while new_input != "-q":
        new_input = input(r"Enter text or '-q': ")
        if new_input != "-q":
            input_text.append(new_input)

    [print(line) for line in call_builder(builder, input_text)]


# Entry point
if __name__ == '__main__':
    parse_txt()
    # app_loop()
