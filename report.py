from genotype_combinations import Allele, Genotypes, Person, THETA
from get_data import LOCUS, RACE, Constants, get_drop_out, get_drop_in, get_allele_freq, get_mixture
from copy import copy, deepcopy

class Report:
    def __init__(self, drop_out_db, knowns_pn, unknowns_pn, knowns_pd, unknowns_pd, genotypes, replicates, case_name, locus, constants):
        self.knowns_pn = knowns_pn
        self.knowns_pd = knowns_pd
        self.unknowns_pn = unknowns_pn
        self.unknowns_pd = unknowns_pd
        self.genotypes = genotypes
        self.replicates = replicates
        self.locus = locus
        self.case_name = case_name.replace('/', '-')
        self.constants = constants

        FREQ_CORRECTION = self.constants.MINIMUM_WILD_FREQUENCY

        self.indicies_pn = []
        self.indicies_pd = []
        
        tmp = []
        for i in range(0, len(genotypes.allele_comb)):
            tmp.append(i)
        if unknowns_pn + len(knowns_pn) > 0 and unknowns_pn + len(knowns_pn) <= len(tmp):
            self.permute_driver(tmp, unknowns_pn + len(knowns_pn), "PN")
        else:
            self.indicies_pn.append(tmp)
        if unknowns_pd + len(knowns_pd) > 0 and unknowns_pd + len(knowns_pd) <= len(tmp):
            self.permute_driver(tmp, unknowns_pd + len(knowns_pd), "PD")
        else:
            self.indicies_pd.append(tmp)
        
        self.persons = []
        self.generate_persons()
        self.population_pn = [[None] * (len(self.knowns_pn) + self.unknowns_pn)] * (len(self.genotypes.allele_comb) ** (len(self.knowns_pn) + self.unknowns_pn))
        self.population_pd = [[None] * (len(self.knowns_pd) + self.unknowns_pd)] * (len(self.genotypes.allele_comb) ** (len(self.knowns_pd) + self.unknowns_pd))
        self.generate_populations()
        
        with open('pn.json', 'w') as o:
            for i in self.population_pn:
                for j in i:
                    o.write('(' + str(j.a.length) + str(j.b.length) + ') ')
                o.write('\n')
        with open('pd.json', 'w') as o:
            for i in self.population_pd:
                for j in i:
                    o.write('(' + str(j.a.length) + str(j.b.length) + ') ')
                o.write('\n')
        input()
        wild_vector = []
        if self.persons[0].a.length == -1 and self.person[0].b.length == -1:
            del population_pn[:]
            for i in range(0, knowns_pn.size() + unknowns_pn):
                wild_vector.append(persons[0])
            self.population_pn.append(wild_vector)
            del wild_vector[:]
        if self.persons[0].a.length == -1 and self.person[0].b.length == -1:
            del population_pd[:]
            for i in range(0, knowns_pd.size() + unknowns_pd):
                wild_vector.append(persons[0])
            self.population_pd.append(wild_vector)
            del wild_vector[:]

        self.check_person()
        
        self.pn = self.generate_px(drop_out_db, "PN")
        self.pd = self.generate_px(drop_out_db, "PD")
        self.lr = self.pn / self.pd
        print self.lr, self.pn, self.pd

    def permute(self, number_items, length, position, depth, perimeter, ID):
        if depth >= length:
            index_vector = []
            for i in range(0, len(position)):
                index_vector.append(number_items[position[i]])
            if ID == "PN":
                self.indicies_pn.append(index_vector)
            elif ID == "PD":
                self.indicies_pd.append(index_vector)
            else:
                print "class Report (Permute) ID is incorrectly inputted"
            return
        for i in range(0, len(number_items)):
            position[depth] = i
            self.permute(number_items, length, position, depth + 1, i, ID)
        return

    def permute_driver(self, number_items, length, ID):
        if length > 0 and length <= len(number_items):
            position = [0] * length
            self.permute(number_items, length, position, 0, 0, ID)

    def generate_persons(self):
        for i in range(0, len(self.genotypes.alleles)):
            for j in range(i, len(self.genotypes.alleles)):
                self.persons.append(Person(self.genotypes.alleles[i], self.genotypes.alleles[j]))

    def check_person(self):
        '''
            If a person's allele(s) is/are not found in the replicates,
            change that/those allele(s) to the wild allele.
            Perform book keep functions such as regenerating person's frequencies
            and setting the hom and het flags accordingly.
            This is done for both PN and PD.
        '''
        for i in range(0, len(self.knowns_pn)):
            found_two = False
            found_a = False
            found_b = False
            for j in range(0, len(self.replicates)):
                for k in range(0, len(self.replicates[j])):
                    if self.knowns_pn[i].a == self.replicates[j][k]:
                        found_a = True
                    if self.knowns_pn[i].b == self.replicates[j][k]:
                        found_b = True
            if found_a and fonud_b:
                self.knowns_pn[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pn[i].generate_freq()
            if not found_a and found_b:
                self.knowns_pn[i].a = self.knowns_pn[i].b
                self.knowns_pn[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pn[i].generate_freq()
            if not found_a and not found_b:
                self.knowns_pn[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pn[i].a = self.persons[len(self.persons) - 1].a
                self.knowns_pn[i].generate_freq()
            if self.knowns_pn[i].a.is_equal(self.knowns_pn[i].b):
                self.knowns_pn[i].hom = True
                self.knowns_pn[i].het = False
            else:
                self.knowns_pn[i].hom = False
                self.knowns_pn[i].het = True
        for i in range(0, len(self.knowns_pd)):
            found_two = False
            found_a = False
            found_b = False
            for j in range(0, len(self.replicates)):
                for k in range(0, len(self.replicates[j])):
                    if self.knowns_pd[i].a == self.replicates[j][k]:
                        found_a = True
                    if self.knowns_pd[i].b == self.replicates[j][k]:
                        found_b = True
            if found_a and fonud_b:
                self.knowns_pd[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pd[i].generate_freq()
            if not found_a and found_b:
                self.knowns_pd[i].a = self.knowns_pd[i].b
                self.knowns_pd[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pd[i].generate_freq()
            if not found_a and not found_b:
                self.knowns_pd[i].b = self.persons[len(self.persons) - 1].b
                self.knowns_pd[i].a = self.persons[len(self.persons) - 1].a
                self.knowns_pd[i].generate_freq()
            if self.knowns_pd[i].a.is_equal(self.knowns_pd[i].b):
                self.knowns_pd[i].hom = True
                self.knowns_pd[i].het = False
            else:
                self.knowns_pd[i].hom = False
                self.knowns_pd[i].het = True

    def generate_populations(self): # SOMETHING IS GOING OUT OF SCOPE HERE
        for i in range(0, len(self.indicies_pn)):
            for j in range(0, len(self.indicies_pn[i])):
                self.population_pn[i][j] = Person(self.genotypes.allele_comb[self.indicies_pn[i][j]][0], self.genotypes.allele_comb[self.indicies_pn[i][j]][1])
                #print self.population_pn[i][j].a.length, self.population_pn[i][j].b.length
        for i in range(0, len(self.population_pn)): # DEBUG LOOP
            for j in range(0, len(self.population_pn[i])):
                print self.population_pn[i][j].a.length, self.population_pn[i][j].b.length, ' ',
            print '\n'
        for i in range(0, len(self.indicies_pd)):
            for j in range(0, len(self.indicies_pd[i])):
                #print self.genotypes.allele_comb[self.indicies_pd[i][j]][0].length, self.genotypes.allele_comb[self.indicies_pd[i][j]][1].length
                self.population_pd[i][j] = Person(self.genotypes.allele_comb[self.indicies_pd[i][j]][0], self.genotypes.allele_comb[self.indicies_pd[i][j]][1])

    def generate_px(self, db, ID):
        if ID == "PN":
            self.set_drop_out(db, self.constants.CONTRIBUTORS_PN, ID)
        elif ID == "PD":
            self.set_drop_out(db, self.constants.CONTRIBUTORS_PD, ID)
        else:
            print "class Report (generate_px) ID is incorrectly inputted"
        product = float(1.0)
        summation = float(0.0)
        if ID == "PN":
            for i in range(0, len(self.population_pn)):
                if self.is_subset_px(i, ID):
                    for j in range(0, len(self.population_pn[i])):
                        if j >= (self.unknowns_pn + len(self.knowns_pn)) - ((self.unknowns_pn + len(self.knowns_pn)) - len(self.knowns_pn)):
                            product *= self.population_pn[i][j].freq
                    for j in range(0, len(self.population_pn[i])):
                        for k in range(0, len(self.replicates)):
                            product *= self.drop_out(self.population_pn[i][j], self.replicates[k], ID)
                    for j in range(0, len(self.replicates)):
                        product *= self.drop_in(self.population_pn[i], self.replicates[j])
                    summation += product
                    product = float(1.0)
            return summation
        elif ID == "PD":
            for i in range(0, len(self.population_pd)):
                if self.is_subset_px(i, ID):
                    for j in range(0, len(self.population_pd[i])):
                        if j >= (self.unknowns_pd + len(self.knowns_pd)) - ((self.unknowns_pd + len(self.knowns_pd)) - len(self.knowns_pd)):
                            product *= self.population_pd[i][j].freq
                    for j in range(0, len(self.population_pd[i])):
                        for k in range(0, len(self.replicates)):
                            product *= self.drop_out(self.population_pd[i][j], self.replicates[k], ID)
                    for j in range(0, len(self.replicates)):
                        product *= self.drop_in(self.population_pd[i], self.replicates[j])
                    summation += product
                    product = float(1.0)
            return summation
        else:
            print "class Report (generate_px) ID is incorrectly inputted"

    def is_subset_px(self, i, ID): # CREATE PERSON EQUALITY CHECKER
        if ID == "PN":
            if self.subset(self.population_pn[i][:len(self.knowns_pn)], self.knowns_pn):
                return True
        elif ID == "PD":
            if self.subset(self.population_pd[i][:len(self.knowns_pd)], self.knowns_pd):
                return True
        else:
            print "class Report (is_subset_px) ID is incorrectly inputted"
        return False

    def subset(self, persons_1, persons_2):
        for i in range(0, len(persons_1)):
            if not persons_1[i].is_equal(persons_2[i]):
                return False
        return True

    def drop_out(self, person, alleles, ID):
        if ID == "PN":
            if person.hom:
                for i in range(0, len(alleles)):
                    if person.a == alleles[i] and person.b == alleles[i]:
                        return self.constants.PN_PHOM0
                return self.constants.PN_PHOM1
            elif person.het:
                present_first = False
                present_second = False
                for i in range(0, alleles):
                    if person.a == alleles[i]:
                        present_first = True
                    if person.b == alleles[i]:
                        present_second = True
                if present_first and present_second:
                    return self.constants.PN_PHET0
                elif not present_first and not present_second:
                    return self.constants.PN_PHET2
                elif (present_first and not present_second) or (not present_first and present_second):
                    return self.constants.PN_PHET1
                else:
                    "class Report (drop_out) present conditions not met"
        elif ID == "PD":
            if person.hom:
                for i in range(0, len(alleles)):
                    if person.a == alleles[i] and person.b == alleles[i]:
                        return self.constants.PD_PHOM0
                return self.constants.PD_PHOM1
            elif person.het:
                present_first = False
                present_second = False
                for i in range(0, alleles):
                    if person.a == alleles[i]:
                        present_first = True
                    if person.b == alleles[i]:
                        present_second = True
                if present_first and present_second:
                    return self.constants.PD_PHET0
                elif not present_first and not present_second:
                    return self.constants.PD_PHET2
                elif (present_first and not present_second) or (not present_first and present_second):
                    return self.constants.PD_PHET1
                else:
                    "class Report (drop_out) present conditions not met"
        else:
            print "class Report (drop_out) ID is incorrectly inputted"

    def drop_in(self, persons, alleles):
        tmp = []
        for i in range(0, len(persons)):
            tmp.append(persons[i].a)
            tmp.append(persons[i].b)
        tmp = set(tmp)
        c = 0
        for i in range(0, len(alleles)):
            if alleles[i] not in tmp:
                c += 1
        if c == 0:
            return self.constants.PC0
        elif c == 1:
            return self.constants.PC1
        else:
            return self.constants.PC2

    def set_drop_out(self, db, num_contributors, ID):
        contributors = str(num_contributors)
        rates = []  # ['HET1', 'HET2', 'HOM1']
        for i in db:
            rates.append(i)
        rates.sort()    # need HET1, then HET2
        quants = ['6.25', '12.5', '25', '50', '100', '150', '250', '500']
        '''
        for i in db['HET1']['1']['D']['FGA']:
            quants.append(i)
        quants = [float(i) for i in quants]
        quants.sort()
        quants = [str(i) for i in quants]
        '''
        l = '25'
        h = '50'
        for i in range(0, len(quants)):
            if float(quants[i]) < self.constants.QUANT and float(quants[i + 1]) > self.constants.QUANT:
                l = quants[i]       # lower quant milepost
                h = quants[i + 1]   # higher quant milepost
        full = float(1.0)
        for i in rates:
            if i == 'HOM1' and self.constants.DEDUCIBLE:
                b = float(0.0)  # y-intercept or value for constant
                slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['D'][self.locus][l] - (slope * float(l))
                PHOM1 = slope * self.constants.QUANT + b
                PHOM0 = full - PHOM1
                if ID == "PN":
                    self.constants.PN_PHOM1 = PHOM1
                    self.constants.PN_PHOM0 = PHOM0
                elif ID == "PD":
                    self.constants.PD_PHOM1 = PHOM1
                    self.constants.PD_PHOM0 = PHOM0
            elif i == 'HET1' and self.constants.DEDUCIBLE:
                b = float(0.0)
                slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['D'][self.locus][l] - (slope * float(l))
                PHET1 = slope * self.constants.QUANT + b
                if ID == "PN":
                    self.constants.PN_PHET1 = PHET1
                elif ID == "PD":
                    self.constants.PD_PHET1 = PHET1
            elif i == 'HET2' and self.constants.DEDUCIBLE:
                b = float(0.0)
                slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['D'][self.locus][l] - (slope * float(l))
                PHET2 = slope * self.constants.QUANT + b
                if ID == "PN":
                    self.constants.PN_PHET2 = PHET2
                    self.constants.PN_PHET0 = full - (self.constants.PN_PHET1 + PHET2)
                elif ID == "PD":
                    self.constants.PD_PHET2 = PHET2
                    self.constants.PD_PHET0 = full - (self.constants.PD_PHET1 + PHET2)
            elif i == 'HOM1' and not self.constants.DEDUCIBLE:
                b = float(0.0)  # y-intercept or value for constant
                slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['ND'][self.locus][l] - (slope * float(l))
                PHOM1 = slope * self.constants.QUANT + b
                PHOM0 = full - PHOM1
                if ID == "PN":
                    self.constants.PN_PHOM1 = PHOM1
                    self.constants.PN_PHOM0 = PHOM0
                elif ID == "PD":
                    self.constants.PD_PHOM1 = PHOM1
                    self.constants.PD_PHOM0 = PHOM0
            elif i == 'HET1' and not self.constants.DEDUCIBLE:
                b = float(0.0)
                slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['ND'][self.locus][l] - (slope * float(l))
                PHET1 = slope * self.constants.QUANT + b
                if ID == "PN":
                    self.constants.PN_PHET1 = PHET1
                elif ID == "PD":
                    self.constants.PD_PHET1 = PHET1
            elif i == 'HET2' and not self.constants.DEDUCIBLE:
                b = float(0.0)
                slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (float(h) - float(1))
                b = db[i][contributors]['ND'][self.locus][l] - (slope * float(l))
                PHET2 = slope * self.constants.QUANT + b
                if ID == "PN":
                    self.constants.PN_PHET2 = PHET2
                    self.constants.PN_PHET0 = full - (self.constants.PN_PHET1 + PHET2)
                elif ID == "PD":
                    self.constants.PD_PHET2 = PHET2
                    self.constants.PD_PHET0 = full - (self.constants.PD_PHET1 + PHET2)

def generate_wild_allele_freq(alleles, minimum):
    c = float(1.0)
    for i in range(0, len(alleles)):
        c -= alleles[i].freq
    if c < 0:
        return minimum
    return c

'''
for i in name_files():
    if i.startswith('Evidence_'):
        numbers = read(i)

import json

with open('odb.json', 'w') as o:
    o.write(json.dumps(get_drop_out('Drop_Out_Rates.csv'), indent=4))

with open('adb.json', 'w') as o:
    o.write(json.dumps(get_allele_freq('Allele_Frequencies.csv'), indent=4))

with open('idb.json', 'w') as o:
    o.write(json.dumps(get_drop_in('Drop_In_Rates.csv'), indent=4))

import json
with open('cdb.json', 'w') as o:
    o.write(json.dumps(get_mixture('case.csv'), indent=4))
'''

def gather():
    odb = get_drop_out('Drop_Out_Rates.csv')
    idb = get_drop_in('Drop_In_Rates.csv')
    adb = get_allele_freq('Allele_Frequencies.csv')
    cdb = get_mixture('case.csv')
    for case in cdb:
        constants = Constants()
        THETA = idb['THETA']
        constants.THETHA = THETA # Redundant
        num_knowns_pn = 0
        num_knowns_pd = 0
        num_unknowns_pn = 0
        num_unknowns_pd = 0
        if 'Unknowns Pn' in cdb[case]['FGA']:
            num_unknowns_pn = int(cdb[case]['FGA']['Unknowns Pn'])
        if 'Unknowns Pn' in cdb[case]:
            num_unknowns_pd = int(cdb[case]['FGA']['Unknowns Pd'])
        if 'Known Pn 1' in cdb[case]['FGA']:
            num_knowns_pn += 1
        if 'Known Pn 2' in cdb[case]['FGA']:
            num_knowns_pn += 1
        if 'Known Pn 3' in cdb[case]['FGA']:
            num_knowns_pn += 1
        if 'Known Pd 1' in cdb[case]['FGA']:
            num_knowns_pd += 1
        if 'Known Pd 2' in cdb[case]['FGA']:
            num_knowns_pd += 1
        if 'Known Pd 3' in cdb[case]['FGA']:
            num_knowns_pd += 1
        if 'Unknowns Pn' in cdb[case]:
            constants.CONTRIBUTORS_PN = num_knowns_pn + num_unknowns_pn
        if 'Unknowns Pd' in cdb[case]:
            constants.CONTRIBUTORS_PD = num_knowns_pd + num_unknowns_pd
        if 'Contributors' in cdb[case]:
            constants.CONTRIBUTORS_PN = int(cdb[case]['Contributors'])
            constants.CONTRIBUTORS_PD = int(cdb[case]['Contributors'])
            num_unknowns_pn = constants.CONTRIBUTORS_PN - num_knowns_pn
            num_unknowns_pd = constants.CONTRIBUTORS_PD - num_knowns_pd
        constants.QUANT = float(cdb[case]['Quant'])
        if constants.QUANT > 500:
            constants.QUANT = 500
        if constants.QUANT < 25 and constants.CONTRIBUTORS_PN > 1:
            constants.QUANT = 25
        if constants.QUANT < 6.25 and constants.CONTRIBUTORS_PN == 1:
            constants.QUANT = 6.25
        if 'Deducible' in cdb[case]:
            constants.DEDUCIBLE = cdb[case]['Deducible']

        if constants.QUANT <= 100:
            constants.PC0 = float(idb['LPC0'])
            constants.PC1 = float(idb['LPC1'])
            constants.PC2 = float(idb['LPC2'])
        else:
            constants.PC0 = float(idb['HPC0'])
            constants.PC1 = float(idb['HPC1'])
            constants.PC2 = float(idb['HPC2'])
        constants.THETA = float(idb['THETA'])

        for race in RACE:
            constants.RACE = race
            if constants.RACE == "BLACK":
                constants.MINIMUM_WILD_FREQUENCY = float(idb['B-MIN-WILD-FREQ'])
            elif constants.RACE == "CAUCASIAN":
                constants.MINIMUM_WILD_FREQUENCY = float(idb['C-MIN-WILD-FREQ'])
            elif constants.RACE == "HISPANIC":
                constants.MINIMUM_WILD_FREQUENCY = float(idb['H-MIN-WILD-FREQ'])
            elif constants.RACE == "ASIAN":
                constants.MINIMUM_WILD_FREQUENCY = float(idb['A-MIN-WILD-FREQ'])

            Overall_LR = float(1.0)
            for locus in LOCUS:
                alleles = []
                for length in cdb[case][locus]['Unique Alleles']:
                    alleles.append(Allele(locus, length, adb[locus][length][race]))
                alleles.append(Allele("W", -1, generate_wild_allele_freq(alleles, constants.MINIMUM_WILD_FREQUENCY)))

                genotypes = Genotypes(alleles)
                
                kpn = []
                if "Known Pn 1" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pn 1"][0]
                    b = cdb[case][locus]["Known Pn 1"][1]
                    kpn.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))
                if "Known Pn 2" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pn 2"][0]
                    b = cdb[case][locus]["Known Pn 2"][1]
                    kpn.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))
                if "Known Pn 3" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pn 3"][0]
                    b = cdb[case][locus]["Known Pn 3"][1]
                    kpn.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))
                kpd = []
                if "Known Pd 1" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pd 1"][0]
                    b = cdb[case][locus]["Known Pd 1"][1]
                    kpd.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))
                if "Known Pd 2" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pd 2"][0]
                    b = cdb[case][locus]["Known Pd 2"][1]
                    kpd.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))
                if "Known Pd 3" in cdb[case][locus]:
                    a = cdb[case][locus]["Known Pd 3"][0]
                    b = cdb[case][locus]["Known Pd 3"][1]
                    kpd.append(Person(Allele(locus, a, adb[locus][a][race]), Allele(locus, b, adb[locus][b][race])))

                reps = []
                if "Replicate 1" in cdb[case][locus]:
                    reps.append(cdb[case][locus]['Replicate 1'])
                if "Replicate 2" in cdb[case][locus]:
                    reps.append(cdb[case][locus]['Replicate 2'])
                if "Replicate 3" in cdb[case][locus]:
                    reps.append(cdb[case][locus]['Replicate 3'])
                report = Report(odb, kpn, num_unknowns_pn, kpd, num_unknowns_pd, genotypes, reps, case, locus, constants)
                Overall_LR *= report.lr
            print case, race, Overall_LR
    

gather()
