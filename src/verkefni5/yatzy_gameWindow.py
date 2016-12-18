import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import yatzy as y

'''
    gtk grid bord with unfinised functions and bugs. :(
'''

#Temporary variables for bord construction and initialization. 
texti = 'Player 1'
texti2 = 'Player 2'
texti3 = 'Player 3'
texti4 = 'Player 4'
Player1 = 'Player1'
Player2 = 'Player2'
Player3 = 'Player3'
Player4 = 'Player4'

#The game users/players:
p1 = y.gameTable()
p2 = y.gameTable()
p3 = y.gameTable()
p4 = y.gameTable()

diceValue = [ 0, 0, 0, 0, 0]

class GameWindow(Gtk.Window):

    def buttonQuitClicked(self, widget):
        print("So long and thank's for all the fish")
        sys.exit()

    def buttonHelpClicked(self, widget):
        class Dialog(Gtk.Dialog):
            def __init__(self):
                Gtk.Dialog.__init__(self)
                self.set_title("Help")
                self.set_default_size(400, 300)
                self.add_button("OK", Gtk.ResponseType.OK)
                self.connect("response", self.on_response)

                label = Gtk.Label("""
            Don't panic, This is perfectly safe.

            To enter a player's name: clik on the PlayerN and enter a name
              leve empty if not needed.
            Click on the dice you want to save in round two.

            ...This and more to come once the game is finished""")
                
                self.vbox.add(label)
                self.show_all()

            def on_response(self, dialog, response):
                dialog.destroy()

        dialog = Dialog()
        dialog.run()

    def buttonThrowClicked(self, widget, numb=5):
        global diceValue
        diceValue = y.rolleDice(numb)
        print(diceValue)

    def __init__(self):
        Gtk.Window.__init__(self, title="- Yatzy game bord -")

        grid = Gtk.Grid()
        self.add(grid)

        # Why do thees need to be here?
        def buttonThrowClicked(self, widget):
            pass
        def buttonHelpClicked(self, widget):
            pass
        def buttonQuitClicked(self, widget):
            pass

        button1_1 = Gtk.Button(label="Reset Game")
        button2_1 = Gtk.Button(label=texti)
        button3_1 = Gtk.Button(label=texti2)
        button4_1 = Gtk.Button(label=texti3)
        button5_1 = Gtk.Button(label=texti4)
        button2_20 = Gtk.Button(label=('throw') ); button2_20.connect("clicked", self.buttonThrowClicked)
        button3_20 = Gtk.Button(label=('help') ); button3_20.connect("clicked", self.buttonHelpClicked)
        button4_20 = Gtk.Button(label=('quit') ); button4_20.connect("clicked", self.buttonQuitClicked)
        buttonQuitClicked
                
        label1_19 = 'Dice 1: ' + str(diceValue[0])
        button1_19 = Gtk.Button(label=label1_19)
        label2_19 = 'Dice 2: ' + str(diceValue[1])
        button2_19 = Gtk.Button(label=label2_19)
        label3_19 = 'Dice 3: ' + str(diceValue[2])
        button3_19 = Gtk.Button(label=label3_19)
        label4_19 = 'Dice 4: ' + str(diceValue[3])
        button4_19 = Gtk.Button(label=label4_19)
        label5_19 = 'Dice 5: ' + str(diceValue[4])
        button5_19 = Gtk.Button(label=label5_19)

        button1_2 = Gtk.Entry(); button1_2.set_text('1');button1_2.set_property("editable", False)
        button1_3 = Gtk.Entry(); button1_3.set_text('2');button1_3.set_property("editable", False)
        button1_4 = Gtk.Entry(); button1_4.set_text('3');button1_4.set_property("editable", False)
        button1_5 = Gtk.Entry(); button1_5.set_text('4');button1_5.set_property("editable", False)
        button1_6 = Gtk.Entry(); button1_6.set_text('5');button1_6.set_property("editable", False)
        button1_7 = Gtk.Entry(); button1_7.set_text('6');button1_7.set_property("editable", False)
        button1_8 = Gtk.Entry(); button1_8.set_text('Bonus');button1_8.set_property("editable", False)
        button1_9 = Gtk.Entry(); button1_9.set_text('One Pair');button1_9.set_property("editable", False)
        button1_10 = Gtk.Entry(); button1_10.set_text('Two pairs');button1_10.set_property("editable", False)
        button1_11 = Gtk.Entry(); button1_11.set_text('Three of a Kind');button1_11.set_property("editable", False)
        button1_12 = Gtk.Entry(); button1_12.set_text('Four of a Kind:');button1_12.set_property("editable", False)
        button1_13 = Gtk.Entry(); button1_13.set_text('Small Straight');button1_13.set_property("editable", False)
        button1_14 = Gtk.Entry(); button1_14.set_text('Large Straight');button1_14.set_property("editable", False)
        button1_15 = Gtk.Entry(); button1_15.set_text('Full House');button1_15.set_property("editable", False)
        button1_16 = Gtk.Entry(); button1_16.set_text('Chance');button1_16.set_property("editable", False)
        button1_17 = Gtk.Entry(); button1_17.set_text('Yatzy');button1_17.set_property("editable", False)
        button1_18 = Gtk.Entry(); button1_18.set_text('Total');button1_18.set_property("editable", False)

        button2_2 = Gtk.Entry(); button2_2.set_text(str(p1[1]));button2_2.set_property("editable", False)
        button2_3 = Gtk.Entry(); button2_3.set_text(str(p1[2]));button2_3.set_property("editable", False)
        button2_4 = Gtk.Entry(); button2_4.set_text(str(p1[3]));button2_4.set_property("editable", False)
        button2_5 = Gtk.Entry(); button2_5.set_text(str(p1[4]));button2_5.set_property("editable", False)
        button2_6 = Gtk.Entry(); button2_6.set_text(str(p1[5]));button2_6.set_property("editable", False)
        button2_7 = Gtk.Entry(); button2_7.set_text(str(p1[6]));button2_7.set_property("editable", False)
        button2_8 = Gtk.Entry(); button2_8.set_text(Player1);button2_8.set_property("editable", False)
        button2_9 = Gtk.Entry(); button2_9.set_text(Player1);button2_9.set_property("editable", False)
        button2_10 = Gtk.Entry(); button2_10.set_text(Player1);button2_10.set_property("editable", False)
        button2_11 = Gtk.Entry(); button2_11.set_text(Player1);button2_11.set_property("editable", False)
        button2_12 = Gtk.Entry(); button2_12.set_text(Player1);button2_12.set_property("editable", False)
        button2_13 = Gtk.Entry(); button2_13.set_text(Player1);button2_13.set_property("editable", False)
        button2_14 = Gtk.Entry(); button2_14.set_text(Player1);button2_14.set_property("editable", False)
        button2_15 = Gtk.Entry(); button2_15.set_text(Player1);button2_15.set_property("editable", False)
        button2_16 = Gtk.Entry(); button2_16.set_text(Player1);button2_16.set_property("editable", False)
        button2_17 = Gtk.Entry(); button2_17.set_text(Player1);button2_17.set_property("editable", False)
        button2_18 = Gtk.Entry(); button2_18.set_text(Player1);button2_18.set_property("editable", False)

        button3_2 = Gtk.Entry(); button3_2.set_text(Player2);button3_2.set_property("editable", False)
        button3_3 = Gtk.Entry(); button3_3.set_text(Player2);button3_3.set_property("editable", False)
        button3_4 = Gtk.Entry(); button3_4.set_text(Player2);button3_4.set_property("editable", False)
        button3_5 = Gtk.Entry(); button3_5.set_text(Player2);button3_5.set_property("editable", False)
        button3_6 = Gtk.Entry(); button3_6.set_text(Player2);button3_6.set_property("editable", False)
        button3_7 = Gtk.Entry(); button3_7.set_text(Player2);button3_7.set_property("editable", False)
        button3_8 = Gtk.Entry(); button3_8.set_text(Player2);button3_8.set_property("editable", False)
        button3_9 = Gtk.Entry(); button3_9.set_text(Player2);button3_9.set_property("editable", False)
        button3_10 = Gtk.Entry(); button3_10.set_text(Player2);button3_10.set_property("editable", False)
        button3_11 = Gtk.Entry(); button3_11.set_text(Player2);button3_11.set_property("editable", False)
        button3_12 = Gtk.Entry(); button3_12.set_text(Player2);button3_12.set_property("editable", False)
        button3_13 = Gtk.Entry(); button3_13.set_text(Player2);button3_13.set_property("editable", False)
        button3_14 = Gtk.Entry(); button3_14.set_text(Player2);button3_14.set_property("editable", False)
        button3_15 = Gtk.Entry(); button3_15.set_text(Player2);button3_15.set_property("editable", False)
        button3_16 = Gtk.Entry(); button3_16.set_text(Player2);button3_16.set_property("editable", False)
        button3_17 = Gtk.Entry(); button3_17.set_text(Player2);button3_17.set_property("editable", False)
        button3_18 = Gtk.Entry(); button3_18.set_text(Player2);button3_18.set_property("editable", False)

        button4_2 = Gtk.Entry(); button4_2.set_text(Player3);button4_2.set_property("editable", False)
        button4_3 = Gtk.Entry(); button4_3.set_text(Player3);button4_3.set_property("editable", False)
        button4_4 = Gtk.Entry(); button4_4.set_text(Player3);button4_4.set_property("editable", False)
        button4_5 = Gtk.Entry(); button4_5.set_text(Player3);button4_5.set_property("editable", False)
        button4_6 = Gtk.Entry(); button4_6.set_text(Player3);button4_6.set_property("editable", False)
        button4_7 = Gtk.Entry(); button4_7.set_text(Player3);button4_7.set_property("editable", False)
        button4_8 = Gtk.Entry(); button4_8.set_text(Player3);button4_8.set_property("editable", False)
        button4_9 = Gtk.Entry(); button4_9.set_text(Player3);button4_9.set_property("editable", False)
        button4_10 = Gtk.Entry(); button4_10.set_text(Player3);button4_10.set_property("editable", False)
        button4_11 = Gtk.Entry(); button4_11.set_text(Player3);button4_11.set_property("editable", False)
        button4_12 = Gtk.Entry(); button4_12.set_text(Player3);button4_12.set_property("editable", False)
        button4_13 = Gtk.Entry(); button4_13.set_text(Player3);button4_13.set_property("editable", False)
        button4_14 = Gtk.Entry(); button4_14.set_text(Player3);button4_14.set_property("editable", False)
        button4_15 = Gtk.Entry(); button4_15.set_text(Player3);button4_15.set_property("editable", False)
        button4_16 = Gtk.Entry(); button4_16.set_text(Player3);button4_16.set_property("editable", False)
        button4_17 = Gtk.Entry(); button4_17.set_text(Player3);button4_17.set_property("editable", False)
        button4_18 = Gtk.Entry(); button4_18.set_text(Player3);button4_18.set_property("editable", False)

        button5_2 = Gtk.Entry(); button5_2.set_text(Player4);button5_2.set_property("editable", False)
        button5_3 = Gtk.Entry(); button5_3.set_text(Player4);button5_3.set_property("editable", False)
        button5_4 = Gtk.Entry(); button5_4.set_text(Player4);button5_4.set_property("editable", False)
        button5_5 = Gtk.Entry(); button5_5.set_text(Player4);button5_5.set_property("editable", False)
        button5_6 = Gtk.Entry(); button5_6.set_text(Player4);button5_6.set_property("editable", False)
        button5_7 = Gtk.Entry(); button5_7.set_text(Player4);button5_7.set_property("editable", False)
        button5_8 = Gtk.Entry(); button5_8.set_text(Player4);button5_8.set_property("editable", False)
        button5_9 = Gtk.Entry(); button5_9.set_text(Player4);button5_9.set_property("editable", False)
        button5_10 = Gtk.Entry(); button5_10.set_text(Player4);button5_10.set_property("editable", False)
        button5_11 = Gtk.Entry(); button5_11.set_text(Player4);button5_11.set_property("editable", False)
        button5_12 = Gtk.Entry(); button5_12.set_text(Player4);button5_12.set_property("editable", False)
        button5_13 = Gtk.Entry(); button5_13.set_text(Player4);button5_13.set_property("editable", False)
        button5_14 = Gtk.Entry(); button5_14.set_text(Player4);button5_14.set_property("editable", False)
        button5_15 = Gtk.Entry(); button5_15.set_text(Player4);button5_15.set_property("editable", False)
        button5_16 = Gtk.Entry(); button5_16.set_text(Player4);button5_16.set_property("editable", False)
        button5_17 = Gtk.Entry(); button5_17.set_text(Player4);button5_17.set_property("editable", False)
        button5_18 = Gtk.Entry(); button5_18.set_text(Player4);button5_18.set_property("editable", False)

        grid.add(button1_1)
        grid.attach(button2_1, 1, 0, 1, 1)
        grid.attach(button3_1, 2, 0, 2, 1)
        grid.attach(button4_1, 6, 0, 3, 1)
        grid.attach(button5_1, 16, 0, 4, 1)
        grid.attach_next_to(button1_2, button1_1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_3, button1_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_4, button1_3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_5, button1_4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_6, button1_5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_7, button1_6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_8, button1_7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_9, button1_8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_10, button1_9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_11, button1_10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_12, button1_11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_13, button1_12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_14, button1_13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_15, button1_14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_16, button1_15, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_17, button1_16, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_18, button1_17, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button1_19, button1_18, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(button2_2, button2_1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_3, button2_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_3, button2_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_4, button2_3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_5, button2_4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_6, button2_5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_7, button2_6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_8, button2_7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_9, button2_8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_10, button2_9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_11, button2_10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_12, button2_11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_13, button2_12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_14, button2_13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_15, button2_14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_16, button2_15, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_17, button2_16, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_18, button2_17, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_19, button2_18, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button2_20, button2_19, Gtk.PositionType.BOTTOM, 1, 1)
        
        grid.attach_next_to(button3_2, button3_1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_3, button3_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_3, button3_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_4, button3_3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_5, button3_4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_6, button3_5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_7, button3_6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_8, button3_7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_9, button3_8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_10, button3_9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_11, button3_10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_12, button3_11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_13, button3_12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_14, button3_13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_15, button3_14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_16, button3_15, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_17, button3_16, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_18, button3_17, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_19, button3_18, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button3_20, button3_19, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(button4_2, button4_1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_3, button4_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_3, button4_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_4, button4_3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_5, button4_4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_6, button4_5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_7, button4_6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_8, button4_7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_9, button4_8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_10, button4_9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_11, button4_10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_12, button4_11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_13, button4_12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_14, button4_13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_15, button4_14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_16, button4_15, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_17, button4_16, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_18, button4_17, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_19, button4_18, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4_20, button4_19, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(button5_2, button5_1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_3, button5_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_3, button5_2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_4, button5_3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_5, button5_4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_6, button5_5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_7, button5_6, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_8, button5_7, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_9, button5_8, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_10, button5_9, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_11, button5_10, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_12, button5_11, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_13, button5_12, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_14, button5_13, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_15, button5_14, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_16, button5_15, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_17, button5_16, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_18, button5_17, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5_19, button5_18, Gtk.PositionType.BOTTOM, 1, 1)

        grid.show_all()

win = GameWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

    
