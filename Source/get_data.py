import csv

LOCUS = ['D8', 'D21', 'D7', 'CSF', 'D3', 'TH01', 'D13', 'D16', 'D2', 'D19', 'vWA', 'TPOX', 'D18', 'D5', 'FGA']
RACE = ['BLACK', 'CAUCASIAN', 'HISPANIC', 'ASIAN']

def name_files():
    files = []
    for (dirpath, dirnames, filenames) in walk(path.dirname(path.realpath(__file__))):
        files.extend(filenames)
        break
    return files

def read_csv(name):
    with open(name, 'rb') as f:
        reader = list(csv.reader(f))
    f.close()
    return reader

class Constants:
    def __init__(self):
        self.PC0 = 0
        self.PC1 = 0
        self.PC2 = 0
        
        self.PN_PHET0 = 0
        self.PN_PHET1 = 0
        self.PN_PHET2 = 0
        self.PN_PHOM0 = 0
        self.PN_PHOM1 = 0

        self.PD_PHET0 = 0
        self.PD_PHET1 = 0
        self.PD_PHET2 = 0
        self.PD_PHOM0 = 0
        self.PD_PHOM1 = 0

        self.RACE = "BLACK"
        self.CONTRIBUTORS_PN = 0
        self.CONTRIBUTORS_PD = 0
        self.QUANT = 0
        self.DEDUCIBLE = 'ND'
        self.MINIMUM_WILD_FREQUENCY = 0.0005
        self.THETA = 0.03

def get_drop_out(name):
    tmp = {}
    data = read_csv(name)
    head = data[0]
    for i in data:
        key_1 = i[0].split('-')
        if key_1[0] not in tmp and key_1[0] != 'Constant':
            tmp[key_1[0]] = {}
            if key_1[1] not in tmp[key_1[0]]:
                tmp[key_1[0]][key_1[1]] = {}
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
            else:
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
        elif key_1[0] != 'Constant':
            if key_1[1] not in tmp[key_1[0]]:
                tmp[key_1[0]][key_1[1]] = {}
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
            else:
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
                    else:
                        for j in range(2, len(head)):
                            tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = float(i[j])
    return tmp

def get_allele_freq(name):
    tmp = {}
    data = read_csv(name)
    head = data[0]
    for i in data:
        if i[0] not in tmp and i[0] != 'Locus':
            tmp[i[0]] = {}
            if i[1] not in tmp[i[0]]:
                tmp[i[0]][float(i[1])] = {}
                for j in range(2, len(head)):
                    tmp[i[0]][float(i[1])][head[j]] = float(i[j])
            else:
                for j in range(2, len(head)):
                    tmp[i[0]][float(i[1])][head[j]] = float(i[j])
        elif i[0] != 'Locus':
            if i[1] not in tmp[i[0]]:
                tmp[i[0]][float(i[1])] = {}
                for j in range(2, len(head)):
                    tmp[i[0]][float(i[1])][head[j]] = float(i[j])
            else:
                for j in range(2, len(head)):
                    tmp[i[0]][float(i[1])][head[j]] = float(i[j])
    return tmp

def get_drop_in(name):
    tmp = {}
    data = read_csv(name)
    for i in data:
        tmp[i[0]] = float(i[1])
    return tmp

