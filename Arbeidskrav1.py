#!/usr/bin/env python
# coding: utf-8

# # Arbeidskrav 1

# Oppgave:
# Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.
# 
# Lag et Python-program som beregner og presenterer (viser) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).
# 
# Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)
# 
# Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
# Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
# Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
# Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
# Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

# In[9]:


FE = 5000 # Forsikring elbil kr/år
FB = 7500 # Forsikring bensinbil kr/år

TA = 8.38 # Trafikkforsikringsavgift kr/dag

DE = 0.2 # Drivstoffbruk elbil kWh/km
SP = 2 # strømpris kr/kWh
PE = DE*SP # Kostnad drivstoff elbil kr/km

PB = 1 # Kostnad drivstoff bensinbil kr/km

BE = 0.1 # Bompenger elbil kr/km
BB = 0.3 # Bompenger bensinbil kr/km

KM = 10000 # Antall kjørte kilometer per år

EL = FE + (TA * 365) + (PE * KM ) + (BE * KM) # Elbil pr år

B = FB + (TA * 365) + (PB * KM ) + (BB * KM) # Bensinbil pr år

DIFF = B-EL


# In[11]:


print ('Årlig totalkostnad for elbil er', EL, 'kr')
print ('Årlig totalkostnad for bensinbil er', B, 'kr')
print ('Årlig kostnadsdifferanse mellom elbil og bensinbil er', DIFF, 'kr')

