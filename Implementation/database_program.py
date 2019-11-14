from guizero import *

app = App(title="Test", width=250, height=300)

def createname():
    colorval = colortxt.value
    adjval = adjbutton.value
    animval = animalcombo.value
    ageval = ageslide.value
    if ageval == 1:
        ageval = 'The First'
    if ageval == 2:
        ageval = 'The Second'
    if ageval == 3:
        ageval = 'The Third'
    updateout.value = "Your hero is: " + adjval + ' ' + colorval + ' ' + animval + ' ' + ageval
    if darkmode.value == True:
        app.bgcolor('darkgrey')
    else:
        app.bgcolor('white')
        
def dark():
    print('this button works')


#Picture(app, image='apple.png')
darkmode = CheckBox(app, text='DarkMode', command=dark)
adjmsg = Text(app, text='Select your adjective')
adjbutton = ButtonGroup(app, options=['Nice', 'good'])
colourmsg = Text(app, text="Type your color")
colortxt = TextBox(app, text='')
animalmsg = Text(app, text='Select your animal')
animalcombo = Combo(app, options=['Dragon', 'Dog', 'Cat'])
ageslide = Slider(app, start=1, end=3)


#button to update whole app
finish = PushButton(app, text ='Push to Update', command=createname)
updateout = Text(app, text='Your color will appear here: ')

app.display()
