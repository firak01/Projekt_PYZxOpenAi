'''
Created on 23.10.2026
Merke: Nicht für Eclipse 4.7 Oxygen Umgebung
       Dort nutze ich PyDev 6.3.2 diese stammt vom März 2018. 
       Python 3.7 erschien erst im Juni 2018. Deshalb ist Python 3.6.8 ein sinnvoller historischer Kompatibilitätskandidat für deine Eclipse-Installation
       ABER: Python 3.6.8 ist für OpenAI nicht geeignet... zu alt. 

@author: Fritz Lindhauer
'''

import openai

# Test
print(openai.version)

# Den openai -Endpoint ChatCompletion aufrufen
# response = openai.debugOpenai.
