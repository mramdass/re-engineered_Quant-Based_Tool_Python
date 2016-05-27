import csv
from os import walk, path

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
        self.DEDUCIBLE = False
        self.MINIMUM_WILD_FREQUENCY = 0.0005

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
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
            else:
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
        elif key_1[0] != 'Constant':
            if key_1[1] not in tmp[key_1[0]]:
                tmp[key_1[0]][key_1[1]] = {}
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
            else:
                if key_1[2] not in tmp[key_1[0]][key_1[1]]:
                    tmp[key_1[0]][key_1[1]][key_1[2]] = {}
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                else:
                    if i[1] not in tmp[key_1[0]][key_1[1]][key_1[2]]:
                        tmp[key_1[0]][key_1[1]][key_1[2]][i[1]] = {}
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                    else:
                        for j in range(2, len(head)):
                            if head[j] not in tmp[key_1[0]][key_1[1]][key_1[2]][i[1]]:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
                            else:
                                tmp[key_1[0]][key_1[1]][key_1[2]][i[1]][head[j]] = i[j]
    return tmp
    
