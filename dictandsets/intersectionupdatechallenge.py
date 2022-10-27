text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

set_of_words = set(text.split())

preps_used = set_of_words.intersection(prepositions)

print(preps_used)


