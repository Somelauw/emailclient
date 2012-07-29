import urwid
import configs
from menu import Menu, Selectable

debug_file = open("debug", "w")
# Since I don't know where I should put code to close this file, I'll rely on the garbage collector for closing this file.

class App: 
    def __init__(self):
        self.emaillist = EmailList(self)
        self.folderlist = FolderList(self)
        self.menu = self.emaillist

        # Try adding colums
        self.contents = [self.emaillist, self.folderlist, self.menu]
        self.columns = urwid.Columns([self.emaillist, self.folderlist, self.menu])

        cm = urwid.command_map#.copy()
        cm["j"] = "cursor down"
        cm["k"] = "cursor up"
        cm["h"] = "cursor left"
        cm["l"] = "cursor right"

    def select_email(self, email):
        debug_file.write(email)
        #self.folderlist.select_email(email)
        
        # Rather I would modify the columns object
        folderlist = FolderList(self, ["poep"])
        self.columns.contents = [folderlist]

    def start(self):
        palette = [('reversed', 'standout', '')]
        loop = urwid.MainLoop(self.columns, palette, unhandled_input=self.update)
        loop.run()

    def update(self, input):
        print input
        if input in ("q", "Q"):
            urwid.ExitMainLoop()

    def keypress(self, a, b):
        print a, b


class EmailList(Menu):
    def __init__(self, app):
        self.app = app
        self.emails = [email["email"] for email in configs.emails.config]
        super(EmailList, self).__init__(app, "Emailadress", self.emails)

    def keypress(self, a, b):
        widget, pos = self.listbox.get_focus()
        email = self.emails[pos - 1]
        self.app.select_email(email)
        return super(EmailList, self).keypress(a, b)

class FolderList(Menu):
    def __init__(self, app, email="bang"):
        self.app = app
        super(FolderList, self).__init__(app, "Folders", [email])

    def select_email(self, email):
        self.content[1:2] = [Selectable(email)]
        pass

App().start()
