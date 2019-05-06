def which_profession(in_ex, sen_int, think_feel, judg_perc):
    list_1 = ['I', 'S', 'T', 'J']
    list_2 = ['I', 'S', 'F', 'J']
    list_3 = ['I', 'N', 'F', 'J']
    list_4 = ['I', 'N', 'T', 'J']
    list_5 = ['I', 'S', 'T', 'P']
    list_6 = ['I', 'S', 'F', 'P']
    list_7 = ['I', 'N', 'F', 'P']
    list_8 = ['I', 'N', 'T', 'P']
    list_9 = ['E', 'S', 'T', 'P']
    list_10 = ['E', 'S', 'F', 'P']
    list_11 = ['E', 'N', 'F', 'P']
    list_12 = ['E', 'N', 'T', 'P']
    list_13 = ['E', 'S', 'T', 'J']
    list_14 = ['E', 'S', 'F', 'J']
    list_15 = ['E', 'N', 'F', 'J']
    list_16 = ['E', 'N', 'T', 'J']

    # in_ex = 'I'
    # sen_int = 'S'
    # think_feel = 'T'
    # judg_perc = 'J'

    total = []
    total.append(in_ex)
    total.append(sen_int)
    total.append(think_feel)
    total.append(judg_perc)

    if (total == list_1):
        return ("ISTJ: ")
    if (total == list_2):
        return ("ISFJ: ")
    if (total == list_3):
        return ("INFJ: ")
    if (total == list_4):
        return ("INTJ: ")
    if (total == list_5):
        return ("ISTP: ")
    if (total == list_6):
        return ("ISFP: ")
    if (total == list_7):
        return ("INFP: ")
    if (total == list_8):
        return ("INTP: ")

    if (total == list_9):
        return ("ESTP: ")
    if (total == list_10):
        return ("ESFP: ")
    if (total == list_11):
        return ("ENFP: ")
    if (total == list_12):
        return ("ENTP: ")
    if (total == list_13):
        return ("ESTJ: ")
    if (total == list_14):
        return ("ESFJ: ")
    if (total == list_15):
        return ("ENFJ: ")
    if (total == list_16):
        return ("ENTJ: ")
