import random
# def interleaved(lst1, lst2):
#      final_lst1 = []
#      total_x = 0
#      for x in range(len(lst1)):
#          while total_x < len(lst1):
#              total_x +=1
#              if lst1[x] > lst1[x+1]:
#                  final_lst1.append(lst1[x])
#                  final_lst1.append(lst1[x+1])
#             elif lst1[x] < lst1

     # for x in range(len(lst1)):
     #     while x < range(len(lst1)):
     #         if lst1[x] >lst1[x+1]:
#             total_x += 1
#     for y in range(len(lst2))
#         while total_y < len(lst2):
#             total_y += 1
#             print(lst2[y])
#this is broken; it's calculating infinitely


    # two index iterator
    # one for each list
    # keep going while both index iterators are less than the last position
    # inside while loop check to see which is smallest
    # append to new list, the smallest of the two; implement either incrementor;
    # if either incrementor is currently at the end of the list, ignore until the other list


def primeFac(number):
    #the numbers and factors must be greater than 1; no negative numbers!
    factors_lst = []
    mod = 2

    #this is also correct
    while number >= mod**2:
        if number%mod:
            mod +=1
        else:
            number//=mod
            factors_lst.append(mod)
            #factors_lst.append(number)
    if number >1:
        factors_lst.append(number)
    return factors_lst


        #this works
        #go over with tutor, make sure that she helps em understand why and how this works
    return factors_lst


        # if number >= p**2:
        #     if number%p == 0:
        #         print(number%p)
        #         factors_lst.append(number%p)
        # # else:
        #     factors_lst.append(number);
        #this else is correct
    #return factors_lst
    #this part is also correct




        #if number < p ** 2:
            #print(number)
            #factors_lst.append(number)
            #this condition in line 33 will work if the number itself is a prime number





def piggyBank(coins):
    total_cents = 0
    x =0
    Q_in_cents = coins.count('Q') * 25
    D_in_cents = coins.count('D') * 10
    N_in_cents = coins.count('N') * 5
    P_in_cents = coins.count('P')* 1
    total_cents = Q_in_cents + D_in_cents + N_in_cents + P_in_cents

        # if 'Q' in coins:
        #     print(25 * coins.count('Q'))
        # elif 'D' in coins:
        #     print
        # elif 'N' in coins:
        #     total_cents += 5 * coins.count('N')
        # elif 'P' in coins:
        #     total_cents += 1 * coins.count('P')
        # else:
        #     total_cents += 0
    final_dict = {}
    final_dict.update({'Q': coins.count('Q')})
    final_dict.update({'D': coins.count('D')})
    final_dict.update({'N': coins.count('N')})
    final_dict.update({'P': coins.count('P')})
    final_tupple = (final_dict,total_cents)
    return final_tupple
#piggy bank works!
def craps():
    player_total = 0
    for i in range(0,2):
        player_total += randrange(1,7)
        print(player_total)


#def testCraps()

if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw6TEST.py'))
