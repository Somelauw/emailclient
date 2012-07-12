import config
import imaplib
import smtplib

def getAccounts(fileName):
    accounts = config.load(fileName)
    return [EmailAccount(account) for account in accounts]

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
            self.imap = self.imap or Imap("imap.gmail.com", 587)
            self.smtp = self.smtp or Smtp("smtp.gmail.com", 587)

        self.sender.login()
        self.receiver.login()

    def __setitem__(self, key, item):
        if key == "email":
            self.email = value
        elif key == "password":
            self.password = value
        elif key == "smtp":
            smtp = value.split(":")
            if len(smtp) == 1:
                self.sender = Smtp(smtp, 25)
            else:
                self.sender = Smtp(smtp[0], smtp[1])
        elif key == "imap":
            imap = value.split(":")
            if len(imap) == 1:
                self.receiver = Imap(imap, 143)
            else:
                self.receiver = Imap(imap[0], imap[1])
        elif key == "pop":
            raise Exception("pop is currently not supported")
        else:
            raise Warning("key %s is ignored" % key)

    def getlabels():
        return self.imap

class Smtp(Sender):
    def __init__(server, port):
        self.server = server
        self.port = port

class Imap(Receiver):
    def __init__(server, port):
        self.server = server
        self.port = port

    def login(self):
        m = imaplib.IMAP4(self.server, self.port)
        self.mail = imaplib.IMAP4_SSL(self.server)
        return self.mail.login(self.email, self.password)

    def getlabels(self):
        return self.mail.list()

# I don't plan on supporting Pop3 anytime soon, so you would have to program this yourself
#class Pop3(object):
    #port = 110
    #pass

class Sender(object):
    def login():
        pass

class Receiver(object):
    def login():
        pass

