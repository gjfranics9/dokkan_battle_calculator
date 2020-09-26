This is a calculator to calculate damage stats on a dokkan battle unit

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
What is "Dragonball Z - Dokkan Battle", and how do the equations work?

Dokkan battle is a mobile game available on IOS and android, published by bandai namco and developed by akatsuki. It is based on characters from Akira Toriyama's "Dragonball" series. The main gameplay of thegame includes collecting Ki orbs to power up your characters as well as partnering characters with the best teams and forming the best teamupsto achieve higher power and defeat the multitude of enemies in the game.

Dokkan Battle released in January 2015 in Japan and July 2015 globally, since then it is contantly updated with a new flow of units. These units include units that can be"summoned" by using an in game currency either earned or bought with real life money, and there are also units that can be "farmed" in in-game events that give the characters as rewards. On average a new summon banner releases every 2-3 weeks; it usually includes 1 or more new units along with content along side the units to allow you to power them up. When received from the summon banner, a unit will be at level one with 0 paths open and 0 super attack levels and 0 link levels (will get to what those all are soon). By training your unit you can increase the level of the character; increasing the fixed stats that come alongside the character, as well as increasing your "link levels"; a
mechanic that gives your units more power depending on how many "link skills" they share with adjacent characters (a link will give a smaller bonus at level 1 compared to level 10). Super attack levels are another way to boost power, as they increase the percentage increase gained when a unit releases a super attack (a special attack gained when a certain amount of ki has been retrieved). Max super attack level can be from level 10 to level 25 depending on the unit. Paths are a way of increasing unit's power too, this is achieved when you summon more than one of a unit and put the duplicate into the first copy (a way to make more money), this drastically increases base stats, abilities and special attributes. There are many more ways of increasing power that would take ages to get into, however theres a lot of in depth research into how this works on the fanmade dokkan wiki, https://dbz-dokkanbattle.fandom.com/wiki/Dragon_Ball_Z_Dokkan_Battle_Wiki , where I received almost all information that I used to make this calculator.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maths

In dokkan every unit will have a base attack stat at its max level, that can be increased in flat boosts with duplicates and equipment. The attack stat is unique to every unit.
The attack stat is the first thing to be put in the equation.
The attack stat is then multiplied by the "leader skill" another skill that is unique to every unit that will give a boost to allies depending on conditions and typing.
It is multiplied by the "Friend skill", another leader skill that you receive from a borrowing system in game - this means a unit has two leader skills acting on it when conditions
are perfect.
Leader skills are calculated as percentages of the characters stats. So if two 150% leaders are acting on a unit the total % boost will be 300%, meaning that the total multiplier will be x4.
Now the game calculates "passive skills", these are skills that are unique to every unit, and can give attack buffs depending on enemies, allies, and more.
Passives are calculated the same as leader skills, so a multiplier of the multiplied attack stat
For example - a unit with 12000 base attack, with two 150% leaders, and a 200% passive boost will total out to ((12000*4)*3)
The next calculation that occurs is support items, these are rarely used however they are calculated the same as leader skills just factoring in the boost of the leader skill.
Going back to the example, a 20% support item will give (((12000*4)*3)*1.2)
Link skills are factored in next, calculated the exact same as before
50% from links -> ((((12000*4)*3)*1.2)*1.5)
Active skills are factored in next, these are given to some units and are conditional abilities that are activated once.
33% from active skills -> (((((12000*4)*3)*1.2)*1.5)*1.33)
Now a multiplier is worked out depending on ki, the more ki a unit has the more power it has. This is actually a % of the total and not an added percentage
A 140% ki multiplier would mean ((((((12000*4)*3)*1.2)*1.5)*1.33)*1.4)
Now if a unit is super attacking it will receive a bunch more multipliers. However that is it for the base stats (minus a few nuances as that would take a while)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Future updates

It is my goal to add more types of buffs to the calculator including discrete buffs that dont show the exact amount its buffing by, buffs that are dependent on amount of attacks, buffs that are dependent on more orbs, and a database that will include most premium units in dokkan (dokkanfest exclusives and LRs), and will show all unique buffs when levels are given. Once the damage stat calculation is perfected I would also like to add an actual damage calculator that will show how much damage an enemy will take rather than just the stat, as defensive stats are also part of this game.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sources
https://dbz-dokkanbattle.fandom.com/wiki/Super_Attack_Multipliers - Helped me work out how to calculate stats
https://dbz-dokkanbattle.fandom.com/wiki/Stack_Attack - Helped work out a few unique scenarios and nuances
https://www.reddit.com/r/DBZDokkanBattle/ - Helped with a few condition unique circumstances
