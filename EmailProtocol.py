#import config
import imaplib
import smtplib

class AccountHandler(object):
    def __init__(self, accounts=[]):
        #accountConfig = config.Config("emails")
        #accounts = accountConfig.config
        self.accounts = [EmailAccount(account) for account in accounts]

class EmailAccount(object):
    def __init__(self, data):
        self.email = None
        self.password = None
        self.smtp = None
        self.imap = None

        for key, value in self.data:
            self[key] = value

        # Simplify the life of users of common protocols
        if self.adress.endswith("@gmail.com"):
            self.receiver = self.receiver or IMAP("imap.gmail.com:587")
            self.sender = self.sender or SMTP("smtp.gmail.com:587")

    def __setitem__(self, key, value):
        if key == "email":
            self.email = value
        elif key == "password":
            self.password = value
        elif key == "smtp":
            self.receiver = SMTP(self, value)
        elif key == "imap":
            self.sender = IMAP(self, value)
        elif key == "pop":
            raise Exception("pop is currently not supported")
        else:
            raise Warning("key %s is ignored" % key)

    def getlabels(self):
        return self.imap

class Sender(object):
    def login():
        pass

class Receiver(object):
    def login():
        pass

class SMTP(Sender):
    def __init__(self, account, data):
        self.account = account
        server, port = parseServer(data)
        self.server = smtplib.SMTP(server, port)

    def sendmail(self, to, message):
        server = self.server
        server.starttls()
        server.ehlo()
        server.login(self.account.email, self.account.password)
        server.sendmail(self.account.email, to, message)
        return server.ehlo()

class IMAP(Receiver):
    def __init__(self, account, data):
        self.account = account
        self.server, self.port = parseServer(data)
        print self.login()

    def login(self):
        imaplib.IMAP4(self.server, self.port)
        self.mail = imaplib.IMAP4_SSL(self.server)
        return self.mail.login(self.account.email, self.account.password)

    def getlabels(self):
        return self.mail.list()

def parseServer(serverstr):
    server = serverstr.split(":")
    if len(server) == 1:
        return (server, 25)
    else:
        return (server[0], int(server[1]))

# I don't plan on supporting Pop3 anytime soon, so you would have to program this yourself
#class Pop3(object):
    #port = 110
    #pass


