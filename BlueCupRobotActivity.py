
from sugar.activity import activity
import pygtk
import random
import gtk
import sys, os
import logging
import getopt




class BlueCupRobotActivity (activity.Activity):
       # This callback quits the program
  
    
    def __init__(self,handle ):
        print "running activity init", handle
        activity.Activity.__init__(self, handle)
        print "activity running"
        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        print "activity running1"
        toolbox.show()

        self.cup = gtk.Image()
        self.sandbox_button = gtk.Button("Play around")
        self.sandbox_button.set_size_request(500, 120)
        self.create_button = gtk.Button("Create a program")
        self.create_button.set_size_request(500, 120)

        self.fix = gtk.Layout()

        

        
        self.table = gtk.Table(10, 10, True)
        
        
        self.fix.put(self.sandbox_button, 150, 80)
        self.fix.put(self.create_button, 150, 240)
 

        self.create_button.show()
        self.sandbox_button.show()
        self.fix.show()
       



        self.sandbox_button.connect("button-release-event", self.startSandbox)
        self.create_button.connect("button-release-event", self.createProgram)


##        #Create image for buttons
        self.left_icon = gtk.Image()
        self.right_icon = gtk.Image()
        self.down_icon = gtk.Image()
        self.flip_icon = gtk.Image()
        self.bottom_image = gtk.Image()
#        self.bottom_image.set_from_file("bottom.svg")  
        #Create Main Toolbar
        self.toolbara = gtk.Toolbar()
##        #Create Secondary Toolbar
        self.toolbarb = gtk.Toolbar()
###
##  
##        #Close Button
        self.close_button = gtk.Button()
##        
##        #Restart Button
        self.restart_button = gtk.Button()
##        #Save Button
        self.save_button = gtk.Button()
##        
##        #Load Button
        self.load_button = gtk.Button()
##        
##        #Start Button
        self.start_button = gtk.Button()
##        
##        #Populate secondary toolbar
##        #Left button
        self.left_button = gtk.Button()
##        
##        #Right button
        self.right_button = gtk.Button()
##        
##        #Rotate button
        self.rotate_button = gtk.Button()
##        
##        #Release button
        self.release_button = gtk.Button()
##
##        #Undo button
        self.undo_button = gtk.Button()
##        
##        #Clear button
        self.clear_button = gtk.Button()
##        
##        #Changecolor button
        self.changecolor_button = gtk.Button()

        # Colorfulcups button
        self.colorfulcups_button = gtk.Button()

         #Start_window button
        self.startwindow_button = gtk.Button()
        
        

##       
        self.codeimages=[]
##        
        self.l=0  ## counter for images left_icon
        self.i=0  ## counter for images right_icon
        self.m=0 ##counter for images flip_icon
        self.n=0 ##counter for images down_icon
        self.r=0   ## indices to fill up the table 
        self.k=0
        
        self.write_symbol = {"release_button":'d', "right_button":'r',"left_button":'l',"rotate_button":'f'}
        self.symbol_load = {'d':"release_button", 'r':"right_button",'l':"left_button",'f':"rotate_button"}
        

##        
##        #Attach VBox
##        
##        self.vbox.show()
####        toolbara.show()
####        toolbarb.show()
        self.color = "blue"
        self.colors = ("blue","olive","green","maroon","purple","yellow")
        
        self.colors_option = []
        
        self.color_imageDown = {"blue":"cupDown1.svg", "green":"greenCupDown1.svg",\
                                "olive":"oliveCupDown1.svg", "maroon":"maroonCupDown1.svg",\
                                "purple":"purpleCupDown1.svg","yellow":"yellowCupDown1.svg"}
        self.color_imageUp = {"blue":"cupUp1.svg", "green":"greenCupUp1.svg",\
                                "olive":"oliveCupUp1.svg", "maroon":"maroonCupUp1.svg",\
                                "purple":"purpleCupUp1.svg","yellow":"yellowCupUp1.svg"}
        

        
        
        self.colors_option = []
        

        self.imagecount = 0
        self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
        self.traceline_imagecount = gtk.image_new_from_file("traceline.svg")
        self.up=False

        self.bottom = 400        
        self.cupwidth = 32
        self.cupheight = 43        
##  

##       self.vbox.show()
        self.x = 0
        self.y = 70
        self.top=70
        self.ty = self.y + self.cupheight
##
        self.fname =None
###        f=open(self.fname,'w+')
        self.ar_col = 0
        self.arrow_color="orange"
##
        self.xx=[]
        self.imagelist=[]
        print "activity running4"
        self.swin = gtk.ScrolledWindow()
        self.swin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
##       
         
        self.set_canvas(self.fix)
        self.fix.show()
        print "activity running5"

 
###################################################################################
#####################################################################################
#####################################################################################

         
##        
    def startSandbox(self,widget, data=None):
        
        self.clear(self)
        self.fix.remove(self.sandbox_button)
        
        self.fix.remove(self.create_button)
        
#
        self.left_icon.set_from_file("arrowLeft.svg")
        self.right_icon.set_from_file("arrowRight.svg")
        self.flip_icon.set_from_file("turnLeft90.svg")
        self.down_icon.set_from_file("arrowDown.svg")
        self.bottom_image = gtk.Image()
        self.bottom_image.set_from_file("bottom.svg") 

       
####        #Create Secondary Toolbar
## 
        self.toolbarb.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        self.toolbarb.set_style(gtk.TOOLBAR_BOTH)
        self.toolbarb.set_border_width(5)

        self.fix.put(self.toolbarb,0,0)

        self.toolbarb.show()
        

        

##        
##        #Startwindow button
        self.startwindow_button = self.toolbarb.append_item(
            "Start\nwindow", 
            "Come back to start window", 
            "Private", 
            None, 
            self.startwindow)
