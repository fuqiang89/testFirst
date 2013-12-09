import time
import os
from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmpwalk(oid=0):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget(('127.0.0.1', 161)),
        '%(oid)s' % {'oid':oid},
        lookupNames=True, lookupValues=True
       )
    
    name, value = varBinds[0]
    
#    print name
    return value

def snmpwalk_e(oid=0):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget(('127.0.0.1', 161)),
        '%(oid)s' % {'oid':oid},
    )
    
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                )
            )
        else:

            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    key = int(val.prettyPrint())
                    return key



#snmp_cpu = snmpwalk_e(oid='1.3.6.1.2.1.25.3.3.1.2')

#print snmp_cpu
