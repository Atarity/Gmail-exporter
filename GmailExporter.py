# Gmail exporter script. It check you Gmail thru IMAP, 
# parse all unseen letters (only first text block) 
# by params and extract only (!) e-mail adresses from 
# body to the file emails.out separate it by break line.
#
# After body parsing mail became SEEN status.

sterm = '(FROM "store@example.ru" UNSEEN SUBJECT "0")'

# Search criteria string examples:
# (FROM "store@example.ru" UNSEEN)
# (FROM "store@example.ru" SEEN SINCE "31-Dec-2012" BEFORE "01-Jan-2013" SUBJECT "Free beer and stuff" TEXT "Some body text")
# Whole search criteria list: http://php.net/manual/ru/function.imap-search.php
# 

import imaplib, re, getpass, email, re, io
from types import *

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


def gmail_checker(username,password):	
	mail=imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(username,password)
	mail.list()
	mail.select('INBOX')
	result, data = mail.uid('search', None, sterm) # Search mails with criteria

	ids = data[0] # data is a list
	id_list = ids.split() # ids is a space separated string

	#print result
	#print ids
	with io.open('emails.out', 'a') as file:
		for  num in id_list:
	#	num = id_list[-1]
			result, mails = mail.uid('fetch', num, "(RFC822)") # fetch the email body (RFC822) for the given ID
			email_body = get_first_text_block(email.message_from_string(mails[0][1]))
			m = re.search('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', email_body)
			if type(m) is NoneType:
				outs = '--------------------------unparsible email (start):--------------------------- \n'+ email_body + '\n--------------------------unparsible email (end):---------------------------'
				print outs
				try :
					file.write(unicode(outs+'\n'))
				except UnicodeDecodeError:
					pass
			else :
				print m.group(0)
				try :
					file.write(unicode(m.group(0)+'\n'))
				except UnicodeDecodeError:
					pass
		file.close()
	mail.close()
	mail.logout()
#mail = 'admin'
#passwd = 'admin'
mail = raw_input('Gmail: ')
passwd = getpass.getpass('password: ')
gmail_checker(mail,passwd)
