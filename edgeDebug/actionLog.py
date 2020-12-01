import sys
import time
import re

# Example "run"
# logread -f | python actionLog.py action_id 876876
# logread -f | python actionLog.py usprxedge:l5f58e19c2ebc93700459b5ca,hmigauge:l5f58e19cda3994a414b567fd,hmisignalled:l5f58e19c2ebc93700459b5c4
# logread -f | python actionLog.py usp:l5f104a5ff936e13e915d6fb9

# Example raw logread OP
# Sep 16 16:08:33 swi-mdm9x28-wp user.info Legato:  INFO | actions[1123]/actionRunner T=Javascript | actionRunner_JS.c js_LogInfoHandler() 1007 | action_id:l5f58e19c2ebc93700459b5c4 | [1,14,0,0,0,15]

actions = {}

def index_in_list(a_list, index):
    print(index < len(a_list))

# print("\n".join(sys.argv))

## match any action name info

numberOfArgs = len(sys.argv) -1

idd = {}

if (numberOfArgs == 1):  # Expected list is ["thisScript", "typeoffilter" ]
    processidlist = sys.argv[1]
    idlist = processidlist.split(',')
    for ids in idlist:
        idss = ids.split(':')
        idd[idss[1]] = idss[0]
        # print idd
    
elif (numberOfArgs == 2):  # Expected list is ["thisScript", "typeoffilter", "filter" ]
    processidlist = sys.argv[1]
    processfilter = sys.argv[2]
    




# process data from logread 

try:
    buff = ''
    while True:
        buff += sys.stdin.read(1)
        if buff.endswith('\n'):
            line = buff[:-1] 
            #print line
            info = line.split('|')

            try:
                if ("action_id:" not in line ):
                    pass
                else:
                    timeofday = info[0].split()
                    timeofday = timeofday[2]
                    id = info[3].strip()
                    id = re.sub('action_id:', '', id)
                    # try and find a matching id name
                    # for key in id.keys():
                    #     if key
                    consolelog = info[4].strip()
                    idname = "xxxxxxxxxx"
                    if id in idd:
                        idname = idd[id]                      
                    print  timeofday.ljust(10)[:10], id.ljust(28)[:28], idname.ljust(18)[:18] , consolelog
            except Exception as e: 
                print(e)
            
            buff = ''
                
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
