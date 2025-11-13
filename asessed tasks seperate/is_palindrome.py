def is_palindrome(text):
    text = text.upper()

    reverse = text[::-1]
    print(reverse)

    if text == reverse:
        return True
    else:
        return False
    
print(is_palindrome("Madam"))
print(is_palindrome("blob"))