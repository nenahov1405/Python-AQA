from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='result.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def file_reader(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        lst = data.split('\n')
        return lst

def file_filter(lst):
    clear_data = []
    for line in lst:
        index = line.find("TSTFEED0300|7E3E|0400")
        if index != -1:
            clear_data.append(line)
    return clear_data

def time_converter(filtered_lst):
    dtime_list = []
    for line in filtered_lst:
        time_part_with_key = line.split('Timestamp ')[1]
        time_part = time_part_with_key.split(' Key')[0].strip()
        time_obj = datetime.strptime(time_part, '%H:%M:%S')
        dtime_list.append(time_obj)
    return dtime_list


def logger_writter(dt_lst):
    for i in range(1, len(dt_lst)):
        current_time = dt_lst[i]
        previous_time = dt_lst[i - 1]
        diff = previous_time - current_time
        diff_seconds = diff.total_seconds()

        time_format = '%H:%M:%S'
        formatted_previous = previous_time.strftime(time_format)
        formatted_current = current_time.strftime(time_format)

        log_message = f'Зафіксовано різницю в {diff_seconds:.1f} ceкунд ({formatted_previous} - {formatted_current})'

        if 31 < diff_seconds < 33:
            logging.warning(log_message)
        elif diff_seconds >= 33:
            logging.error(log_message)


lst = file_reader('hblog.txt')
filtered_lst = file_filter(lst)
dt_objects = time_converter(filtered_lst)
logger_writter(dt_objects)
