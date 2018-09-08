import yagmail

def send(filename, recipient):
    yag = yagmail.SMTP('mylock123456@gmail.com')

    subject = 'Order confirmation'
    body = ('''Thank you for your order.
            In the attachement you will find your acces codes.
            
            Have a good day!''')
    file = (filename+'.png')

    yag.send(recipient, subject, [body, file])
