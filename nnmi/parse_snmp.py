#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pprint import pprint

srcfile = 'nnm.csv'
outfile = 'sites_and_buildings.csv'
exclude = '3925'

def sites_and_buildings(inputfile, outputfile):
    '''Functions read from the NNMi (Nodes (All Attributes)) CSV export and write to the CSV-file only uniq parsed site with buildings were equipement installed.
    Location should set in 'Site, Building' format.
    Function ignore devices with exclude string in the hostname.
    '''
    with open(inputfile, mode='r', encoding='utf-8') as f:
        rdr = csv.DictReader(f, delimiter=",")
        csv_dict = dict()
#        list_devices = list()
        for single in rdr:
            fulllocation = single['System Location'].strip()
            if not fulllocation:
                continue
#                fulllocation = 'Empty'
#            print(bool(fulllocation))
            site = fulllocation.split(sep=',')[0].strip()
            building = ','.join(fulllocation.split(sep=',')[1:]).strip()
            device = single['Hostname']
            if exclude in device:
                continue
#            print('row for', device)
#            print('fullloc is',fulllocation ,'building is',building, 'and site is', site, 'and dev is', device)
            if site not in csv_dict:
#                print(csv_dict)
                csv_dict[site] = {building}
#            elif building not in csv_dict[site]:
#                csv_dict[site][building] = [device]
            else:
                csv_dict[site].add(building)
        sorted_dict = dict()
        for a in sorted(csv_dict.keys()):
            sorted_dict[a] = csv_dict.get(a)

#        csv_dict = sorted(csv_dict)
#        print(type(csv_dict))
#        pprint(sorted_dict)
#    pprint([list.append()site,','.join(node) for site, building in csv_dict.items() for build, node in building.items()])
    with open(outputfile, mode='w', encoding='utf-8') as dst:
#        filednames = ['Site', 'building', 'Device']
        filednames = ['Site', 'buildings']
        writer = csv.writer(dst, delimiter=",", quoting=csv.QUOTE_ALL)

#        writer.writeheader()
        writer.writerow(filednames)
        for  site, building in sorted_dict.items():
            for build in building:
                writer.writerow([site, build])

    pass

sites_and_buildings(srcfile, outfile)


