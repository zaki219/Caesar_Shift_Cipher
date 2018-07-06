
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "loon goon"
 
def decode(secretMessage):    
    for key in range(len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
 
        for i in range(len(secretMessage)):
            index = alphabet.find(secretMessage[i])
 
            if index < 0:
                attempt += secretMessage[i]
            else:
                attempt += newAlphabet[index]
 
        print("Key: " + str(key) + " - " + attempt)

decode(message)