def get_mixture(name):
    tmp = {}
    data = read_csv(name)
    head = {}
    for i in range(0, len(data[0])):
        head[data[0][i]] = i
            
    for i in data:
        if i[0] not in tmp and i[0] != 'Case Name':
            tmp[i[0]] = {}
            for j in head:
                if j not in ['Case Name', 'Locus', 'Replicate 1', 'Replicate 2', 'Replicate 3', 'Known Pn 1', 'Known Pn 2', 'Known Pn 3', 'Known Pn 1', 'Known Pn 2', 'Known Pn 3']:
                    tmp[i[0]][j] = i[head[j]]
            for j in LOCUS:
                tmp[i[0]][j] = {}
                if 'Replicate 1' in head:
                    if i[head['Replicate 1']] not in ['INC', 'NEG', '']:
                        tmp[i[0]][j]['Replicate 1'] = [float(k) for k in i[head['Replicate 1']].split(';')]
                    elif i[head['Replicate 1']] == 'NEG':
                        tmp[i[0]][j]['Replicate 1'] = []
                    elif i[head['Replicate 1']] in ['INC', '']:
                        if 'Replicate 1' in tmp[i[0]][j]:
                            tmp[i[0]][j].pop('Replicate 1')
                    
                if 'Replicate 2' in head:
                    if i[head['Replicate 2']] not in ['INC', 'NEG', '']:
                        tmp[i[0]][j]['Replicate 2'] = [float(k) for k in i[head['Replicate 2']].split(';')]
                    elif i[head['Replicate 2']] == 'NEG':
                        tmp[i[0]][j]['Replicate 2'] = []
                    elif i[head['Replicate 2']] in ['INC', '']:
                        if 'Replicate 2' in tmp[i[0]][j]:
                            tmp[i[0]][j].pop('Replicate 2')
                    
                if 'Replicate 3' in head:
                    if i[head['Replicate 3']] not in ['INC', 'NEG', '']:
                        tmp[i[0]][j]['Replicate 3'] = [float(k) for k in i[head['Replicate 3']].split(';')]
                    elif i[head['Replicate 3']] == 'NEG':
                        tmp[i[0]][j]['Replicate 3'] = []
                    elif i[head['Replicate 3']] in ['INC', '']:
                        if 'Replicate 3' in tmp[i[0]][j]:
                            tmp[i[0]][j].pop('Replicate 3')
                    
                if 'Known Pn 1' in head:
                    if i[head['Known Pn 1']] != '':
                        tmp[i[0]][j]['Known Pn 1'] = (float(i[head['Known Pn 1']].split(';')[0]), float(i[head['Known Pn 1']].split(';')[1]))
                if 'Known Pn 2' in head:
                    if i[head['Known Pn 2']] != '':
                        tmp[i[0]][j]['Known Pn 2'] = (float(i[head['Known Pn 2']].split(';')[0]), float(i[head['Known Pn 2']].split(';')[1]))
                if 'Known Pn 3' in head:
                    if i[head['Known Pn 3']] != '':
                        tmp[i[0]][j]['Known Pn 3'] = (float(i[head['Known Pn 3']].split(';')[0]), float(i[head['Known Pn 3']].split(';')[1]))
                if 'Known Pd 1' in head:
                    if i[head['Known Pd 1']] != '':
                        tmp[i[0]][j]['Known Pd 1'] = (float(i[head['Known Pd 1']].split(';')[0]), float(i[head['Known Pd 1']].split(';')[1]))
                if 'Known Pd 2' in head:
                    if i[head['Known Pd 2']] != '':
                        tmp[i[0]][j]['Known Pd 2'] = (float(i[head['Known Pd 2']].split(';')[0]), float(i[head['Known Pd 2']].split(';')[1]))
                if 'Known Pd 3' in head:
                    if i[head['Known Pd 3']] != '':
                        tmp[i[0]][j]['Known Pd 3'] = (float(i[head['Known Pd 3']].split(';')[0]), float(i[head['Known Pd 3']].split(';')[1]))
        elif i[0] != 'Case Name':
            if 'Replicate 1' in head:
                if i[head['Replicate 1']] not in ['INC', 'NEG', '']:
                    tmp[i[0]][i[head['Locus']]]['Replicate 1'] = [float(k) for k in i[head['Replicate 1']].split(';')]
                elif i[head['Replicate 1']] == 'NEG':
                    tmp[i[0]][i[head['Locus']]]['Replicate 1'] = []
                elif i[head['Replicate 1']] in ['INC', '']:
                    if 'Replicate 1' in tmp[i[0]][i[head['Locus']]]:
                        tmp[i[0]][i[head['Locus']]].pop('Replicate 1')
            if 'Replicate 2' in head:
                if i[head['Replicate 2']] not in ['INC', 'NEG', '']:
                    tmp[i[0]][i[head['Locus']]]['Replicate 2'] = [float(k) for k in i[head['Replicate 2']].split(';')]
                elif i[head['Replicate 2']] == 'NEG':
                    tmp[i[0]][i[head['Locus']]]['Replicate 2'] = []
                elif i[head['Replicate 2']] in ['INC', '']:
                    if 'Replicate 2' in tmp[i[0]][i[head['Locus']]]:
                        tmp[i[0]][i[head['Locus']]].pop('Replicate 2')
            if 'Replicate 3' in head:
                if i[head['Replicate 3']] not in ['INC', 'NEG', '']:
                    tmp[i[0]][i[head['Locus']]]['Replicate 3'] = [float(k) for k in i[head['Replicate 3']].split(';')]
                elif i[head['Replicate 3']] == 'NEG':
                    tmp[i[0]][i[head['Locus']]]['Replicate 3'] = []
                elif i[head['Replicate 3']] in ['INC', '']:
                    if 'Replicate 3' in tmp[i[0]][i[head['Locus']]]:
                        tmp[i[0]][i[head['Locus']]].pop('Replicate 3')
            
            if 'Known Pn 1' in head:
                if i[head['Known Pn 1']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pn 1'] = (float(i[head['Known Pn 1']].split(';')[0]), float(i[head['Known Pn 1']].split(';')[1]))
            if 'Known Pn 2' in head:
                if i[head['Known Pn 2']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pn 2'] = (float(i[head['Known Pn 2']].split(';')[0]), float(i[head['Known Pn 2']].split(';')[1]))
            if 'Known Pn 3' in head:
                if i[head['Known Pn 3']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pn 3'] = (float(i[head['Known Pn 3']].split(';')[0]), float(i[head['Known Pn 3']].split(';')[1]))
            if 'Known Pd 1' in head:
                if i[head['Known Pd 1']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pd 1'] = (float(i[head['Known Pd 1']].split(';')[0]), float(i[head['Known Pd 1']].split(';')[1]))
            if 'Known Pd 2' in head:
                if i[head['Known Pd 2']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pd 2'] = (float(i[head['Known Pd 2']].split(';')[0]), float(i[head['Known Pd 2']].split(';')[1]))
            if 'Known Pd 3' in head:
                if i[head['Known Pd 3']] != '':
                    tmp[i[0]][i[head['Locus']]]['Known Pd 3'] = (float(i[head['Known Pd 3']].split(';')[0]), float(i[head['Known Pd 3']].split(';')[1]))
    
    for case in tmp:
        for locus in LOCUS:
            unique_alleles = []
            if 'Replicate 1' in tmp[case][locus]:
                unique_alleles += tmp[case][locus]['Replicate 1']
            if 'Replicate 2' in tmp[case][locus]:
                unique_alleles += tmp[case][locus]['Replicate 2']
            if 'Replicate 3' in tmp[case][locus]:
                unique_alleles += tmp[case][locus]['Replicate 3']
            unique_list = list(set(unique_alleles))
            unique_list.sort()
            tmp[case][locus]['Unique Alleles'] = unique_list
    
    return tmp
            
    
