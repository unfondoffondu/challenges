validator = input("What is the flag? >>> ")
var1 = "0x001b"
var2 = "0x0016"

def phase_one():
    if len(validator) ^ 10 == int(var1,0):
        if ord(validator[0]) ^ 22 + ord(validator[1]) ^ 22 == 242 and len(validator) ^ 10 == int(var1, 0):
            phase_two(validator)
        if phase_three(phase_two(validator)):
            print(f"*****congrats*****")
        else:
            exit("Better luck next time.")
    else:
        exit("Not even close.")
def phase_two(ordinal):
    id_code = "0x01cb"
    if ord(ordinal[2]) ^ int(var2,0) + ord(ordinal[3]) ^ int(var2, 0) + ord(ordinal[4]) ^ int(var2, 0) == int("0x126", 0):
        pass
    if ord(ordinal[5]) ^ int(var2,0) == 85:
        return([id_code, 68, 73, 85, 69, 85, 73, 36, 38, 36, 36, 107])
    else:
        exit()
def phase_three(ordinals):
    iterator = 6
    ordinals.pop(0)
    flag = False
    for i in ordinals:
        if ord(validator[iterator]) ^ int(var2, 0) == i:
            iterator += 1
        else:
            return flag

    flag = True
    return flag

phase_one()
