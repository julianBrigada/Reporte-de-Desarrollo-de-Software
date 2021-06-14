import json
with open('data10.json') as file:
    data = json.load(file)

    for client in data['clients']:
        print('Marca:', client['marca'])
        print('Tecnologias c:', client['tecnologias_c'])
        print('Tecnologias especiales:', client['tecnologias_especiales'])
        print('')

