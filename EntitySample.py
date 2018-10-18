import nltk

#nltk.download()

text = 'Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.'

phrases = nltk.tokenize.sent_tokenize(text)
print(phrases)

tokens = nltk.word_tokenize(text)
print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

entity = nltk.chunk.ne_chunk(classes)
print(entity)