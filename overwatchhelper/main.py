import os
from collections import defaultdict
from collections import Counter
from rich.console import Console
from rich.table import Table
tanks = [
    "T1 = Dva",
    "T2 = Doomfist",
    "T3 = JunkerQueen",
    "T4 = Mauga",
    "T5 = Ramatra",
    "T6 = Reinhardt",
    "T7 = Roadhog",
    "T8 = Sigma",
    "T9 = Winston",
    "T10 = WreckingBall",
    "T11 = Zarya",
    "T12 = Orisa",
    "","","","","","", ""
]
damage = [
    "A1 = Ashe",
    "A2 = Bastion",
    "A3 = Cassidy",
    "A4 = Echo",
    "A5 = Genji",
    "A6 = Hanzo",
    "A7 = Junkrat",
    "A8 = Mei",
    "A9 = Pharah",
    "A10 = Reaper",
    "A11 = Sojourn",
]
damage2 = [
    "A12 = Soldier76",
    "A13 = Sombra",
    "A14 = Symmetra",
    "A15 = Tobjorn",
    "A16 = Tracer",
    "A17 = Venture",
    "A18 = Widowmaker",
]

support = [
    "S1 = Ana",
    "S2 = Baptiste",
    "S3 = Brigitte",
    "S4 = Illari",
    "S5 = Juno",
    "S6 = Kiriko",
    "S7 = Lifeweaver",
    "S8 = Lucio",
    "S9 = Mercy",
    "S10 = Moira",
    "S11 = Zenyatta",
    "","","","","","", " "
]
#Tanks
T1 = 'Dva'
T2 = 'Doomfist'
T3 = 'JunkerQueen'
T4 = 'Mauga'
T5 = 'Ramatra'
T6 = 'Reinhardt'
T7 = 'Roadhog'
T8 = 'Sigma'
T9 = 'Winston'
T10 = 'WreckingBall'
T11 = 'Zarya'
T12 = 'Orisa'

#Damage
A1 = 'Ashe'
A2 = 'Bastion'
A3 = 'Cassidy'
A4 = 'Echo'
A5 = 'Genji'
A6 = 'Hanzo'
A7 = 'Junkrat'
A8 = 'Mei'
A9 = 'Pharah'
A10 = 'Reaper'
A11 = 'Sojourn'
A12 = 'Soldier76'
A13 = 'Sombra'
A14 = 'Symmetra'
A15 = 'Tobjorn'
A16 = 'Tracer'
A17 = 'Venture'
A18 = 'Widowmaker'

#Support
S1 = 'Ana'
S2 = 'Baptiste'
S3 = 'Brigitte'
S4 = 'Illari'
S5 = 'Juno'
S6 = 'Kiriko'
S7 = 'Lifeweaver'
S8 = 'Lucio'
S9 = 'Mercy'
S10 = 'Moira'
S11 = 'Zenyatta'


#Counterlist

#Tank
Dva =  [T11, T9, A14, A11, A2, S10]
Doomfist =  [A13, A16, A2, A5, S1, S3]
JunkerQueen =  [T10, A18, S1, S6, S8]
Mauga =  [T2, T10, T4, A13, S11, S6]
Orisa = [T1, T11, A8, A4, S10]
Ramatra =  [T7, A10, A16, A9, A5, A3, S6]
Reinhardt =  [A13, A3, A8, A7, A9, S11]
Roadhog =  [T10, T7, A10, A4, A7, S1]
Sigma =  [T8, T7, A5, A13, A16, S8]
Winston =  [T1, A7, A9, A2, S1, S3]
WreckingBall = [T7, T2, A8, A13, S1, S3] 
Zarya =  [T1, A6, A18, A3, A16, S11]

#Damage
Ashe = [T11, A18, A16, A5, S1, S6]
Bastion = [T11, T12, A5, A7, A9, A16, S1]
Cassidy = [T6, T9, A5, A3, A1]
Echo = [T9, T11, A1, A3, A12, A18]
Genji = [T9, T11, A8, A14, S10, S1]
Hanzo = [T1, T10, A5, A18, S8]
Junkrat = [T10, T11, A3, A12, S8, S3, S7]
Mei = [T1, A13, A4, A9,  S6]
Pharah = [T1, A12, A3, A1, A18, S2]
Reaper = [T11, A9, A7, A4, A18, S1]
Sojourn = [T9, T4, A16, A5, S8]
Soldier76 = [T7, A1, A3, A5, A7, S1, S8]
Sombra = [A9, A7, A6, A8, S1, S6]
Symmetra = [T9, T4, A7, A8, A4]
Tobjorn = [T1, A7, A1]
Tracer = [T9, T4, A14, A15, A8, S3, S10]
Venture = [T1, T9, T11, T8, A8, A9, A12, S1]
Widowmaker = [T1, T9, A5, A16, A13, S11]

