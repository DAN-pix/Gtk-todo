from typing import Text
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ToDo")
        self.set_default_size(500, 400)
        self.set_border_width(10)
        
        # window title
        header = Gtk.HeaderBar(title="Gtk ToDo app")
        header.props.show_close_button = True
        self.set_titlebar(header)
        
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.main_box)
        
        fbox = Gtk.Box(spacing=6)
        self.main_box.pack_start(fbox, False, False, 10)
        
        # Entry and labels
        input_title = Gtk.Label(label="Task")
        self.add_button = Gtk.Button(label="Add")
        self.add_button.connect("clicked", self.add_todo)
        self.input = Gtk.Entry()
        self.input.connect("activate", self.add_todo)
        
        # add widgets 
        fbox.pack_start(input_title, False, True, 6)
        fbox.pack_start(self.input, True, True, 0)
        fbox.pack_start(self.add_button, False, False, 0)
     
        # TASK TABLE
        self.list_tasks = Gtk.ListStore(str, bool)
        treeview = Gtk.TreeView(model=self.list_tasks)
        
        # task column
        renderer_tasks = Gtk.CellRendererText()
        renderer_tasks.set_property("editable", True)
        renderer_tasks.connect("edited", self.task_edited)
        column_tasks = Gtk.TreeViewColumn("task", renderer_tasks, text=0)
        treeview.append_column(column_tasks)
        
        renderer_complete = Gtk.CellRendererToggle()
        renderer_complete.connect("toggled", self.complete_task)
        column_complete = Gtk.TreeViewColumn("Complete", renderer_complete, active=1)
        treeview.append_column(column_complete)
                
        self.main_box.pack_start(treeview, False, True, 0)
    
    def task_edited(self, widget, path, new_task):
        self.list_tasks[path][0] = new_task
    
    def complete_task(self, widget, path):
        del self.list_tasks[path]
    
    def add_todo(self, widget):
        if self.input.get_text():
            new_task = [self.input.get_text(), False]
            self.list_tasks.append(new_task)
            self.input.set_text('')

if __name__ ==  '__main__':
    window = Window()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
