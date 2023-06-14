import string
def caesar_cipher(sntc, shift_amount):
    alpha_lower=list(string.ascii_lowercase)
    alpha_upper=list(string.ascii_uppercase)
    answer=''
    for ltr in sntc:
        if ltr== ltr.upper() and ltr.isalpha():
            idx=alpha_upper.index(ltr)+shift_amount
            if idx>26:
                idx-=26
            answer+= alpha_upper[idx]
        elif ltr== ltr.lower() and ltr.isalpha():
            idx=alpha_lower.index(ltr)+shift_amount
            if idx>26:
                idx-=26
            answer+= alpha_lower[idx]
        else:
            answer+=ltr
    return answer