import datetime as dt
import os
import json

db_dir = './data/'
time_fmt = "%Y/%m/%d %H:%M:%S"


def is_car_in_db(car_name: str) -> bool:
    exp_file = db_dir + car_name + '.json'
    return os.path.exists(exp_file)


def get_cars_available() -> list[str]:
    file_in_db = os.listdir(db_dir)
    return [file.split('.')[0] for file in file_in_db]


# assume the file of the car is existing!
def add_new_car(car_name: str) -> str:
    msg = ''
    exp_file = db_dir + car_name + '.json'
    try:
        with open(exp_file, 'w') as f:
            f.write('{}')
        msg = f'succesfully added {car_name} to the database'
    except Exception:
        msg = f'{car_name} is already present in the database'
    return msg


# assume the file of the car is existing!
def update_car(car_name: str, new_info: dict) -> str:
    exp_file = db_dir + car_name + '.json'
    time = dt.datetime.now()
    time_str = time.strftime(time_fmt)
    with open(exp_file, 'r+') as f:
        cont = json.load(f)
    cont[time_str] = new_info
    with open(exp_file, 'w') as f:
        json.dump(cont, f, indent=2)
    msg = f'{car_name} updated succesfully'
    return msg


# assume the file of the car is existing!
def get_car_last_info(car_name: str) -> str:
    exp_file = db_dir + car_name + '.json'
    with (open(exp_file, 'r') as f):
        car_log = json.load(f)
    log_dates = [dt.datetime.strptime(date, time_fmt)
                 for date in car_log.keys()]
    if len(log_dates) == 0:
        return f'no information yet for {car_name}'
    last_update = sorted(log_dates)[-1].strftime(time_fmt)
    last_info = car_log[last_update]
    msg = f"last positon from {last_info['user']}: {last_info['location']}"
    return msg


def get_car_raw_info(car_name: str) -> str:
    exp_file = db_dir + car_name + '.json'
    with (open(exp_file, 'r') as f):
        car_log = json.load(f)
    return json.dumps(car_log, indent=2)


if __name__ == "__main__":
    print(get_car_last_info('fiesta'))
