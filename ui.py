import urwid
import configs

class App: 
    def __init__(self):
        emails = [email["email"] for email in configs.emails.config]
        self.menu = Menu("", emails)

    def start(self):
        palette = [('reversed', 'standout', '')]
        loop = urwid.MainLoop(self.menu, palette, unhandled_input=self.update)
        loop.run()

    def update(self, input):
        self.menu.update(input)

class Selectable(urwid.WidgetWrap):
    def __init__(self, *param, **kw):
        self._selectable = True
        text = urwid.Text(*param, **kw)
        text = urwid.AttrMap(text, None, 'reversed')
        urwid.WidgetWrap.__init__(self, text)

    def selectable(self):
        return True

    def keypress(self, size, key):
        self.text = "%s-%s" % (size, key)
        return key

class Menu(urwid.WidgetWrap):
    def __init__(self, caption="", items=[]):
        self.items = items

        self.content = urwid.SimpleListWalker(
                [urwid.Text(caption)] +\
                [Selectable(item) for item in self.items])

        self.listbox = urwid.ListBox(self.content)
        urwid.WidgetWrap.__init__(self, self.listbox)

        # TODO add title

    def update(self, input):
        return True

App().start()
