# run and see result ___> really cool example

from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

filename = 'c_12/buzzers.csv'
with open(filename) as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
print("----->------>first version - original<-----<-----<---") 
print()
pprint.pprint(flights)
print()
print("----->------>second version - convert2ampm + title <-----<-----<---") 
print()

fts = {convert2ampm(k): v.title() for k, v in flights.items()}

pprint.pprint(fts)
print()
print("----->------>third version - departure schedule for each destination <-----<-----<---") 
print()

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}

pprint.pprint(when)
print()