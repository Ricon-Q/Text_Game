import random
import sys

PlayerName = input("플레이어의 이름을 입력하시오 : ")
print("\n========================================\n")

print("{}의 직업은 무엇입니까?" .format(PlayerName))
print("1. 전사\n2. 마법사\n3. 궁수")
Jobnum = int(input(">>>"))


def Job(jobnum): #캐릭터의 직업별 기본 스탯

    #1. 전사, 2. 마법사, 3. 궁수
    if jobnum == 1:
        P_HP = 100
        P_STR = 20
        P_DEF = 20
        P_MP = 50
        P_SPD = 20
        P_LV = 1

        return P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV

    if jobnum == 2:
        P_HP = 60
        P_STR = 10
        P_DEF = 10
        P_MP = 80
        P_SPD = 40
        P_LV = 1

        return P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV

    if jobnum == 3:
        P_HP = 75
        P_STR = 15
        P_DEF = 15
        P_MP = 65
        P_SPD = 50
        P_LV = 1

        return P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV

def check_stat():
    print("{}의 스테이터스는 다음과 같습니다." .format(PlayerName))
    print("이름 : {}" .format(PlayerName))
    print("레벨 : {} \t 체력 : {}" .format(P_LV, P_HP))
    print("힘   : {} \t 방어 : {}" .format(P_STR, P_DEF))
    print("마나 : {} \t 민첩 : {}" .format(P_MP, P_SPD))

def travel(P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV):
    Mname, Mlv, Mhp, Mstr, Mdef, Mspd = monster()

    print("{}이(가) 나타났다!" .format(Mname))
    while 1:
        print("<{}>의 체력 : {} \t <{}>의 체력 : {}" .format(PlayerName, P_HP, Mname, int(Mhp)))
        print("\n무엇을 하시겠습니까?")
        print("1. 공격 \t 2. 도망")

        do_input = int(input(">>"))

        #공격
        if do_input == 1:
            print("\n----------------------------------------\n")
            if P_SPD < Mspd:
                Mdmg = int(random.uniform(0, Mstr * 1.5 - 0.5 * P_DEF))
                Pdmg = int(random.uniform(0, P_STR * 1.5 - 0.5 * Mdef))
                print("{}의 공격! {}는 {}의 데미지를 입었습니다." .format(Mname, PlayerName, Mdmg))
                P_HP -= Mdmg
                if (P_HP <= 0):
                    print("{}에게 치명적인 데미지! \n\n{}는 사망하였습니다..." .format(PlayerName, PlayerName))
                    print("\n----------------------------------------\n")
                    return P_HP

                else:
                    print("{}의 공격! {}는 {}의 데미지를 입었습니다.".format(PlayerName, Mname, Pdmg))
                    print("\n----------------------------------------\n")
                    Mhp -= Pdmg

                    if Mhp <= 0:
                        print("{}을 쓰러트렸습니다!" .format(Mname))
                        print("\n----------------------------------------\n")
                        return P_HP

            if P_SPD >= Mspd:
                Mdmg = int(random.uniform(0, Mstr * 1.5 - 0.5 * P_DEF))
                Pdmg = int(random.uniform(0, P_STR * 1.5 - 0.5 * Mdef))
                print("{}의 공격! {}는 {}의 데미지를 입었습니다.".format(PlayerName, Mname, Pdmg))
                Mhp -= Pdmg
                if Mhp <= 0:
                    print("{}을 쓰러트렸습니다!".format(Mname))
                    print("\n----------------------------------------\n")
                    return P_HP
                else:
                    print("{}의 공격! {}는 {}의 데미지를 입었습니다.".format(Mname, PlayerName, Mdmg))
                    print("\n----------------------------------------\n")
                    P_HP -= Mdmg

                    if P_HP <= 0:
                        print("\n{}에게 치명적인 데미지!\n<<{}>>는 사망하였습니다...".format(PlayerName, PlayerName))
                        print("\n----------------------------------------\n")
                        return P_HP

        elif (do_input == 2):
            run_per = random.randint(1, 100)
            if run_per <= P_SPD:
                print("\n{}로부터 성공적으로 도망쳤습니다!" .format(Mname))
                return P_HP

            else:
                print("\n{}으로부터 도망치는데 실패하였습니다!" .format(Mname))
                print("\n----------------------------------------\n")
                continue

        else:
            print("\n<<잘못된 입력입니다!>>")
            print("\n----------------------------------------\n")
            continue



def rest(P_HP, MAX_HP):
    if P_HP < MAX_HP and MAX_HP - P_HP <= 10:
        P_HP = MAX_HP
    elif P_HP < MAX_HP and MAX_HP - P_HP >= 10:
        P_HP += 10
    elif P_HP == MAX_HP:
        print("이미 체력이 최대치입니다")

    return P_HP

def monster():
    mon_num = 1

    if mon_num == 1:
        M_Name = "고블린"
        M_LV = random.randint(P_LV - 2, P_LV + 2)
        M_HP = random.uniform(100 * 0.90 + 10 * M_LV, 100 * 1.10 + 10 * M_LV)
        M_STR = random.randint(10, 20)
        M_DEF = random.uniform(P_DEF * 0.9 + 0.3 * M_LV, P_DEF * 1.1 + 0.3 * M_LV)
        M_SPD = random.uniform(P_SPD * 0.9 + 0.5 * M_LV, P_SPD * 1.1 + 0.5 * M_LV)

        return M_Name, M_LV, M_HP, M_STR, M_DEF, M_SPD

P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV = Job(Jobnum)
MAX_HP = P_HP

while 1:
    if P_HP <= 0:
        print("#GAME OVER#")
        sys.exit()

    print("\n========================================\n")
    print("무엇을 하시겠습니까?\n")
    print("1. 스테이터스 확인하기 \t 2. 탐험하기")
    print("3. 휴식하기           \t 4. 종료하기")

    num = int(input(">>>"))

    if num == 1:
        print("\n========================================\n")
        check_stat()
    if num == 2:
        print("\n========================================\n")
        P_HP = travel(P_HP, P_STR, P_DEF, P_MP, P_SPD, P_LV)
    if num == 3:
        print("\n========================================\n")
        P_HP = rest(P_HP, MAX_HP)
    if num == 4:
        print("게임을 종료합니다")
        break