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



unit = attacking_char(0,0,0)
base_attack = unit.base_attack()
leader_multiplier = (unit.leaderSkills_multiplier(unit.leader_skill(),unit.friend_skill()))
leaderskillin = base_attack * leader_multiplier
print(attackxleaders)
