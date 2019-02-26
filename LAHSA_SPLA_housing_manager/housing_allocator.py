import copy
import time

'''
10  beds
10  spaces in SPLA
1   LAHSA selections
00005
1
00002  SPLA selections
5
00001F  020  N  N  Y   Y 1001000
00002F  020  N  N  Y   Y 1000111
00003M  040  N  N  Y   Y 1000110
00004M  033  N  N  Y   Y 1000000
00005F  020  N  N  Y   Y 1000110
id   G  AGE  P  M  Car Dl
'''

'''
task - choose the most wanted person by LAHSA who statisfies 
the reqs of SPLA 
ideas to optimize, keep days as a bitwise array 



To be considered - 
availability at SPLA and LAHSA 

1. if lahsa is full, just choose the one that has most occupancy 

'''
class Applicant:
    def __init__(self, id="00000", gender="", age="", pet="", med="",
                 car="", dl="", days=0, shelter="0", days_list=[]):
        self.id = id
        self.gender = gender
        self.age = age
        self.pet = pet
        self.med = med
        self.car = car
        self.dl = dl
        self.days = days
        self.days_list = days_list
        self.shelter = shelter

def checkSPLAavailability(daysList, availabityGrid):
    for d in daysList:
        if (availabityGrid[d] -1) < 0:
            return False
    return True
def checkLahsaAvailability(daysList, availabilityGrid):
    for d in daysList:
        if (availabilityGrid[d] -1) < 0:
            return False
    return True

# from the given list, it returns people who qualify for lahsa
def checkSplaReqs(details):
    if details.car == "Y" and details.dl == "Y" and details.med == "N":
        return True
    else:
        return False

def checkLahsaReqs(details):
    if details.age > 17 and details.gender == "F" and details.pet == "N":
        return True
    else:
        return False

#efficiency calculations function
def gE2(squals, lquals, player, sGrid, lGrid, spla_coverage, lahsa_coverage , parent):

    seff_max = 0
    leff_max = 0
    smax_id = ""

    if len(squals) == 0 and len(lquals) == 0:
        return spla_coverage, lahsa_coverage

    if player == "l":
        if len(lquals) == 0:
            for s in squals:
                s_pick = applicants[s]
                spla_coverage += s_pick.days
                #might have to remove nodes and generate new tree
            return spla_coverage, lahsa_coverage
        else:
            for i in lquals:
                l_pick = applicants[i]
                #make deepcopies
                if(checkLahsaAvailability(l_pick.days_list, lGrid)):
                    t_lGrid = copy.copy(lGrid)
                    t_coverage = copy.copy(lahsa_coverage)
                    t_squals = copy.copy(squals)
                    t_lquals = copy.copy(lquals)
                    t_lquals.pop(i)
                    try:
                        del t_squals[i]
                    except KeyError:
                        pass
                    for d in l_pick.days_list:
                        t_lGrid[d] -= 1
                        t_coverage += 1
                    player = "s"
                    # print "lahsa's turn", i
                    seff, leff = gE2(t_squals, t_lquals, player, sGrid, t_lGrid,
                                     spla_coverage, t_coverage, parent)

                    # this is doing max-max part for spla where it chooses the max of
                    #  given possibilities of that level
                    if seff == seff_max:
                        if i < smax_id:
                            seff_max = seff
                            leff_max = leff
                            smax_id = i
                    if seff > seff_max:
                        seff_max = seff
                        leff_max = leff

        return seff_max, leff_max

    elif player == "s":
        if len(squals) == 0:
            for l in lquals:
                l_pick = applicants[l]
                lahsa_coverage += l_pick.days
                #might have to remove nodes and generate new tree
            return spla_coverage, lahsa_coverage

        for i in squals:
            s_pick = applicants[i]
            #make deepcopies
            if(checkSPLAavailability(s_pick.days_list, sGrid)):
                t_sGrid = copy.copy(sGrid)
                t_coverage = copy.copy(spla_coverage)
                t_squals = copy.copy(squals)
                t_lquals = copy.copy(lquals)
                t_squals.pop(i)
                try:
                    del t_lquals[i]
                except KeyError:
                    pass
                for d in s_pick.days_list:
                    t_sGrid[d] -= 1
                    t_coverage += 1
                player = "l"

                ''# print "spla's turn", i
                seff, leff = gE2(t_squals, t_lquals, player, t_sGrid, lGrid, t_coverage, lahsa_coverage, parent)

                # this is doing max-max part for spla where it chooses the max of
                #  given possibilities of that level
                if seff == seff_max:
                    if i < smax_id:
                        seff_max = seff
                        leff_max = leff
                        smax_id = i
                if seff > seff_max:
                    seff_max = seff
                    leff_max = leff
                    smax_id = i

    return seff_max, leff_max

