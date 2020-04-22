'''''''''''''''
LISTA ESEMPIO CODICI

012, 0123, 4, 310, 1024, 2402, 2401, 4013              # UD
a, ad, abb, bad, deb, bbcde                            # UD
abc, abcd, e, dba, bace, ceac, ceab, eabd              # UD
010, 0001, 0110, 1100, 00011, 00110, 11110, 101011     # non UD
00, 01, 10, 11                                         # UD
0, 10, 110, 1110                                       # UD
0, 01, 011, 0111                                       # UD
a, c, ad, abb, bad, deb, bbcde                         # non UD
0, 01, 10, 1                                           # non UD
'''''''''''''''


S = []


def insert_input_code():
    S_0=[]

    print("Inserire il codice di input (-1 per terminare):")
    while(True):
        x = input()
        if(x == '-1'):
            return S_0
        else:
            S_0.append(x)


def create_Si():
    # Creazione di S_1
    S_1 = []
    for i in range(len(S[0])):
        for j in range(len(S[0])):
            if(j != i):
                if(S[0][j].startswith(S[0][i])):
                    if S[0][j][len(S[0][i]) : ] not in S_1:
                        S_1.append(S[0][j][len(S[0][i]) : ])

    if(S_1 == []):
        print_cod(True)
    else:
        S.append(S_1)

        # Creazione di S_i, con i > 1
        flag = -1
        ud = True

        while(flag != 0):
            S_i = []
            last_index = len(S)-1

            for i in range(len(S[0])):
                if(ud == False):
                    break

                for j in range(len(S[last_index])):
                    if(S[0][i] == S[last_index][j]):
                        ud = False
                        flag = 0
                        break
                    else:
                        if(S[0][i].startswith(S[last_index][j])):
                            if S[0][i][len(S[last_index][j]) : ] not in S_i:
                                S_i.append(S[0][i][len(S[last_index][j]) : ])
                        if(S[last_index][j].startswith(S[0][i])):
                            if S[last_index][j][len(S[0][i]) : ] not in S_i:
                                S_i.append(S[last_index][j][len(S[0][i]) : ])

            # Controllo se per ogni i,j,  S_i = S_j
            if(S_i in S):
                ud = True
                flag = 0

            if(ud):
                if(S_i == []):
                    flag = 0
                else:
                    S.append(S_i)

        print_cod(ud)


def print_cod(ud):
    print('\n\nCodice di input: {0}\n'.format(S_0))

    for i in range(len(S)):
        print('S_{0}: {1}'.format(i, S[i]))

    if(ud == False):
        print("\nIl codice non è univocamente decifrabile\n")
    else:
        print("\nIl codice è univocamente decifrabile\n")



S_0 = insert_input_code()
S.append(S_0)
create_Si()
