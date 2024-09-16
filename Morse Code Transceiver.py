# MORSECODE TRANSCEIVER
# group_B18
# E/17/157  E/17?158  E/17/159

print("-----------------------")
print("Morse Code Transceiver")
print("-----------------------")

mode = input("Select the device mode transmitter (T) or Receiver(R) : ")



if mode == 'T' or mode == 't':

    # Import modules from pyfirmata library
    from pyfirmata import Arduino, OUTPUT

    # Import inbuilt time library
    import time

    # Initial configurations

    # Create an arduino board instance
    board = Arduino("COM9")

    led_pin = 9

    buzzer_pin = 6

    board.digital[led_pin].mode = OUTPUT

    # Time parameters define
    dotLen = 0.2;               # Length of the morse code 'dot'
    dashLen = dotLen * 3;       # Length of the morse code 'dash'
    elemSpace = dotLen;         # Length of the pause between elements of a character
    letterSpace = dotLen * 3;   # Length of the spaces between characters
    wordSpace = dotLen * 7;     # Length of the pause between words

    # Morsecode dictionary
    morsecodes = {

        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-..",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-..",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        ":": "---...",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
        " ": "     "

    }


    def split(word):
        return [char for char in word]


    print('--------------------------')
    print('Morse code Transmitter')
    print('--------------------------')

    while True:
        word = input('Enter a string to transmit: ')

        # Executing the function "split"
        list_one = split(word)

        list_two = []

        morsecode_list = []

        for i in range(len(list_one)):
            morsecode_list.append(morsecodes.get(list_one[i]))

        print('Sending: ', *morsecode_list, sep = ' ')

        for letter in range(len(list_one)):
            Letter_In_Morse = morsecodes.get(list_one[letter])
            list_two.append(Letter_In_Morse)

        for symbol in range(len(list_two)):

            list_three = []
            list_three.append(list_two[symbol])

            for element in list_three[0]:

                if element == ".":
                    board.digital[buzzer_pin].write(1)
                    board.digital[led_pin].write(1)
                    time.sleep(dotLen)
                    board.digital[buzzer_pin].write(0)
                    board.digital[led_pin].write(0)
                    time.sleep(elemSpace)

                elif element == "-":
                    board.digital[led_pin].write(1)
                    board.digital[buzzer_pin].write(1)
                    time.sleep(dashLen)
                    board.digital[led_pin].write(0)
                    board.digital[buzzer_pin].write(0)
                    time.sleep(elemSpace)

            del list_three[0]

            time.sleep(letterSpace)

    
elif mode == "R" or mode == "r":
            
        print("-----------------------")
        print("Morse Code Receiver")
        print("-----------------------")

        from pyfirmata import Arduino, util, INPUT, OUTPUT
        
        import time
        
        board = Arduino("COM9")
        
        ldr_pin = 0
        board.analog[ldr_pin].mode = INPUT

        buzzer_pin = 5
        #board.digital[ldr_pin].mode = OUTUT
        
        it = util.Iterator(board)
        it.start()
        
        on_off = 0

        intensity_of_darkness = 0.9

        # Time increments during the loop for Symbols and spaces
        symbolTime = 0
        spaceTime = 0
        
        appendingList = []
        
        
        char = ''

        
        flag_1 = 0
        flag_2 = 0

        # Morse codes tree                                                                                                                           
        morseTree = [['E',[['I',[['S',[['H',['5','4']],['V',[None,'3']]]],['U',['F',[None,[None,'2']]]]]],['A',[['R',['L',None]],['W',['P',['J',[None,'1']]]]]]]],
                     ['T',[['N',[['D',[['B',['6',None]],'X']],['K',['C','Y']]]],['M',[['G',[['Z',['7',None]],'Q']],['O',[[None,['8',None]],[None,['9','0']]]]]]]]]
        access = morseTree

        morseGap = 0
        charGap = 0

        # Time definitions
        dotLen = 0.2
        dashLen = dotLen * 3
        
        
        
        while True:
                    
            ldr_val = board.analog[ldr_pin].read()
            
            if ldr_val != None:
                    
                if ldr_val > intensity_of_darkness:
                    on_off = 0
                else:
                    on_off = 1
            
            if on_off == 1:      # ON
                if flag_1 == 0:  # If flag_1 = 0 then Received
                    print('Received: ',end='')
                    flag_1 = 1   # Code has now receivd
                    
                flag_2 = 1      # Letter Entered
                charGap = 1    
                
                if morseGap == 1:  
                    print('     ',end='')
                    morseGap = 0   
                
                symbolTime += on_off    
                
                if spaceTime > 20:              
                    appendingList.append(0)     
                    print(' ',end='')           
                    
                    for i in appendingList:
                        access = access[i]
                        
                    if access != morseTree[0]:
                        char = char + access
                        
                        print('('+access+')',end='')
                        print(' ',end='')
                        
                    access = morseTree
                    appendingList = []
                    
                elif spaceTime > 0:
                    appendingList.append(1)
                spaceTime = 0
                
            elif on_off == 0:           # OFF
                if spaceTime > 150:     # End and prints
                    if flag_2 == 1:
                        
                        morseGap = 0       
                        print('')
                        flag_2 = 0
                        print('Message: ' + char)   
                        print('')
                        flag_1 = 0
                        char = ''
                    
                elif spaceTime > 60:                
                    appendingList.append(0)
                    
                    for i in appendingList:
                        access = access[i]
                    if (access != morseTree[0]):
                        char = char + access
                        char = char + ' '
                        
                        print('('+access+')',end='')
                        
                    access = morseTree
                    appendingList = []
                    
                    if charGap == 1:        
                        morseGap = 1
                        charGap = 0         
                        
                if symbolTime > 20:         
                    appendingList.append(1)
                    print('-',end='')
                    #board.digital[buzzer_pin].write(1)
                    #time.sleep(dashLen)
                    board.digital[buzzer_pin].write(0)
                    
                elif symbolTime > 0:
                    appendingList.append(0)
                    print('.',end='')
                    #board.digital[buzzer_pin].write(1)
                    #time.sleep(dotLen)
                    board.digital[buzzer_pin].write(0)
                    

                symbolTime = 0
                
                spaceTime += 1

            time.sleep(0.01)
    
        

else:
        print('Error input')


