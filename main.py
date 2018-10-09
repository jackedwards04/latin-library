import qrcode
from PIL import Image
def retdb (name):
  with open("holder.txt","r+") as f:
    s = f.read()
    lyst = s.split(',')
    counter = 0
    for i in lyst:
      if str(i) == name:
        return([lyst[counter],lyst[counter+1],lyst[counter+2],counter,lyst[counter+3]])
      counter += 1
def checkTimes(naMe):
  if int(retdb(str(naMe))[2]) < 3:
    return True
  else:
    return False
def checkRooms(room,block):
  with open("rooms.txt","r+") as f:
    s = f.read()
    lyst = s.split(',')
    counter = 0
    for i in lyst:
      if i == room:
        if int(lyst[counter+block]) == 0:
          return 1
      counter += 1  
def register ():
  namE = str(input("Name: "))
  rooM = str(input("Which room would you like? "))
  rooM = rooM.lower()
  blocK = str(input("Block: "))
  if checkTimes(namE) == True and checkRooms(str(rooM),int(blocK)) != 1:
    if str(input("Please verify that all the data above is correct. (Y/n)")) == "y":
      a = [namE,rooM,blocK]
      img = qrcode.make(a)
      img.save("libraryqr.png")
      with open("holder.txt","r") as y:
        g = y.read().split(',')
        g[retdb(namE)[3]+2] = int(g[retdb(namE)[3]+2]) + 1
      with open("holder.txt","w") as y:
        y.write(','.join(map(str, g)))
      with open("rooms.txt","r") as y:
        g = y.read().split(',')
        counter = 0
        for i in g:
          if counter+96 == ord(rooM):
            print(i)
        g[counter+int(blocK)] = 0
        counter += 1
      with open("rooms.txt","w") as y:
        y.write(','.join(map(str, g)))
  else:
    print("Oops! Looks like that is not an option! Maybe you've checked out too many rooms this week (the max is 3) or the room is unavailable.")
    quit()  
  return namE


# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
register()

fromaddr = "latin.school.library@gmail.com"
toaddr = str(input("Please enter your email: "))
print("Ok! Soon you will get an email verifying your reservation!") 
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Subject of the Mail"
  
# string to store the body of the mail 
body = "Body_of_the_mail"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "libraryqr.png"
attachment = open("libraryqr.png", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "cloudbox") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 

   
fromaddr = "latin.school.library@gmail.com"
toaddr = "jackeddie04@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Subject of the Mail"
  
# string to store the body of the mail 
body = "Body_of_the_mail"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "libraryqr.png"
attachment = open("libraryqr.png", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "cloudbox") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 

raw_input()