##       self.toolbarb.append_space()
       
        
        #Populate secondary toolbar
        #Left button
        self.left_button = self.toolbarb.append_item(
            "Left", 
            "Inserts a Move Left command",
            
            "Private", 
            self.left_icon, 
            self.moveleft)
##        self.toolbarb.append_space()
        self.left_button.show()
        
        #Right button
        self.right_button = self.toolbarb.append_item(
            "Right", 
            "Inserts a Move Right command", 
            "Private", 
            self.right_icon, 
            self.moveright)
##        self.toolbarb.append_space()
        self.right_button.show()
        
        #Rotate button
        self.rotate_button = self.toolbarb.append_item(
            "Rotate", 
            "Inserts a Rotate command", 
            "Private", 
            self.flip_icon, 
            self.rotate)
##        self.toolbarb.append_space()
        self.rotate_button.show()
        
        #Release button
        self.release_button = self.toolbarb.append_item(
            "Release", 
            "Drops the cup", 
            "Private", 
            self.down_icon, 
            self.release)
##        self.toolbarb.append_space()
        self.release_button.show()

        #Undo button
        self.undo_button = self.toolbarb.append_item(
            "Undo", 
            "Undo", 
            "Private", 
            None, 
            self.undo)
##        self.toolbarb.append_space()
        self.undo_button.show()

        
        #Clear button
        self.clear_button = self.toolbarb.append_item(
            "Clear", 
            "Clear", 
            "Private", 
            None, 
            self.clear)
##        self.toolbarb.append_space()
        self.clear_button.show()
        
        #Changecolor button
        self.changecolor_button = self.toolbarb.append_item(
            "Change\ncups'\ncolor", 
            "Change cups' color", 
            "Private", 
            None, 
            self.changecolor)
##        self.toolbarb.append_space()
        self.changecolor_button.show()

        #Colorfulcups button
        self.colorfulcups_button = self.toolbarb.append_item(
            "Make\ncups\ncolorful", 
            "Make cups colorful", 
            "Private", 
            None, 
            self.makeCupsColorful)
##        self.toolbarb.append_space()
        self.colorfulcups_button.show()

        
        self.table = gtk.Table(10, 10, True)
        self.swin = gtk.ScrolledWindow()
        self.fix.put(self.image_imagecount, self.x, self.y)
        self.fix.put(self.traceline_imagecount, self.x, self.ty)
        self.image_imagecount.show()
        self.traceline_imagecount.show()
        self.fix.put(self.bottom_image,0,405)
        self.bottom_image.show()
        self.fix.put(self.swin,0, 420)
        
        #viewport = gtk.Viewport()
        self.swin.set_size_request(700, 100)
 
  
        self.swin.add_with_viewport(self.table)
        self.table.show()
        self.swin.show()
  
        self.fix.show()

##       
##        
####################################################################
####################################################################
####################################################################
##
    def createProgram(self, widget, data = None):

        self.fix.remove(self.sandbox_button)
        self.fix.remove(self.create_button)
        
        

        self.fix = gtk.Layout()
        print "createPrgrm1"
  
        
##        
        self.left_icon.set_from_file("arrowLeft.svg")
        self.right_icon.set_from_file("arrowRight.svg")
        self.flip_icon.set_from_file("turnLeft90.svg")
        self.down_icon.set_from_file("arrowDown.svg")
        print "createPrgrm2" 
##        

##        
####        #Create Secondary Toolbar
        print "createPrgrm3"
        self.toolbarb.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        self.toolbarb.set_style(gtk.TOOLBAR_BOTH)
        self.toolbarb.set_border_width(5)
        self.fix.put(self.toolbarb,0,0)
        self.toolbarb.show()
        print "createPrgrm3"
####

##        
        #Startwindow button
        self.startwindow_button = self.toolbarb.append_item(
            "Start\nwindow", 
            "Come back to start window", 
            "Private", 
            None, 
            self.startwindow)
        self.startwindow_button.show()
##        self.toolbara.append_space()
##        
##        #Save Button
        self.save_button = self.toolbarb.append_item(
            "Save\nthe\nprogram", 
            "Saves the program", 
            "Private", 
            None, 
            self.saveProgram)
        self.save_button.show()
##        self.toolbara.append_space()
##        
        #Load Button
        self.load_button = self.toolbarb.append_item(
            "Load\na\nprogram", 
            "Loads a program", 
            "Private", 
            None, 
            self.loadProgram)
        self.load_button.show()
##        self.toolbara.append_space()
##        
##        #Start Button
        self.start_button = self.toolbarb.append_item(
            "Run\nthe\nprogram", 
            "Runs the current program", 
            "Private", 
            None, 
            self.startRunProgram)
        self.start_button.show()
##        self.toolbara.append_space()
##        
##        #Populate secondary toolbar
##        #Left button
        self.left_button = self.toolbarb.append_item(
            "Left", 
            "Inserts a Move Left command",
            "Private", 
            self.left_icon, 
            self.moveleftCode)
        self.left_button.show()
##        self.toolbarb.append_space()
##        
##        #Right button
        self.right_button = self.toolbarb.append_item(
            "Right", 
            "Inserts a Move Right command", 
            "Private", 
            self.right_icon, 
            self.moverightCode)
        self.right_button.show()
##        self.toolbarb.append_space()
##        
##        #Rotate button
        self.rotate_button = self.toolbarb.append_item(
            "Rotate", 
            "Inserts a Rotate command", 
            "Private", 
            self.flip_icon, 
            self.rotateCode)
        self.rotate_button.show()
##        self.toolbarb.append_space()
##        
##        #Release button
        self.release_button = self.toolbarb.append_item(
            "Release", 
            "Drops the cup", 
            "Private", 
            self.down_icon, 
            self.releaseCode)
        self.release_button.show()
