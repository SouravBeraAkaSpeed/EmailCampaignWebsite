import os
from django.shortcuts import render

from Data.main import main
from .handle_files import *
from .forms import UploadFileForm
import pandas as pd
from django.http import JsonResponse
from .Instance import instance
from asgiref.sync import async_to_sync,sync_to_async
from channels.layers import get_channel_layer

from .thread import EmailThread
import threading
# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        return dashboard(request)
    else:
        context={
            "isredirected":True
        }
        return render(request, 'E_campaign/base.html',context)


def setting(request,pk=None):

    if request.user.is_authenticated:


        if pk==1:
            delete_previous_data()
    

        if request.method =='POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                if "smtp" in request.FILES.keys() and  "data" in request.FILES.keys() and "content" in  request.FILES.keys() and "attachments" in request.FILES.keys() and "subjects" in request.FILES.keys():
                    delete_previous_data()
                    
                if "smtp" in request.FILES.keys():

                    handle_smtp_file(request.FILES['smtp'])
                if "data" in request.FILES.keys():
                    handle_data_file(request.FILES['data'])
                
                if "content" in  request.FILES.keys():
                   handle_content_file(request.FILES['content'])
                if "attachments" in request.FILES.keys():
                    handle_attachments_file(request.FILES['attachments'])
                if "subjects" in request.FILES.keys():
                    handle_subjects_file(request.FILES['subjects'])
                
                proxies=request.POST.get('proxies')
                phone=request.POST.get('phone')
                instance=request.POST.get('instance')
                time_delay=request.POST.get('time_delay')
                handle_instance_file(instance)
                handle_proxy_input(proxies)
                handle_instance_input(instance)
                handle_delay_input(time_delay)
                handle_phone_input(phone)

                # Data_listener()
            
            
                
        else:
            form = UploadFileForm()

        
        context={
            'form':form,
        }
        return render(request, 'E_campaign/settings.html',context)

    else:
        context={
            "isredirected":True
        }
        return render(request, 'E_campaign/base.html',context)

def dashboard(request,pk=None):

    
    
    if request.user.is_authenticated:
        layer = get_channel_layer()
        isDataUploaded=False
        try:
            try:
                df=pd.read_csv('Data/smtps.csv')
                no_of_smtp=df.shape[0]
                print(no_of_smtp)
            except Exception as e:
                no_of_smtp=0
            try:
                df=pd.read_excel('Data/Data.xlsx')
                contacts=df.shape[0]
            except Exception as e:
                contacts=0
            try:
            
                contents=len(os.listdir("Data/content/"))
            except Exception as e:
                contents=0
            with open('Data/instance.txt','r') as f:
                no_of_instance=str(f.read())
            try:
                df=pd.read_csv('Data/phone_no.csv')
                no_of_phone_numbers=df.shape[0]
            except Exception as e:
                no_of_phone_numbers=0
            try:
                df=pd.read_csv('Data/subjects.csv')
                no_of_subjects=df.shape[0]
            except Exception as e:
                no_of_subjects=0
            with open('Data/Proxy_list.txt','r') as f:
                r=f.read()
                if r=="":
                    no_of_proxy=0
                else:
                    no_of_proxy=str(len(r.split("\n")))
                print(no_of_proxy)
            isDataUploaded=True
        except Exception as e:
            
            no_of_smtp=0
            contacts=0
            contents=0
            no_of_instance=0
            no_of_phone_numbers=0
            no_of_subjects=0
            no_of_proxy=0
        
        with open("./isrunning.txt","r") as f:
            r=f.read()
            if int(r) == 1:
                event={
                        'type':'send_message',
                        'message':f"STOP",
                        'isStarted':True
                    }
                async_to_sync(layer.group_send)(
                            'notification', event)

        if pk==1:
            
            # Loading....
            if isDataUploaded:
                
                data = {
                    'no_of_smtp': no_of_smtp,
                    'contacts': contacts,
                    'contents':contents,
                    'no_of_instance':no_of_instance,
                    'no_of_phone_numbers':no_of_phone_numbers,
                    'no_of_subjects':no_of_subjects,
                    'no_of_proxy':no_of_proxy
                    }
            else:
                data={
                    'isDataNotUploaded':True
                }
            return JsonResponse(data)  
        if pk==2:
            # start campaign...
            
            with open('Data/time_delay.txt','r') as f:
                    no_of_delay=str(f.read())

            with open('Data/instance.txt','r') as f:
                    no_of_instance=str(f.read())
            event={
                        'type':'send_message',
                        'message':f"Starting Campaign...",
                        'isStarting':True
                    }
            async_to_sync(layer.group_send)(
                        'notification', event)
            instance(no_of_delay,no_of_instance )

            event={
                        'type':'send_message',
                        'message':f"STOP",
                        'isStarted':True
                    }
            async_to_sync(layer.group_send)(
                        'notification', event)
            # t1 = threading.Thread(target=main, args=(no_of_delay,))
            # t1.start()
            # EmailThread(no_of_delay).start()
            # main(no_of_delay)
            
        
        if pk==3:
            # Stop campaign

            
            with open(f'./isrunning.txt','w') as f:
                    f.write(str(0))
            event={
                        'type':'send_message',
                        'message':f"Stoping...(Closing the campaign)"
                    }
            async_to_sync(layer.group_send)(
                        'notification', event)
        
        if pk==4:

            with open("./isPause.txt","w") as f:
                f.write(str(1))
            event={
                        'type':'send_message',
                        'message':f"PLAY",
                        'isPaused':True
                    }
            async_to_sync(layer.group_send)(
                        'notification', event)

        if pk==5:

            with open("./isPause.txt","w") as f:
                f.write(str(0))
            event={
                        'type':'send_message',
                        'message':f"PAUSE",
                        'isPaused':True
                    }
            async_to_sync(layer.group_send)(
                        'notification', event)

        if pk==6:
            with open("./logs.txt","r") as f:
                logs=str(f.read())
            event={
                'type':'send_message',
                'message':f"{logs}",
                'isLog':True
            }
            async_to_sync(layer.group_send)(
                            'notification', event)
            data={
                'no_of_smtp':no_of_smtp,
                'contacts':contacts,
                'contents':contents,
                'no_of_instance':no_of_instance,
                'no_of_phone_numbers':no_of_phone_numbers,
                'no_of_subjects':no_of_subjects,
                'no_of_proxy':no_of_proxy
            }
            return JsonResponse(data) 
            
        context={
            'no_of_smtp':no_of_smtp,
            'contacts':contacts,
            'contents':contents,
            'no_of_instance':no_of_instance,
            'no_of_phone_numbers':no_of_phone_numbers,
            'no_of_subjects':no_of_subjects,
            'no_of_proxy':no_of_proxy
        }
        return render(request, 'E_campaign/dashboard.html',context)
    else:
        context={
            "isredirected":True
        }
        return render(request, 'E_campaign/base.html',context)
