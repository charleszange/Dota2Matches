from datetime import datetime
event_log_file_name = 'event_log.txt'
def log(input_source_process = 'No process specified', input_log_message = 'No message specified'):
    with open (event_log_file_name, 'a') as event_log_file:
        log_message = datetime.now().strftime('%Y:%m:%d::%H:%M:%S:%f') + \
            '|' + input_source_process + '|' + input_log_message + '\n'
        event_log_file.write(log_message)