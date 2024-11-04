from collections import defaultdict


#names
t1 = 'boongo'
t2 = 'batman'
t3 = 'spiderman'
t4 = 'overwatch'
#counters
Dva = [t1, t2]
tracer = [t3, t4]
#user chosen character list
ch_list = [tracer,Dva,t3]
cha_count = len(ch_list)
#counter list
comp_list2 = [Dva, tracer]
comp_list = ["Dva", "tracer"]
counter_count = len(comp_list)
#buffer list
ghost_list = list(range(5))
ch = list(range(5))
enemy = [Dva, tracer]
def ch_sel():
    i =0
    while i < 5:
        i +=1
        print(f"what are you up against? {i}")
        enemies = input("")
        ch[i-1] = enemies
    return ch
def ghost_list1(ch):
    ch_list = ch
    list_len = len(ch_list)
    for i in range (list_len):
        for k in range(counter_count):
            if ch_list[i] == comp_list[k]:
                ghost_list[i] = comp_list2 [k]
                print(f"{ghost_list[i]}, {i}")
    return(ghost_list1)
tallyitem = [Dva, tracer]
def tally(items):
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1
    return counts
print(tally(tallyitem[0]))