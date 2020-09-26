class attacking_char:

    def __init__(self,base_atk,leader_stat,friend_stat):
        self.base_atk = 0
        self.leader_stat = 0
        self.friend_stat = 0

    def stats(self):
        return{'base attack': self.base_atk, "leader skill": self.leader_stat, "friend's leader skill": self.friend_stat}
    
    def base_attack(self):
        #base attack
        while True:
            try:
                self.base_atk = int(input("Please input the attack stat of the unit (include hidden potential buffs)"))
                return self.base_atk
                break
            except:
                continue

    def leader_skill(self):
        #primary leader skill
        while True:
            try:
                self.leader_stat = int(input("Please input atk bonus percentage from leader (Nuke leaders not yet implemented)"))
                if self.leader_stat < 0 or self.leader_stat > 177:
                    continue
                else:
                    return self.leader_stat
            except:
                continue

    def friend_skill(self):
        #secondary leader skill
        while True:
            try:
                self.friend_stat = int(input("Please input atk bonus percentage from friend leader (Nuke leaders not yet implemented)"))
                if self.friend_stat < 0 or self.friend_stat > 177:
                    continue
                else:
                    return self.friend_stat
            except:
                continue

    def leaderSkills_multiplier(self,leader_stat,friend_stat):
        leader_stat += 100
        leader_stat += friend_stat
        leader_multiplier = leader_stat/100
        return leader_multiplier

    def leaderBuffed_atk(self, leader_multiplier, base_atk):
        return leader_multiplier * base_atk
#everything downwards is just for reference from the first version of the calculator that worked but didnt allow more features that id like

def conditional_stats():
    while True:
        try:
            print("Total passive boost (not 'when attacking boosts') ~ include support type buffs")
            passive_skill = int(input("What % boost from passive skill"))
            Passive_retrieve = True
        except:
            continue
    support_item_retrieve = False
    while not support_item_retrieve:
        try:
            support_item = int(input("Boost from support items"))
            support_item_retrieve = True
        except:
            continue
    link_skill_retrieve = False
    while not link_skill_retrieve:
        try:
            link_skill = int(input("Total link skill boost"))
            link_skill_retrieve = True
        except:
            continue
    active_skill_retrieve = False
    while not active_skill_retrieve:
        try:
            active_skill = int(input("Boost from active skills (total)"))
            active_skill_retrieve = True
        except:
            continue
    ki_retrieve = False
    while not ki_retrieve:
        try:
            ki_multiplier = int(input("ki multiplier"))
            ki_retrieve = True
        except:
            continue
    passive_sa = False
    while not passive_sa:
        try:
            attack_on_super = int(input("Boost gained from attacking on super in passive"))
            passive_sa = True
        except:
            continue
    SA_multiplier_retrieve = False
    while not SA_multiplier_retrieve:
        try:
            print("multiplier can be found at https://dbz-dokkanbattle.fandom.com/wiki/Super_Attack_Multipliers")
            SA_multiplier = int(input("SA Multiplier"))
            SA_multiplier_retrieve = True
        except:
            continue
    hipo_sa_retrieve = False
    while not hipo_sa_retrieve:
        try:
            hipo_sa = int(input("What is the level of SA in hidde potential"))
            hipo_sa *= 5
            hipo_sa_retrieve = True
        except:
            continue
    stack_retrieve = False
    while not stack_retrieve:
        try:
            stack = int(input("Total % from stacks/Super atk boost"))
            stack_retrieve = True
        except:
            continue
    ally_sa_retrieve = False
    while not ally_sa_retrieve:
        try:
            ally_sa = int(input("Boost from ally's SA"))
            ally_sa_retrieve = True
        except:
            continue

##    total_leader = leader_stat + friend_stat
##    one = attack_stat * (total_leader/100)
##    two = ((one/100)*passive_skill) + one
##    three = ((two/100)*support_item) + two
##    four = ((three/100)*link_skill) + three
##    five = ((four/100)*active_skill) + four
##    six = (((five/100))*ki_multiplier) + five
##    seven = ((six/100)*attack_on_super) + six
##    total_sa_multiplier = (SA_multiplier + hipo_sa + stack + ally_sa)/100
##    
##    eight = seven*total_sa_multiplier
##    print(eight)

unit = attacking_char(0,0,0)
base_attack = unit.base_attack()
leader_multiplier = (unit.leaderSkills_multiplier(unit.leader_skill(),unit.friend_skill()))
leaderskillin = base_attack * leader_multiplier
print(attackxleaders)