#Support 
Ana = [T9, T5, A4, A9, A16, S6]
Baptiste = [A3, A1, A8, S8]
Brigitte = [A9, A4, A7]
Illari = [T11, T12, T1, A3, A1, A18, S2, S7, S8]
Juno = [T1, T9, T6, A12, A13, A18, S8, S1]
Kiriko = [T7, A16, A13, A5, A8]
Lifeweaver = [A8, A12, S8]
Lucio = [T7, T9, A12, A3, A14, A15, A8, S10]
Mercy = [T9, T7, A4, A3, A18, A5, A16]
Moira = [T7, T11, A4, A9, A18, A7, A8, A1, S1]
Zenyatta = [A7, A9, A3, A18, A1, A16, A6, S6, S11]

Test_list = ('Dva', 'JunkerQueen', 'Ana', 'Mercy', 'Moira' )
counter_list = (Dva,Doomfist,JunkerQueen,Mauga,Orisa,Ramatra,Reinhardt,Roadhog,Sigma,Winston,WreckingBall,Zarya,Ashe,Bastion,Cassidy,Echo,Genji,Hanzo,Junkrat,Mei,Pharah,Reaper,Sojourn,Soldier76,Sombra,Symmetra,Tobjorn,Tracer,Venture,Widowmaker,Ana,Baptiste,Brigitte,Illari,Juno,Kiriko,Lifeweaver,Lucio,Mercy,Moira,Zenyatta,)
counter_list3 = ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11",)
counter_list2 = ('Dva','Doomfist','JunkerQueen','Mauga','Ramatra','Reinhardt','Roadhog','Sigma','Winston','WreckingBall','Zarya','Orisa','Ashe','Bastion','Cassidy','Echo','Genji','Hanzo','Junkrat','Mei','Pharah','Reaper','Sojourn','Soldier76','Sombra','Symmetra','Tobjorn','Tracer','Venture','Widowmaker','Ana','Baptiste','Brigitte','Illari','Juno','Kiriko','Lifeweaver','Lucio','Mercy','Moira','Zenyatta')
ghost_list = list(range(5))
ch = list(range(5))
counter_count = len(counter_list)
console = Console()

#Functions

#First Prompt
def ch_sel():
    i =0
    while i < 5:
        clear_terminal()
        prompt()
        i +=1
        print(f"what are you up against? {i}")
        enemies = input("")
        ch[i-1] = enemies
    return ch
    clear_terminal()
def conversion(ch):
    ch_list = ch
    list_len = len(ch_list)
    for i in range (list_len):
        for k in range(counter_count):
            if ch_list[i] == counter_list3[k]:
                ghost_list[i] = counter_list [k]
    return(ghost_list)

def inner_tally(items):
    counts = defaultdict(int)
    i = 0
    while i < 5:
        for item in items[i]:
            counts[item] +=1
        i +=1
        clear_terminal()
        print(counts)
    return(counts)
def sort_tally(data):
    counts = Counter(data)
    sorted_by_frequency = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    clear_terminal()
    return(sorted_by_frequency)    
def main():
    enemies = ch_sel()
    converted_list = conversion(enemies)
    tally_list = inner_tally(converted_list)
    sorted = sort_tally(tally_list)
    for i in range(5):
        print(sorted[i])

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def prompt():
    table = Table(show_header= True)

    table.add_column("tanks", justify="left", style="cyan", no_wrap=True)
    table.add_column("damage", justify = "left", style="red")
    table.add_column("damage", justify = "left", style="red")
    table.add_column("support", justify="left", style="green")
    
    for tank, dam, dam2, sup in zip(tanks, damage,damage2,  support):
        table.add_row(tank, dam, dam2, sup)
    
    console.print(table)
def end_table(name, number):
    table = Table(show_header=True)
    table.add_column("Counter", justify="left")
    table.add_column("#", justify = "left")
    console.print(table)

main()