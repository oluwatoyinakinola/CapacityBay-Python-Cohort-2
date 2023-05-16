multilist = [[1,2,3],4,5,[6,7,8],9,10,[11,[12,13,[23,[24]]],14,15,16,[17,18]]]
num = [3,5,8,10,11,13,15,18,23]

#Using for loop interate through the list and print out the following Multidimention list
#3,5,8,10,11,13,15,18


def rec_print(multilist, num):
    for element in multilist:
        if element in num:
            print(element)
        elif isinstance(element, list):
            rec_print(element, num)
            

rec_print(multilist, num)    