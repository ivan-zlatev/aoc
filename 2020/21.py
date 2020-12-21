#!/usr/bin/python

import copy
import re
import math
import numpy

def main(data):
   foods = []
   for row in data:
      ingredients = row.split(' (')[0].split(' ')
      allergens = row.split(' (contains ')[1].split(')')[0].split(', ')
      foods.append([ingredients, allergens])
   allAllergens = dict()
   for food in foods:
      for allergen in food[1]:
         if allergen not in allAllergens.keys():
            allAllergens[allergen] = ''
   while '' in allAllergens.values():
      for allergen, ingredient in allAllergens.items():
         if ingredient == '':
            tmpFoods = []
            for food in foods:
               if allergen in food[1]:
                  tmpFoods.append(food[0])
            result = findCommonValsInLists(tmpFoods)
            if len(result) > 1:
               itemsToBeRemoved = []
               for i in range(len(result)):
                  if result[i] in allAllergens.values():
                     itemsToBeRemoved.append(result[i])
               for i in itemsToBeRemoved:
                  result.remove(i)
            if len(result) == 1:
               allAllergens[allergen] = result[0]
   #for k,v in allAllergens.items():
   #   print k, v
   result = []
   for food in foods:
      for ingredient in food[0]:
         if ingredient not in allAllergens.values():
            result.append(ingredient)
   print "Q1: Inert ingredient {}".format(len(result))
   allergens = allAllergens.keys()
   allergens.sort()
   result = []
   for allergen in allergens:
      result.append(allAllergens[allergen])
   print "Q2: Canonical dangerous ingredients {}".format(','.join(result))

def findCommonValsInLists(p):
   result = set(p[0])
   for s in p[1:]:
      result.intersection_update(s)
   return list(result)

inputData = [
   'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
   'trh fvjkl sbzzf mxmxvkd (contains dairy)',
   'sqjhc fvjkl (contains soy)',
   'sqjhc mxmxvkd sbzzf (contains fish)',
]
main(inputData)

