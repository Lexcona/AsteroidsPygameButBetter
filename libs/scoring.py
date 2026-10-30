import globals

player_score = 0

scoreText = None

def score_update():
    global scoreText
    scoreText = globals.pixelFont.render(f"Score: {player_score}", True, "green")
