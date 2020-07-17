import sys

def CaesarCypher(givenText, steps):
    returnedText = []

    if isinstance(givenText, str):
        
        for letter in givenText:
            if letter.isalpha():
                origin = ord(letter)
                crypt = origin + steps
                crypt = chr(crypt)
                returnedText.append(crypt)
            if letter.isspace():
                returnedText.append(letter)

        return returnedText
    
    else:
        print("Wrong type.  Exiting.")
        sys.exit()

def BacktoNorm(test, steps):
    returnedText = []

    if isinstance(test, str):
        
        for letter in test:
            if letter.isalpha():
                origin = ord(letter)
                crypt = origin - steps
                crypt = chr(crypt)
                returnedText.append(crypt)
            if letter.isspace():
                returnedText.append(letter)

        return returnedText
    

steps = 4
givenText = "This is a Test"
print(givenText, "\n")

test = CaesarCypher(givenText, steps)
print(test)
test = ''.join(test)
print(test)

review = BacktoNorm(test, steps)
print(review)
print(''.join(review))

