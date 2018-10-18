import nltk

#nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwords_nltk = nltk.corpus.stopwords.words('portuguese')

#print(stopwords_nltk)


def removes_stopwords(text):
    phrases = []
    for(words, emotion) in text:
        without_stopwords = [p for p in words.split() if p not in stopwords_nltk]
        phrases.append((without_stopwords, emotion))
    return phrases

#print(removestopwords(base))


def apply_stemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    phrases_stemming = []
    for(words, emotion) in text:
        with_stemming = [str(stemmer.stem(p)) for p in words.split() if p not in stopwords_nltk]
        phrases_stemming.append((with_stemming, emotion))
    return phrases_stemming

phrases_with_stemming = apply_stemmer(base)
#print(phrases_with_stemming)


def search_words(phrases):
    all_words = []
    for(words, emotion) in phrases:
        all_words.extend(words)
    return all_words

words_radical = search_words(phrases_with_stemming)
#print(words_radical)


def search_frequency(words):
    words = nltk.FreqDist(words)
    return words

frequency = search_frequency(words_radical)
#print(frequency.most_common(50))


def search_unique_words(words):
    keywords = words.keys()
    return keywords

unique_words = search_unique_words(frequency)
#print(unique_words)

def word_extractor(document):
    document = set(document)
    attributes = {}
    for words in unique_words:
        attributes['%s' % words] = (words in document)
    return attributes

attributes_phrases = word_extractor(['am', 'nov', 'dia'])
print(attributes_phrases)

