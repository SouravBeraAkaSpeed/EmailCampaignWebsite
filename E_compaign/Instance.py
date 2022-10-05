import importlib
import os
from distutils.dir_util import copy_tree
import pandas as pd
import errno, os, stat, shutil
import asyncio
from .run_thread import open_py_file
from asgiref.sync import async_to_sync
from Data.main import main
import threading
# async def sleep():
#     print(f'Time: {time.time() - start:.2f}')
#     await asyncio.sleep(1)

# async def sum(name, numbers):
#     total = 0
#     for number in numbers:
#         print(f'Task {name}: Computing {total}+{number}')
#         await sleep()
#         total += number
#     print(f'Task {name}: Sum = {total}\n')

# start = time.time()

# loop = asyncio.get_event_loop()
# tasks = [
#     loop.create_task(sum("A", [1, 2])),
#     loop.create_task(sum("B", [1, 2, 3])),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# end = time.time()
# print(f'Time: {end-start:.2f} sec')


folder_num=1

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise
def Execute_instances(folder,directory_path,number_of_smtp,number_of_send):
        global folder_num
        
        
        df= pd.read_csv(f'{folder}/contacts.csv')
        
        rows=df.shape[0]
        
        rows_per_file=rows/number_of_smtp
        


        contacts=[]
        
        for index, col in df.iterrows():
            
            if rows_per_file*(folder_num-1)<=index<rows_per_file*folder_num:
                    
                    contacts.append(col['contacts'])
                    

        df2=pd.DataFrame({'contacts':contacts}) 
        df2.to_csv(f'{folder}/contacts.csv',index=False) 
        # shutil.move(f'{folder}/contacts.csv', f'Data/contacts.csv')
        # with open(f"{folder}/contact.txt", 'r') as fp:
        #     x = len(fp.readlines())

        
        # content=''
        # with open(f'{folder}/contact.txt','r') as f:
        #     i=0
        #     for lines in f.readlines():
                
        #         if (x/number_of_smtp)*(folder_num-1)<=i<(x/number_of_smtp)*folder_num:
        #             content+=lines

        #         i=i+1    
        
        # with open(f'{folder}/contact.txt','w') as f:
        #     f.write(content)

        
        df= pd.read_csv(f'{folder}/smtps.csv')
        
        rows=df.shape[0]
        
        rows_per_file=rows/number_of_smtp
        


        Email=[]
        Password=[]
        SMTP=[]
        PORT=[]
        Limit=[]
        No_of_send=[]

        for index, col in df.iterrows():
            
            if rows_per_file*(folder_num-1)<=index<rows_per_file*folder_num:
                    
                    Email.append(col['Email'])
                    Password.append(col['Password'])
                    SMTP.append(col['SMTP'])
                    PORT.append(col['PORT'])
                    Limit.append(col['Limit'])
                    No_of_send.append(col['No_of_send'])

        df2=pd.DataFrame({'Email':Email,'Password':Password,'SMTP':SMTP,'PORT':PORT,'Limit':Limit,'No_of_send':No_of_send}) 
        df2.to_csv(f'{folder}/smtps.csv',index=False)        
        
        # shutil.move(f'{folder}/smtps.csv', f'Data/smtps.csv')
        
        folder_num=folder_num+1  
        # main(number_of_send)
        
        # args=['python','-c',f"import {folder}.main; "]
        # # args=['python','-c',f"import {folder}.main; main({number_of_send})"] 
        # print(3)
        # # {folder}.main.main(number_of_send)
        # open_py_file(args) 
        # moduleNames = [f'{folder}.main'] 
        my_module = importlib.import_module(f'{folder}.main')
        my_module.main(number_of_send,folder)
        # os.system(f' python -c "import {folder}.main;  main({number_of_send})"')

# os.system('python main.py')
# copy_tree("Manish_project", "test_project")
def instance(number_of_send,number_of_instance):

    global folder_num

    folders=[]
    for f in os.listdir():
        if "instance"  in f:
            folders.append(f)

    for folder in folders:
        shutil.rmtree(folder, ignore_errors=False, onerror=handleRemoveReadonly)


    number_of_smtp=int(number_of_instance)
    for i in range(number_of_smtp):
        shutil.copy("Data", "instance"+str(i+1))

        

    folders=[]
    for f in os.listdir():
        if "instance"  in f:
            folders.append(f)

    directory_path = os.getcwd()
    


    
        

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # # executor = concurrent.futures.ThreadPoolExecutor(5)
    # # loop.set_default_executor(executor)
    # tasks = []

    for folder in folders:
        t1 = threading.Thread(target=Execute_instances, args=(folder,directory_path,number_of_smtp,number_of_send))
        t1.start()
        
        # Execute_instances()

    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

        


    # def change_configuration():
    #     pass




    # for i in range(number_of_smtp):
    #     globals()["p"+str(i)]=multiprocessing.Process(target=run,args=[folders[i]])
        

    # if __name__ =='__main__':
    #     for i in range(number_of_smtp):
    #         globals()["p"+str(i)].start()
            
        
        



    