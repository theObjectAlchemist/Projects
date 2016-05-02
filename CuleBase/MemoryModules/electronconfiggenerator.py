def Erray(num:int)->list:
    pi = 2 #'keeping track'
    si = 1 #which orbital
    ti = 1 #which quantum number
    counter = 1 #which iteration
    while counter < num:
        if si == 1:
            
            if ti == 1: #base case 1
                ti += 1
                pi += 1
            elif (ti == 2) or (ti == 3): #base case 2 and 3
                si += 1
            else: #all other cases
                if ti % 2 != 0:
                    si = int(((ti-1)/2)+1)
                else:
                    si = int((ti/2)+1)
                ti = pi

        elif ((si > 1) and (si != pi)): #middle case
            si -= 1
            ti += 1
            
        elif si == pi: #edge case
            si -= 1
            pi += 1
            ti = pi
        counter += 1

    return [ti, si]

for i in range (1,16):
    print(Erray(i))
