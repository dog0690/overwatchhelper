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
comp_list = [Dva, tracer]
counter_count = len(comp_list)
#buffer list
ghost_list = list(range(5))
def main():

    for i in range (cha_count):
        for k in range(counter_count):
            if ch_list[i] == comp_list[k]:
                ghost_list[i] = comp_list [k]
                print(f"{ghost_list[i]}, {i}")
    #i = 0
    #k = 0
    #while i < cha_count:
    #    while k < counter_count:
    #        if ch_list[i] == comp_list[k]:
    #            ghost_list[i] = comp_list [k]
    #            print(ghost_list[i])
    #        else:
    #            k += 1
    #        print(f"working on {i} {k}")
    #        break
    #    i +=1
main()
