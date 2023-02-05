score = input("Enter Score Between 0.0 and 1.0: ")


try:
    fScore = float(score) # Took me forever to figure out that I needed to put this line in the try block. This link helped me https://gist.github.com/jmangrad/1da5d7152c65537251bd24b104bec7e3
    if fScore >= 0.9 and fScore <= 1.0:
         # print("Your grade is:", 'A')
        print('A')
    elif fScore >= 0.8 and fScore < 0.9:
        # print("Your grade is:", 'B')
        print('B')
    elif fScore >= 0.7 and fScore < 0.8:
        # print("Your grade is:", 'C')
        print('C')
    elif fScore >= 0.6 and fScore < 0.7:
        # print("Your grade is:", 'D')
        print('D')
    elif fScore > 0.0 and fScore < 0.6:
        # print("Your grade is:", 'F')
        print('F')
    else:
        print('Error. Please enter a number between 0.0 and 1.0.')

except:
    print('Error. Please enter a number between 0.0 and 1.0')