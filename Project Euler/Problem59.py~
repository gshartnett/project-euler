#!/usr/bin/python -tt
import sys
import time
from collections import Counter
start_time = time.clock()

#load the encrypted message
with open('supplementary_files/p059_cipher.txt') as f:
    encrypted_string = f.read()

#annoyingly, this is as a string, convert it to a list
encrypted = []
temp_string = ''
i = 0
while i < len(encrypted_string):
  if encrypted_string[i] != ',':
    temp_string += encrypted_string[i]
    i += 1
  else:
    encrypted.append(int(temp_string))
    temp_string = ''
    i += 1
encrypted.append(int(temp_string)) #don't forget the last one

#find the most common p-letter combinations (trigraphs)
monograph = []
bigraph = []
trigraph = []
for i in range(len(encrypted)):
  monograph.append( chr(encrypted[i]) )
for i in range(len(encrypted)-1):
  bigraph.append( chr(encrypted[i])+ chr(encrypted[i+1]) )
for i in range(len(encrypted)-2):
  trigraph.append( chr(encrypted[i])+ chr(encrypted[i+1]) + chr(encrypted[i+2]) )
monograph_rank = Counter(monograph)
bigraph_rank = Counter(bigraph)
trigraph_rank = Counter(trigraph)

p = 6

print 'the ' + str(p) + ' most common monographs (letters) are:'
for i in range(p):
  print ord(monograph_rank.most_common(p)[i][0][0]), ' frequency = ', monograph_rank.most_common(p)[i][1]/float(len(encrypted))
print ''

print 'the ' + str(p) + ' most common bigraphs are:'
for i in range(p):
  print ord(bigraph_rank.most_common(p)[i][0][0]), ord(bigraph_rank.most_common(p)[i][0][1]), ' frequency = ', bigraph_rank.most_common(p)[i][1]/float(len(encrypted))
print ''

print 'the ' + str(p) + ' most common trigraphs are:'
for i in range(p):
  print ord(trigraph_rank.most_common(p)[i][0][0]), ord(trigraph_rank.most_common(p)[i][0][1]), ord(trigraph_rank.most_common(p)[i][0][2]), ' frequency = ', trigraph_rank.most_common(p)[i][1]/float(len(encrypted))
print ''

for n1 in range(97,123):
  for n2 in range(97,123):
    for n3 in range(97,123):
      #convert the 3-byte key into an n-byte key for the entire message
      key = [n1,n2,n3]
      bigkey = []
      for i in range(len(encrypted)/3):
        bigkey += key
      if len(encrypted) % 3 == 1:
        bigkey += [key[0]]
      if len(encrypted) % 3 == 2:
        bigkey += key[0:1]

      #preform the XOR cipher and tally up the ASCII score
      decrypted = []
      ascii_sum = 0
      for i in range(len(encrypted)):
        decrypted.append( bigkey[i]^encrypted[i] )
        ascii_sum += decrypted[i]

      #convert decrypted number list to string
      message = ''
      for i in range(len(encrypted)):
        message += chr(decrypted[i])
      
      if 'the' and 'and' and 'is' and 'that' and 'extinguish' in message:
        key_soln = key
        print 'key is', key_soln, 'aka', chr(key_soln[0])+chr(key_soln[1])+chr(key_soln[2])
        print 'answer is ', ascii_sum
        print message

print 'clock time = ', time.clock() - start_time, "seconds"





