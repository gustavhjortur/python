from gi.repository import Gtk
import sys

class Dialog(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.set_title("Help")
        self.set_default_size(400, 300)
        self.add_button("OK", Gtk.ResponseType.OK)
        #self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.connect("response", self.on_response)

        label = Gtk.Label("""
    Don't panic, This is perfectly safe.

    To enter a Name klik on the Playern and enter a name
      leve empty if not needed.
    Click on the dice you want to save in round two.""")
        
        self.vbox.add(label)

        self.show_all()

    def on_response(self, dialog, response):
        #if response == Gtk.ResponseType.OK:
        #    print("OK button clicked")
        if response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")
        #dialog.destroy()
        sys.exit()

dialog = Dialog()
dialog.run()
Dialog.connect("delete-event", Gtk.main_quit)