##        self.toolbarb.append_space()
##
##        #Undo button
        self.undo_button = self.toolbarb.append_item(
            "Undo", 
            "Undo last action", 
            "Private", 
            None, 
            self.undoCode)
        self.undo_button.show()
##        self.toolbarb.append_space()
##
##        
##        #Clear button
        self.clear_button = self.toolbarb.append_item(
            "Clear", 
            "Clear", 
            "Private", 
            None, 
            self.clearCode)
        self.clear_button.show
##        self.toolbarb.append_space()
        print "createPrgrm4"

        self.table = gtk.Table(10, 10, True)
        self.swin=gtk.ScrolledWindow()
      
        self.swin.set_size_request(750,750)
   
        self.swin.add_with_viewport(self.table)
        self.table.show()
 
        self.fix.put(self.swin, 0,100)
        self.swin.show()
#
        self.fix.show()
        
        self.set_canvas(self.fix)
        print "createPrgrm6"

########################################################################
#######################################################################
########################################################################
##
    def runProgram(self, widget, data = None):
##
        print "runprgrm2"  
##        self.fix.remove(self.sandbox_button)
##        self.fix.remove(self.create_button)
#
        self.fix = gtk.Layout()
 

##        
####        #Create Secondary Toolbar
## 
        self.toolbarb.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        self.toolbarb.set_style(gtk.TOOLBAR_BOTH)
        self.toolbarb.set_border_width(5)
        self.fix.put(self.toolbarb, 0, 0)
        self.toolbarb.show()

##
        print "runprgrm3"   
##        #Startwindow button
        self.startwindow_button = self.toolbarb.append_item(
            "Start\nwindow", 
            "Come back to start window", 
            "Private", 
            None, 
            self.startwindow)
        self.startwindow_button.show()
##        self.toolbarb.append_space()
##        
##   
##        #Display_code button
        self.createwindow_button = self.toolbarb.append_item(
            "Display\na\nprogram", 
            "Shows the current program", 
            "Private", 
            None, 
            self.createwindow)
        self.createwindow_button.show()
##        self.toolbarb.append_space()
##        
##        #Populate secondary toolbar
## 
        #Changecolor button
        self.changecolor_button = self.toolbarb.append_item(
            "Change\ncups'\ncolor", 
            "Change cups' color", 
            "Private", 
            None, 
            self.changecolorRun)
        self.changecolor_button.show()
##        self.toolbarb.append_space()
##
##        #Colorfulcups button
        self.colorfulcups_button = self.toolbarb.append_item(
            "Make\ncups\ncolorful", 
            "Make cups colorful", 
            "Private", 
            None, 
            self.makeCupsColorfulRun)
        self.colorfulcups_button.show()
        print "runprgrm4"
##        self.toolbarb.append_space()
##
        self.bottom_image = gtk.Image()
        self.bottom_image.set_from_file("bottom.svg") 
##
        print "runprgrm5"  
        self.bottom = 400        
        self.cupwidth = 32
        self.cupheight = 43        
        self.fix.put(self.bottom_image,0, self.bottom)        
        self.bottom_image.show()
        
        self.set_canvas(self.fix)
##        self.swin.show()
        self.fix.show()

        self.x = 0
        self.y = 100
        self.top = 100

        
        self.xx=[]
        self.imagelist=[]

 
        if self.fname == None:
            if len(com)>0:
                self.saveProgram(self)
        else:        
            f=open(self.fname,'r')
        
            com = f.readlines()

        print "runrgrm8"  
##        
## #       print com
        if len(com)>0:
            for i in com[0]:  
#                print "Command is ", i
                if i == 'd':
                    self.releaseRun(self)
                elif i == 'r':
                    self.moverightRun(self)
                elif i == 'l':
                    self.moveleftRun(self)
                elif i == 'f':
                    self.rotateRun(self)
        else:
            self.createwindow(self)
        print "runprgrm9"
        return False
####            
##                
############################################################################                
#       
##    def restartgame(self, widget, data=None):
##        self.startwindow(self, widget)
##############################################################################
  
################################################################################        
    def startRunProgram(self, widget, data=None):
         
        self.saveCode(self)
            
        self.startwindow(self)
        self.runProgram(self)
        
        
        
        
        
#############################################################################        
    def saveCode(self,widget,data=None):
        if self.fname == None:
            self.saveProgram(self)
        else:
            if  len(self.codeimages)>0:
                f = open(self.fname,'w+')
                for i in range(0,len(self.codeimages)):
                    f.write(self.codeimages[i][5])
                f.close()
            else:
                f = open(self.fname,'w')
            
                parent = None
                md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "Create a program to save or run")

                c = md.run()
                if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                    c= gtk.RESPONSE_CLOSE
                md.destroy()
                f.close()
                self.createwindow(self)
        return True
#################################################################################
    def saveProgram(self, widget, data = None):
      
        if len(self.codeimages)>0:
            dialog=gtk.FileChooserDialog(title="Save a File", action=gtk.FILE_CHOOSER_ACTION_SAVE,\
                                     buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK))


            filter_text = gtk.FileFilter()
            filter_text.set_name("Text files")
            filter_text.add_mime_type("text/txt")
            filter_text.add_pattern("*.txt")
            dialog.add_filter(filter_text)

    
            self.fname=None
    
      
    
            response = dialog.run()
            
            if response == gtk.RESPONSE_OK:
                self.fname = os.path.join(self.get_activity_root(),dialog.get_filename())
  
            elif response == gtk.RESPONSE_CANCEL or response == gtk.RESPONSE_NONE:
 #               print 'Cancel Clicked'
                pass
            dialog.destroy()
    
            if self.fname != None:
                self.saveCode(self)
        
            print "File Saved: ", self.fname
        else:
            
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "Create a program to save or run")
            c= md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            md.destroy()
            
            self.createwindow(self)
        return 1
     

            
