import curses
#import os
#import sys
import time
import curses.wrapper

# TODO: Make everything configurable and split everything in subfiles

def main(stdscr):
    MenuHandler(stdscr).run()

class MenuHandler():
    def __init__(self, window):
        self.window = window
        self.menu = EmailChooser(self)
    def update(self, keypress):
        self.menu.update(keypress)
    def refresh(self):
        self.menu.refresh()
    def run(self):
        while True:
            self.refresh()
            time.sleep(0.01)
            c = self.window.getch()
            self.update(c)
            time.sleep(0.01)

class Menu(object):
    def __init__(self, menuhandler, title="", options="-"):
        self.menuhandler = menuhandler
        self.pad = curses.newpad(100, 100)
        self.selected = 0
        self.title = title
        self.options = options

    def update(self, keypress):
        actions = {
                ord("j"): self.next_item,
                ord("k"): self.previous_item,
                curses.KEY_ENTER: self.crash,
                10: self.crash,
                }
        if keypress != None:
            actions[keypress]()

    def next_item(self):
        self.selected = (self.selected + 1) % len(self.options)

    def previous_item(self):
        self.selected = (self.selected - 1) % len(self.options)

    def crash(self):
        self.menuhandler.window = None

    def refresh(self):
        self.pad.addstr(0, 0, self.title, curses.A_BOLD)

        # Show the items
        for index, option in enumerate(self.options):
            self.pad.addstr(1 + 1 * index, 0, option)

        # Show which item is highlighted
        self.pad.addstr(1 + 1 * self.selected, 0, self.options[self.selected], curses.A_STANDOUT)
        self.pad.refresh( 0,0, 0,0, 20,75)

class EmailChooser(Menu):
    def __init__(self, menuHandler):
        super(EmailChooser, self).__init__(
                menuHandler, 
                "Email accounts", 
                ["Gmail", "Yahoo"])


curses.wrapper(main)

