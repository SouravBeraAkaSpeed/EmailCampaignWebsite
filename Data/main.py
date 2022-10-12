
import time
import os
import socket
import glob,socks
import pandas as pd
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
from email.header import Header
from email.utils import formatdate, make_msgid
import random,string
import smtplib
from asgiref.sync import async_to_sync
from .Html_to_Pdf_convertor import Convert
from channels.layers import get_channel_layer
import traceback
from datetime import date

now = time.time()
def leftRotate(arr, d):
    for i in range(d):
        leftRotatebyOne(arr, len(arr))

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
        arr[n-1] = temp

def main(delay_per_email,folder):


    with open(f'./isrunning.txt','w') as f:
        f.write(str(1))

    layer = get_channel_layer()

    # notification=NotificationConsumer()
    # # notification.send_message(event)
    # notification.
    # notification.send(text_data=event['message'])

    # os.chdir('Manish_project')



    with open(f'{folder}/Body_template.html', 'r') as f:
        msg_body = f.read()


    # print("\n <----- Please keep this in mind this software will work only when your less secure apps setting" +
    #       "is enabled,\n if it is not enabled you can enable it here: https://myaccount.google.com/lesssecureapps ----->")


    # os.chdir(f'{folder}/attachments')
    attachments = glob.glob(f"{folder}/attachments/*.pdf")
    images_png = glob.glob(f"{folder}/attachments/*.png")
    images_jpg = glob.glob(f'{folder}/attachments/*.jpg')

    # os.chdir("../")
    # os.chdir('Data/content')

    contents = glob.glob(f'{folder}/content/*.html')

    bodys = []

    for body in contents:
        with open(body, 'r') as f:
            content_body = f.read()
            bodys.append({
                "body": content_body,
                "name": body.split(".")[0],
            })


    # os.chdir('../')


    csvs= glob.glob(f'{folder}/*.csv')
    csv_files=[]
    for csv in csvs:
        csv_files.append(csv.replace(f"{folder}","").replace("\\",""))



    for file in csv_files:
        globals()[f"{file.split('.')[0].replace('/','')}"]=[]

        df=pd.read_csv(f"{folder}/{file}")
        for index, column in df.iterrows():
            cols= df.columns
            mydict = {f'{col}':column[col] for col in cols}
            globals()[f"{file.split('.')[0].replace('/','')}"].append(mydict)




    UseHtmlConvertor='n'
    if UseHtmlConvertor == 'y':

        Output_pdf_name = input(
            "Enter the name of the file that will be coverted into pdf: ")

    i=0
    s=[]
    for contact in contacts:

        while True:
            with open("./isPause.txt", "r") as f:
                if int(f.read()) == 0:
                    break
                else:
                    print("paused")
                    continue

        with open(f'./isrunning.txt','r') as f:
            r=f.read()
            if int(r) == 0:
                isrunning=False
            else:
                isrunning=True

        if not isrunning:

            break

        contact=contact['contacts']
        smtp_index=0




        limit_reached = False
        for smtp in smtps:
            if smtp['No_of_send'] >= smtp['Limit']:
                limit_reached = True
            else:
                limit_reached = False
                break

        if limit_reached == True:
            print("Limit of Email Sending is Reached.")


        try:
            
            s=[]
            while True:
                if len(s)==len(smtps):
                    s=[]
                print("stuck")
                smtp = random.choice(smtps)
                if smtp['Email'] in s:
                    continue
                else:
                    break
            s.append(smtp['Email'])


            msg = MIMEMultipart()




            Email = smtp['Email']
            PassWord = smtp['Password']
            SMTP = smtp['SMTP']
            PORT = smtp['PORT']
            name=smtp['From']
            num = smtp['No_of_send']
            smtp['No_of_send'] = num+1
            subject = subjects[0]
            Subject = Header(subject['subjects'])
            body = bodys[0]
            Body = body['body']
            Body_name = body['name'].split("\\")[1]
            msg.set_charset('utf-8')
            msg['Date'] = formatdate(localtime=True)
            msg['Message-ID'] = make_msgid()
            msg['Subject'] = Subject
            msg['From'] = str(Header(f' {name}<{Email}>'))
            msg['To'] = contact
            # msg['Cc'] = Email
            # msg['Bcc'] = Email
            msg['In-Reply-To'] = contact
            # msg['References'] = contact

            randomnumber=random.randint(100000000000,999999999999)
            alphanumeric=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(12))
            code=random.randint(1000,9999)
            date1=date.today().strftime(" %d %B %Y")
            date2=date.today().strftime(" %A %d %B %Y")
            html = msg_body.replace("[body]", Body)

            for file in csv_files:

                if  "smtps" not in file:
                    html = html.replace(f"[{file.split('.')[0].replace('/','')}]", str(globals()[f"{file.split('.')[0].replace('/','')}"][0][f"{file.split('.')[0].replace('/','')}"]))

            html=html.replace("[randomnumber]",str(randomnumber))
            html=html.replace("[alphanumeric]",str(alphanumeric))
            html=html.replace("[code]",str(code))
            html=html.replace("[date1]",str(date1))
            html=html.replace("[date2]",str(date2))
            part = MIMEText(html, 'html')
            msg.attach(part)
            event={
                    'type':'send_message',
                    'message':f"Processing Data..."
                }
            async_to_sync(layer.group_send)(
                    'notification', event)
    #

            for file in attachments:
                
                if Body_name == file.split("\\")[1].split('.')[0]:
                    with open(f"{file}", 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                    attach = MIMEBase(
                        'application', 'octate-stream', Name=file_name)
                    attach.set_payload(file_data)
                    encoders.encode_base64(attach)
                    attach.add_header('Content-Decomposition',
                                      'attachment', filename=file.split("\\")[1])
                    msg.attach(attach)

            for image in images_jpg:
                if Body_name == image.split("\\")[1].split('.')[0]:
                    
                    with open(f"{image}", 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                    msgImage = MIMEImage(file_data, _subtype="jpg")
                    msgImage.add_header('Content-ID', f'<{image}>')
                    msgImage.add_header('Content-Disposition',
                                        'attachment', filename=file_name)
                    msg.attach(msgImage)

            for image in images_png:
                if Body_name == image.split("\\")[1].split('.')[0]:
                    with open(f"{image}", 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                    msgImage = MIMEImage(file_data, _subtype="png")
                    msgImage.add_header('Content-ID', f'<{image}>')
                    msgImage.add_header('Content-Disposition',
                                        'attachment', filename=file_name)
                    msg.attach(msgImage)



            if UseHtmlConvertor == 'y':

                print("Creating Pdf...")
                try:
                    with open(f'{folder}/test.html', 'w') as f:
                        f.write(html)

                    Convert('test.html', f'{Output_pdf_name}.pdf')
                    os.remove('test.html')

                    with open(f'Data/{Output_pdf_name}.pdf', 'rb') as f:
                        file_data = f.read()
                        file_name = f.name
                    attach = MIMEBase(
                        'application', 'octate-stream', Name=f'{Output_pdf_name}.pdf')
                    attach.set_payload(file_data)
                    encoders.encode_base64(attach)
                    attach.add_header('Content-ID', '<pdf>')
                    attach.add_header('Content-Disposition',
                                      'attachment', filename=str(f'{Output_pdf_name}.pdf'))
                    print("created!")
                    msg.attach(attach)
                    print("Pdf attached!")
                    os.remove(f'{Output_pdf_name}.pdf')

                except Exception as e:
                    print("Error while converting, error:"+str(traceback.format_exc()))
                    event={
                            'type':'send_message',
                            'message':f"Error while converting, error: {str(traceback.format_exc())}"
                        }

            flag = 0
            print("Sending...")
            event={
                    'type':'send_message',
                    'message':f"Sending..."
                }
            async_to_sync(layer.group_send)(
                    'notification', event)
            with open(f'./isrunning.txt','r') as f:
                r=f.read()
                print(r)
                if int(r) == 0:
                    isrunning=False
                else:
                    isrunning=True

            if not isrunning:

                break
            if("outlook.com" in Email.split("@") or "icloud.com" in Email.split("@")):

                try:
                    with smtplib.SMTP(SMTP, PORT) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(Email, PassWord)
                        smtp.sendmail(Email, contact, msg.as_string())
                        smtp.quit()
                        time.sleep(int(delay_per_email))
                        with open(f"./logs.txt", 'a') as f:
                            f.write('<br/> \n EMAIL SENDED TO ' +
                                    contact)
                            print('\n EMAIL SENDED TO '+contact)
                            i+=1
                            event={
                                'type':'send_message',
                                'message':f"EMAIL SENDED TO {contact}.(Total Email sent {i})",
                                'isLog':True
                            }
                except Exception as e:
                    print(e)
                    flag = 1
                    with open(f"./logs.txt", 'a') as f:
                        f.write('<br/> \n You have problem in '+Email)
                        print('\n You have problem in '+Email)
                        event={
                                'type':'send_message',
                                'message':f"You have problem in  {Email} , error: {str(e)}",
                                'isLog':True
                            }
                async_to_sync(layer.group_send)(
                    'notification', event)
            else:

                try:
                    # s = socks.socksocket()
                    # s.set_proxy(socks.SOCKS5, "geo.iproyal.com", [
                    #             22325, [True, ['prht2017', ['proxy2022']]]])
                    # socks.set_default_proxy(
                    #     socks.PROXY_TYPE_HTTP, "133.18.172.217", 8080)
                    # # socket.socket = socks.socksocket
                    # # print(requests.get('http://httpbin.org/ip').text)
                    # socks.set_default_proxy(socks.SOCKS5, addr='geo.iproyal.com',
                    #                         port=8080, rdns=True, username='prht2017', password='proxy2022')
                    # socket.socket = socks.socksocket
                    # sock = socket.socket()

                    # socks.wrapmodule(smtplib)
                    # ,proxy_addr="proxy.packetstream.io",proxy_port=3111,proxy_rdns=True,proxy_username="kuchbhientertainment",proxy_password="bhkXQOTQgJmyygXW"
                    # print(1)
                    # smtplib.SMTP._get_socket = socket.create_connection((SMTP,PORT))

                    with smtplib.SMTP(SMTP, PORT) as smtp:
                        # smtp.set_debuglevel(1)

                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(Email, PassWord)
                        smtp.sendmail(Email, contact, msg.as_string())
                        # smtp.send_message(msg)
                        smtp.quit()
                        time.sleep(int(delay_per_email))
                        with open(f"./logs.txt", 'a') as f:
                            f.write('<br/> \n EMAIL SENDED TO '+contact)
                            print('\n EMAIL SENDED TO '+contact)
                            i+=1
                            event={
                                'type':'send_message',
                                'message':f"EMAIL SENDED TO {contact} .(Total Email sent {i})",
                                'isLog':True
                            }
                except Exception as e:
                    print(e)
                    flag = 1
                    with open(f"{folder}/Effected_Smtps.txt", "a") as f:
                        f.write(str(Email)+"\n")
                    with open(f"./logs.txt", 'a') as f:
                        f.write('<br/> \n You have problem in '+Email)
                        print('\n You have problem in '+Email)
                        event={
                                'type':'send_message',
                                'message':f"You have problem in {Email} , error: {str(e)}",
                                'isLog':True
                            }
                async_to_sync(layer.group_send)(
                    'notification', event)


            async_to_sync(layer.group_send)(
                    'notification', event)
            df_smtp=pd.read_csv(f'{folder}/smtps.csv')
            time.sleep(5)
            print(3)
            if flag == 0:
                print(4)
                df_smtp.at[smtp_index, 'No_of_send'] = num+1
                df_smtp.loc[smtp_index, 'No_of_send'].round().astype(int)
                df_smtp.loc[smtp_index, 'Limit'].round().astype(int)
                df_smtp.loc[smtp_index, 'PORT'].round().astype(int)
                print(df_smtp)
                df_smtp.to_csv(f'{folder}/smtps.csv', index=False)

        except Exception:
            print("error:"+str(traceback.format_exc()))
            event={
                    'type':'send_message',
                    'message':f"error: {str(traceback.format_exc())}"
                }
            async_to_sync(layer.group_send)(
                    'notification', event)


        leftRotate(phone_no, 1)
        leftRotate(subjects, 1)
        leftRotate(bodys, 1)
        for file in csv_files:

                if  "smtps" not in file and "contacts" not in file:
                    leftRotate(globals()[f"{file.split('.')[0].replace('/','')}"], 1)



        if smtp_index == len(smtps)-1:
            smtp_index = 0
        else:
            smtp_index += 1




    print('\n ALL EMAILS ARE SENDED! ')
    with open(f'./isrunning.txt','w') as f:
        f.write(str(0))
    event={
            'type':'send_message',
            'message':f"ALL EMAILS ARE SENDED!"
        }
    async_to_sync(layer.group_send)(
                    'notification', event)