##
##            
#################################################################################                
##            
    def loadProgram(self, widget,  data=None):
        if self.fname != None:
            f=open(self.fname, 'r')
            f.close()
             
        self.clearCode(self)
        dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter_text = gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/txt")
        filter_text.add_pattern("*.txt")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            print dialog.get_filename(), 'selected'
            self.fname = dialog.get_filename()
  #          self.window.set_title("Blue Cup Robot    " +self.fname )
            dialog.destroy()
            self.loadCode(self)
        elif response == gtk.RESPONSE_CANCEL or response == gtk.RESPONSE_NONE:
            pass
        dialog.destroy()
              
##        
##    
##
########################################################################
    def createwindow(self, widget, data=None):
        self.startwindow(self)
        self.createProgram(self)
        self.loadCode(self)
##
#########################################################################        
##        
    def startProgram(self, widget, data=None):
        self.startwindow(self,widget)
        return False
##    
########################################################################
##    
##    def quitgame(self, widget, event, data=None):
##        gtk.main_quit()
##        return False
##
##    
######################################################################
#######################################################################
############################################################################
    def startwindow(self, widget, data=None):
        
#        self.clear(self)
        self.fix.remove(self.toolbarb)
        self.fix.remove(self.swin)
        self.fix.remove(self.table)
        self.fix.remove(self.swin)
        self.fix.remove(self.bottom_image)
 
        
   
 #       self.vbox = gtk.VBox(False, 0)
        
        self.sandbox_button = gtk.Button("Play around")
        self.sandbox_button.set_size_request(500, 120)
        self.create_button = gtk.Button("Create a program")
        self.create_button.set_size_request(500, 120)


        self.fix = gtk.Layout()

        self.fix.put(self.sandbox_button, 150, 80)
        self.fix.put(self.create_button, 150, 240)


        self.sandbox_button.connect("button-release-event", self.startSandbox)
        self.create_button.connect("button-release-event", self.createProgram)
#       self.run_button.connect("button-release-event", self.runProgram)
 
   
        

        #Create image for buttons
        self.left_icon = gtk.Image()
        self.right_icon = gtk.Image()
        self.down_icon = gtk.Image()
        self.flip_icon = gtk.Image()
        
        #Create Main Toolbar
#        self.toolbara = gtk.Toolbar()
##        #Create Secondary Toolbar
        self.toolbarb = gtk.Toolbar()
 
##        #Close Button
        self.close_button = gtk.Button()
##        
##        #Restart Button
        self.restart_button = gtk.Button()
##        #Save Button
        self.save_button = gtk.Button()
##        
##        #Load Button
        self.load_button = gtk.Button()
##        
##        #Start Button
        self.start_button = gtk.Button()
##        
##        #Populate secondary toolbar
##        #Left button
        self.left_button = gtk.Button()
##        
##        #Right button
        self.right_button = gtk.Button()
##        
##        #Rotate button
        self.rotate_button = gtk.Button()
##        
##        #Release button
        self.release_button = gtk.Button()
##
##        #Undo button
        self.undo_button = gtk.Button()
##        
##        #Clear button
        self.clear_button = gtk.Button()
##        
##        #Changecolor button
        self.changecolor_button = gtk.Button()

         #Start_window button
        self.startwindow_button = gtk.Button()
        
        self.table = gtk.Table(10, 12, True)


## 
##        self.swin = gtk.ScrolledWindow()
##       

        self.codeimages=[]
        self.l=0  ## counter for images left_icon
        self.i=0  ## counter for images right_icon
        self.m=0 ##counter for images flip_icon
        self.n=0 ##counter for images down_icon
        self.r=0   ## indices to fill up the table 
        self.k=0

        self.create_button.show()
        self.sandbox_button.show()
        
        #Attach VBox
        self.set_canvas(self.fix)
        self.fix.show()
  
        self.color = "blue"
        self.colors = ("blue","olive","green","maroon","purple","yellow")
        
        self.colors_option = []
        

        self.imagecount = 0
        self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
        self.traceline_imagecount = gtk.image_new_from_file("traceline.svg")
        self.up=False
        
        self.bottom = 400        
        self.cupwidth = 32
        self.cupheight = 43        
  
 #       self.vbox.pack_start(self.fix)
   
 #       self.swin.show()
#        self.vbox.show()
        self.x = 0
        self.y = 70
        self.ty = self.y + self.cupheight 

        self.xx=[]
        self.imagelist=[]
        
##   
#############################################################################
##        
    def changecolor(self, widget, data=None):
  
        color_options = (x for x in self.colors if x != self.color)
        self.colors_option = list(color_options)
        i=random.randint(0, len(self.colors_option)-1)
        
        self.color = self.colors_option[i]
  
        if len(self.imagelist)>0:
            for i in range(0,len(self.imagelist)):
                if   self.xx[i][2]:
                    pass
                else:
                    self.imagelist[i].clear()

                    
                    if self.xx[i][3]:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageUp[self.color])
                    else:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageDown[self.color])
                    self.fix.put(self.imagelist[i], self.xx[i][0][0], self.xx[i][1]) 
                    self.imagelist[i].show()
        self.image_imagecount.clear()
        if self.up ==True:
            self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.color])
        else:
            self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
        self.fix.put(self.image_imagecount, self.x, self.y)
        self.image_imagecount.show()
        
