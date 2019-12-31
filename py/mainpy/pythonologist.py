# pythonologist.py
import random # random, random, random
import re # for commented part
from time import strftime, localtime # for phrase

lastSubject = 'your concern'
print('// type break twice to end // \n')
print('what is your concern? ')
subject = input('')
subject = str(subject)

if subject == '':
        subject = lastSubject

phrases = [
    'why are you asking this?', 'what does %s have to do with this?' %subject,
    'is this necessary?', 'have you asked your doctor about %s?' %subject,
    'so?', '%s is quite brief.' %subject, 'are you sure it is %s?' %subject,
    'what is your current situation about %s?' %subject,
    'are you sure you\'re not dreaming?', 'death is inevitable.',
    'it is already %s!' %strftime('%I:%M %p', localtime())
]

def ifs():
    global subject

    #if '__' in subject:
    #    print('I like %s too!' % re.sub('__', '', subject))

    if subject == '__koala42__':
        print('I like koalas too!')
        
    if subject == '':
        subject = lastSubject

ifs()
x = random.choice(phrases)

print('\n' + x)

while True:
    subject = input('')

    ifs()
    if subject == 'break break':
        break
        
    lastSubject = subject
    
    phrases[1] = 'what does %s have to do with this?' %subject
    phrases[3] = 'have you asked your doctor about %s?' %subject
    phrases[5] = '%s is quite brief.' %subject
    phrases[6] = 'are you sure it is %s?' %subject
    phrases[7] = 'what is your current situation about %s?' %subject
    phrases[9] = 'it is already %s!' %strftime('%I:%M %p', localtime())
    

    x = random.choice(phrases)

    print('\n' + x)
    lastChoice = x
