def mv_task(from_list, to_list):
    to_list.append(from_list.pop())

def rm_task(task, list):
    list.remove(task)

def print_priority_task(list):
    print(list[-1])


new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

mv_task(new_tasks, completed_tasks)
rm_task('task_007', new_tasks)
print_priority_task(new_tasks)