##########################################################################
##
    def changecolorRun(self, widget, data=None):
        
        color_options = (x for x in self.colors if x != self.color)
        self.colors_option = list(color_options)
        i=random.randint(0, len(self.colors_option)-1)
        
        self.color = self.colors_option[i]
  
        if len(self.imagelist)>0:
            for i in range(0,len(self.imagelist)):
                if   self.xx[i][2]:
                    pass
                else:
                    self.imagelist[i].clear()

                    
                    if self.xx[i][3]:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageUp[self.color])
                    else:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageDown[self.color])
                    self.fix.put(self.imagelist[i], self.xx[i][0][0], self.xx[i][1]) 
                    self.imagelist[i].show()
        if self.x == 0 :
            pass
        else:
            self.image_imagecount.clear()
            if self.up ==True:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.color])
            else:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
            self.fix.put(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()
##
######################################################################################
    def makeCupsColorful(self, widget, data=None):
        k=random.randint(0, len(self.colors)-1)
        
        
  
        if len(self.imagelist)>0:
            for i in range(0,len(self.imagelist)):
                k=random.randint(0, len(self.colors)-1)
                
                if   self.xx[i][2]:
                    pass
                else:
                    self.imagelist[i].clear()

                    
                    if self.xx[i][3]:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageUp[self.colors[k]])
                    else:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageDown[self.colors[k]])
                    self.fix.put(self.imagelist[i], self.xx[i][0][0], self.xx[i][1]) 
                    self.imagelist[i].show()
        
            
            self.image_imagecount.clear()
            
            self.imagecount+=1
            if self.up ==True:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.colors[k]])
            else:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.colors[k]])
            
            self.fix.put(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()

        
       
##        
## ####################################################################################
    def makeCupsColorfulRun(self, widget, data=None):
        k=random.randint(0, len(self.colors)-1)
        
        
  
        if len(self.imagelist)>0:
            for i in range(0,len(self.imagelist)):
                k=random.randint(0, len(self.colors)-1)
                
                if   self.xx[i][2]:
                    pass
                else:
                    self.imagelist[i].clear()

                    
                    if self.xx[i][3]:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageUp[self.colors[k]])
                    else:
                        self.imagelist[i]=gtk.image_new_from_file(self.color_imageDown[self.colors[k]])
                    self.fix.put(self.imagelist[i], self.xx[i][0][0], self.xx[i][1]) 
                    self.imagelist[i].show()
        if self.x == 0 :
            pass
        else:
            
            self.image_imagecount.clear()
            
            self.imagecount+=1
            if self.up ==True:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.colors[k]])
            else:
                self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.colors[k]])
            self.fix.put(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()

        
##       
##        
##
##
#######################################################################################            
##        
    def undo(self, widget, data=None):

#        print id(self.imagelist[len(self.imagelist)-1])
#        print id(self.imagelist[0])
        if len(self.imagelist)>0:
            if self.x == 0:
                self.imagelist[len(self.imagelist)-1].clear()
                self.imagelist.remove(self.imagelist[len(self.imagelist)-1])
                self.xx.remove(self.xx[len(self.xx)-1])
                i= len(self.codeimages)-1
                undo_row = self.codeimages[len(self.codeimages)-1][3]
                while self.codeimages[i][3] == undo_row and i>=0:
 
                    self.table.remove(self.codeimages[i][0])
                    self.codeimages.remove(self.codeimages[i])
                    if i>0:
                        i=i-1
                    else:
                        break

            
                self.r =self.r- 1
            else:
                parent = None
                md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "Use left and right buttons")
                md.run()
                md.destroy()
                
        else:
             parent = None
             md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "Use left and right buttons")
             c = md.run()
             if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                 c= gtk.RESPONSE_CLOSE
             
             md.destroy()
##       
## #########################################################################           
##
    def clear(self, widget, data=None):

        if self.x != 0:
            self.x = 0
            self.y = 70
            self.fix.move(self.image_imagecount, self.x, self.y)
            self.fix.move(self.traceline_imagecount, self.x, self.ty)
            
        if len(self.xx)>0:
            
            for i in range(0, len(self.xx)):
                self.imagelist[i].clear()
            self.xx[:]=[]
            self.imagelist[:] = []
        if len(self.codeimages)>0:
            for i in range(0,len(self.codeimages)):
                self.codeimages[i][0].clear()
            self.codeimages[:] = []
            self.r = 0
            self.k = 0
            self.l=0  ## counter for images left_icon
            self.i=0  ## counter for images right_icon
            self.m=0 ##counter for images flip_icon
            self.n=0 ##counter for images down_icon
            
################################################################################
##            
    def undoCode(self,widget,data=None):
        if len(self.codeimages)>0:
            self.codeimages[len(self.codeimages)-1][0].clear()
            
            self.k = self.codeimages[len(self.codeimages)-1][1]
            self.r = self.codeimages[len(self.codeimages)-1][3]
            self.codeimages.remove(self.codeimages[len(self.codeimages)-1])
           
##            
##############################################################################
##                
    def clearCode(self, widget, data = None):
        if len(self.codeimages)>0:
            for i in range(0,len(self.codeimages)):
                self.codeimages[i][0].clear()
            self.codeimages[:] = []
            self.r = 0
            self.k = 0
            self.l=0  ## counter for images left_icon
            self.i=0  ## counter for images right_icon
            self.m=0 ##counter for images flip_icon
            self.n=0 ##counter for images down_icon
        
##
#############################################################################            
##        
    def moveleft(self, widget):
 
       
        if self.x >= self.cupwidth/2:
 #           self.fill_table("left_button")
            self.fill_table_1("left_button")
            self.x = self.x - self.cupwidth/2
            self.fix.move(self.image_imagecount, self.x, self.y)
            self.fix.move(self.traceline_imagecount, self.x, self.ty)
            self.image_imagecount.show()
            self.traceline_imagecount.show()
        else:
            self.x = 0
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move left")
            c = md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            while c != gtk.RESPONSE_CLOSE:
                md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move left")
                md.run()
            
            md.destroy()
