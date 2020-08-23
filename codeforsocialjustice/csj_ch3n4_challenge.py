# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:33:53 2020

Following the "Coding for Social Justice" challenges by Eric Matthes.
Challenges can be found here:
    https://ehmatthes.github.io/pcc_2e/challenges/coding_for_social_justice/

Chapter 3 Challenge:
    Know their Names
    Helping Organizations
Chapter 4 Challenge:
    Efficient Output

Source for Names and information: https://interactive.aljazeera.com/aje/2020/know-their-names/index.html

@author: Levitannin
"""

#   Know their Names
#       Original challenge is to make a list of names of the victims of police
#       brutality.  Initially this is done; then updated it to a dictionary.
knowTheirNames = [
    "Tanisha Anderson",
    "Michael Brown",
    "Tamir Rice",
    "Gabriella Nevarez",
    "Akai Gurley",
    "Eric Garner",
    "Janisha Fonville",
    "Freddie Gray",
    "Michelle Cusseaux",
    "Alton Sterling",
    "Philando Castille",
    "Botham Jean",
    "Stphon Clark",
    "Aura Rosser",
    "Alatiana Jefferson",
    "Breonna Taylor",
    "George Floyd"
]

#   CH 4 challenge is to add the loop printing process.
print("Know their names:\n")
for name in knowTheirNames:
    print(f"Know {name}.")

knowThesePeople = {
    1: {
     "name": "Tanisha Anderson",
     "age": 37,
     "year": 2014,
     "location": "Cleveland, OH",
     "death": "Fell or was slamed on the ground.  Estimated she was handcuffed on the ground for 21 minutes before parametics arrived."
     },
    2: {
     "name": "Michael Brown",
     "age": 18,
     "year": 2014,
     "location": "Ferguson, MI",
     "death": "Officer Darren Wilson shot and killed Brown claiming self defence after confronting Brown and his friend." 
     },
    3: {
     "name": "Tamir Rice",
     "age": 12,
     "year": 2014,
     "location": "Cleveland, OH",
     "death": "Played with a toy gun in a park leading to Officer Timothy Loehmann fatally shooting Rice upon arriving at the park."
     },
    4: {
     "name": "Gabriella Nevarez",
     "age": 22,
     "year": 2014,
     "location": "Sacramento CA",
     "death": "Nevarez rammed into a patrol car when asked to pull over.  Police opened fire on the car."
     },
    5: {
     "name": "Akai Gurley",
     "age": 28,
     "year": 2014,
     "location": "Brooklyn, NY",
     "death": "Officer Peter Liang and his partner were conducting 'vertical patrol' in a housing project when Gurley walked down the unlit stairs.  Liang fired his weapon."
     },
    6: {
     "name": "Eric Garner",
     "age": 43,
     "year": 2014,
     "location": "Staten Island, NY",
     "death": "Officer Daniel Pantaleo held Garner in a chokehold inspite of Garner saying 'I can't breathe' 11 times.  Garner was allegedly selling loose cigarettes."
     },
    7: {
     "name": "Aura Rosser",
     "age": 40,
     "year": 2014,
     "location": "Ann Arbor, MI",
     "death": "Rosser's boyfriend called police, asking her to be removed from the location after an altercation.  She had a knife she refused to put down; one officer tased her while another, Officer David Ried, fired a fatal shot."
     },
    8: {
     "name": "Janisha Fonville",
     "age": 20,
     "year": 2015,
     "location": "Charlotte, NC",
     "death": "Officers Anthony Holzhauer and Shon Sheffield arrived to take Fonville to a mental health facility after her partner, Korneshia Banks, was concerned Fonville would harm herself with a knife.  She was shot for lundging with a knife, though Banks says she did not see a knife in Fonville's hand"
     },
    9: {
     "name": "Freddy Gray",
     "age": 23,
     "year": 2015,
     "location": "Baltimore, MD",
     "death": "Placed in the back of a police fan with hands and feet shackled but no seatbelt, leaving him unable to protect himself as he was tossed around inside the vehicle.  Found dead 45 minutes after initial arrest, spinal cord nearly severed."
     },
    10: {
     "name": "Michelle Cusseaux",
     "age": 50,
     "year": 2015,
     "location": "Phoenix, AZ",
     "death": "Four police offcers arrived to transport Cusseaux to a court-ordered mental health facility.  Officers claimed she charged toward them with a hammer.  Sergeant Percy Dupra fired a single fatal shot."
     },
    11: {
     "name": "Alton Sterling",
     "age": 37,
     "year": 2016,
     "location": "Baton Rogue, LO",
     "death": "Officer Blane Salamoni and another officer tasered and pinned Sterling to the ground before firing six shots, killing him for selling CDs and DVDs."
     },
    12: {
     "name": "Philando Castille",
     "age": 32,
     "year": 2016,
     "location": "Falcon Heights, MN",
     "death": "Police shot Castile moments after he informed the officer he had a legal firearm in the vehicle during a traffic stop."
     },
   13: {
     "name": "Botham Jean",
     "age": 26,
     "year": 2018,
     "location": "Dallas, Texas",
     "death": "Died after off-duty police officer Amber Guyger entered his appartment, claiming she thought it was her own, and shot him."
     },
    14: {
     "name": "Stephon Clark",
     "age": 22,
     "year": 2018,
     "location": "Sacramento, CA",
     "death": "Officers claimed Clark was holding a gun as they shot him over 20 times; he was holding a mobile phone."
     },
    15: {
     "name": "Alatiana Jefferson",
     "age": 28,
     "year": 2019,
     "location": "Miami, FL",
     "death": "A neighbor called, saying Jefferson's front door was left open.  When police arrived, an officer shot Jefferson through the window."
     },
    16: {
     "name": "Breonna Taylor",
     "age": 26,
     "year": 2020,
     "location": "Louisville, KY",
     "death": "Taylor and her boyfriend, Kenneth Walker, were sleeping when plainclothes officers entered the home to execute a search warrant.  Thinking the officers were robers, Walker called 911 and fired a lisenced firearm.  Taylor, unarmed, was shot 8 timmes by police."
     },
    17: {
     "name": "George Floyd",
     "age": 46,
     "year": 2020,
     "location": "Minneapolis, MN",
     "death": "Officer Derek Chauvin knelt on Floyd's neck for eight minutes and 46 seconds while he was handcuffed on the ground.  Floyd pleaded with the four officers, three holding him down, that he could not breath.  This continued until he was unresponsive."
    }
    }

#   CH 4 challenge is to add the loop printing process.
for d in knowThesePeople:
    print(f"""
    Know {knowThesePeople[d]["name"]}.
    Who, in {knowThesePeople[d]["year"]}, died in {knowThesePeople[d]["location"]} the age {knowThesePeople[d]["age"]}.
    {knowThesePeople[d]["name"]} died because {knowThesePeople[d]["death"]}.
          """)

#   Helping Organizations
#   Make a list of several non-;police organizations in your community that 
#       which addresses any or all of these issues:
#           addition, domestic violence, mental health, etc.
organizations = [
    "NY Organization of Narcotics,\n\t212.689.1737",
    "Center on Addiction,\n\t212.841.5200",
    "Addiction Angel,\n\t646.404.0637",
    "Childhood Domestic Violence Association,\n\t212.330.8016",
    "New York City Anti-Violence Project,\n\t212.714.1141",
    "NYC Domestic Violence Inc.,\n\t917.736.4655",
    "National Alliance on Mental Illness - NYC,\n\t212.684.3264",
    "Vibrant Emotional Health,\n\t 212.254.0333",
    "Baltic Street AEH, Inc.,\n\t917.565.8294"
    ]

print("The following are resources external of the police force:\n")
for item in organizations:
    print(item)
