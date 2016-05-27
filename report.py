from genotype_combinations import Allele, Genotypes, Person
from get_data import Constants, get_drop_out

FREQ_CORRECTION = 0.005 # In the event the wild frequency goes below 0

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
            permute_driver(tmp, unknowns_pn + len(knowns_pn), "PN")
        else:
            self.indicies_pn.append(tmp)
        if unknowns_pd + len(knowns_pd) > 0 and unknowns_pd + len(knowns_pd) <= len(tmp):
            permute_driver(tmp, unknowns_pd + len(knowns_pd), "PD")
        else:
            self.indicies_pd.append(tmp)

        self.persons = []
        self.generate_persons()

        self.population_pn = [[None] * (len(self.knowns_pn) + self.unknowns_pn)] * (self.genotypes.allele_comb.size() ** (len(self.knowns_pn) + self.unknowns_pn))
        self.population_pd = [[None] * (len(self.knowns_pd) + self.unknowns_pd)] * (self.genotypes.allele_comb.size() ** (len(self.knowns_pd) + self.unknowns_pd))
        self.generate_populations()
        
        wild_vector = []
        if persons[0].a.length == -1 and person[0].b.length == -1:
            del population_pn[:]
            for i in range(0, knowns_pn.size() + unknowns_pn):
                wild_vector.append(persons[0])
            self.population_pn.append(wild_vector)
            del wild_vector[:]
        if persons[0].a.length == -1 and person[0].b.length == -1:
            del population_pd[:]
            for i in range(0, knowns_pd.size() + unknowns_pd):
                wild_vector.append(persons[0])
            self.population_pd.append(wild_vector)
            del wild_vector[:]

        self.check_person()
        
        self.pn = generate_px(drop_out_db, "PN")
        self.pd = generate_px(drop_out_db, "PD")
        self.lr = self.pn / self.pd

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
                permute(number_items, length, position, depth + 1, i, ID)
            return

        def permute_driver(self, number_items, length, ID):
            if length > 0 and length <= len(number_items):
                position = [0] * length
                permute(number_items, length, position, 0, 0, ID)

        def generate_persons(self):
            for i in range(0, len(genotypes.alleles)):
                for j in range(i, len(genotypes.alleles)):
                    self.persons.append(Person(genotypes.alleles[i], genotypes.alleles[j]))

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
                    for k in range(0, len(self.replicates[i])):
                        if self.knowns_pn[i] == self.replicates[j][k]:
                            found_a = True
                        if self.knowns_pn[i] == self.replicates[j][k]:
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
                    self.known_pn[i].hom = True
                    self.known_pn[i].het = False
                else:
                    self.known_pn[i].hom = False
                    self.known_pn[i].het = True
            for i in range(0, len(self.knowns_pd)):
                found_two = False
                found_a = False
                found_b = False
                for j in range(0, len(self.replicates)):
                    for k in range(0, len(self.replicates[i])):
                        if self.knowns_pd[i] == self.replicates[j][k]:
                            found_a = True
                        if self.knowns_pd[i] == self.replicates[j][k]:
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
                    self.known_pd[i].hom = True
                    self.known_pd[i].het = False
                else:
                    self.known_pd[i].hom = False
                    self.known_pd[i].het = True

        def generate_populations(self):
            for i in range(0, len(self.indicies_pn)):
                for j in range(0, len(self.indicies_pn[i])):
                    self.population_pn[i][j] = Person(self.genotypes.allele_comb[self.indicies_pn[i][j]].first, self.genotypes.allele_comb[self.indicies_pn[i][j]].second)
            for i in range(0, len(self.indicies_pd)):
                for j in range(0, len(self.indicies_pd[i])):
                    self.population_pd[i][j] = Person(self.genotypes.allele_comb[self.indicies_pd[i][j]].first, self.genotypes.allele_comb[self.indicies_pd[i][j]].second)

        def generate_px(self, db, ID):
            self.set_drop_out(db, CONTRIBUTORS_PN, ID)       # TO DO
            product = float(1.0)
            summation = float(0.0)
            if ID == "PN":
                for i in range(0, len(self.population_pn)):
                    if self.is_subset_px(i, ID):
                        for j in range(0, len(self.population_pn[i])):
                            if j >= (self.unknowns_pn + len(knowns_pn)) - ((self.unknowns_pn + len(self.knowns_pn)) - len(self.knowns_pn)):
                                product *= self.population_pn[i][j].freq
                        for j in range(0, len(self.population_pn[i])):
                            for k in range(0, len(self.replicates)):
                                product *= self.drop_out(self.population_pn[i][j], self.replicates[k], ID)
                        for j in range(0, len(replicates)):
                            product *= self.drop_in(self.population_pn[i], self.replicates[j])
                        summation += product
                        product = float(1.0)
                return summation
            elif ID == "PD":
                for i in range(0, len(self.population_pd)):
                    if self.is_subset_px(i, ID):
                        for j in range(0, len(self.population_pd[i])):
                            if j >= (self.unknowns_pd + len(knowns_pd)) - ((self.unknowns_pd + len(self.knowns_pd)) - len(self.knowns_pd)):
                                product *= self.population_pd[i][j].freq
                        for j in range(0, len(self.population_pd[i])):
                            for k in range(0, len(self.replicates)):
                                product *= self.drop_out(self.population_pd[i][j], self.replicates[k], ID)
                        for j in range(0, len(replicates)):
                            product *= self.drop_in(self.population_pd[i], self.replicates[j])
                        summation += product
                        product = float(1.0)
                return summation
            else:
                print "class Report (generate_px) ID is incorrectly inputted"

        def is_subset_px(self, i, ID):
            if ID == "PN":
                if self.population_pn[i][:len(self.knowns_pn)] in self.knowns_pn:
                    return True
                return False
            elif ID == "PD":
                if self.population_pd[i][:len(self.knowns_pd)] in self.knowns_pd:
                    return True
                return False
            else:
                print "class Report (is_subset_px) ID is incorrectly inputted"

        def drop_out(self, person, alleles, ID):
            if ID == "PN":
                if person.hom:
                    for i in range(0, alleles):
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
                    for i in range(0, alleles):
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

        def set_drop_out(self, db, contributors, ID):
            rates = []  # ['HET1', 'HET2', 'HOM1']
            for i in db:
                rates.append(i)
            rates = rates.sort()    # need HET1, then HET2
            quants = []
            for i in db['HET1'][1]['D']:
                quants.append(i)
            quants = quants.sort()
            l = float(0.0)
            h = float(0.0)
            for i in range(0, len(quants)):
                if quants[i] < self.constants.QUANT and quants[i + 1] > self.constants.QUANT:
                    l = quants[i]       # lower quant milepost
                    h = quants[i + 1]   # higher quant milepost
            full = float(1.0)
            for i in rates:
                if i == 'HOM1' and self.constants.DEDUCIBLE:
                    b = float(0.0)  # y-intercept or value for constant
                    slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['D'][self.locus][l] - (slope * l)
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
                    slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['D'][self.locus][l] - (slope * l)
                    PHET1 = slope * self.constants.QUANT + b
                    if ID == "PN":
                        self.constants.PN_PHET1 = PHET1
                    elif ID == "PD":
                        self.constants.PD_PHET1 = PHET1
                elif i == 'HET2' and self.constants.DEDUCIBLE:
                    b = float(0.0)
                    slope = (db[i][contributors]['D'][self.locus][h] - db[i][contributors]['D'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['D'][self.locus][l] - (slope * l)
                    PHET2 = slope * self.constants.QUANT + b
                    if ID == "PN":
                        self.constants.PN_PHET2 = PHET2
                        self.constants.PN_PHET0 = full - (self.constants.PN_PHET1 + PHET2)
                    elif ID == "PD":
                        self.constants.PD_PHET2 = PHET2
                        self.constants.PD_PHET0 = full - (self.constants.PD_PHET1 + PHET2)
                elif i == 'HOM1' and not self.constants.DEDUCIBLE:
                    b = float(0.0)  # y-intercept or value for constant
                    slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['ND'][self.locus][l] - (slope * l)
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
                    slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['ND'][self.locus][l] - (slope * l)
                    PHET1 = slope * self.constants.QUANT + b
                    if ID == "PN":
                        self.constants.PN_PHET1 = PHET1
                    elif ID == "PD":
                        self.constants.PD_PHET1 = PHET1
                elif i == 'HET2' and not self.constants.DEDUCIBLE:
                    b = float(0.0)
                    slope = (db[i][contributors]['ND'][self.locus][h] - db[i][contributors]['ND'][self.locus][l]) / (h - 1)
                    b = db[i][contributors]['ND'][self.locus][l] - (slope * l)
                    PHET2 = slope * self.constants.QUANT + b
                    if ID == "PN":
                        self.constants.PN_PHET2 = PHET2
                        self.constants.PN_PHET0 = full - (self.constants.PN_PHET1 + PHET2)
                    elif ID == "PD":
                        self.constants.PD_PHET2 = PHET2
                        self.constants.PD_PHET0 = full - (self.constants.PD_PHET1 + PHET2)

def generate_wild_allele_freq(alleles):
    c = float(1.0)
    for i in len(alleles):
        c -= alleles[i].freq
    if c < 0:
        c = FREQ_CORRECTION
    return c

'''
for i in name_files():
    if i.startswith('Evidence_'):
        numbers = read(i)

import json
with open('o.json', 'w') as o:
    o.write(json.dumps(get_drop_out('Drop_Out_Rates.csv'), indent=4))
'''

