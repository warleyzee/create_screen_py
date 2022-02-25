import PySimpleGUI as sg
# sg.theme('DarkAmber')   # Add a little color to your windows




# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Name Submittal:', size=(15,1 )), sg.InputText()],
            [sg.Text('Submitall To:', size=(15,1 )), sg.InputText()],
            [sg.Text('Description:', size=(15,1 )), sg.InputText()],
            [sg.Text('Num Submittal:', size=(15,1 )), sg.InputText()],
            [sg.Text('Date Submittal:', size=(15,1 )), sg.InputText()],
            [sg.Text('Required By:', size=(15,1 )), sg.InputText()],
            [sg.Text('Infromation:', size=(15,1 )), sg.InputText()],
            [sg.In(key='input', size=(64,1 ))],
            [sg.FileBrowse(size=(10, 1), file_types=(("MIDI files", "*.pdf"),))],
            [sg.OK('OK'), sg.Cancel( )]]




# Create the Window
window = sg.Window('Create Submittal', layout)
win_confirm = False
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if not win_confirm and event == 'OK':
        win_confirm = True
        layout_confirm = [
            [sg.Text('Test:', size=(15,1 )), sg.InputText()],
            [sg.Text('Test 1:', size=(15,1 )), sg.InputText()],
            [sg.Button('Exit')]]

        win2 = sg.Window('Confirm', layout_confirm)
    
    if win_confirm:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
            win_confirm  = False
            win2.close()
      
# Close
window.close()