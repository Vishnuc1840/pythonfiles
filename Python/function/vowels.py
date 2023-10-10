text="python is a proggramming language and it is a interpretter language"

words=text.split(" ")
for word in words:
    if word[0] in ["a","e","i","o","u"]:
        print(word)