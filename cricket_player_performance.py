run_scored = int(input("Enter the Runs scored by Player: "))
print(run_scored)

ball_faced = int(input("Enter the Balls faced by Player: "))
print(ball_faced)

fours = int(input("Enter the total Fours hit by Player: "))
print(fours)

sixes = int(input("Enter the Total Sixes hit by Player: "))
print(sixes)

wickets_taken = int(input("Enter the wickets taken by Player: "))
print(wickets_taken)

run_conc = int(input("Enter the Runs conceded by Player: "))
print(run_conc)

overs_bowled = int(input("Enter the overs bowled by Player: "))
print(overs_bowled)

catch_taken = int(input("Enter the catches taken by Player: "))
print(catch_taken)

print("Calculating the batting strike rate of player:")
sr = (run_scored / ball_faced) * 100
print(sr)

print("Calculating the Bowling Economy of player:")
eco = run_conc / overs_bowled
print(eco)

if run_scored >= 50 and sr >= 120:
    print("Excellent Batter")
    batter = 1
elif run_scored >= 30 and sr >= 100:
    print("Good Batter")
    batter = 2
elif run_scored >= 20:
    print("Average Batter")
    batter = 3
else:
    print("Poor Batter")
    batter = 4

if wickets_taken >= 3 and eco <= 6:
    print("Excellent Bowler")
    bowler = 1
elif wickets_taken >= 2 and eco <= 8:
    print("Good Bowler")
    bowler = 2
elif wickets_taken >= 1:
    print("Average Bowler")
    bowler = 3
else:
    print("Poor Bowler")
    bowler = 4

if catch_taken >= 2:
    print("Outstanding Fielder")
elif catch_taken == 1:
    print("Active Player")
else:
    print("Need Improvement")

print("Overall All-Rounder Decision:")

if batter == 1 and bowler == 1:
    print("Star All-Rounder")
elif batter == 2 and bowler == 2:
    print("Strong All-Rounder")
elif batter == 3 and bowler == 3:
    print("Supporting All-Rounder")
else:
    print("Developing All-Rounder")
