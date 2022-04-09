from FieldBook import *
import LoadTxt
from datetime import date, timedelta


paralist = {
    'type': '',
    'name': '',
    'password': '',
    'borrower_name1': '',
    'borrower_name2': '',
    'borrower1contact_info': '',
    'borrower2contact_info': '',
    'field_type': 1,
    'date': '',
    'start_time': '',
    'how_long': 2,
    'join_num': 2,
    'person_id': 1,
    'person_response': '',
    'person_tel': '',
    'user_list': '',
}

if __name__ == '__main__':
    # default: after 2 days
    curr_time = date.today()
    delta = timedelta(days=2)
    dates = (curr_time + delta).strftime("%Y-%m-%d")
    paralist['date'] = dates

    filename = 'auto_info.txt'
    LoadTxt.load_txt(paralist, filename)

    robot = Auto(paralist)
    robot.FieldBook()
    if int(paralist['how_long']) == 2:
        paralist['start_time'] += 1
        robot2 = Auto(paralist)
        robot2.FieldBook()
