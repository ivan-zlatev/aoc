#!/usr/bin/python

import re

def main(hp, dmg, arm):
   wepShop = {
      #Weapons:         Cost  Damage   Armor
      'Dagger'       : [8,    4,       0],
      'Shortsword'   : [10,   5,       0],
      'Warhammer'    : [25,   6,       0],
      'Longsword'    : [40,   7,       0],
      'Greataxe'     : [74,   8,       0],
   }
   armShop = {
      #Armor:           Cost  Damage   Armor
      'Leather'      : [13,   0,       1],
      'Chainmail'    : [31,   0,       2],
      'Splintmail'   : [53,   0,       3],
      'Bandedmail'   : [75,   0,       4],
      'Platemail'    : [102,  0,       5],
   }
   rngShop = {
      #Rings:           Cost  Damage   Armor
      'Damage+1'     : [25,   1,       0],
      'Damage+2'     : [50,   2,       0],
      'Damage+3'     : [100,  3,       0],
      'Defense+1'    : [20,   0,       1],
      'Defense+2'    : [40,   0,       2],
      'Defense+3'    : [80,   0,       3],
   }
   gear        = {}
   for wep in wepShop.keys():
      player_hp   = 100
      player_dmg  = 0
      player_arm  = 0
      moneySpent  = 0
      wepMoneySpent  = moneySpent + wepShop[wep][0]
      wepPlayer_dmg  = player_dmg + wepShop[wep][1]
      wepPlayer_arm  = player_arm + wepShop[wep][2]
      gear[wep]      = [fight(player_hp, wepPlayer_dmg, wepPlayer_arm, hp, dmg, arm, True), wepMoneySpent]
      for armour in armShop:
         armMoneySpent  = wepMoneySpent + armShop[armour][0]
         armPlayer_dmg  = wepPlayer_dmg + armShop[armour][1]
         armPlayer_arm  = wepPlayer_arm + armShop[armour][2]
         gear[wep+'_'+armour] = [fight(player_hp, armPlayer_dmg, armPlayer_arm, hp, dmg, arm, True), armMoneySpent]
         for ring1 in rngShop:
            ring1MoneySpent   = armMoneySpent + rngShop[ring1][0]
            ring1Player_dmg   = armPlayer_dmg + rngShop[ring1][1]
            ring1Player_arm   = armPlayer_arm + rngShop[ring1][2]
            gear[wep+'_'+armour+'_'+ring1]   = [fight(player_hp, ring1Player_dmg, ring1Player_arm, hp, dmg, arm, True), ring1MoneySpent]
            for ring2 in rngShop:
               if not ring1 == ring2:
                  ring2MoneySpent   = ring1MoneySpent + rngShop[ring2][0]
                  ring2Player_dmg   = ring1Player_dmg + rngShop[ring2][1]
                  ring2Player_arm   = ring1Player_arm + rngShop[ring2][2]
                  gear[wep+'_'+armour+'_'+ring1+'_'+ring2]  = [fight(player_hp, ring2Player_dmg, ring2Player_arm, hp, dmg, arm, True), ring2MoneySpent]
            ring1MoneySpent   = wepMoneySpent + rngShop[ring1][0]
            ring1Player_dmg   = wepPlayer_dmg + rngShop[ring1][1]
            ring1Player_arm   = wepPlayer_arm + rngShop[ring1][2]
            gear[wep+'_'+ring1]  = [fight(player_hp, ring1Player_dmg, ring1Player_arm, hp, dmg, arm, True), ring1MoneySpent]
            for ring2 in rngShop:
               if not ring1 == ring2:
                  ring2MoneySpent   = ring1MoneySpent + rngShop[ring2][0]
                  ring2Player_dmg   = ring1Player_dmg + rngShop[ring2][1]
                  ring2Player_arm   = ring1Player_arm + rngShop[ring2][2]
                  gear[wep+'_'+ring1+'_'+ring2] = [fight(player_hp, ring2Player_dmg, ring2Player_arm, hp, dmg, arm, True), ring2MoneySpent]
   cheapest = 100000
   mostExpensive = 0
   for i in gear:
      if gear[i][0]:
         if gear[i][1] <= cheapest:
            cheapest = gear[i][1]
            print 'New cheaper combination found: {}\t{}'.format(gear[i][1], i)
   for i in gear:
      if not gear[i][0]:
         if gear[i][1] >= mostExpensive:
            mostExpensive = gear[i][1]
            print 'New most expensive combination where you lose found: {}\t{}'.format(gear[i][1], i)

def fight(player_hp, player_dmg, player_arm, boss_hp, boss_dmg, boss_arm, turn): # recursive function to calculate the fight
   if player_hp <= 0:
      return False
   if boss_hp <= 0:
      return True
   if turn:
      # player does dmg
      dmg = max(1, player_dmg - boss_arm)
      boss_hp -= dmg
      #print "Player deals '{}' dmg; the boss goes down to '{}' hp.".format(dmg, boss_hp)
      return fight(player_hp, player_dmg, player_arm, boss_hp, boss_dmg, boss_arm, False)
   else:
      # boss does dmg
      dmg = max(1, boss_dmg - player_arm)
      player_hp -= dmg
      #print "Boss deals '{}' dmg; the player goes down to '{}' hp.".format(dmg, player_hp)
      return fight(player_hp, player_dmg, player_arm, boss_hp, boss_dmg, boss_arm, True)

hp = 104
dmg = 8
arm = 1

main(hp, dmg, arm)
