# problem_03.py

teams = [
    {"name": "Tigers", "played": 0, "won": 0, "lost": 0, "points": 0},
    {"name": "Lions", "played": 0, "won": 0, "lost": 0, "points": 0}
]

def update_match(winner, loser):
    for t in teams:
        if t["name"] == winner:
            t["played"] += 1
            t["won"] += 1
            t["points"] += 3
        elif t["name"] == loser:
            t["played"] += 1
            t["lost"] += 1

# Helper function to get points for sorting
def get_points(team):
    return team["points"]

while True:
    result = input("Enter match result (winner loser) or 'stop': ").strip()
    if result.lower() == "stop":
        break
    w, l = result.split()
    update_match(w, l)

# Leaderboard sorted by points
leaderboard = sorted(teams, key=get_points, reverse=True)

print("\nLeaderboard:")
for team in leaderboard:
    print(f"{team['name']}: Played {team['played']}, Won {team['won']}, Lost {team['lost']}, Points {team['points']}")
