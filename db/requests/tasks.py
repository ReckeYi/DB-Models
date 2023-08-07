from db.engine import session
from db.models.tasks import Task


class TaskRequests:

    # GET TASK DATA

    def get_all_tasks(self):
        tasks = session.query(
            Task
        ).order_by(
            Task.id
        ).all()
        return tasks

    def get_tasks_by_task_title(self, title):
        tasks = session.query(
            Task
        ).filter(
            Task.title == title
        ).order_by(
            Task.id
        ).all()
        return tasks

    def get_task_by_task_assignee(self, assignee):
        tasks = session.query(
            Task
        ).filter(
            Task.assignee == assignee
        ).order_by(
            Task.id
        ).all()
        return tasks

    def get_task_by_task_status(self, status):
        tasks = session.query(
            Task
        ).filter(
            Task.status == status
        ).all()
        return tasks

    # ADD TASK

    def add_task(self, title, description, assignee, deadline, status):
        tasks = Task(
            title=title,
            description=description,
            assignee=assignee,
            deadline=deadline,
            status=status
        )
        session.add(tasks)
        session.commit()

    # DELETE TASK

    def del_task_by_id(self, task_id):
        tasks = session.query(
            Task
        ).filter(
            Task.id == task_id
        ).first()
        session.delete(tasks)
        session.commit()

    def del_task_by_title(self, title):
        tasks = session.query(
            Task
        ).filter(
            Task.title == title
        ).first()
        session.delete(tasks)
        session.commit()

    # UPDATE TASK

    def change_task_title(self, title, new_title):
        tasks = session.query(
            Task
        ).filter(
            Task.title == title
        ).first()
        tasks.title = new_title
        session.commit()

    def change_task_title_by_id(self, task_id, new_title):
        tasks = session.query(
            Task
        ).filter(
            Task.id == task_id
        ).first()
        tasks.title = new_title
        session.commit()

    def change_task_description_by_id(self, task_id, new_description):
        tasks = session.query(
            Task
        ).filter(
            Task.id == task_id
        ).first()
        tasks.description = new_description
        session.commit()

    def change_task_assignee_by_id(self, task_id, new_assignee):
        tasks = session.query(
            Task
        ).filter(
            Task.id == task_id
        ).first()
        tasks.assignee = new_assignee
        session.commit()

    def change_task_status_by_id(self, task_id, new_status):
        tasks = session.query(
            Task
        ).filter(
            Task.id == task_id
        ).first()
        tasks.status = new_status
        session.commit()


# task_request = TaskRequests()
# task_request.add_task('Task6', 'The first Task', '16', '2023-08-26 15:33', 'Active')
# task_request.get_all_tasks()
# print(task_request.get_all_tasks())
# task_request.get_task_by_task_assignee(16)
# task_request.get_task_by_task_status('Active')
# task_request.get_tasks_by_task_title('Task6')
# task_request.del_task_by_title('Task45')
# print(task_request.get_task_by_task_assignee(16))
# print(task_request.get_task_by_task_status('Active'))
# print(task_request.get_tasks_by_task_title('Task6'))
# task_request.change_task_status_by_id('12', 'Closed')
# task_request.change_task_assignee_by_id('1', '17')
# task_request.change_task_title('Task2', 'Renamed task')
# task_request.change_task_description_by_id('13', 'This task has id "13"')
# task_request.change_task_title_by_id('8', 'Task')
