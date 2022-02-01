import requests
import re

BASE_URL = "https://pokeapi.co/api/v2/"


def request_data(pattern):
    response = requests.get(BASE_URL + pattern)
    body = response.json()
    return body


def pokemon_name_macht():
    # Get the number of pokemon (count)
    query_parameter = "pokemon?limit=1"
    body = request_data(query_parameter)
    count = body['count']

    # Get all the pokemon
    query_parameter = "pokemon?limit={}".format(count)
    body = request_data(query_parameter)

    count_match = 0

    for pokemon in body['results']:
        name = pokemon['name']
        if name.count('a') == 2 and 'at' in name:
            count_match += 1

    return count_match


def species_raichu_can_procreate():
    pattern = "pokemon-species/raichu"
    body = request_data(pattern)
    egg_groups = body['egg_groups']

    total_species = 0
    for egg_group in egg_groups:
        response = requests.get(egg_group['url'])
        body = response.json()
        total_species += len(body['pokemon_species'])

    return total_species


def max_min_type_fighting_generation_i_pokemon():
    pokemons = []
    id_max_generation_1 = 151
    fighting_type = request_data("/type/2")

    for pokemon in fighting_type["pokemon"]:
        id = re.findall('[0-9]+', pokemon["pokemon"]["url"][33:])

        if int(id[0]) <= id_max_generation_1:
            name = pokemon["pokemon"]["name"]
            url_pattern = "pokemon/{}".format(name)
            details = request_data(url_pattern)
            pokemons.append(int(details["weight"]))

    pokemons.sort()
    return pokemons[-1], pokemons[0]

