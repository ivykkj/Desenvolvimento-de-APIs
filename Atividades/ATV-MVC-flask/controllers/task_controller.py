from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == "POST":
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']

            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()
            
            return redirect(url_for("list_tasks"))
        
        users = User.query.all() 
        return render_template("create_task.html", users=users)
    
    @staticmethod
    def update_task_status(task_id):
        task_to_update = Task.query.get(task_id)
        if task_to_update:
            if task_to_update.status == 'Pendente':
                task_to_update.status = 'Concluído'
            elif task_to_update.status == 'Concluído':
                task_to_update.status = 'Pendente'
            db.session.commit()
        pass
        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        task_to_delete = Task.query.get(task_id)
        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
        pass
        return redirect(url_for("list_tasks"))