##
#############################################################################
##
    def moveleftRun(self,widget, data=None):
 
        if self.x >= self.cupwidth/2:
            self.x = self.x - self.cupwidth/2
            self.fix.put(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()            
        else:
            self.x = 0
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move left\n Edit the program")
            c=md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            md.destroy()
#            createProgram()
##
#############################################################################    
##        
    def moveright(self, widget):

        if self.x < 500:
            self.x = self.x + self.cupwidth/2
            self.fix.move(self.image_imagecount, self.x, self.y)
            self.fix.move(self.traceline_imagecount, self.x, self.ty)
 #           self.fill_table("right_button")
            self.fill_table_1("right_button")
            self.image_imagecount.show()
            self.traceline_imagecount.show()
        else:
            self.x = 500
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move right")
            c = md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            while c != gtk.RESPONSE_CLOSE:
                md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move right")
                md.run()
            md.destroy()
##############################################################################
##            
    def moverightCode(self, widget, data = None):
        self.fill_tableCode("right_button")
        
################################################################################
##
    def moverightRun(self, widget, data=None):
 
        if self.x < 500:
            self.x = self.x + self.cupwidth/2
            self.fix.put(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()
        else:
            self.x = 500
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't move right\nEdit the program")
            c=md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            md.destroy()
#            createProgram(self)
##################################################################################
##
    def rotate(self, widget, data=None):
        self.image_imagecount.clear()
        
        self.imagecount=self.imagecount+1
        if self.up == False:
            self.up = True
            self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.color]) 
            
        else:
            self.up = False 
            self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
                                              
#        self.fill_table("rotate_button")
        self.fill_table_1("rotate_button")
        self.fix.put(self.image_imagecount, self.x, self.y)
        self.image_imagecount.show()
##########################################################################################
##        
    def rotateCode(self, widget, data = None):
        self.fill_tableCode("rotate_button")
##
##########################################################################################
##
    def rotateRun(self, widget, data=None):
 
        self.image_imagecount.clear()
        
        self.imagecount=self.imagecount+1
        if self.up == False:
            self.up = True
            self.image_imagecount = gtk.image_new_from_file(self.color_imageUp[self.color]) 
            
        else:
            self.up = False 
            self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
                                              
        
        self.fix.put(self.image_imagecount, self.x, self.y)
        self.image_imagecount.show()
##        
##########################################################################################
##        
    def moveleftCode(self, widget, data = None):
        self.fill_tableCode("left_button")

###########################################################################################
        
    def repaint_red(self):
       
        self.image_imagecount.clear()
        self.imagecount=self.imagecount+1
        if self.up:
            self.image_imagecount = gtk.image_new_from_file("redCupUp1.svg")
        else:
            self.image_imagecount = gtk.image_new_from_file("redCupDown1.svg") 
        self.image_imagecount.show()        
############################################################################################                                             
##
##            
##        
    def release(self, widget, data=None):
        self.traceline_imagecount.clear()
        b=[]
        h=[]
        r=[]
  
        a=range(self.x, self.x+self.cupwidth)
#        print "a of image",self.imagecount, "is ", a
        red = False
        if len(self.xx) > 0:
            for i in range(0,len(self.xx)):
                for n in range(0,len(self.xx[i][0])):
 #               print "self.xx[i][0]=",self.xx[i][0]                   
                    if a[n] in self.xx[i][0]:
                        
                        if len(h)>0 and self.xx[i][1]< min(h):
                            b[:]=[]
                        h.append(self.xx[i][1])
                        b.append(a[n])
                        
                        r.append(self.xx[i][2])
                        
            if len(b)>0:
                self.y = min(h) - self.cupheight
                
 #               print "min(h)=",min(h),"self.y=",self.y
                for i in r:
                    if i:
                        red= True
                              
            else:            
                self.y = self.bottom - self.cupheight
        else:
            self.y = self.bottom - self.cupheight
        
        b = list(set(b))

        if 0 < len(b) <= self.cupwidth/2:
            red = True
            self.repaint_red()
        if red:
            self.repaint_red()
            

        if  self.y > 3*self.cupheight:
  
            self.fix.put(self.image_imagecount, self.x, self.y)
        
        
            self.image_imagecount.show()
        

#        print "self.y =",self.y           
            self.fix.move(self.image_imagecount, self.x, self.y)
            self.image_imagecount.show()
            self.imagelist.append(self.image_imagecount)
            self.xx.append((a,self.y,red , self.up))
#            self.fill_table("release_button")
            self.fill_table_1("release_button")
#        self.xx.sort()
        else:
            

            self.image_imagecount.clear()
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't be released here")
            c = md.run()
            
            
            if c== gtk.RESPONSE_DELETE_EVENT or c==gtk.RESPONSE_NONE:
                c= gtk.RESPONSE_CLOSE
            if c==gtk.RESPONSE_NONE:
                gtk.BUTTONS_CLOSE.clicked()
            while c != gtk.RESPONSE_CLOSE:
                md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't be released here")
                md.run()
            
                
            if self.right_button.clicked():
                self.x = 0
                self.y = 70
                self.ty = self.y + self.cupheight
                self.up = False

                self.imagecount=self.imagecount+1
                self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
                self.traceline_imagecount = gtk.image_new_from_file("traceline.svg")
                self.fix.put(self.image_imagecount, self.x, self.y)
                self.fix.put(self.traceline_imagecount, self.x, self.ty)
                
                self.image_imagecount.show()
                self.traceline_imagecount.show()
                
            
                  
                
            md.destroy()
            
            if self.k > 0:
                i= len(self.codeimages)-1
                undo_row = self.codeimages[len(self.codeimages)-1][3]
                while self.codeimages[i][3] == undo_row and i>=0:
 
                    self.table.remove(self.codeimages[i][0])
                    self.codeimages.remove(self.codeimages[i])
                    if i>0:
                        i=i-1
                    else:
                        break

            
            self.k = 0
            
            
       
        
        self.x = 0
        self.y = 70
        self.ty = self.y + self.cupheight
        self.up = False

        self.imagecount=self.imagecount+1
        self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
        self.traceline_imagecount = gtk.image_new_from_file("traceline.svg")
        self.fix.put(self.image_imagecount, self.x, self.y)
        self.fix.put(self.traceline_imagecount, self.x, self.ty)
        
        self.image_imagecount.show()
        self.traceline_imagecount.show()
