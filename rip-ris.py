#! /usr/bin/env python3
###############################################################################
# SIDN Labs
# Fri Mar  6 11:55:19 CET 2020
# Joao Ceron  - jooa.ceron@sidn.nl
###############################################################################

###############################################################################
### Python modules
import requests
import pandas as pd
import numpy as np
import os
import sys
import argparse
from datetime import datetime

###############################################################################
### Program settings
verbose = False
version = 0.1
program_name = os.path.basename(__file__)

###############################################################################
### Definitions
router_collector = {
    "00" : "AMS-RIPE",
    "01" : "LHR-LINX",
    "02" : "CDG-SFINX",
    "03" : "AMS-AMIX",
    "04" : "GVA-Geneva",
    "05" : "VIE-VIENNA",
    "06" : "NRT-JAPAN",
    "07" : "ANR-SWEDEN",
    "08" : "SJC-USA",
    "09" : "ZRH-ZURICH",
    "10" : "MXP-MILAN",
    "11" : "NYC-USA",
    "12" : "FRA-DE-CIX",
    "13" : "DME-MSK-IX",
    "14" : "PAO-USA",
    "15" : "GRU-IXBR",
    "16" : "MIA-MIA",
    "18" : "BCN-CATNIX",
    "19" : "JNB-AFRICA",
    "20" : "ZHR-SWISSIX",
    "21" : "CDG-FranceIX",
    "22" : "OTP-ROMANIA.",
    "23" : "SIN-SINGAPURE",
    "24" : "MVD-URUGUAY",
}

###############################################################################
### Subrotines

def parser_args ():
    parser = argparse.ArgumentParser(prog=program_name, usage='%(prog)s [options]')
    parser.add_argument('-v',"--version", help="print version and exit", action="store_true")
    parser.add_argument("-d","--debug", help="print debug info", action="store_true")
    parser.add_argument('-p','--prefix', nargs='?', help="prefix to be searched on the system. Ex.: 194.0.28.53/24")
    parser.add_argument('-t','--timestamp', nargs='?', help="timestamp used in the search. Ex.: 1579686913")
    parser.add_argument("--csv", help="print output in CSV format", action="store_true")
    return parser
#------------------------------------------------------------------------------
def get_peers(args):

    if (args.timestamp):
        url = 'https://stat.ripe.net/data/bgp-state/data.json?resource={0}&timestamp={1}'.format(args.prefix, args.timestamp)
    else:
        url = 'https://stat.ripe.net/data/bgp-state/data.json?resource={0}'.format(args.prefix)

    if (args.debug):
        print("# {}".format(url))

    data = requests.get(url).json()
    if not any(data['data']):
        return (None,None)
    query_time =  data['data']['query_time']

    data = data['data']['bgp_state']
    bgp_state = []

    # evaluate all the routes in the consolitated BGP table
    if data:
        for item in data:
            route_info = {
                'peer': item['path'][0],
                'collector': router_collector[item['source_id'].split("-")[0]],
                'as_path': item['path'],
                'community': item['community'],
            }
            bgp_state.append(route_info)

    return (bgp_state, query_time)

###############################################################################
## Main Process

parser = parser_args()
args = parser.parse_args()

if (args.version):
    print (version)
    sys.exit(0)

if not (args.prefix):
    print ("You should define a prefix to be requested on the system RIP RIS.")
    sys.exit(0)

# do the query
(bgp_state, query_time) = get_peers(args)
df = pd.DataFrame(bgp_state)

if (args.timestamp):
    ts = int(args.timestamp)

print ("# {}".format(query_time))
if (args.csv):
    print(df.to_csv(index=False))
else:
    print(df.to_string())

