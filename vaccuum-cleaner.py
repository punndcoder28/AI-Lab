print("Available Status: Dirty, Clean")
left = input("Left Status: ")
right = input("Right Status: ")

env = [left, right]

pos = int(input("Position (L=0 or R=1): "))

def clean():
    global pos
    if env[pos]=='Dirty':
        env[pos]='Clean'
        return 'Suck'
    elif pos==0:
        pos=1
        return 'Right'
    else:
        pos=0
        return 'Left'

while "Dirty" in env:
    print(clean())
else:
    print(env)