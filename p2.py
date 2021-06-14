import json
data = {}
data['clients'] = []

data['clients'].append({
    'marca': 'cisco',
    'tecnologias_c': 'servidores de alto rendimiento',
    'tecnologias_especiales': 'Firewall NG'})
data['clients'].append({
    'marca': 'huawei',

    'tecnologias_c': 'servidores de alto rendimiento',
    'tecnologias_especiales': 'Soluciones SD-WAN'})
data['clients'].append({
    'marca': 'hp',
    'tecnologias_c': 'almacenamiento en la nube',
    'tecnologias_especiales': 'Corteza XDR'})

with open('data10.json', 'w') as file:
    json.dump(data, file, indent=4)



