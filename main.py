pers_name = input("Set the name ")
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1


def attack(pers_hp, dmg=10):
    global armor, nr_hits

    if armor - dmg > 0:
        armor = armor - dmg
    else:
        pers_hp = pers_hp - dmg
    return pers_hp


def heal(pers_hp, live):
    global max_pers_hp

    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp
    else:
        pers_hp = pers_hp + live

    return pers_hp


# Make a battle
for i in range(1, 100):

    if pers_hp > 0:
        pers_hp = attack(pers_hp)
    else:
        break

    print("Live ", pers_hp)
    print("Armor", armor)
    print("Hit nr ", i)

print("You are dead")

for i in range(1, 100):

    if pers_hp > 0:
        nr_hits = nr_hits + 1

        if nr_hits % 3 == 0:
            pass
        else:
            pers_hp = attack(pers_hp)
        print("----" + pers_name + "---")
        print("Live ", pers_hp)
        print("Armor", armor)
        print("Hit nr ", nr_hits)

    else:
        break

print("You are dead")