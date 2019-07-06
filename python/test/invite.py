#!/usr/bin/env python
# -*- coding: utf-8 -*-

invites = ['father', 'mather', 'son']
for invite in invites:
    print("%s, invite you to have dinner with me." % (invite.title()))

print("\nMy %s can\'t keep the appointment." % (invites[0]))
invites[0] = 'wife'
for invite in invites:
    print("%s, invite you to have dinner with me." % (invite.title()))

print("\nI found a bigger taber.")
invites.insert(0, 'gradefather')
middle = int(len(invites)/2)
invites.insert(middle, 'brother')
invites.append('sister')
for invite in invites:
    print("%s, invite you to have dinner with me." % (invite.title()))

print("\nBecause the new table can\'t be delivered, only two people are\
 invited.")
while len(invites)>2:
    pops =invites.pop()
    print("%s, Because the new table can\'t be deliverd, so you can\'t\
 invite you to dinner." % (pops))  
for invite in invites:
    print("%s, invite you to have dinner with me." % (invite.title()))

del invites[:]
print(invites)

