url = 'http://172.16.50.41:8001'
db = 'myproject'
username = 'zawnainglinninfo9@gmail.com'
password = 'winningway'



import xmlrpc.client

common= xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# url, db, username, password = \
#     common['host'], common['database'], common['user'], common['password']
print(common)
version=common.version()
print('Version of Odoo',version)

uid=common.authenticate(db,username,password,{})
print(uid)


models=xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
Project=models.execute_kw(db,uid,password, 'project.project','search',[[]])
print('Our Project',Project)
projecttask=models.execute_kw(db,uid,password, 'project.task','search',[[]])
print('Our Project task',projecttask)

project_task_count=models.execute_kw(db,uid,password,'res.partner','search_count',[[]])
print(project_task_count)
project_task_rec=models.execute_kw(db,uid,password,'project.task','read',[projecttask],{'fields':['id','name','user_id']},)
print(project_task_rec)




