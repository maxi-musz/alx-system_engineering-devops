#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            EMPLOYEE_NAME = emp_req.get('name')
            TOTAL_NUMBER_OF_TASKS = list(filter(lambda x: x.get('userId') == id, task_req))
            NUMBER_OF_DONE_TASKS = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    EMPLOYEE_NAME,
                    len(NUMBER_OF_DONE_TASKS),
                    len(TOTAL_NUMBER_OF_TASKS)
                )
            )
            if len(NUMBER_OF_DONE_TASKS) > 0:
                for TOTAL_NUMBER_OF_TASKS in NUMBER_OF_DONE_TASKS:
                    print('\t {}'.format(TOTAL_NUMBER_OF_TASKS.get('title')))
