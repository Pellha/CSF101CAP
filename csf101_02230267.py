################################
# Namgyel Pellha
# MECHANICAL ENGINEERING
# 02230267
################################
# REFERENCES
# https://youtu.be/LpZmZs2_BC4?feature=sharedm
# https://youtu.be/Uh2ebFW8OYM?feature=shared
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
################################
# SOLUTION
# Your Solution Score:50169
# Put your number here:7
################################
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