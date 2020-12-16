#!/usr/bin/python

import copy
import re
import math

def main(data):
   rules = [[x.split(':')[0], x.split(':')[1].split(' ')[1].split('-'), x.split(':')[1].split(' ')[3].split('-')] for x in data[0]]
   myTicket = data[1][1].split(',')
   allTickets = [x.split(',') for x in data[2][1:]]
   invalidNumbers = []
   validTickets = []
   for ticket in allTickets:
      result = getInvalidNumbers(ticket, rules)
      if len(result) > 0:
         for i in range(len(result)):
            invalidNumbers.append(int(result[i]))
      else:
         validTickets.append(ticket)
   print "Q1: {}".format(sum(invalidNumbers))
   tmpName(validTickets, myTicket, rules)

def getInvalidNumbers(ticket, rules):
   validTicket = [False]*len(ticket)
   for i in range(len(ticket)):
      for rule in rules:
         for ruleRange in rule[1:]:
            if int(ticket[i]) in range(int(ruleRange[0]), int(ruleRange[1])+1):
               validTicket[i] = True
   return [x[1] for x in zip(validTicket, ticket) if not x[0]]

def tmpName(tickets, myTicket, rules):
   ticketCols = []
   for i in range(len(tickets[0])):
      ticketCols.append(zip(*tickets)[i])
   for i in range(len(ticketCols)):
      ticketCols[i] = list(ticketCols[i])
      ticketCols[i].append(myTicket[i])
   ruleDict = {}
   for rule in rules:
      ruleName = rule[0]
      ruleDict[ruleName] = []
      ruleRanges = rule[1:]
      for i in range(len(ticketCols)):
         inRange = True
         for k in ticketCols[i]:
            if int(k) not in range(int(ruleRanges[0][0]), int(ruleRanges[0][1])+1) and int(k) not in range(int(ruleRanges[1][0]), int(ruleRanges[1][1])+1):
               inRange = False
         if inRange:
            ruleDict[ruleName].append(i)
   keyToChange = 'tmp'
   while keyToChange != '':
      keyToChange = ''
      for r in ruleDict.keys():
         if len(ruleDict[r]) == 1:
            tmpDict = copy.deepcopy(ruleDict)
            tmpDict.pop(r, None)
            if any(ruleDict[r][0] in sublist for sublist in tmpDict.values()):
               keyToChange = r
      if keyToChange != '':
         for r in ruleDict.keys():
            if r != keyToChange and ruleDict[keyToChange][0] in ruleDict[r]:
               ruleDict[r].remove(ruleDict[keyToChange][0])
   for r in ruleDict.keys():
      ruleDict[r] = ruleDict[r][0]
   res = 1
   for r in ruleDict.keys():
      if r.split(' ')[0] == 'departure':
         res *= int(myTicket[int(ruleDict[r])])
   print "Q2: {}".format(res)

inputData = [
   [
      "class: 1-3 or 5-7",
      "row: 6-11 or 33-44",
      "seat: 13-40 or 45-50"
   ],
   [
      "your ticket:",
      "7,1,14"
   ],
   [
      "nearby tickets:",
      "7,3,47",
      "40,4,50",
      "55,2,20",
      "38,6,12"
   ]
]

inputData = [
   [
      "class: 0-1 or 4-19",
      "row: 0-5 or 8-19",
      "seat: 0-13 or 16-19"
   ],
   [
      "your ticket:",
      "11,12,13",
   ],
   [
      "nearby tickets:",
      "3,9,18",
      "15,1,5",
      "5,14,9"
   ]
]
main(inputData)

