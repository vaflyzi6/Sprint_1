from itertools import count


def get_year(year, country):
    world_champions[year] = country

def get_world_champions(dict):
    for year_country in world_champions.items():
        print(f'{year_country[0]} - {year_country[1]}')

def check_country(country):
    if country in world_champions.values():
        print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
    else:
        print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')


world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

country = 'Италия'

get_year(2022, 'Аргентина')
get_world_champions(world_champions)
check_country(country)
