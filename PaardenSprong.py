# ["V", "R", "N", "I", "K", "T", "E", "A"]
def get_paardensprong_opties_inner(array, reverse):
    len3 = len(array)
    if len3 != 8:
        return len3

    alle_opties = []
    counter = 0

    if reverse:
        array.reverse()

    i = 0;
    for v in array:
        moving_index = i
        alle_opties.append([])
        while counter < len3:
            alle_opties[i].append(array[moving_index])
            moving_index = get_next_number(moving_index)
            counter += 1
        alle_opties[i] = array_to_string(alle_opties[i])
        counter=0
        i += 1

    return alle_opties

def get_next_number(num):
    if num + 3 > 7:
        return num+3-8
    return num+3

def array_to_string(array):
    return "".join(array)

def get_paardensprong_opties(array):
    l1 = get_paardensprong_opties_inner(array, False)
    l2 = get_paardensprong_opties_inner(array, True)
    return l1+l2;

def get_correct_word(array):
    paardensprong_opties = get_paardensprong_opties(array)
    for i in paardensprong_opties:
        if check_word(i.lower()):
            return i.lower()
    return False

def check_word(word):
    file = open("opentaal-hunspell/nl.dic", "rb").read()
    contents = file.decode('latin1')
    rows = contents.split("\n")
    c = 0
    for row in rows:
        rows[c] = rows[c].split("/")[0]
        c+=1

    if word in rows:
        return True
    return False

