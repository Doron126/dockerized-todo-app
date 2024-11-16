## **dockerized-todo-app**
# **Overview**
A Python-based to-do list application that allows users to add, view, and manage tasks using a MySQL database for persistent storage. The application has been deployed using Docker Hub on two separate application servers, both connected to a shared MySQL database.

# **Technologies**
* Docker
* Python
* MySQL

# **Instructions**
1. Set up 3 Ubuntu machines.
   
2. Set up MySQL on one of the machines.
   Create the database:
   "CREATE DATABASE tasks_db;
   CREATE USER 'todo_user'@'%' IDENTIFIED BY 'todo_password';
   GRANT ALL PRIVILEGES ON tasks_db.* TO 'todo_user'@'%';
   FLUSH PRIVILEGES;
   and then create and configure the table:
   USE tasks_db;
   CREATE TABLE tasks (
   id INT AUTO_INCREMENT PRIMARY KEY,
   title VARCHAR(255) NOT NULL,
   completed BOOLEAN DEFAULT FALSE
   );"
   then edit the configuration file to allow remote connection:
   on /etc/mysql/mysql.conf.d/mysqld.cnf change the bind-address from 127.0.0.1 to 0.0.0.0
   then restart the mysql service.

3. On the machine where you want to store the script, create a directory and pull the attached files.

4. install Docker on both machines.

5. login to dockerub on both machines.
   push the container to your dockerhub user:
   sudo docker tag todo-app your-user/todo-app:latest
   "sudo docker push your-user/todo-app:latest"
   then pull it on the other machine:
   "sudo docker pull your-user/todo-container:latest"

6. Run the app on the machines:
   "sudo docker build -t your-dockerhub-username/python-todo-app ."
   "sudo docker run -it --name python-todo-app -e DATABASE_HOST=your-ip -e DATABASE_USER=todo_user -e 
    DATABASE_PASSWORD=password -e DATABASE_NAME=tasks_db your-user/python-todo-app"