if __name__ == '__main__':
    start = time.time()
    input = open("test\input0151.txt", 'r')
    output = open("output.txt", 'w')
    beds = int(input.readline().strip())
    parking_space = int(input.readline().strip())
    num_lahsa = int(input.readline().strip())
    lahsa_list = []
    for i in range(num_lahsa):
        id = input.readline().strip()
        lahsa_list.append(id)
    num_spla = int(input.readline())
    spla_list = []
    for i in range(num_spla):
        id = input.readline().strip()
        spla_list.append(id)
    num_app = int(input.readline())
    applicants = {}
    for i in range(num_app):
        entry = input.readline()
        a = Applicant()
        a.id = entry[:5]
        a.gender = entry[5]
        a.age = int(entry[6:9])
        a.pet = entry[9]
        a.med = entry[10]
        a.car = entry[11]
        a.dl = entry[12]
        #a.days = entry[13:].strip()
        days_str = entry[13:].strip()
        days = 0
        days_list = []

        for i in range(len(days_str)):
            if days_str[i] == "1":
                days += 1
                days_list.append(i)
        a.days = days
        a.days_list = days_list
        applicants[a.id] = a

    # print lahsa_grid
    # print spla_grid
    spla_grid = [parking_space for x in range(7)]
    lahsa_grid = [beds for x in range(7)]
    l_heur = 0
    s_heur = 0
    for i in lahsa_list:
        applicants[i].shelter = "l"
        for d in applicants[i].days_list:
            l_heur += 1
            lahsa_grid[d] -= 1
    for i in spla_list:
        applicants[i].shelter = "s"
        for d in applicants[i].days_list:
            s_heur += 1
            spla_grid[d] -= 1
    #print s_heur,", " ,l_heur
    #create a list of lahsa
    l_quals = {}
    s_quals = {}

    for k,v in applicants.iteritems():
        if v.shelter == "0":
            # if Lqual: add to Lahsa
            if checkSplaReqs(v):
                s_quals[k] = 1
            if checkLahsaReqs(v):
                l_quals[k] = 1
    spla_coverage = 0
    lahsa_coverage = 0
    smax = 0
    lmax = 0
    sid = ""
    lid = ""

    for id in s_quals:
        person = applicants[id]
        if(checkSPLAavailability(person.days_list, spla_grid)):
            temp_spla_grid = copy.copy(spla_grid)
            temp_coverage = copy.copy(spla_coverage)
            temp_squals = copy.copy(s_quals)
            temp_lquals = copy.copy(l_quals)

            temp_squals.pop(id)
            temp_lquals.pop(id,None)
            #print person.days_list

            for d in person.days_list:
                temp_spla_grid[d] -= 1
                temp_coverage = temp_coverage + 1

            sval,lval = gE2(temp_squals, temp_lquals, "l",
                            temp_spla_grid, lahsa_grid,
                            temp_coverage, lahsa_coverage, id)
            print "sval:",sval," lval:",lval, "id: ", id
            if sval == smax and sval!=0:
                sid_details = applicants[sid]
                id_satisfiesLahsa = checkLahsaReqs(person)
                max_id_satisfiesLahsa = checkLahsaReqs(sid_details)
                if id_satisfiesLahsa and max_id_satisfiesLahsa:
                    if person.days > sid_details.days:
                        lmax = lval
                        sid = id
                elif id_satisfiesLahsa:
                        lmax = lval
                        sid = id
                elif not id_satisfiesLahsa and not max_id_satisfiesLahsa:
                    if id<sid:
                        smax = sval
                        lmax = lval
                        sid = id

            if (sval > smax):
                smax = sval
                lmax = lval
                sid = id

    end = time.time()
    print end-start
    output.write(sid)





