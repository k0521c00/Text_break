import textwrap
from pip._vendor.distlib.compat import raw_input

sample = raw_input("Enter your phrase")

def text_break(text):
    w = textwrap.TextWrapper(13, break_long_words=True)
    return w.wrap(text)
splitted=text_break(sample)

print(*splitted, sep="\n")