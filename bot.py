import discord
import urllib
from db import add_new_car, is_car_in_db, get_car_last_info, update_car


async def hello(message: discord.Message, av: list[str]) -> str:
    await message.author.send('hello')
    return f'Hello {message.author.mention}'


async def add(message: discord.Message, av: list[str]) -> str:
    if len(av) != 2:
        return 'Wrong number of arguments! Run: $add <name of the car>'
    car_name = av[1].lower()
    if is_car_in_db(car_name):
        return f'{car_name} is already in the database!'
    # maybe check if the user is allowed to add
    return add_new_car(av[1])


async def where(message: discord.Message, av: list[str]) -> str:
    if len(av) != 2:
        return 'Wrong number of arguments! Run: $where <name of the car>'
    car_name = av[1].lower()
    # add "all" option that showcases the postion of all the cars
    if is_car_in_db(car_name):
        return get_car_last_info(car_name)
    return f'{car_name} is not in the database! Add the car with $add command'


def is_location_valid(new_location: str) -> bool:
    parsed_url = urllib.parse.urlparse(new_location)
    if 'goo.gl' in parsed_url.netloc and\
            ('maps' in parsed_url.netloc or 'maps' in parsed_url.path):
        return True
    return False


async def update(message: discord.Message, av: list[str]) -> str:
    if len(av) != 3:
        return """Wrong number of arguments!
    Run: $update <name of the car> <new poistion - google maps link>"""
    car_name = av[1].lower()
    if is_car_in_db(car_name) and is_location_valid(av[2]):
        print(f'location valid: {is_location_valid(av[2])}')
        # maybe check if the user is allowed to update position
        new_info = {
            'location': av[2],
            'user': str(message.author)
        }
        return update_car(car_name, new_info)
    return f'{car_name} is not in the database! Add the car with $add command'


async def commands(key: str, message: discord.Message, av: list[str]) -> str:
    commands = {
        # help -> show all the commands options
        '$hello': hello,
        '$add': add,
        '$where': where,
        '$update': update,
        # reserve ?
        # info -> share all the raw data in private message
    }
    command_to_exec = commands.get(key)
    if command_to_exec:
        return await command_to_exec(message, av)
    return 'Unknown command'
