def emoji_converter(message):
    words = message.split(" ")
    emojis = {
    ":)" : "😁",
    ":(" : "😖",
    ":}" : "😭"  
    }
    output = ""
    for word in words:
        out += emojis.get(word, word)+ " "
    return out
