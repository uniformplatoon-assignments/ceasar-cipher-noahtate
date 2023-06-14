#iterate through the given string
#shift each letter to the right by the given amount
#start from a if passing z

#   What a string! => Bmfy f xywnsl!
                  #   Cmfy f xywnsl!


#
def caesar_cipher(string, shift_amount):
    lower_case_bounds = [97,122]
    upper_case_bounds = [65,90]
    return_string = ""
    forbidden_string = " !@#$%^&*()_+-=,.?1234567890"
    print(string,shift_amount)
    for i in string:
        #print(i)
        if i in forbidden_string:
            return_string += i
            continue
        if(ord(i) >= 97 and ord(i) <= 122): #lower cases 
            if ord(i)+shift_amount > 122: #alg : lowest number + (shifted number - highest number)
                return_string += chr(96+(ord(i)+shift_amount)-122)         
            elif ord(i) + shift_amount < 97: #alg : highest number + (shifted number - lowest number)
                return_string += chr(123+(ord(i)+shift_amount)-97) # this is +1 for some reason
            else:
                return_string += chr(ord(i)+shift_amount)

        elif(ord(i) >= 65 and ord(i) <= 90): #upper cases
            if ord(i)+shift_amount > 90:# too high, goes back to a
                return_string += chr(64+(ord(i)+shift_amount)-90)
            elif ord(i)+shift_amount < 65: # too low, goes back to z
                return_string += chr(91+(ord(i)+shift_amount)-65) # this is +1 for some reason?
            else:
                return_string += chr(ord(i)+shift_amount)
       

    print(return_string)
    return return_string    
        


caesar_cipher("What a string! W", 5)


print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!","correct answer:","Wjt! Rcvo v nomdib!")
print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")






















    # alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    # # for x in alphabet.values():
    # string = string.lower()


    # for i in string:
    #     for x in range(shift_amount):
    #         print(i)
    #         print(alphabet[i])

# alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphalist = alpha.split('')
# print(alphalist)
