################################
# Your Name
# Your Section
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################
# Read the input.txt file
def read_input():
    f = open('input_7_cap1.txt', 'r')
    print(f.read())
    f.close()

def forwarder():
     return open('input_7_cap1.txt', 'r')

     
def calculate_score(file):
    scoreboard={'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7} 
    score=0
    for round in file:
        striper=round.strip()
        if striper in scoreboard:
          score+= scoreboard[striper]
    print("totalscore",score)

read_input()
calculate_score(forwarder())