inputData = [
   [
      "departure location: 32-615 or 626-955",
      "departure station: 47-439 or 454-961",
      "departure platform: 31-98 or 119-969",
      "departure track: 45-746 or 763-967",
      "departure date: 49-723 or 736-954",
      "departure time: 42-556 or 581-962",
      "arrival location: 46-401 or 418-964",
      "arrival station: 39-281 or 295-974",
      "arrival platform: 43-80 or 99-950",
      "arrival track: 28-670 or 682-959",
      "class: 43-504 or 520-957",
      "duration: 31-358 or 365-959",
      "price: 41-626 or 650-956",
      "route: 26-488 or 495-949",
      "row: 46-913 or 931-965",
      "seat: 40-223 or 249-958",
      "train: 32-832 or 853-966",
      "type: 36-776 or 798-960",
      "wagon: 38-122 or 134-969",
      "zone: 27-870 or 885-952"
   ],
   [
      "your ticket:",
      "191,61,149,157,79,197,67,139,59,71,163,53,73,137,167,173,193,151,181,179"
   ],
   [
      "nearby tickets:",
      "482,948,368,336,171,501,192,438,384,499,692,331,527,624,344,859,351,902,213,615",
      "391,405,942,203,174,467,611,553,65,544,349,899,221,264,547,800,942,144,738,304",
      "470,497,358,169,599,613,804,342,820,865,594,58,825,167,362,771,269,768,706,765",
      "891,526,368,191,296,295,270,497,735,378,351,688,317,186,526,896,813,544,683,72",
      "544,396,163,686,911,137,59,322,884,586,597,223,692,525,316,704,483,72,683,745",
      "712,763,626,594,555,377,440,651,945,693,500,51,281,475,948,817,687,314,320,189",
      "461,295,273,386,872,57,143,497,147,657,520,901,202,170,824,704,815,600,663,706",
      "670,215,74,607,159,862,389,266,61,250,127,320,193,592,687,167,769,147,555,653",
      "395,342,197,865,990,525,912,377,278,897,799,366,464,689,398,901,597,204,667,546",
      "550,936,205,686,886,340,183,800,251,905,338,605,486,945,343,141,935,903,155,110",
      "479,947,418,809,421,687,221,136,56,712,420,433,612,748,196,349,357,298,381,466",
      "126,370,66,341,939,530,501,886,626,664,275,250,55,250,270,175,63,80,520,419",
      "687,170,171,326,249,879,60,868,329,400,352,663,813,719,529,217,72,946,937,498",
      "895,173,393,147,439,525,489,827,137,942,684,454,499,525,832,178,597,78,714,298",
      "897,154,60,429,856,165,657,184,857,63,897,765,719,144,577,220,257,476,63,907",
      "797,866,541,712,307,589,539,683,689,895,908,473,556,496,54,949,143,173,765,60",
      "832,146,205,699,652,443,209,376,190,438,421,424,823,886,197,901,255,691,300,72",
      "997,591,435,945,943,811,485,465,399,652,382,51,387,484,692,911,535,696,705,336",
      "884,521,351,809,533,120,260,179,588,186,277,581,667,314,218,435,324,808,546,551",
      "292,350,51,805,344,461,670,57,342,389,551,310,217,767,160,938,662,599,908,420",
      "821,630,175,324,387,150,609,532,327,206,687,328,817,76,932,317,890,336,301,700",
      "453,433,251,708,775,461,775,276,460,524,469,583,67,626,896,858,521,367,309,315",
      "151,316,806,170,356,67,618,861,912,157,250,168,826,432,469,352,803,612,390,195",
      "534,704,886,600,552,313,367,897,59,804,496,361,154,722,436,859,375,209,74,169",
      "62,165,61,707,609,278,470,350,544,430,886,866,469,649,943,316,599,910,764,424",
      "698,334,61,212,688,979,745,688,656,420,356,141,66,384,193,421,828,767,277,718",
      "61,219,68,460,381,856,684,745,422,979,769,251,470,69,719,421,612,466,301,295",
      "799,670,325,419,824,258,767,58,295,853,803,211,55,120,555,129,334,154,530,181",
      "594,910,862,765,589,602,745,498,486,722,895,163,419,805,623,904,392,861,715,263",
      "853,145,132,320,254,652,658,260,169,768,311,711,150,668,346,366,279,178,188,467",
      "198,202,913,600,346,326,597,864,743,554,300,522,607,192,737,603,316,146,625,933",
      "702,90,345,655,463,853,608,541,389,272,653,330,864,885,657,859,484,831,259,310",
      "686,489,668,597,501,526,272,71,829,500,471,811,62,949,201,603,306,530,196,304",
      "491,482,822,600,603,523,136,177,252,208,378,435,212,525,194,488,67,698,717,475",
      "894,167,332,126,385,265,315,583,154,694,433,541,56,773,326,170,149,156,119,771",
      "223,460,377,480,975,814,582,534,611,385,524,373,769,340,154,396,175,260,302,868",
      "353,746,661,200,982,773,276,907,656,221,173,119,314,370,460,341,912,370,720,462",
      "305,334,251,186,766,557,766,772,706,392,799,170,721,58,708,198,765,457,776,205",
      "522,164,521,419,352,802,218,531,813,364,263,737,145,931,439,77,809,605,354,664",
      "66,697,63,655,321,481,651,887,931,422,342,375,372,878,863,220,165,597,423,465",
      "394,281,523,264,947,500,473,654,70,603,813,682,765,299,551,857,330,150,613,879",
      "317,400,277,717,147,310,705,615,317,136,812,503,582,377,333,335,539,544,4,303",
      "329,770,772,723,690,82,709,803,217,336,854,588,804,458,540,189,650,262,335,303",
      "58,932,827,541,556,806,119,423,334,313,204,893,203,864,182,814,714,528,315,360",
      "771,750,309,526,805,807,142,429,479,365,868,270,206,318,186,824,502,328,582,802",
      "168,155,581,767,434,438,934,815,939,303,743,313,373,902,705,947,339,310,225,771",
      "384,805,542,212,426,419,336,536,346,173,336,270,270,578,200,163,831,456,324,474",
      "609,890,488,258,496,422,663,669,173,161,892,892,78,771,260,89,485,702,615,64",
      "75,652,866,906,545,167,184,274,610,941,161,52,944,626,912,302,625,615,314,313",
      "604,50,467,284,63,203,379,467,309,377,304,438,692,191,394,304,256,818,365,215",
      "831,393,528,366,476,361,485,400,382,535,500,689,891,158,809,496,934,213,341,501",
      "933,328,180,588,542,582,799,327,292,455,210,464,178,305,581,899,368,498,803,663",
      "384,663,586,503,941,304,16,819,210,741,153,709,537,664,156,854,377,650,430,153",
      "5,336,908,152,903,740,208,605,398,462,398,949,816,767,348,302,718,486,688,934",
      "248,601,554,202,911,354,369,279,165,78,464,531,944,295,590,170,141,483,812,900",
      "76,198,943,484,317,210,415,58,907,140,811,766,70,162,251,911,897,463,658,604",
      "137,939,827,348,92,896,939,214,437,667,807,62,159,904,480,707,173,904,349,337",
      "218,137,866,631,199,467,708,938,438,742,660,667,434,547,539,665,610,55,607,340",
      "661,853,434,372,600,287,742,595,587,936,478,942,341,68,861,51,541,158,468,210",
      "204,189,878,740,390,692,393,419,526,905,262,742,383,868,375,316,656,694,746,894",
      "554,538,722,272,312,103,946,893,591,527,775,887,50,597,544,906,817,311,524,258",
      "577,821,255,427,218,832,720,281,704,200,855,434,54,503,152,613,885,865,201,389",
      "712,396,392,144,308,458,943,804,473,520,545,249,190,806,249,163,730,263,144,376",
      "195,263,422,109,372,767,155,302,177,323,547,336,73,194,763,501,742,393,436,469",
      "892,217,829,342,700,279,776,657,488,698,432,206,666,260,706,214,311,128,430,608",
      "60,622,140,71,825,427,866,178,391,387,947,138,503,68,72,866,599,691,369,57",
      "136,319,474,145,891,705,314,122,304,334,642,583,258,717,191,319,859,469,909,936",
      "824,653,75,685,716,886,743,61,394,369,465,828,76,803,432,768,685,601,682,98",
      "608,300,56,718,439,219,896,808,825,52,377,862,899,272,104,912,203,219,183,65",
      "334,530,274,222,550,685,601,249,692,13,188,689,420,669,434,419,861,50,604,169",
      "158,867,395,854,78,552,938,816,331,427,745,888,824,57,64,197,669,298,92,476",
      "660,350,23,213,79,744,500,437,832,899,524,211,815,461,819,143,300,699,859,607",
      "54,549,663,264,145,685,629,210,469,554,860,183,309,503,65,387,664,155,769,899",
      "75,104,478,742,465,659,388,696,327,662,314,597,392,700,372,626,329,695,307,615",
      "556,272,179,887,462,805,217,464,278,205,274,740,766,176,800,217,606,484,18,938",
      "354,545,521,941,818,699,312,666,495,936,199,273,665,980,769,702,348,540,399,329",
      "471,278,693,660,947,198,378,56,992,78,426,684,221,601,667,863,596,817,888,521",
      "148,545,481,78,544,342,544,437,430,397,397,350,294,597,655,697,665,465,831,892",
      "932,867,355,659,313,659,666,703,745,151,314,890,254,356,302,463,108,296,910,66",
      "743,253,817,196,587,993,158,523,723,829,149,889,862,173,715,313,496,401,192,160",
      "459,176,461,396,291,264,136,831,810,297,189,888,545,862,711,668,376,700,656,550",
      "937,522,204,870,382,537,107,51,870,425,465,822,392,134,866,908,299,658,50,587",
      "416,433,253,121,812,818,370,868,540,223,343,807,162,79,548,421,722,940,429,870",
      "548,907,320,156,495,597,168,665,469,394,333,347,78,258,696,187,808,606,923,818",
      "147,901,479,855,171,820,770,439,465,478,587,259,301,100,422,468,853,811,803,607",
      "701,352,458,905,50,279,501,309,889,356,809,869,831,256,422,482,644,390,348,330",
      "270,989,894,210,827,394,377,461,251,723,60,714,503,897,201,802,157,370,891,54",
      "486,274,656,199,272,813,708,142,156,931,122,477,65,68,460,931,906,667,413,372",
      "462,14,192,899,140,801,376,818,62,332,942,223,547,591,670,210,500,396,901,888",
      "684,542,266,69,425,395,310,431,439,162,936,357,169,890,424,347,716,524,446,894",
      "375,763,651,704,189,471,934,304,603,462,335,887,337,136,472,528,656,169,282,158",
      "480,276,298,172,656,53,273,488,660,741,163,813,55,125,698,395,376,346,432,669",
      "71,69,897,893,393,391,740,422,907,275,207,431,901,743,877,75,465,549,551,544",
      "166,297,856,687,166,62,503,864,720,268,653,345,771,80,9,265,948,202,472,537",
      "272,820,485,737,370,332,202,503,219,718,699,775,186,435,223,501,819,361,378,306",
      "337,767,302,999,583,670,712,934,137,373,936,684,216,66,799,266,458,334,615,318",
      "178,480,555,379,341,181,354,258,13,163,190,196,652,257,77,350,602,176,940,801",
      "818,377,869,723,600,120,703,161,153,466,173,161,528,534,827,534,990,536,167,720",
      "135,451,139,217,264,267,422,420,651,211,369,660,941,889,861,545,521,718,461,326",
      "53,544,943,172,862,255,214,317,602,530,223,218,16,217,218,669,819,434,396,373",
      "61,68,162,566,156,886,159,687,325,318,317,393,155,197,855,798,774,653,205,151",
      "495,474,535,22,742,806,154,368,316,887,276,152,949,347,122,261,536,464,861,264",
      "273,160,867,152,73,933,826,433,153,466,180,945,473,474,735,334,523,157,333,718",
      "261,164,606,768,740,138,386,251,818,184,290,808,215,707,202,66,474,207,379,592",
      "381,55,461,829,596,581,375,661,79,303,553,153,269,71,540,347,443,376,904,338",
      "51,806,540,216,552,334,739,329,359,64,381,281,258,419,199,458,495,355,321,324",
      "748,467,179,281,503,309,181,603,195,949,339,477,210,540,949,591,164,720,689,902",
      "51,477,540,186,829,811,126,692,764,939,892,256,158,612,69,139,309,376,602,119",
      "812,870,495,186,202,502,711,137,525,859,274,667,201,24,597,609,435,528,662,708",
      "142,216,327,807,370,899,360,828,595,717,307,334,932,764,864,193,774,870,691,934",
      "686,862,858,720,75,188,223,522,401,467,359,603,144,766,63,223,152,161,371,889",
      "829,859,946,585,315,120,890,310,538,682,371,853,465,706,820,541,913,819,654,562",
      "911,743,68,258,354,396,459,947,626,741,218,771,264,674,378,612,310,120,831,394",
      "214,397,265,477,814,759,467,656,375,193,811,909,709,342,347,77,744,481,459,943",
      "864,690,865,437,611,312,150,366,546,162,98,823,152,166,398,736,933,426,177,520",
      "379,887,460,281,746,870,345,457,144,272,421,457,746,899,23,176,200,607,668,159",
      "329,158,314,472,576,393,251,545,537,170,467,454,222,427,267,67,809,220,548,466",
      "147,894,56,813,738,60,474,163,370,809,250,393,95,666,466,203,418,419,438,400",
      "423,302,705,250,943,763,335,194,368,164,897,548,177,406,395,737,907,590,425,520",
      "154,472,859,808,654,273,73,344,615,311,297,299,474,80,351,996,315,299,399,528",
      "486,67,903,223,890,434,355,298,216,487,774,189,881,765,764,885,891,310,525,488",
      "280,73,660,337,156,281,870,710,657,435,539,150,72,203,638,147,901,799,766,933",
      "818,650,184,831,613,806,308,658,944,200,937,356,434,148,183,325,532,947,689,127",
      "178,553,221,556,391,385,147,802,504,71,815,543,996,474,61,304,813,390,437,701",
      "466,770,737,530,688,184,82,259,172,329,719,192,380,498,187,465,467,887,197,426",
      "425,503,935,419,392,905,945,153,273,653,943,389,495,182,893,368,175,690,734,484",
      "815,541,581,267,586,717,499,589,307,358,767,217,62,897,603,593,430,479,839,533",
      "642,269,435,435,500,253,178,808,269,461,669,456,71,316,710,819,428,501,594,716",
      "434,468,522,317,119,317,247,258,590,712,860,456,120,742,765,198,940,254,430,476",
      "322,327,298,534,147,717,221,261,631,423,901,479,269,712,260,194,250,355,805,63",
      "773,145,701,912,706,308,651,213,124,346,685,175,899,936,310,907,314,937,739,319",
      "374,698,739,70,435,354,892,250,464,151,309,658,262,335,144,371,553,70,492,691",
      "906,217,769,134,830,75,462,522,469,206,803,56,715,911,86,386,898,899,136,178",
      "537,804,891,527,302,277,369,885,550,272,769,147,275,350,315,297,653,327,109,255",
      "626,64,337,452,737,435,650,539,277,351,352,744,933,178,651,314,768,401,605,199",
      "378,395,278,889,689,306,720,467,93,369,328,599,461,150,530,68,261,454,184,943",
      "721,578,742,860,454,801,59,524,295,587,438,626,602,547,70,686,554,122,527,209",
      "588,146,385,538,298,270,546,353,975,911,144,479,77,475,51,767,767,528,527,165",
      "581,14,389,609,434,666,380,432,146,496,158,319,80,254,295,900,164,219,520,885",
      "655,710,305,894,202,495,832,469,435,613,149,261,166,832,815,901,873,79,944,377",
      "806,670,592,699,645,161,144,161,466,307,78,687,534,157,57,543,457,911,539,934",
      "720,378,859,726,825,718,595,888,605,146,365,743,594,457,433,535,503,694,210,819",
      "360,465,605,595,829,345,807,597,173,280,69,485,168,831,180,175,150,476,437,198",
      "498,246,194,801,183,539,690,613,265,146,854,540,142,892,945,279,501,377,303,266",
      "701,656,351,137,345,128,819,374,713,540,819,775,614,603,824,743,64,582,687,197",
      "804,54,54,432,156,764,760,602,424,773,824,399,689,153,891,458,626,665,887,907",
      "892,606,504,359,158,260,392,467,163,276,389,332,208,549,378,719,322,538,908,397",
      "142,859,630,255,906,74,73,462,695,692,368,295,829,657,538,316,901,457,310,253",
      "86,685,357,390,372,549,370,379,550,864,539,933,203,54,273,605,329,171,486,155",
      "249,289,597,167,703,187,357,763,745,690,189,389,377,393,313,609,607,603,340,223",
      "995,693,420,497,57,134,811,252,686,776,495,318,314,341,394,79,314,668,468,177",
      "462,802,5,270,805,805,552,595,340,819,682,827,215,939,652,656,704,910,524,348",
      "552,690,853,266,324,655,378,165,179,391,598,149,355,418,549,669,896,482,777,899",
      "650,500,521,825,203,594,529,51,540,367,181,900,162,846,178,553,341,830,399,703",
      "700,654,348,661,772,729,812,481,368,370,467,547,432,484,504,737,249,161,165,500",
      "473,356,357,763,51,525,571,418,162,438,682,252,343,822,308,461,53,170,386,333",
      "817,741,340,903,386,699,670,933,265,712,303,377,705,311,702,186,392,987,904,609",
      "375,910,352,887,746,769,656,668,888,605,484,433,523,854,554,547,80,250,570,477",
      "717,384,459,586,265,434,433,74,136,434,817,168,2,581,258,60,220,909,156,78",
      "815,713,97,668,498,323,397,169,122,897,602,299,736,897,182,906,811,907,767,221",
      "304,295,596,988,587,70,817,138,478,764,942,66,896,253,257,832,370,471,909,163",
      "324,698,764,184,153,152,462,186,424,855,614,185,381,238,344,855,609,891,193,472",
      "693,457,531,3,220,182,366,669,207,302,707,687,798,887,695,609,55,267,538,303",
      "711,473,468,321,439,549,655,456,475,71,612,721,23,191,374,541,665,156,350,328",
      "422,363,266,300,892,889,272,741,864,65,250,60,591,856,664,537,375,457,455,905",
      "207,161,890,542,64,154,203,496,80,864,157,294,536,298,462,175,321,521,199,803",
      "693,523,472,538,523,201,430,172,220,371,80,548,105,933,946,943,686,343,739,652",
      "682,803,520,816,313,523,827,300,547,807,613,857,350,391,611,863,361,596,181,909",
      "625,266,799,547,68,911,174,192,122,694,599,379,277,390,463,53,341,209,488,317",
      "905,331,934,712,281,946,435,186,169,806,499,859,724,398,737,885,693,433,693,158",
      "476,771,334,802,581,934,731,719,387,669,662,668,938,255,532,706,57,811,773,203",
      "53,459,202,913,476,588,287,700,181,69,182,768,498,350,472,147,664,340,605,798",
      "382,174,338,373,554,536,75,906,328,397,342,765,984,801,139,345,692,692,281,366",
      "428,894,308,623,145,542,358,170,821,257,535,582,214,120,710,593,171,221,583,369",
      "54,767,151,756,458,380,271,260,803,197,427,262,905,803,773,78,533,462,537,899",
      "67,881,298,207,210,320,321,597,261,829,745,770,534,153,815,223,372,611,488,161",
      "134,346,715,470,439,633,318,554,454,800,336,524,807,469,52,525,58,896,140,496",
      "316,356,366,896,660,252,736,135,169,458,653,533,268,299,999,374,194,134,375,191",
      "467,939,168,385,359,774,342,383,547,389,251,461,718,64,867,171,821,171,483,606",
      "720,386,186,379,258,716,345,737,768,723,478,584,156,333,821,283,934,138,419,597",
      "531,160,169,889,608,207,822,459,892,858,431,327,393,656,653,601,534,706,163,1",
      "194,501,60,223,321,165,718,464,823,775,500,554,711,269,442,499,814,798,379,77",
      "613,540,191,746,702,551,179,932,323,605,808,867,346,743,532,214,92,932,892,397",
      "715,377,503,713,906,541,249,424,120,439,392,395,361,719,867,399,863,463,932,718",
      "183,816,650,170,862,393,466,869,665,718,818,299,579,538,530,401,438,743,594,366",
      "59,126,354,806,208,196,77,719,61,162,604,470,260,504,275,901,320,215,549,467",
      "460,311,185,169,466,553,150,997,342,418,583,50,344,537,495,693,382,598,318,146",
      "689,725,373,553,191,175,885,353,207,822,775,530,703,774,390,353,171,585,556,333",
      "250,591,337,820,335,338,504,69,668,905,657,375,705,9,256,738,169,196,808,803",
      "674,154,468,382,716,435,397,462,935,739,531,399,477,526,268,598,657,261,611,295",
      "726,888,173,64,203,154,179,595,312,936,188,380,207,772,308,273,712,464,894,202",
      "59,553,685,298,741,597,312,273,596,688,428,321,167,363,267,890,74,165,706,138",
      "117,121,538,372,135,270,140,712,296,495,249,56,190,65,949,369,773,276,435,265",
      "540,813,931,83,59,268,701,936,342,323,713,743,312,327,827,896,266,261,590,69",
      "893,337,165,874,199,719,342,386,328,485,612,533,281,76,861,652,900,821,393,611",
      "436,51,742,259,661,188,437,606,737,175,9,769,399,343,742,585,337,775,268,61",
      "66,306,205,705,660,550,388,473,198,931,436,801,830,294,706,433,944,185,169,908",
      "870,831,151,892,654,690,255,543,162,167,168,221,355,96,178,829,539,653,314,142",
      "310,75,267,824,693,209,458,714,14,176,71,420,393,214,169,79,686,200,424,265",
      "588,259,219,315,550,374,741,436,714,368,353,191,537,658,127,549,522,329,460,718",
      "688,807,828,475,215,804,332,51,473,889,273,581,483,599,183,276,291,935,341,262",
      "71,525,597,893,828,545,708,307,367,303,325,251,686,586,197,608,391,821,355,2",
      "23,905,719,495,166,715,774,554,810,737,217,948,198,135,278,691,267,458,421,711",
      "420,806,207,192,353,352,711,868,464,277,811,168,713,320,984,326,300,354,583,700",
      "314,329,626,344,550,424,611,743,520,855,462,771,369,719,682,476,557,381,208,149",
      "379,58,80,809,391,540,270,296,365,269,527,380,937,489,337,581,498,668,258,401",
      "983,427,808,278,859,152,667,213,775,320,357,697,305,685,799,522,553,530,594,183",
      "690,913,853,600,197,804,874,190,427,860,830,741,400,501,822,943,553,376,941,696",
      "811,150,314,312,823,531,704,693,700,942,264,164,695,938,497,860,500,856,258,642",
      "209,253,815,431,601,382,277,375,167,810,591,318,906,178,611,203,417,886,526,698",
      "536,541,436,813,600,593,939,763,175,210,945,384,295,739,151,201,431,582,129,715",
      "464,709,463,317,663,472,547,715,563,458,606,771,605,626,186,859,866,304,253,821",
      "63,79,423,188,819,616,553,774,588,142,279,477,343,68,180,155,252,736,302,905",
      "333,701,815,398,824,336,305,690,467,142,202,378,127,140,820,481,607,661,312,533",
      "596,211,554,742,595,906,273,340,829,272,855,770,912,311,814,76,748,348,370,259",
      "219,906,363,803,350,350,769,525,280,430,767,398,332,155,358,556,864,531,266,535",
      "823,692,712,905,212,865,603,555,383,610,162,145,722,792,600,381,168,869,471,433",
      "891,589,177,194,429,338,344,372,162,436,477,821,388,259,369,864,695,64,691,997",
      "744,486,284,530,372,603,765,169,305,432,454,204,344,212,181,693,892,707,948,172",
      "521,266,317,860,487,250,275,122,888,61,430,327,636,593,477,858,461,476,865,464",
      "462,537,894,889,700,763,171,482,298,223,822,931,155,498,159,891,897,319,361,265",
      "520,768,531,935,476,595,668,77,710,855,183,805,659,939,721,359,270,332,391,171",
      "326,717,399,474,297,706,431,522,598,799,533,706,894,817,289,935,669,482,597,394",
      "197,496,686,545,349,716,167,55,866,931,477,310,716,427,168,73,892,282,553,864",
      "887,223,159,655,458,889,607,331,175,464,495,143,540,865,54,811,370,67,680,398",
      "170,343,418,466,549,373,80,78,695,310,302,594,375,731,168,814,146,460,704,71",
      "419,888,352,338,898,478,820,589,948,421,667,307,607,174,933,819,599,595,700,12",
      "605,463,353,821,539,862,594,596,327,556,152,372,894,309,435,11,581,801,432,159",
      "313,389,774,272,908,811,890,822,815,709,270,422,145,660,460,167,128,251,317,899",
      "667,316,458,259,67,400,168,60,705,5,696,688,193,355,431,137,814,219,477,470",
      "343,0,59,592,771,813,502,654,682,720,338,55,933,422,376,457,741,694,174,151",
      "598,714,253,606,854,399,357,668,148,471,270,194,378,702,213,79,532,799,634,810",
      "936,366,53,775,861,329,691,765,397,626,861,164,190,531,690,354,310,322,753,596",
      "279,343,157,416,654,381,768,551,427,737,64,609,742,503,421,457,252,317,827,497",
      "547,222,212,163,691,179,346,813,617,723,936,487,868,768,938,819,581,396,172,221",
      "932,773,214,742,370,717,63,61,300,737,719,869,480,278,460,718,224,823,590,600",
      "398,485,350,222,739,198,211,472,590,984,139,354,615,664,144,591,742,931,590,395",
      "419,865,800,355,805,613,668,596,545,469,197,654,659,452,389,340,262,185,486,433",
      "814,160,70,217,768,176,938,582,53,374,587,552,651,936,592,439,912,995,484,369",
      "545,386,713,594,500,54,268,610,220,354,810,275,548,374,454,198,524,593,877,897",
      "371,680,176,818,433,66,801,340,527,302,187,655,664,302,454,534,887,909,911,313",
      "203,189,687,683,50,53,300,263,99,336,399,166,540,480,717,329,890,704,691,318",
      "701,254,400,218,78,398,613,931,58,531,148,651,481,15,703,425,524,154,534,554",
      "822,192,207,222,830,295,894,187,599,135,798,933,894,253,822,423,383,170,438,288",
      "772,188,73,486,129,78,897,595,426,486,481,772,652,266,548,187,892,692,534,256"
   ],
]

main(inputData)

