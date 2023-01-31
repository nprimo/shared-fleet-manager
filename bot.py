import discord
import db
from utils import check_av_len, is_location_valid, car_not_in_db


def hello(message: discord.Message, av: list[str]) -> str:
    return f'Hello {message.author.mention}'


@check_av_len([2])
def add(message: discord.Message, av: list[str]) -> str:
    car_name = av[1].lower()
    if db.is_car_in_db(car_name):
        return db.get_car_last_info(car_name)
    # maybe check if the user is allowed to add
    return db.add_new_car(av[1])


@check_av_len([1, 2])
def where(message: discord.Message, av: list[str]) -> str:
    if len(av) == 1:
        cars_available = db.get_cars_available()
        return '\n'.join([
            f'{car}: {db.get_car_last_info(car)}'
            for car in cars_available
        ])
    car_name = av[1].lower()
    if db.is_car_in_db(car_name):
        return db.get_car_last_info(car_name)
    return car_not_in_db(car_name)


@check_av_len([3])
def update(message: discord.Message, av: list[str]) -> str:
    car_name = av[1].lower()
    if db.is_car_in_db(car_name) and is_location_valid(av[2]):
        print(f'location valid: {is_location_valid(av[2])}')
        # maybe check if the user is allowed to update position
        new_info = {
            'location': av[2],
            'user': str(message.author)
        }
        return db.update_car(car_name, new_info)
    return f'{car_name} is not in the database! Add the car with $add command'


@check_av_len([1, 2])
def info(message: discord.Message, av: list[str]) -> str:
    if len(av) == 1:
        msg = 'The available cars are:\n'
        msg += '\n'.join(db.get_cars_available())
        return msg
    car_name = av[1].lower()
    if db.is_car_in_db(car_name):
        msg = db.get_car_raw_info(car_name)
    else:
        msg = car_not_in_db(car_name)
    return msg


def commands(key: str, message: discord.Message, av: list[str]) -> str:
    commands = {
        # help -> show all the commands options
        '$hello': hello,
        '$add': add,
        '$where': where,
        '$update': update,
        '$info': info,
        # reserve ?
    }
    command_to_exec = commands.get(key)
    if command_to_exec:
        return command_to_exec(message, av)
    return 'Unknown command'
