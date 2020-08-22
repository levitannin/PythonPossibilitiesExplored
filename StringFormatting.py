# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:11:46 2020

Some Basic Python Pratice and notes while preparing for python tutorial 101
on twitch.tv/levitannin

@author: Levitannin
"""

#------------------------------------------------------------------------------
#   Old school, or original python formatting using %-formatting-code
creepycrawly = "Spider"
print("Hello, %s." % creepycrawly)  #   %s == string format.

num = 8
print("Hello, %s.  You have %s legs!" % (creepycrawly, num))

#       Issues with this formatting: multiple parameters make this terrible to
#           read and write out the code.
profession = "intel gathering"
bestfriend = "Julius Squeezer"
print("Hello %s!  Did you know you have %s legs and are an %s?  How is your best friend, %s" % (creepycrawly, num, profession, bestfriend))

#------------------------------------------------------------------------------
#   Mid school, str.format() method
#   Use normal function call syntax
print("Hello {}, you have {} legs, woah!".format(creepycrawly, num))

#   Change order of variables called.
print("What has {1} legs?  Oh, a {0}!".format(creepycrawly, num))

#   Pull this data from a dictionary
spiderfriend = {"insect": "Spider", "legs": 8}
print("What has {legs} legs?  Oh, a {insect}!".format(legs = spiderfriend["legs"], insect = spiderfriend["insect"]))
#   Or use ** as a neat trick for dealing with dictionaries!
print("What has {legs} legs?  Oh, a {insect}!".format(**spiderfriend))

#       Issues with the format: just barely better than above!
print(("Hello {creepycrawly}!  Did you know you have {num} legs and are an {profession}?  How is your best friend, {bestfriend}") \
      .format(creepycrawly = creepycrawly, num = num, profession = profession, bestfriend = bestfriend))
#           Only if this is done with a dictionary could this be cleaned up.  

#------------------------------------------------------------------------------
#   New school, f-strings
#   Also referred to as formatting string literals.
print(f"Hello, {creepycrawly}.  You have {num} legs?!")

#   f-strings are evaluated at runtime so valid expressions can be made internal
s = f"{2 * 37}"
print(s)

#   You can also call functions in an f-string call.
def lowerit(x):
    return x.lower()

excite = "SPIDER"
print(f"You were too excited so, I lowered {excite} to {lowerit(excite)}")
print(f"{excite.lower()}")
#   Can even be used with classes!

#   Multiple lines with f-strings
message = (
    f"Hi {creepycrawly}! "
    f"Do you like being an {profession} "
    f"How is {bestfriend}?"
    )
print(message)
#   To do this with one f you need triple quotes.
message = f"""
Hi {creepycrawly}!
Do you like being an {profession}
How is {bestfriend}?
"""

print(message)
