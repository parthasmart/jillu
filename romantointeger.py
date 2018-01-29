class solution:
def roman to int(self,s):
roman_value={'I':1,'V':5,'X':10.'L':50}
int_value=0
for i range (len(s)):
if i>0 and roman_value[s[i]]>roman_value[s[i-1]]:
  int_value+=rom_value[s[i]]-2*roman_val[s[i-1]]
else:
  int_value+=rom_value[s[i]]
  return int_val
  