##        
########################################################################################
##        
    def releaseCode(self, widget, data=None):
        self.fill_tableCode("release_button")
##
########################################################################################
##
    def releaseRun(self, widget, data=None):
 

        b=[]
        h=[]
        r=[]

        a=range(self.x, self.x+self.cupwidth)
#        print "a of image",self.imagecount, "is ", a
        red = False
        if len(self.xx) > 0:
            for i in range(0,len(self.xx)):
                for n in range(0,len(self.xx[i][0])):
 #               print "self.xx[i][0]=",self.xx[i][0]                   
                    if a[n] in self.xx[i][0]:
                        
                        if len(h)>0 and self.xx[i][1]< min(h):
                            b[:]=[]
                        h.append(self.xx[i][1])
                        b.append(a[n])
                        
                        r.append(self.xx[i][2])
                        
            if len(b)>0:
                self.y = min(h) - self.cupheight
                
 #               print "min(h)=",min(h),"self.y=",self.y
                for i in r:
                    if i:
                        red= True
                              
            else:            
                self.y = self.bottom - self.cupheight
        else:
            self.y = self.bottom - self.cupheight
        
        b = list(set(b))

        if 0 < len(b) <= self.cupwidth/2:
            red = True
            self.repaint_red()
        if red:
            self.repaint_red()
            

        if  self.y > 3*self.cupheight:
  
            self.fix.put(self.image_imagecount, self.x, self.y)
        
        
            self.image_imagecount.show()
        

#        print "self.y =",self.y           
            self.fix.move(self.image_imagecount, self.x, self.y)
            self.imagelist.append(self.image_imagecount)
            self.xx.append((a,self.y,red , self.up))
            
#        self.xx.sort()
        else:
            

            self.image_imagecount.clear()
            
            
            parent = None
            md = gtk.MessageDialog(parent,gtk.DIALOG_DESTROY_WITH_PARENT,\
                                   gtk.MESSAGE_INFO,gtk.BUTTONS_CLOSE,\
                                   "The cup can't be released here\nEdit your program")
            c=md.run()
            if c== gtk.RESPONSE_NONE or c== gtk.RESPONSE_DELETE_EVENT:
                c= gtk.RESPONSE_CLOSE
            md.destroy()
            
       
        
        self.x = 0
        self.y = 100
#        self.ty = self.y + self.cupheight
        self.up = False

        self.imagecount=self.imagecount+1
        self.image_imagecount = gtk.image_new_from_file(self.color_imageDown[self.color])
 
        
        self.image_imagecount.show()
 #       self.traceline_imagecount.show()
##
#################################################################################################    
    def fill_table(self,button):
 
        left_icon_l=gtk.image_new_from_file("arrowLeft.svg")
        self.l=self.l+1
 
        right_icon_i=gtk.image_new_from_file("arrowRight.svg")
        self.i=self.i+1

        
        flip_icon_m=gtk.image_new_from_file("turnLeft90.svg")
        self.m=self.m+1
        down_icon_n=gtk.image_new_from_file("arrowDown.svg")
        self.n=self.n+1

        symbols = {"release_button":down_icon_n, "right_button":right_icon_i,"left_button":left_icon_l,"rotate_button":flip_icon_m }

  
        if self.x == 0 and button =="left_button":
            pass
        elif button == "right_button" and self.x >= 500:
            pass

        else:
            self.table.attach(symbols[button],self.k, self.k+2, self.r,\
                              self.r+2,xoptions=gtk.FILL,yoptions=gtk.FILL,xpadding = 0,ypadding=0)
            self.codeimages.append((symbols[button],self.k, self.k+2, self.r,self.r+2))
#            self.r = self.r + 1
        if button == "release_button" :
  
            self.r = self.r+1
            self.k = 0
        elif button == "left_button" and self.x == 0: 
            pass
        elif button == "right_button" and self.x >= 500:
            pass
        
        
        else:
            self.k = self.k + 1
        if button == "undo_button":
            self.r = self.r - 1 
        symbols[button].show()
        symbols[button].set_visible(True)
        symbols[button].show()
        self.table.show()
        self.swin.show()
        self.fix.show()

###########################################################################################
###########################################################################################
    def fill_table_1(self,button):
        
        left_icons = ("arrowLeft.svg","arrowLeftRed.svg","arrowLeftYellow.svg","arrowLeftLime.svg","arrowLeftFuchsia.svg","arrowLeftAqua.svg")
        right_icons = ("arrowRight.svg","arrowRightRed.svg","arrowRightYellow.svg", "arrowRightLime.svg","arrowRightFuchsia.svg","arrowLeftAqua.svg")
        flip_icons = ("turnLeft90.svg","turnLeft90Red.svg","turnLeft90Yellow.svg", "turnLeft90Lime.svg","turnLeft90Fuchsia.svg","turnLeft90Aqua.svg")
        down_icons = ("arrowDown.svg","arrowDownRed.svg","arrowDownYellow.svg","arrowDownLime.svg","arrowDownFuchsia.svg","arrowDownAqua.svg")
        arrow_colors = ("orange","red","yellow","lime","fuchsia","aqua")
        
        
        left_icon_l=gtk.image_new_from_file(left_icons[self.ar_col])
        self.l=self.l+1 
        right_icon_i=gtk.image_new_from_file(right_icons[self.ar_col])
        self.i=self.i+1        
        flip_icon_m=gtk.image_new_from_file(flip_icons[self.ar_col])
        self.m=self.m+1
        down_icon_n=gtk.image_new_from_file(down_icons[self.ar_col])
        self.n=self.n+1
        
       

        symbols = {"release_button":down_icon_n, "right_button":right_icon_i,"left_button":left_icon_l,"rotate_button":flip_icon_m }

  
        if self.x == 0 and button =="left_button":
            pass
        elif button == "right_button" and self.x >= 500:
            pass

        else:
            self.table.attach(symbols[button],self.k, self.k+2, self.r,\
                              self.r+2,xoptions=gtk.FILL,yoptions=gtk.FILL,xpadding = 0,ypadding=0)
            self.codeimages.append((symbols[button],self.k, self.k+2, self.r,self.r+2))
