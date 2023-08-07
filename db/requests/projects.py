from db.engine import session
from db.models.projects import Project


class ProjectRequests:

    # GET PROJECT DATA

    def get_all_projects(self):
        projects = session.query(
            Project
        ).order_by(
            Project.id
        ).all()
        return projects

    def get_projects_by_project_title(self, title):
        projects = session.query(
            Project
        ).filter(
            Project.title == title
        ).order_by(
            Project.id
        ).all()
        return projects

    def get_projects_by_project_status(self, status):
        projects = session.query(
            Project
        ).filter(
            Project.status == status
        ).order_by(
            Project.id
        ).all()
        return projects

    def get_projects_by_project_owner(self, owner):
        projects = session.query(
            Project
        ).filter(
            Project.owner == owner
        ).order_by(
            Project.id
        ).all()
        return projects

    # ADD PROJECT

    def add_project(self, title, description, status, owner):
        projects = Project(
            title=title,
            description=description,
            status=status,
            owner=owner
        )
        session.add(projects)
        session.commit()

    # DELETE PROJECT

    def del_project_by_id(self, project_id):
        projects = session.query(
            Project
        ).filter(
            Project.id == project_id
        ).first()
        session.delete(projects)
        session.commit()

    def del_project_by_title(self, title):
        projects = session.query(
            Project
        ).filter(
            Project.title == title
        ).first()
        session.delete(projects)
        session.commit()

    # UPDATE PROJECT

    def change_project_title(self, title, new_title):
        projects = session.query(
            Project
        ).filter(
            Project.title == title
        ).first()
        projects.title = new_title
        session.commit()

    def change_project_title_by_id(self, project_id, new_title):
        projects = session.query(
            Project
        ).filter(
            Project.id == project_id
        ).first()
        projects.title = new_title
        session.commit()

    def change_project_description_by_id(self, project_id, new_description):
        projects = session.query(
            Project
        ).filter(
            Project.id == project_id
        ).first()
        projects.description = new_description
        session.commit()

    def change_project_owner_by_id(self, project_id, new_owner_id):
        projects = session.query(
            Project
        ).filter(
            Project.id == project_id
        ).first()
        projects.owner = new_owner_id
        session.commit()

    def change_project_status_by_id(self, project_id, new_status):
        projects = session.query(
            Project
        ).filter(
            Project.project_id == project_id
        ).first()
        projects.status = new_status
        session.commit()


# project_request = ProjectRequests()

# project_request.add_project('Project1', 'This is description of  the project', 'Active', '16')
# print(project_request.get_all_projects())
# print(project_request.get_all_projects())
# print(project_request.get_projects_by_project_title('Projectq'))
# print(project_request.get_projects_by_project_status('Active'))
# print(project_request.get_projects_by_project_owner(16))
# project_request.del_project_by_id(3)
# project_request.del_project_by_title('Projectq')
# project_request.change_project_title('Projectq', 'Changed Title')
# project_request.change_project_title_by_id(4, 'New Project Title')
# project_request.change_project_description_by_id(5, 'Changed Description')
# project_request.change_project_owner_by_id(6, 17)
# project_request.change_project_status_by_id(7, 'Closed')

