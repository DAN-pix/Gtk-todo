import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ToDo")
        
        main_box = Gtk.Box(spacing=6)
        self.add(main_box)

        # Entry and labels
        input_title = Gtk.Label(label="task")
        self.add_button = Gtk.Button(label="Add")
        self.add_button.connect("clicked", self.add_todo)
        self.input = Gtk.Entry()
        self.input.connect("activate", self.add_todo)
        
        # add widgets 
        main_box.pack_start(input_title, True, True, 7)
        main_box.pack_start(self.input, True, True, 0)
        main_box.pack_start(self.add_button, True, False, 7)
        
        
    def add_todo(self, widget):
        print(self.input.get_text())
        
if __name__ ==  '__main__':
    window = Window()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
