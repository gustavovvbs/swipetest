#!/usr/bin/env python

import csv
from collections import defaultdict
import os

def log_treater(folder):
    '''wals by the first 20 logs and extracts the data of the words and the events. If there is a file for that word, it adds the events in that file, if not, it creates a new file to store all the events of that word.'''
    logs = os.listdir(folder)
    for log in logs[:20]:
        if log.endswith('.log'):
            rows = defaultdict(list)
            with open(folder + log) as csvfile:
                reader = csv.reader(csvfile, delimiter=' ')
                for row in reader:
                    if len(row) < 12 or row[11] not in ['0','1']:
                        continue
                    entry = {
                        'sentenceHash': row[0],
                        'timestamp': int(row[1]),
                        'canvasWidth': int(row[2]),
                        'canvasHeight': int(row[3]),
                        'event': row[4],
                        'x': int(row[5]),
                        'y': int(row[6]),
                        'word': row[10],
                        'isFailedWord': row[11] == '1',
                    }
                    #checks if there is a file for that word, if not, creates a new file
                    if os.path.exists('logs_per_word/' + entry['word'] + '.log'):
                        with open('logs_per_word/' + entry['word'] + '.log', 'a') as file:
                            file.write(str(entry) + '\n')
                    else:
                        with open('logs_per_word/' + entry['word'] + '.log', 'w') as file:
                            file.write(str(entry) + '\n')
    return entry['word']
    


if __name__ == '__main__':
    log_treater('logs/')