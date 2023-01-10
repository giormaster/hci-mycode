import random
import time
myscore = 0
comscore = 0
matchround = 0
print("Rock.. Paper.. Scissors")
print("Choose your option")
while myscore < 3 and comscore < 3:
	matchround += 1
	print("Round:", matchround)
	print("\n1)Rock\n2)Paper\n3)Scissors")
	choose = int(input())
	comchoose = random.randrange(1, 4)
#selection message
	if choose == 1:
		print("You choose rock")
	if choose == 2:
		print("Player choose paper")
	if choose == 3:
		print("Player choose scissors")
	if comchoose == 1:
		print("Advesery choose rock")
	if comchoose == 2:
 		print("Advesery choose paper")
	if comchoose == 3:
		print("Advesery choose scissors")
#selection over
	if choose == comchoose:
		print("Draw")
	#playerwins
	elif (choose == 1 and comchoose == 2) or (choose == 2 and comchoose == 3) or (choose == 3 and comchoose == 1):
		print("You Lost the round")
		comscore += 1
	elif (choose == 2 and comchoose == 1) or (choose == 1 and comchoose == 3) or (choose == 3 and comchoose ==2):
		print("You Won the round")
		myscore += 1
	print("Score You:",myscore," Advesery:",comscore)
	time.sleep(3)
if myscore > comscore:
	print("You win")
else:
	print("You lose")
	
