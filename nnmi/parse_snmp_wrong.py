#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pprint import pprint

srcfile = 'nnm.csv'
outfile = 'sites_and_buildings.csv'
exclude = 'res'

def sites_and_buildings(inputfile, outputfile):
    '''Functions read from the NNMi (Nodes (All Attributes)) CSV export and write to the CSV parsed site with buildings and nodes.
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
#            device = single['Hostname']
            if exclude in device:
                continue
#            print('row for', device)
#            print('fullloc is',fulllocation ,'building is',building, 'and site is', site, 'and dev is', device)
            if site not in csv_dict:
                csv_dict[site] = dict()
#                print(csv_dict)
                csv_dict[site] = {building: [device]}
            elif building not in csv_dict[site]:
                csv_dict[site][building] = [device]
            else:
                csv_dict[site][building].append(device)
#    pprint([list.append()site,','.join(node) for site, building in csv_dict.items() for build, node in building.items()])
    with open(outputfile, mode='w', encoding='utf-8') as dst:
        filednames = ['Site', 'building', 'Device']
        writer = csv.writer(dst, delimiter=",", quoting=csv.QUOTE_ALL)

#        writer.writeheader()
        writer.writerow(filednames)
        for  site, building in csv_dict.items():
            for build, node in building.items():
#                print(site)
#                print(build)
#                print(', '.join(node))
                writer.writerow([site, build, ','.join(node)])
#        writer.writerow([site, building, device\
#                         for site, building in csv_dict.items()\
#                         for build, device in building.items() ])



#        pprint(csv_dict)
#            csv_dict[site] = 
#            csv_dict.setdefault(site, {building.strip(): list_devices.append(device)})
            #print(site, building)
#        pprint(csv_dict)

#            fulllocation = line['System Location']
#            hostname = line['Hostname']

#            csv_dict.
#        csv_dict = {line['System Location']: csv_dict[line['System Location']]line['Name'] for line in rdr }
        i = 0
#        for one in rdr:
#            if i < 50:
#                print(one['System Location'])
#                print(line['Name'], line['System Location'])
#                i += 1
    pass

sites_and_buildings(srcfile, outfile)


