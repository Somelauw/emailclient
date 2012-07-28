import urwid

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
    def __init__(self, master=None, caption="", items=[]):
        self.master = master
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
        #print input
        if input in ("q", "Q"):
            #print "exit"
            urwid.ExitMainLoop()
            # FIXME Doesn't exit

        return True
