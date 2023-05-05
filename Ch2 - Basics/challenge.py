# This is a program to detect for Plaindromes in enterest text.
# Or exit if the user enters the text exit


def convString(strCase):
    text=str.upper(strCase)
    print('Upper case string is: ',text)
    return(text)

def exitString(strText):
    text=strText
    if(text=='EXIT'):
        exit()
    else:
        print('String is not Exit: ',text)
        return(text)

def alphanumeric(strAN):
    text=''.join(filter(str.isalnum, strAN))
    print('String without symbols is: ',text)
    return(text)

def revString(strRev):
    text=strRev[::-1]
    print('String reversed is: ',text)
    return(text)

def compString(cleanText, revText):
    if(cleanText==revText):
        return(' ')
    else:
        return(' not ')

def main():
    text=input("Please enter text: ")
    stagingText=convString(text)
    stagingText=exitString(stagingText)
    stagingText=alphanumeric(stagingText)
    cleanedText=stagingText
    stagingText=revString(stagingText)
    comparison=compString(cleanedText, stagingText)
    print('String is',comparison,'a Palindrome',sep="")
    main()

main()