from bs4 import BeautifulSoup
import requests 

#pulls html source code for powerballs front page
html = requests.get("http://www.powerball.com/").text
soup = BeautifulSoup(html, 'html5lib')

winnings = [0,0,0,0,0,0]
#pulls the span tags with the white ball and the power ball numbers
winning1 = soup('span', {'class':'white ball '})
winning2 = soup('span', {'class':'red ball '})

x = 0
for i in winning1:
    #gets just the data in the tags for the white balls
    winnings[x] = int(''.join(i.find_all(text=True)))
    x = x+1
#gets just the data in the tags for the powerball number
winnings[5] = int(''.join(winning2[0].find_all(text=True)))

#our ticket numbers
tickets = {
'ticket 1' : {
    'row 1' : [2,4,6,24,34,25],
    'row 2' : [14,41,48,54,61,2],
    'row 3' : [16,22,55,58,64,4],
    'row 4' : [35,39,52,60,66,26],
    'row 5' : [3,46,48,50,63,2],
    'row 6' : [13,15,16,52,62,6],
    'row 7' : [13,20,24,34,57,26],
    'row 8' : [16,31,34,60,62,8],
    'row 9' : [6,11,23,44,52,26],
    'row 10' : [32,39,45,58,59,23]
},

'ticket 2': {
    'row 1' : [25,41,51,63,65,4],
    'row 2' : [22,24,33,57,65,6],
    'row 3' : [14,39,46,58,66,22],
    'row 4' : [9,28,30,45,67,7],
    'row 5' : [8,22,27,42,56,1],
    'row 6' : [18,29,37,42,58,7],
    'row 7' : [28,29,33,45,48,20],
    'row 8' : [10,22,39,47,42,12],
    'row 9' : [28,31,48,55,58,7],
    'row 10' : [12,24,29,45,57,6]
},

'ticket 3' : {
    'row 1' : [7,26,39,50,56,17],
    'row 2' : [1,33,34,47,69,24],
    'row 3' : [24,45,46,49,61,20],
    'row 4' : [2,10,34,43,51,25],
    'row 5' : [3,26,38,51,69,6],
    'row 6' : [1,28,42,44,48,15],
    'row 7' : [16,20,24,49,55,4],
    'row 8' : [6,8,31,68,69,2],
    'row 9' : [15,46,55,58,65,7],
    'row 10' : [3,20,27,39,66,9]
},

'ticket 4' : {
    'row 1' : [22,27,38,63,67,12],
    'row 2' : [8,13,15,51,52,9],
    'row 3' : [8,10,16,42,55,2],
    'row 4' : [14,19,37,52,67,24],
    'row 5' : [11,13,26,38,65,18],
    'row 6' : [6,14,34,53,54,18],
    'row 7' : [10,13,43,48,53,20],
    'row 8' : [3,8,25,37,54,9],
    'row 9' : [25,28,34,53,66,19],
    'row 10' : [27,38,48,61,66,11] 
    

},

'ticket 5' :{
    'row 1' : [21,29,39,42,59,1],
    'row 2' : [15,20,50,60,68,12],
    'row 3' : [1,36,45,48,53,12],
    'row 4' : [12,24,36,39,41,12],
    'row 5' : [23,53,54,57,58,2],
    'row 6' : [4,13,16,18,51,14],
    'row 7' : [4,11,12,33,35,13],
    'row 8' : [19,24,54,56,66,19],
    'row 9' : [5,24,34,45,61,11],
    'row 10' : [13,35,46,54,64,3]
},
}

#winning = raw_input('Enter winning numbers as a comma separated list: ')
#winning = winning.split(',')
#winning = [int(x) for x in winning]
#winning = [4,8,19,27,34,10]

#This loop checks each ticket against most current winning numbers on 
#powerballs front page to see if we won anything. Returns info on the
#tickets that have winning numbers and the sum of all non Jackpot winnings
sum = 0
for i in tickets:
    for j in tickets[i]:
        counter = 0
        powerball = False
        #check for powerball win
        if tickets[i][j][-1] == winning[-1]:
            powerball = True
        #check how many numbers we got
        for k in tickets[i][j][:-1]:
            if k in winning[:-1]:
                counter = counter + 1
        
        #5 numbers and powerball
        if (counter == 5) and (powerball == True):
            print i + ' ' + j + ' JACKPOT BITCHES'
        #5 numbers no powerball
        elif counter == 5:
            print i + ' ' + j + ' 1M JACKPOT BITCHES'
            sum = sum + 1000000
        #4 numbers and power ball
        elif (counter == 4) and (powerball == True):
            print i + ' ' + j + ' 50K JACKPOT BITCHES'
            sum = sum + 50000
        #4 numbers
        elif (counter == 4):
            print i + ' ' + j + ' $100 prize'
            sum = sum + 100
        #3 numbers and powerball
        elif (counter == 3) and (powerball == True):
            print i + ' ' + j + ' $100 prize'
            sum = sum + 100
        #3 numbers
        elif counter == 3:
            print i + ' ' + j + ' $7 prize'
            sum = sum + 7
        elif (counter == 2) and (powerball == True):
            print i + ' ' + j + ' $7 prize'
            sum = sum + 7
        #powerball
        elif (powerball == True):
            print i + ' ' + j + ' POWERBALL WINNER'
            sum = sum + 4
print 'Total Winnings: ' + str(sum)
winning = raw_input('Press Enter to exit.')