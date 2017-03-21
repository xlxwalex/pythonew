pytxt=open("6.1eg.py","rt",encoding='utf-8')
print(pytxt.encoding)
excludes=['def','from','import','for','in','range,','random','randint','if','else','return','chr','print']
for line in pytxt.readlines():
    line=line.replace("\n","")
    words=line.split(" ")
    liner=""
    for word in range (len(words)):
        s=""
        if words[word] == "":
            words[word] = " "
        if words[word] in excludes:
            continue
        else:
            stempo=words[word]
            for alpha in range (len(words[word])):
                if 97 <= ord(words[word][alpha]) <=122:
                    s+=chr(ord(words[word][alpha])-32)
                else:
                    s=stempo
                    continue                   
            words[word]=s
    for wordaf in range(len(words)):
        liner += words[wordaf]
        liner += " "
    print(liner)
pytxt.close()
