text="hi hellow hi goodafternoon zyton"

# longest word
words=text.split(" ")

# l_word=max(words,key=lambda w:len(w))
# print(l_word)
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)