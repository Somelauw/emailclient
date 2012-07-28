import urwid
import configs

class App: 
    def __init__(self):
        emails = [email["email"] for email in configs.emails.config]
        self.menu = Menu("Emailadress:", emails)
        cm = urwid.command_map#.copy()
        cm["j"] = "cursor down"
        cm["k"] = "cursor up"
        #self._command_map = cm

    def start(self):
        palette = [('reversed', 'standout', '')]
        loop = urwid.MainLoop(self.menu, palette, unhandled_input=self.update)
        loop.run()

    def update(self, input):
        if input in ("q", "Q"):
            #print "exit"
            urwid.ExitMainLoop()
        self.menu.update(input)

        #cm = CommandMap(); cm['j'] = 'cursor up'; cm['k'] = 'cursor down'; my_listbox._command_map = cm
         #cm = my_listbox._command_map.copy()

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

        self.listbox = listbox = urwid.ListBox(self.content)
        urwid.WidgetWrap.__init__(self, listbox)

    #def next(self, shift=1):
        #(frame, index) = self.content.get_focus()
        #(frame, index) = self.content.get_next(index)
        #print index
        #self.content.set_focus(index)

    #def prev(self, shift=1):
        #(frame, index) = self.content.get_focus()
        #(frame, index) = self.content.get_prev(index)
        #print index
        #self.content.set_focus(index)

    #def move_selection(self, movement):
        #(frame, index) = self.content.get_focus()
        #index += movement
        #index %= len(self.content)
        #self.content.set_focus(index)

    def up(self, size):
        return self.listbox.keypress(size, "up")

    def down(self, size):
        return self.listbox.keypress(size, "down")

    #def keypress(self, size, key):
        #self.listbox._command_map["j"] = "cursor down"
        #self.listbox._command_map["k"] = "cursor up"

        #mappings = {
                ##"j": self.down,
                ##"k": self.up,
                #}

        ## Fall back on default behaviour
        #return mappings.get(key, lambda size: self.listbox.keypress(size, key))(size)

    def update(self, input):
        print input
        if input in ("q", "Q"):
            #print "exit"
            urwid.ExitMainLoop()
            # FIXME Doesn't exit

        return True

App().start()
