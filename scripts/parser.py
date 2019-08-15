#!/usr/bin/env python3

'''Scripts builds routes in OpenVPN format from DNS-names list,
to exclude some host from routing to VPN.
It reads current /etc/openvpn/client/client.conf and merge with builded routes
to a new config without dublicates '''

import dns.resolver

src_dns_list = '/etc/openvpn/client/routes/dnslist'
tmp_ovpn_routelist = '/etc/openvpn/client/routes/routes'

gw = '192.168.1.1'
mask = '255.255.255.255'

src_ovpn_config = '/etc/openvpn/client/client.conf'
tmp_ovpn_config = '/etc/openvpn/client/client.tmp'


# Build uniq routes in OpenVPN format from dnslist file with DNS names

with open(src_dns_list) as dnslst, open(tmp_ovpn_routelist, 'w+') as routelist:
    #liststrings = ()
    routeset = set()
    for line in dnslst:
        dnsitem = line.strip()
        # print(line.readline())
        if dnsitem :
            answers = dns.resolver.query(dnsitem, 'A')
            for a_record in answers:
                single_route = 'route {} {} {} \n'.format(str(a_record), mask, gw)
                routeset.add(single_route)
    routestring = ''.join(routeset)
    routelist.write(routestring)
    #print(routestring)

# Extract from current OpenVPN config - config WITHOUT routes and build new temporary config with current OpenVPN config and routes

with open(tmp_ovpn_routelist) as src, open (src_ovpn_config) as config, open (tmp_ovpn_config, 'w+') as tempcong:
    for line in config:
        if not line.startswith('route'):
            tempcong.write(line)
    # last clear line
    tempcong.write('')
    for line2 in src:
        tempcong.write(line2)
    tempcong.write('')


# Rewrite current OpenVPN config with new config

with open (tmp_ovpn_config) as src, open (src_ovpn_config, 'w+') as dst:
    for line in src:
        dst.write(line)

