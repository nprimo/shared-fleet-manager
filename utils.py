import urllib
import discord


# Error messages
def car_not_in_db(car_name: str) -> str:
    return f'{car_name} is not in the database!'


# functions
def is_location_valid(new_location: str) -> bool:
    parsed_url = urllib.parse.urlparse(new_location)
    if 'goo.gl' in parsed_url.netloc and\
            ('maps' in parsed_url.netloc or 'maps' in parsed_url.path):
        return True
    return False


def check_av_len(len_accepted: list[int]):
    def inner(func):
        def wrapped(message: discord.Message, av: list[str]):
            if len(av) in len_accepted:
                return func(message, av)
            else:
                return f'Error! Run command with number of args in {len_accepted}'
        return wrapped
    return inner
