import easygui

a = easygui.buttonbox("Who are you?",
                 choices = ['God','pig','people'])
while a == 'God' or a == 'people':
    easygui.msgbox ("you are not right!")
    a = easygui.buttonbox("Who are you?",
                 choices = ['God','pig','people'])
b = easygui.buttonbox("How do you look like?",
                 choices = ['beautiful','clever','stupid'])
while b == 'clever' or b == 'beautiful':
    easygui.msgbox ("you are not right!")
    b = easygui.buttonbox("How do you look like?",
                 choices = ['beautiful','clever','stupid'])
easygui.msgbox ("you are a " + b + a)