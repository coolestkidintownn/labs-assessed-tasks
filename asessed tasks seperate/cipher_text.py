def cipher_text(cipherText, key):
    decryptedText = ""
    tempChar = ""
    
    for i in cipherText:
        tempChar = ord(i) - key
        tempChar = tempChar % 256
        decryptedText = decryptedText + chr(tempChar)

    return decryptedText

cipherText = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
key = 3
print(cipher_text(cipherText, key))
# expected output: some… meaningful English text



