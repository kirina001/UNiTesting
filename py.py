import os
i=0
while True:
    
    #write

    f = open('test69.txt', 'a')
    f.write(".")

    #Add
    os.system('git add .')
    os.system('git commit -m "69"')
    i=i+69
    print(str(i)+':commits')
