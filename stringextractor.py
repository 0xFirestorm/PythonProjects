import re

file_path = '#ENTER .EXE FILE PATH HERE'
with open(file_path,'rb') as file:
    allstrings = file.read()
    #Decode Byte Literal into strings
    #Use the appopriate encoding based on the character sets, common ones include ASCII/utf-8/latin-1
    allstrings = allstrings.decode('#ENTER ENCODING TYPE HERE')
    #for ip address:
    ip_add = re.findall("\d+\.\d+\.\d+\.\d+", allstrings)
    #for dll files:
    dllfile = re.findall(".+\.dll",allstrings)
    #for urls:
    urlex = re.findall("www\..+\..+",allstrings)

print(f"There are {len(allstrings)} strings present in this file:\n",allstrings)
print(f"There are {len(ip_add)} ip addresses present in the above strings:\n",ip_add,"\n")
print(f"There are {len(dllfile)} .dll files present in the above strings:\n",dllfile,"\n")
print(f"There are {len(urlex)} URL's present in the above strings:\n",urlex,"\n")
