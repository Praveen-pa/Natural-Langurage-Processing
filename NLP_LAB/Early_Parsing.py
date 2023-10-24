import nltk
nltk.download('earley_parser')
from nltk.parse.earleychart import EarleyChartParse
parser = EarleyChartParser()
sentence = "The cat chased the mouse."
parser.parse(sentence.split()):
    tree.pretty_print()
