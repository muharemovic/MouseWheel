import sys
import os
import gi
import warnings
gi.require_version('Gtk', '3.0')
warnings.filterwarnings("ignore")
from gi.repository import Gtk

class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Scale Example", application=app)
        self.set_default_size(200, 100)
        self.set_border_width(5)

        ad1 = Gtk.Adjustment(int(self.get_info_scroll()), 0, 30, 1, 1, 0)
        self.h_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        self.h_scale.set_digits(0)
        self.h_scale.set_hexpand(True)
        self.h_scale.set_valign(Gtk.Align.START)
        self.h_scale.connect("value-changed", self.scale_moved)

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.attach(self.h_scale, 0, 3, 3, 2)
        self.add(grid)
        if os.path.isfile('~/.config/autostart/imwheel.desktop') == False:
            imwheel_desktop = '''[Desktop Entry]
            Type=Application
            Exec=imwheel
            Hidden=false
            NoDisplay=false
            X-GNOME-Autostart-enabled=true
            Name[en_US]=imwheel
            Name=imwheel
            Comment[en_US]=
            Comment='''
            with open(os.path.expanduser('~/.config/autostart/imwheel.desktop'), 'w') as f:
                f.write(imwheel_desktop)
                f.close()



    def scale_moved(self,event):
        val = str(int(self.h_scale.get_value()))

        config_imwheelrc = '''".*"
                None,      Up,   Button4, {}
                None,      Down, Button5, {}
                Control_L, Up,   Control_L|Button4
                Control_L, Down, Control_L|Button5
                Shift_L,   Up,   Shift_L|Button4
                Shift_L,   Down, Shift_L|Button5'''.format(val, val)

        with open(os.path.expanduser('~/.imwheelrc'), 'w') as f:
            f.write(config_imwheelrc)
        f.close()
        os.system("imwheel -kill")

    def get_info_scroll(self):
        with open(os.path.expanduser('~/.imwheelrc')) as f:
            imwheelrc_config = [line.split() for line in f]
            return imwheelrc_config[2][3]

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)