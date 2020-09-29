class attacking_char:
#this is object oriented for almost no reason - possible damage total calculation factoribng in enemy defensive stats and damage reduction in future
    def __init__(self,base_atk,leader_stat,friend_stat):
        #sets base for all stats currently
        self.base_atk = 0
        self.leader_stat = 0
        self.friend_stat = 0

    def stats(self):
        #an output to check current stats and output, used to verify everything
        return{'base attack': self.base_atk, "leader skill": self.leader_stat, "friend's leader skill": self.friend_stat}
    
    def base_attack(self):
        #base attack
        while True:
            #validation for integer values
            try:
                #base atk retrieve
                self.base_atk = int(input("Please input the attack stat of the unit (include hidden potential buffs)"))
                return self.base_atk
                break
            except:
                continue

    def leader_skill(self):
        #primary leader skill
        while True:
            try:
                #primary leader retrieve
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
                #friend leader retrieve
                self.friend_stat = int(input("Please input atk bonus percentage from friend leader (Nuke leaders not yet implemented)"))
                if self.friend_stat < 0 or self.friend_stat > 177:
                    continue
                else:
                    return self.friend_stat
            except:
                continue

    def leaderSkills_multiplier(self,leader_stat,friend_stat):
        #leader multiplier is +total %. This finds the multiplier
        leader_stat += 100
        leader_stat += friend_stat
        leader_multiplier = leader_stat/100
        return leader_multiplier

    def leaderBuffed_atk(self, leader_multiplier, base_atk):
        #temporary value that calculates the first step of damage calculation
        return leader_multiplier * base_atk


unit = attacking_char(0,0,0)
leaderskillin = unit.base_attack() * (unit.leaderSkills_multiplier(unit.leader_skill(),unit.friend_skill()))
print(leaderskillin)
