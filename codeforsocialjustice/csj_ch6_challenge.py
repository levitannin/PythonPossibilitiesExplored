# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:33:53 2020

Following the "Coding for Social Justice" challenges by Eric Matthes.
Challenges can be found here:
    https://ehmatthes.github.io/pcc_2e/challenges/coding_for_social_justice/

Chapter 6 Challenge:
    Annual Incidents of US Police Killings
    International Rates of Police Killings
    Incarcration Rates
    Police Killings and Incarceration Rates

@author: Levitannin
"""
#------------------------------------------------------------------------------
#   Annual Incidents of US Police Killings
#       Visit National Trends for Police Violence: https://mappingpoliceviolence.org/
#       Choose several years, make a dictionary where keys are years and value
#       is the number of deaths via police in that year in the US.
policeViolence = {
    2013: "1,107",
    2014: "1,051",
    2015: "1,104",
    2016: "1,072",
    2017: "1,094",
    2018: "1,143",
    2019: "1,102",
    2020: "732"
    }

for year, death in policeViolence.items():
    print(f"In {year}, {death} people died due to Police Violence.")

#------------------------------------------------------------------------------
#   International Rates of Police KIllings
#   Find the rates for police violence in 5 - 10 other countries.
internationalViolence = {
    "Venezuela": "1830.2",
    "Jamaica": "472.7",
    "Philippines": "322.4",
    "Afghanistan": "170.5",
    "South Africa": "76.9",
    "Iran": "36.6",
    "Canada": "9.7",
    "Japan": "0.2",
    "Denmark": "0"
    }

print()
for country, rate in internationalViolence.items():
    print(f"In {country}, the rate for death by police violence for every 10 "\
          f"million people is {rate}")

#------------------------------------------------------------------------------
#   Incarcration Rate
#   Find the rates for incarceration in 5 - 10 countries
internationalIncarceration = {
    "Venezuela": "178",
    "Jamaica": "138",
    "Philippines": "179",
    "Afghanistan": "87",
    "South Africa": "275",
    "Iran": "25.1",
    "Canada": "107",
    "Japan": "39",
    "Denmark": "63"
    }

print()
for country, rate in internationalIncarceration.items():
    print(f"In {country}, the rate for incarceration per 100,000 population is"\
          f" {rate}")

#------------------------------------------------------------------------------
#   Police Killings and Incarceration Rates
#       Combine the above dictionaries into one, then print with a loop.
policeAndIncarceration={
    "Venezuela": ["178", "1830.2"],
    "Jamaica": ["138", "472.7"],
    "Philippines": ["179", "322.4"],
    "Afghanistan": ["87", "170.5"],
    "South Africa": ["275", "76.9"],
    "Iran": ["25.1", "36.6"],
    "Canada": ["107", "9.7"],
    "Japan": ["39", "0.2"],
    "Denmark": ["63", "0"]
    }

print()
for country, rate in internationalIncarceration.items():
    print(f"In {country}, the rate for incarceration per 100,000 population is"\
          f" {rate[0]} and the rate for death by police violence for every 10 "\
              f"million people is {rate[1]}")
