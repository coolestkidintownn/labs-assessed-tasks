def decrypt_cypher_text(encrypted_text, key):
    # function implementation here...

    decrypted_text = ""

    for i in range(len(encrypted_text)):
        temp = ord(encrypted_text[i])
        temp = temp - key
        temp = temp % 256 
        temp = chr(temp)
        decrypted_text = decrypted_text + temp

    return decrypted_text

print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorsh", 3))