#            self.r = self.r + 1
        if button == "release_button" :
             
            self.r = self.r+1
            self.k = 0
            arrow_color_options = (x for x in arrow_colors if x != self.arrow_color)
            arrow_colors_option = list(arrow_color_options)
            self.ar_col=random.randint(0, len(arrow_colors_option)-1)
            self.arrow_color = arrow_colors_option[self.ar_col]
        
          
        elif button == "left_button" and self.x == 0: 
            pass
        elif button == "right_button" and self.x >= 500:
            pass
        
        
        else:
            self.k = self.k + 1
        if button == "undo_button":
            self.r = self.r - 1 
        symbols[button].show()
        symbols[button].set_visible(True)
        symbols[button].show()
        self.table.show()
        self.swin.show()
        self.fix.show()

###########################################################################################
###########################################################################################
        
    def fill_tableCode(self,button):
        left_icons = ("arrowLeft.svg","arrowLeftRed.svg","arrowLeftYellow.svg","arrowLeftLime.svg","arrowLeftFuchsia.svg","arrowLeftAqua.svg")
        right_icons = ("arrowRight.svg","arrowRightRed.svg","arrowRightYellow.svg", "arrowRightLime.svg","arrowRightFuchsia.svg","arrowLeftAqua.svg")
        flip_icons = ("turnLeft90.svg","turnLeft90Red.svg","turnLeft90Yellow.svg", "turnLeft90Lime.svg","turnLeft90Fuchsia.svg","turnLeft90Aqua.svg")
        down_icons = ("arrowDown.svg","arrowDownRed.svg","arrowDownYellow.svg","arrowDownLime.svg","arrowDownFuchsia.svg","arrowDownAqua.svg")
        arrow_colors = ("orange","red","yellow","lime","fuchsia","aqua")
        
        
        left_icon_l=gtk.image_new_from_file(left_icons[self.ar_col])
        self.l=self.l+1 
        right_icon_i=gtk.image_new_from_file(right_icons[self.ar_col])
        self.i=self.i+1        
        flip_icon_m=gtk.image_new_from_file(flip_icons[self.ar_col])
        self.m=self.m+1
        down_icon_n=gtk.image_new_from_file(down_icons[self.ar_col])
        self.n=self.n+1

        
        symbols = {"release_button":down_icon_n, "right_button":right_icon_i,"left_button":left_icon_l,"rotate_button":flip_icon_m }

        symbol_write = {"release_button":"d", "right_button":"r", "left_button":"l","rotate_button":"f" }
 
        self.table.attach(symbols[button],self.k, self.k+2, self.r,\
                              self.r+2,xoptions=gtk.FILL,yoptions=gtk.FILL,xpadding = 0,ypadding=0)
        
        self.codeimages.append((symbols[button],self.k, self.k+2, self.r,self.r+2,symbol_write[button]))
        
      
#            self.r = self.r + 1
        if button == "release_button" :
  
            self.r = self.r+1
            self.k = 0
            arrow_color_options = (x for x in arrow_colors if x != self.arrow_color)
            arrow_colors_option = list(arrow_color_options)
            self.ar_col=random.randint(0, len(arrow_colors_option)-1)
            self.arrow_color = arrow_colors_option[self.ar_col]
        
        else:
            self.k = self.k + 1
        
        symbols[button].show()
        self.table.show()
##        self.swin.show()
        self.fix.show()
##
###############################################################################
##   
    def loadCode(self, widget, data=None):
        if self.fname != None:
            f = open(self.fname, 'r')
##            f.close
        
        

        
            com = f.readlines()
            if len(com)>0:
                for i in com[0]:
                    self.fill_tableCode (self.symbol_load[i])
            f.close()
        return False
##
##################################################################################
##
####    def keypress(self,widget,event):
####        "Respond when the user presses one of the arrow keys"
#####        keymap = gtk.gdk.keymap_get_default()
#####        keyname = gtk.gdk.keyval_name(event.keyval)
####        keyname = gtk.gdk.keyval_name(event.keyval)
####        if keyname == "Right":
####            self.moveright(self)
####            print "Moving right"
#### #           return True
####        if keyname == "Left":
####            self.moveleft(self)
####            print "Moving left"
#### #           return True
####        if keyname == "Down" :
####            self.release(self)
####            print "Moving down"
#### #       return False
#########################################################################################
####    def keypressCode(self, widget, event):
####        "Respond when the user presses one of the arrow keys"
####        keyname = gtk.gdk.keyval_name(event.keyval)
####        if keyname == 'Right':
####            self.moverightCode()
####            return True
####        if keyname == 'Left':
####            self.moveleftCode()
####            return True
####        if keyname == 'Down' :
####            self.releaseCode()
####        return False
##############################################################################################
####
####    def keypressRun(self, widget, event):
####        "Respond when the user presses one of the arrow keys"
####        gtk.gdk.keymap_get_default()
####        keyname = gtk.gdk.keyval_name(event.keyval)
####        if keyname == 'Right':
####            self.moverightRun()
####            return True
####        if keyname == 'Left':
####            self.moveleftRun()
####            return True
####        if keyname == 'Down' :
####            self.releaseRun()
####            return True
####        return False
####       
####

