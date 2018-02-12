import smtplib

content = 'example email content'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('khalifngeno@gmail.com','Poheri333')

mail.sendmail('khalifngeno@gmail.com','sethkrm@gmail.com',content)

mail.close()

print('Email Sent')