print("******TOWER OF HANOI******")
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
print("------------------------")
print("******For 2 Disks******")
print("------------------------")

moveTower(2,"A","B","C")
print("------------------------")
print("******For 3 Disks******")
print("------------------------")
moveTower(3,"A","B","C")

print("------------------------")
print("******For 3 Disks******")
print("------------------------")
moveTower(4,"A","B","C")
