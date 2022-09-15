import pandas as pd


no_of_instance=1
def handle_smtp_file(f):
    with open('Data/smtps.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
def handle_content_file(f):
    
    
    with open(f'Data/content/{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_instance_file(f):
    with open('Data/instance.txt', 'w') as destination:
        destination.write(str(f))

def handle_attachments_file(f):
    
    
    with open(f'Data/attachments/{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_subjects_file(f):
    
    
    with open(f'Data/{f}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_data_file(f):
    with open('Data/Data.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    df=pd.read_excel('Data/Data.xlsx')
    for col in df.columns:
        with open(f'Data/{col}.csv',"w") as ff:
            ff.write(col+str('\n'))

        for index, column in df.iterrows():
            with open(f'Data/{col}.csv',"a") as ff:
                ff.write(str(column[col])+"\n")



def handle_proxy_input(f):
    with open('Data/Proxy_list.txt', 'w') as destination:
        destination.write(str(f))
    

def handle_phone_input(p):
    with open("Data/phone_no.csv","w") as f:
        f.write(str('phone_no')+"\n")
    df=pd.read_csv('Data/phone_no.csv')
    df.at[0,'phone_no']=p
    df.to_csv('Data/phone_no.csv',index=False)
        

def handle_instance_input(p):
    global no_of_instance
    no_of_instance=int(p)

def handle_delay_input(f):
    with open('Data/time_delay.txt', 'w') as destination:
        destination.write(f)