import discord
from db import add_new_car, is_car_in_db, get_car_last_info, update_car


def hello(message: discord.Message, av: list[str]) -> str:
    return f'Hello {message.author.mention}'


def add(message: discord.Message, av: list[str]) -> str:
    if len(av) != 2:
        return 'Wrong number of arguments! Run: $add <name of the car>'
    if is_car_in_db(av[1]):
        return f'{av[1]} is already in the database!'
    # maybe check if the user is allowed to add
    return add_new_car(av[1])


def where(message: discord.Message, av: list[str]) -> str:
    if len(av) != 2:
        return 'Wrong number of arguments! Run: $where <name of the car>'
    if is_car_in_db(av[1]):
        return get_car_last_info(av[1])
    return f'{av[1]} is not in the database! Add the car with $add command'


def is_location_valid(new_location: str) -> bool:
    # check if location is a valid - for example Gmap?
    return True


def update(message: discord.Message, av: list[str]) -> str:
    if len(av) != 3:
        return """Wrong number of arguments!
    Run: $update <name of the car> <new poistion>"""
    if is_car_in_db(av[1]) and is_location_valid(av[2]):
        # maybe check if the user is allowed to update position
        new_info = {
            'location': av[2],
            'user': str(message.author)
        }
        return update_car(av[1], new_info)
    return f'{av[1]} is not in the database! Add the car with $add command'


def commands(key: str, message: discord.Message, av: list[str]) -> str:
    commands = {
        '$hello': hello,
        '$add': add,
        '$where': where,
        '$update': update,
    }
    command_to_exec = commands.get(key)
    if command_to_exec:
        return command_to_exec(message, av)
    return 'Unknown command'
