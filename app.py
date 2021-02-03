import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ToDo")
        
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.main_box)
        
        fbox = Gtk.Box(spacing=6)
        self.main_box.pack_start(fbox, True, True, 10)
        
        # Entry and labels
        input_title = Gtk.Label(label="Task")
        self.add_button = Gtk.Button(label="Add")
        self.add_button.connect("clicked", self.add_todo)
        self.input = Gtk.Entry()
        self.input.connect("activate", self.add_todo)
        
        # add widgets 
        fbox.pack_start(input_title, True, True, 7)
        fbox.pack_start(self.input, True, True, 0)
        fbox.pack_start(self.add_button, True, False, 7)
        
        
    def add_todo(self, widget):
        if self.input.get_text():
            new_task = Gtk.Label(label=self.input.get_text())
            self.main_box.pack_start(new_task, True, True, 0)
            self.main_box.show_all()
            self.input.set_text('')

if __name__ ==  '__main__':
    window = Window()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