inputData = [
   'gjqt bxfbb dcqtc xbbcnx bsjqq zzjt svzg gnrpml pmm shh vmhqr fgngbms tbmn djdgk mlmf snxvqf fnks cqkrlq zchcj vfvtj rdffqv mkrf xgftsb xrmxxvn txrjf vqxtr rxqd sqsmc qjcn spmsczc vqjct fhcpkt lvn vcpk mlxh xfhbfvp vrxp zjptr shltgt vmftt mhbxmfq jzs bgclkbpr lcpkxl lnjrvsz lhpgn nd xvn rfqqg mnjlf hhst vs fxbx jpfq ptjhk pnm vdgj dcj nvfkp zhtq xqvz hvllxq rdfr qxfzc jcb vtrf jxh pqxx vtrqn xntpv dcxncsm vjqr bfncxv frbq hkhkjm khpdjv ldgs nkff bdvkpj vgbz cbmvcj (contains peanuts)',
   'rszfj qblrk lnjrvsz qfffx shh ttrjb bdvkpj lmfr jpb rgx jxxgtl qxfzc mlxh vrxp jxh fhcpkt rdfr spmsczc gnrpml xrmxxvn jncbh hvllxq vspsdz zbjjnvn qtz jpfq nd khpdjv xgftsb pbpgl xhqh vdgj qjkng lrlgmm nvfkp pxjhvr bxfbb ffgkmhh lpgvh nhqljxg xcx dltgm snxvqf ljgmg vmhqr gnvg vmftt vqxtr (contains peanuts, nuts, dairy)',
   'xrmxxvn cqkrlq mlmf gnrpml dcqkt rdfr jxxgtl xgftsb bksvfq vs kpmnz pxjhvr rfmvh jpb vmhqr szztlx vdgj lkbnjx lpxc qjcn qjkng ctbjc qblrk fxbx rpsnkz xrqrlb ldgs jxh lpgvh mlxh shh zbjjnvn hqmkj lnjrvsz vqxtr zjptr qfffx rlqgq qvtfr frbq txrjf vmftt bdvkpj dcqtc vfvtj lxcxp jncbh vrxp xcx gknhqs knhvxg hfkxc nvfkp tbmn vspsdz ltrzm jndzl prdtb tpgtm qxfzc nktph jpfq pnm kjhdl vgldq qslbqf djdgk xntpv ttrjb qmzn thgljm znrb nd gjqt (contains eggs)',
   'qjcn rmhh dcj hvllxq czn ffgkmhh rdfr mlmf rfmvh jncbh qdtfkcls vgldq gnrpml snxvqf shh rbcp bgclkbpr rzddk qfnhsjj dlr cmzz xqvz jxh fnks lhpgn vmhqr ntqss tzkf nktph mnjlf frbq txrjf qxfzc pkmbb qtz dltgm bsjqq qblrk lmfr xrmxxvn cbmvcj vdgj rlqgq kfttq tdmfz ttrjb bxfbb tbmn qvtfr vjqr pnm rszfj lvn fhcpkt xbbcnx sqsmc nd nxs xcx qgvhn rxvc (contains nuts, sesame, wheat)',
   'zqrg tbmn kjhdl vqjct vtrqn xqvz dclkt vqxtr zdrptcx bgfc ffgkmhh rfmvh nktph vrjh lhpgn vdgj kdxs rdffqv jpb lmfr nd jxxgtl tdmfz bsjqq jpfq qslbqf rfqqg gjqt shltgt gksqg jzs ljgmg vxcdsr dcj cqkrlq jxh gckzr qgvhn zzjt xrmxxvn vcpk mltp lcpkxl gnrpml bfncxv dcqkt cpcxj spmsczc rzddk qjcn rdfr gknhqs qxfzc qvtfr gbxsxs pgkm txrjf vs tppnl bkls svzg pxctl ptjhk khpdjv zhtq qfnhsjj tdvzl jcb lxcxp xhqh qblrk pqxx bxfbb lpxc dcqtc (contains fish, wheat)',
   'xrmxxvn pxjhvr vjqr bvvkd gnrpml jndzl bcpks vqjct dcqkt vgbz rdfr hrxjrg lmfr gjqt sqsmc xfhbfvp qgvhn rxvc hfkxc mfqrl mlxh rgx ljgmg fnks szztlx lpgvh tzkf jxh rszfj rxqd qxfzc qjkng skzxjnc vmftt dclkt vmhqr bsjqq zhtq vfvtj jncbh vspsdz qtz mrffh plpl rfmvh gknhqs (contains dairy)',
   'vfvtj dvd svzg dbvqq fhcpkt lkbnjx rfmvh vqjct gbxsxs gckzr mhbxmfq gnrpml pbpgl mltp qslbqf jvcjhg sqsmc hqmkj jzs mrffh rdfr gnvg tbmn xcx vmhqr czn nd bsjqq bgclkbpr rpsnkz lxcxp rxvc vqxtr fgngbms ntqss xfhbfvp tkg khpdjv vs jrr dclkt cddpfxx hvllxq xrmxxvn rgx lpgvh mlmf flr ctbjc bkls rrtlfh cpcxj xqvz zhtq tpgtm jxh vjqr pxjgxr bxfbb shrnc zdrptcx dcxncsm jpfq gxlzr mnjlf (contains wheat, soy)',
   'pkmbb qkggr plpl tpgtm mkrf hrxjrg szztlx mfqrl qgvhn rzddk gbxsxs fgngbms xcx xhqh rxvc rpsnkz lkbnjx zjptr cqkrlq spmsczc nvfkp pnm rblnlnk nktph khpdjv bqt shrnc mzdlxl dclkt jvcjhg jxxgtl vcpk vtrf vdgj lmfr rmhh rfmvh gnrpml bxfbb hhst xrmxxvn tzkf jpfq dcqkt bvvkd fxbk vs rdfr gknhqs nkff hfkxc djmfxp pbpgl jcb shltgt tlrpk hvllxq rbcp qxfzc zchcj dltgm gpg cbmvcj mlmf dbvqq dcxncsm shh vqjct vmhqr ltrzm nnsnh qmzn tkg fnks vjqr tdmfz vgldq (contains sesame, dairy, peanuts)',
   'rdffqv mrffh thgljm dcxncsm qkggr qblrk dcqtc bgclkbpr nxs tppnl hkhkjm gpg tpgtm xfhbfvp nktph bqt qslbqf ldgs jxxgtl qfnhsjj jxh lkbnjx xrmxxvn qxfzc khpdjv dcj knhvxg pxjhvr djmfxp gksqg vmftt sqsmc jncbh hfkxc fnks gnrpml pxjgxr zhtq txrjf mhbxmfq rgx lhpgn vspsdz vqjct svzg qfffx frbq lrlgmm nkff zhxvv vqxtr ptjhk bdvkpj vgldq nhqljxg xrqrlb cmzz dltgm rpsnkz bfncxv flr fgngbms tkg fxbk cqkrlq qgvhn qdtfkcls rdfr rfmvh xcx gnvg snxvqf kpmnz tdmfz mltp (contains wheat, nuts)',
   'hkhkjm rfmvh dbvqq fxbx bgfc gbxsxs vmhqr lkbnjx hvllxq pbpgl rxqd frbq vjqr bxfbb ffgkmhh ctbjc xqvz bdvkpj mlmf rmhh lhpgn rzddk cpcxj jpfq vfvtj rpsnkz dltgm vgbz bpkh svzg gnrpml fxbk vrjh czn vrxp vspsdz gckzr szztlx shrnc hrxjrg lmfr pxctl bcpks xvn nd ldgs ldpkn xfhbfvp mfqrl qgvhn khpdjv pnm xrmxxvn nktph mnjlf mrffh rdfr rblnlnk kdxs sqsmc gpg prdtb mhbxmfq bgclkbpr gjqt kpmnz ttrjb vgldq pkmbb shltgt dlr tdmfz nhqljxg zhxvv zhtq jxh thgljm gnvg dvd fsfhp vs rlqgq (contains peanuts)',
   'djdgk jpb vmhqr tbmn vgldq vtrqn lrlgmm lhpgn rlqgq rblnlnk xntpv mrffh dltgm zchcj xrqrlb kfttq rxvc rdfr qmzn qblrk gxlzr fxbx bxfbb lxcxp xrmxxvn qfffx khpdjv plpl tdmfz qslbqf pxjhvr lpxc pbpgl mkrf gksqg vqxtr zhtq jzs dlr dbvqq bcpks cddpfxx hkhkjm gnrpml qtz rzddk mnjlf qgvhn bpkh hhnxvg jxh pgkm pkmbb frbq pmm dcxncsm vs jpfq nhqljxg xfhbfvp cqkrlq mhbxmfq qjkng qxfzc rrtlfh qvtfr djmfxp zhxvv jndzl xbbcnx (contains eggs, soy)',
   'rxvc fgngbms jxh plpl qxfzc vtrqn qjcn lkbnjx mlxh ntqss xvn nnsnh tbmn gxlzr rdfr dcqtc xfhbfvp dlr txrjf gnrpml rfmvh vdgj rdffqv ldgs jpfq rmhh gpg hhnxvg dclkt vxcdsr vmhqr cddpfxx vspsdz jndzl qgvhn zchcj ldpkn sqsmc zqrg mlmf bgclkbpr rxqd lmfr rgx nxs snxvqf nhqljxg dvd jxxgtl qtz tlrpk nvfkp qjkng fxbx qkggr xrmxxvn (contains sesame, nuts)',
   'xrmxxvn jndzl szztlx cpcxj rfmvh rzddk vmhqr sqsmc xhqh zhxvv hqmkj rdfr zzjt xntpv tzkf tdvzl jpfq nd gckzr lpgvh bfncxv lnjrvsz fnks jxh ffnq jxxgtl gxlzr ttrjb shh spmsczc ldpkn hvllxq fhcpkt gnrpml mfqrl dltgm hhnxvg qdtfkcls dbvqq kjhdl thgljm czn vqjct knhvxg dvd rpsnkz rxvc khpdjv vgbz kpmnz lkbnjx (contains nuts, dairy)',
   'fsfhp thgljm jxxgtl xfhbfvp rdfr ldpkn vrxp tpgtm hfkxc rblnlnk jpb rlqgq qxfzc djmfxp dbvqq mhbxmfq gckzr lnjrvsz pgkm bpkh gnrpml vmftt vmhqr rzddk rfmvh pkmbb tzkf tdvzl qvtfr ffgkmhh xgftsb bkls hkhkjm vfvtj skzxjnc mlmf rmhh rdffqv qtz knhvxg vtrqn qblrk ptjhk dcxncsm ntqss fgngbms jvcjhg svzg mzdlxl rrtlfh lkbnjx sqsmc bvvkd xntpv lxcxp mrffh jxh frbq khpdjv nkff fxbk jndzl gksqg hvllxq bgclkbpr qfnhsjj kjhdl jrr nvfkp dvd mfqrl qkggr mnjlf nd bcpks hhnxvg nnsnh vrjh xhqh qmzn (contains wheat, dairy, eggs)',
   'rblnlnk spmsczc tlrpk nxs xntpv hhst mzdlxl lxcxp qkggr dbvqq gnrpml sqsmc bpkh rdfr knhvxg skzxjnc mfqrl rpsnkz lpgvh rlqgq nd tkg hkhkjm bxfbb zchcj zzjt nvfkp dcqkt vfvtj dltgm xrmxxvn vmhqr xbbcnx rszfj lkbnjx mlxh khpdjv fxbk jncbh bcpks qvtfr rfmvh vqxtr rgx pgkm rmhh fnks jcb vgbz cqkrlq lmfr zjptr cpcxj djmfxp kdxs hrxjrg dvd vtrqn kjhdl kfttq qxfzc bkls dlr qfffx xhqh qslbqf flr ptjhk fgngbms gckzr shh (contains soy, eggs, nuts)',
   'bfncxv snxvqf hfkxc prdtb khpdjv pxctl dcj plpl xhqh lmfr tlrpk ptjhk vgbz ffnq mkrf hkhkjm lxcxp gxlzr zhtq dclkt qblrk vspsdz pnm zchcj rfmvh tbmn rxqd rrtlfh hvllxq nktph qfffx rmhh bdvkpj nhqljxg vxcdsr mzdlxl gksqg gbxsxs xqvz vgldq vmhqr mnjlf gnrpml xrmxxvn txrjf ljgmg bkls lrlgmm jndzl rpsnkz jxh thgljm djdgk qxfzc shh dcqkt ntqss (contains fish, nuts, peanuts)',
   'tpgtm qgvhn pnm vmftt rszfj bkls hhnxvg mlxh gksqg ttrjb ljgmg rxqd pxjgxr djmfxp sqsmc tbmn qdtfkcls dcj jvcjhg mlmf czn qxfzc snxvqf hhst vqxtr mkrf fxbk zchcj gnrpml nhqljxg nvfkp tdmfz nnsnh nd shltgt xrmxxvn vtrf bsjqq lvn gknhqs dcqtc qblrk dlr zhxvv jzs shrnc svzg rfmvh dclkt bksvfq rbcp cddpfxx jcb vmhqr jxh dbvqq bgclkbpr skzxjnc rdfr (contains soy)',
   'flr vtrqn mkrf jcb jxh xcx nvfkp lrlgmm pkmbb dcxncsm rxvc vtrf xqvz rzddk vcpk rdfr vmhqr ldpkn tdmfz fsfhp lpxc dbvqq rfmvh zjptr vqjct gnrpml gckzr gnvg khpdjv mltp mnjlf hqmkj lkbnjx rszfj gbxsxs vgbz pmm gksqg vspsdz qfnhsjj mlxh tbmn shltgt lxcxp pqxx ptjhk mzdlxl dvd tppnl bvvkd ltrzm qxfzc nhqljxg (contains dairy, nuts)',
   'rrtlfh nxs xhqh hkhkjm tbmn jzs dltgm bgfc pnm gjqt cqkrlq zhxvv jrr kjhdl vjqr qslbqf khpdjv ctbjc xcx mzdlxl hfkxc vqxtr jvcjhg qmzn jndzl frbq fxbx shrnc zjptr lpgvh vxcdsr qfnhsjj lkbnjx plpl gnrpml fhcpkt pxctl qvtfr qdtfkcls gbxsxs mfqrl rfmvh fnks dbvqq shltgt vfvtj pmm lmfr vtrqn rdfr ntqss zdrptcx lhpgn nhqljxg xgftsb xrqrlb bfncxv kfttq bkls lcpkxl mrffh xrmxxvn bgclkbpr dcqkt szztlx dclkt vmhqr qxfzc snxvqf dcqtc bqt rblnlnk pxjgxr gpg jncbh xntpv kdxs dvd xvn (contains eggs, fish, nuts)',
   'shh dcxncsm vqxtr vxcdsr gjqt zjptr vqjct xntpv zhxvv bsjqq rbcp snxvqf vmhqr rfqqg khpdjv rblnlnk lmfr fnks lkbnjx mltp shrnc mfqrl jpb skzxjnc dcj ntqss gnrpml rlqgq jzs bpkh vjqr cddpfxx jcb lpxc pgkm xrmxxvn rdfr pkmbb dltgm qjkng zbjjnvn xrqrlb rpsnkz gksqg vtrf jrr gpg knhvxg plpl jvcjhg bgfc vdgj tlrpk znrb vmftt tzkf jxh nd xcx lcpkxl fgngbms vspsdz mhbxmfq bxfbb qxfzc thgljm (contains wheat, peanuts)',
   'bvvkd bfncxv qfnhsjj vqxtr lrlgmm rbcp rfmvh tdvzl spmsczc lxcxp lhpgn dcxncsm qdtfkcls rdfr nvfkp vs kpmnz jxh rpsnkz pxctl gckzr zhtq ltrzm qslbqf khpdjv vtrf tlrpk vmhqr rzddk qtz rfqqg hqmkj mzdlxl vxcdsr sqsmc qxfzc bksvfq zjptr qfffx bsjqq bkls fxbx dcqtc hfkxc vcpk qblrk fgngbms jndzl pkmbb lpgvh qjcn fxbk ttrjb zdrptcx lpxc lcpkxl gbxsxs bdvkpj jncbh xvn xfhbfvp gnvg pnm lmfr bqt kjhdl hvllxq xrmxxvn (contains eggs, sesame)',
   'jpb jxh tbmn spmsczc vmhqr zchcj xhqh jvcjhg zhxvv qmzn xntpv vfvtj knhvxg dcxncsm mlmf nvfkp djmfxp sqsmc rdfr bsjqq tdvzl rbcp tpgtm xcx dbvqq ptjhk cqkrlq cbmvcj flr shrnc qslbqf tkg rfmvh ffnq gnrpml lpxc rxvc ltrzm qfffx qxfzc rxqd gksqg khpdjv ttrjb (contains sesame, wheat, dairy)',
   'kpmnz zdrptcx vfvtj rlqgq gbxsxs djdgk rdfr ptjhk nkff gksqg rfqqg tbmn dlr mfqrl qxfzc nxs djmfxp vmhqr dcqtc lhpgn skzxjnc pxjgxr kfttq lmfr fxbk svzg szztlx vqxtr dltgm snxvqf gnrpml kdxs ctbjc ltrzm pkmbb xfhbfvp xrqrlb nktph fsfhp ntqss rfmvh pnm tdmfz nhqljxg vcpk vrxp thgljm xrmxxvn lkbnjx hqmkj flr rxvc nvfkp khpdjv qvtfr vqjct bcpks qdtfkcls vgbz vtrqn (contains sesame)',
   'dclkt zchcj khpdjv rzddk bcpks jzs dlr qdtfkcls pbpgl pnm sqsmc vs nhqljxg xrmxxvn qtz tdmfz nnsnh snxvqf gnrpml qfffx pxjhvr jcb cddpfxx gksqg rdffqv mnjlf rrtlfh gknhqs rfmvh vspsdz zhtq tkg qjkng gbxsxs jxh mhbxmfq fxbx fsfhp fxbk cbmvcj rfqqg nd dvd vqxtr zzjt spmsczc tdvzl hrxjrg ctbjc vmhqr vcpk hhst qmzn frbq qgvhn tbmn lpxc kpmnz rdfr ffnq znrb bvvkd szztlx zdrptcx (contains nuts)',
   'nxs pbpgl qblrk ldpkn jcb svzg dltgm gxlzr lxcxp dcqkt dclkt jxh khpdjv bgfc ljgmg tdvzl vs qfffx hqmkj hvllxq lrlgmm lpxc ptjhk pxctl prdtb lhpgn pxjhvr spmsczc cqkrlq mltp vjqr rgx qkggr gpg mnjlf nvfkp fsfhp xvn dcj vtrf rlqgq vgldq fhcpkt fxbx dcqtc qjcn kpmnz jpb czn thgljm vxcdsr qdtfkcls ldgs frbq vrxp bcpks qjkng xrmxxvn pgkm fgngbms gknhqs ntqss tkg qxfzc rszfj rxvc qvtfr rzddk rfmvh lcpkxl xqvz gnrpml bpkh bqt rdfr jxxgtl lnjrvsz mlmf (contains eggs, soy)',
   'gjqt vfvtj rgx shltgt dvd tpgtm xqvz bfncxv lmfr fnks ltrzm sqsmc qmzn jncbh hkhkjm lvn pxjgxr jndzl qxfzc rxvc tbmn xgftsb gnrpml pbpgl qtz fxbk nkff szztlx rdffqv txrjf bksvfq rdfr mrffh vspsdz gknhqs jxh vmhqr rfmvh xrmxxvn xntpv dbvqq xbbcnx ntqss mltp nnsnh lhpgn tdmfz mkrf rlqgq lpgvh xhqh zchcj tppnl (contains nuts)',
   'xqvz zzjt gxlzr zdrptcx qdtfkcls qblrk hqmkj qxfzc fnks hfkxc vmftt rfmvh pxjgxr rblnlnk gnrpml xcx rxvc mnjlf vrxp bqt fhcpkt dcqkt pbpgl dcxncsm bgclkbpr vmhqr xrmxxvn rdfr tlrpk khpdjv rgx kpmnz mkrf gckzr mrffh fxbx jzs (contains nuts)',
   'pnm mlmf jxh zhtq lmfr hfkxc fxbx bvvkd zhxvv qmzn qxfzc gjqt vdgj lpxc bpkh sqsmc lrlgmm vfvtj vjqr rzddk vmhqr qjkng spmsczc dltgm tkg cpcxj rblnlnk mlxh svzg mnjlf vxcdsr gnrpml khpdjv qblrk rdffqv bsjqq rmhh rgx mhbxmfq bgfc rszfj qslbqf lhpgn pxjgxr lpgvh shh xrmxxvn gckzr kdxs tpgtm snxvqf kjhdl dcxncsm hrxjrg pgkm jzs vspsdz czn djmfxp xrqrlb rfmvh ctbjc lvn jpfq xfhbfvp zdrptcx qdtfkcls bxfbb nvfkp qvtfr pxjhvr (contains fish, wheat)',
   'mrffh prdtb vqxtr pqxx hrxjrg vgbz vmhqr jxh kfttq znrb rfmvh bkls pgkm bdvkpj qxfzc ldgs lnjrvsz pkmbb dcxncsm lpxc jpb shh pxjhvr qmzn lmfr skzxjnc lrlgmm vtrf mlmf bgclkbpr khpdjv gnrpml fnks zqrg ffnq bksvfq ntqss vqjct cmzz gknhqs tpgtm dcqkt vcpk knhvxg hqmkj hkhkjm snxvqf mfqrl tppnl jndzl bcpks dclkt rdfr bqt mltp frbq xvn djmfxp tdmfz bgfc jrr gckzr rbcp qjkng fhcpkt mhbxmfq ldpkn qfffx czn fgngbms jcb (contains fish, soy, dairy)',
   'zjptr rfmvh xntpv lxcxp znrb djdgk lpxc pgkm khpdjv fsfhp rmhh hfkxc pbpgl hhnxvg gknhqs qfffx gjqt nktph vgbz gksqg zbjjnvn cmzz qgvhn fxbk bdvkpj lkbnjx vjqr rrtlfh zchcj vcpk vrjh qblrk gbxsxs fxbx rdfr xhqh bcpks bsjqq pkmbb tdvzl hkhkjm xrqrlb dcqkt qslbqf jvcjhg zhxvv rgx thgljm mlxh bksvfq zqrg rxqd dbvqq bgfc ljgmg pxjgxr dcj shh mlmf xcx dcqtc ffnq rbcp vdgj dvd jncbh gpg tkg qfnhsjj jpfq pxctl qxfzc xrmxxvn jzs gnrpml vmhqr fnks tppnl ldpkn (contains peanuts)',
   'szztlx tdvzl rszfj jxxgtl nd pxjgxr gpg bgfc mfqrl qxfzc fhcpkt ltrzm bpkh jpb dcxncsm ldgs jxh pbpgl sqsmc lhpgn zdrptcx rfqqg bgclkbpr tdmfz bvvkd xgftsb hfkxc vrxp lvn rfmvh cbmvcj ljgmg rxqd gnrpml xbbcnx fgngbms qslbqf vqjct rbcp pxctl cmzz dcj zbjjnvn bcpks dclkt cpcxj mhbxmfq vcpk rxvc mzdlxl qgvhn gckzr fnks rdfr snxvqf qvtfr bfncxv vqxtr rlqgq kjhdl lmfr xrmxxvn dvd mkrf khpdjv mlxh gnvg hhnxvg flr vrjh lnjrvsz kfttq (contains nuts, peanuts, sesame)',
   'vxcdsr pmm dcj vmftt bgfc rxqd ttrjb nxs xrmxxvn kfttq qslbqf djmfxp dlr bgclkbpr cbmvcj xntpv bpkh gjqt shh kdxs xcx gckzr hvllxq rblnlnk jncbh jxh khpdjv flr dctqb cpcxj lcpkxl qxfzc zjptr xvn vtrf gknhqs qjkng kjhdl rfmvh tdvzl gnrpml nnsnh zchcj pxctl vrxp lxcxp fnks czn qvtfr gbxsxs bxfbb djdgk ffnq rdfr bsjqq pqxx jpb vqjct plpl (contains fish, soy)',
   'qmzn rfmvh rfqqg hvllxq lcpkxl dcqkt mlmf vtrqn kdxs gckzr rlqgq shrnc jncbh zzjt lpgvh rdfr frbq tdmfz vs vqxtr zhtq nktph ffgkmhh vqjct rrtlfh xcx vdgj zhxvv cmzz thgljm jpfq kpmnz gnrpml xrmxxvn vmhqr fhcpkt rpsnkz pgkm ntqss txrjf fnks nnsnh hqmkj tpgtm vgbz ctbjc xqvz lxcxp qvtfr qxfzc zqrg khpdjv lrlgmm jrr cbmvcj ldpkn rbcp vjqr (contains soy)',
   'rlqgq rblnlnk bxfbb xcx bkls mlxh ljgmg zbjjnvn mkrf ffgkmhh svzg cmzz dcqkt qslbqf mlmf vgbz prdtb tlrpk nnsnh qfffx lpgvh txrjf cqkrlq bqt tdmfz rfmvh rdffqv jrr jzs fhcpkt fsfhp qxfzc vmhqr shrnc bsjqq ldpkn lcpkxl vjqr vqjct jndzl skzxjnc bvvkd pgkm bdvkpj gnrpml bcpks rdfr bksvfq qtz gjqt qkggr dlr pxctl xrmxxvn kjhdl jxh (contains nuts)',
   'gjqt vtrf vrjh djmfxp rdfr hhst mnjlf vrxp pmm rdffqv bcpks ctbjc lpgvh vxcdsr qfnhsjj jncbh xqvz dctqb kjhdl nnsnh gnrpml zjptr hvllxq cmzz lmfr qxfzc nd vmhqr ptjhk hrxjrg qfffx lnjrvsz cddpfxx ljgmg xfhbfvp qkggr hhnxvg tdmfz qgvhn khpdjv plpl jxxgtl rlqgq dbvqq szztlx nvfkp mhbxmfq knhvxg cpcxj rpsnkz mzdlxl jxh bfncxv xrmxxvn jpfq mlxh nkff vtrqn fhcpkt bsjqq prdtb jzs flr (contains soy, eggs)',
   'rzddk mnjlf djmfxp bxfbb vrjh xrmxxvn gnrpml rfqqg mlxh dcxncsm xvn czn hhst jpfq qxfzc vqjct vdgj lnjrvsz mrffh rszfj vrxp rdfr shh cbmvcj frbq shrnc xcx khpdjv djdgk dctqb hvllxq ntqss dltgm shltgt spmsczc nktph tppnl bksvfq gknhqs mzdlxl tpgtm hrxjrg ldgs nxs pkmbb xqvz vfvtj rfmvh hfkxc sqsmc knhvxg lmfr tzkf jxh tkg vcpk rbcp nkff nhqljxg hkhkjm xhqh lvn pbpgl mltp qblrk pgkm (contains peanuts)',
   'cmzz qfnhsjj kdxs gpg ldgs vxcdsr znrb qdtfkcls dctqb svzg gbxsxs jxh kjhdl vtrqn ffgkmhh mnjlf nnsnh pqxx zdrptcx bxfbb lnjrvsz xrmxxvn rpsnkz dcqkt dcj cpcxj rfmvh qgvhn bqt pgkm ptjhk jpfq jzs rmhh fhcpkt qxfzc nktph qmzn mlmf qblrk nxs nkff xbbcnx djmfxp gnrpml mzdlxl bksvfq tlrpk thgljm rgx vrxp rdfr dcqtc mlxh vqjct nhqljxg ctbjc lhpgn xhqh ldpkn pbpgl fnks jvcjhg bvvkd vmhqr jrr nvfkp hvllxq (contains eggs, peanuts)',
   'xhqh cbmvcj hhnxvg dcqtc khpdjv vmhqr nvfkp flr gpg ntqss rxqd bgclkbpr bsjqq mrffh thgljm jpb gjqt lnjrvsz txrjf lpgvh rdfr vfvtj bgfc bksvfq gnvg rdffqv fhcpkt pbpgl gckzr jxh tlrpk xrmxxvn ltrzm jndzl czn ctbjc qvtfr bdvkpj gnrpml pgkm vgbz qxfzc bqt tpgtm szztlx ffgkmhh dcqkt qtz qmzn zqrg rblnlnk mfqrl plpl mltp hkhkjm vgldq pqxx zjptr rmhh xbbcnx qkggr djmfxp (contains dairy, soy)',
   'rfqqg pbpgl vqjct lhpgn khpdjv cddpfxx gnvg xgftsb mltp xntpv kdxs sqsmc gjqt fhcpkt vmhqr nd pnm mnjlf mlmf szztlx fxbk qjkng snxvqf hvllxq xcx frbq bkls skzxjnc gnrpml zhtq ffgkmhh svzg ntqss xrmxxvn vtrqn qxfzc fgngbms rdfr rfmvh dcqkt hrxjrg thgljm gksqg (contains fish, sesame)',
   'vtrf tkg xrmxxvn tzkf rlqgq lnjrvsz bxfbb vcpk rgx pnm nd rfmvh lhpgn vxcdsr fhcpkt qtz lcpkxl jxh nkff gnrpml vrjh rdfr vdgj jvcjhg jcb fxbk rbcp gjqt bfncxv dclkt ffgkmhh zhtq gksqg sqsmc vmhqr mhbxmfq knhvxg ttrjb qblrk bkls gknhqs zzjt zjptr pkmbb gpg lkbnjx mkrf xhqh vgldq rxvc ptjhk skzxjnc czn lrlgmm ltrzm mfqrl qjkng rszfj bgclkbpr bqt jndzl hkhkjm bdvkpj pxjhvr rxqd mlmf vtrqn lmfr bcpks mrffh qvtfr shltgt cpcxj djmfxp ctbjc hhnxvg pbpgl zhxvv kfttq pqxx xbbcnx nhqljxg nxs znrb dcxncsm qxfzc vmftt jxxgtl xfhbfvp (contains wheat)',
   'mkrf znrb pkmbb kpmnz gckzr mnjlf pxjgxr fsfhp shrnc jncbh txrjf nktph rdfr gxlzr xqvz kjhdl gjqt dltgm qxfzc plpl vgbz xgftsb qfffx fxbk rpsnkz frbq rbcp cddpfxx prdtb jxh vjqr tdvzl bcpks dcxncsm vspsdz gknhqs tkg qkggr gnvg rxvc khpdjv rfqqg qvtfr dbvqq hvllxq ltrzm xntpv bpkh gnrpml kfttq lcpkxl rfmvh xrmxxvn vxcdsr cmzz rmhh ptjhk ljgmg (contains soy)',
   'gxlzr qxfzc ltrzm jxh hhst qgvhn bgfc rzddk rfmvh tppnl vmhqr lvn vqjct rdfr lhpgn gjqt xgftsb cqkrlq vdgj lnjrvsz vgldq qjcn rszfj qfffx pxjhvr gnrpml ttrjb xrmxxvn lcpkxl djdgk dctqb ldgs rxqd qfnhsjj zqrg qmzn vtrqn bdvkpj pkmbb mfqrl pnm bfncxv mzdlxl zzjt dclkt xrqrlb shrnc ffnq mrffh shh knhvxg hfkxc pxctl mnjlf djmfxp fgngbms znrb fxbx tzkf cmzz svzg vcpk rblnlnk (contains sesame, dairy)',
   'xrmxxvn rdfr czn zhxvv gnrpml qfffx lxcxp lrlgmm pqxx txrjf khpdjv vdgj pgkm mltp vtrf cqkrlq kdxs vmhqr xntpv rrtlfh tzkf qxfzc tkg dltgm vgbz bgclkbpr bdvkpj qkggr qslbqf jrr pkmbb ltrzm rfmvh fxbx ptjhk ldpkn tlrpk bvvkd hfkxc nvfkp (contains sesame, fish, nuts)',
   'skzxjnc lkbnjx mlmf lpgvh rpsnkz thgljm dlr vmhqr tzkf tppnl jpfq pgkm rdfr mlxh vjqr qmzn rblnlnk vqxtr dcj bqt gckzr ljgmg nd czn tdvzl rfmvh gnrpml gbxsxs hhst xbbcnx pkmbb jxh lrlgmm rgx ldpkn djmfxp qxfzc tkg bcpks jzs zzjt kdxs qkggr tpgtm vspsdz zbjjnvn bdvkpj xrmxxvn qvtfr bfncxv mhbxmfq mnjlf dbvqq rmhh gxlzr (contains eggs, sesame)',
   'gksqg qxfzc lxcxp kfttq dvd frbq vtrqn cbmvcj qvtfr tbmn rmhh vcpk rrtlfh qgvhn khpdjv jxh lhpgn gpg rpsnkz vfvtj ntqss zqrg bksvfq zzjt kdxs cqkrlq jzs thgljm shh hhnxvg dcqtc zchcj sqsmc dclkt bqt fgngbms vmhqr tpgtm nhqljxg bkls jxxgtl tppnl bpkh kpmnz vjqr bdvkpj flr ffnq skzxjnc xcx ptjhk zbjjnvn hkhkjm bxfbb jncbh lmfr nvfkp lkbnjx dcxncsm rdffqv rdfr pkmbb vqjct rlqgq mrffh jvcjhg jcb nkff rfmvh rzddk vrxp vspsdz cpcxj pnm gnrpml mlmf vtrf ltrzm rxvc fhcpkt xbbcnx (contains fish)',
]
main(inputData)

