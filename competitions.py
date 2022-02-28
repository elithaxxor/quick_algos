
## result will be numernical, setWinner is str val of team
def score_logger(setWinner, result):
    best_team = []
    best_team.append(setWinner)
    best_team.sort()
    print(best_team)
    current_best_team = ''
    scores = {f'{setWinner}': f'{result + 1}'}
    print(scores)
    return scores
    #print('setwinner' , setWinner, 'result', result)
    #print(result)

def whosWinner():

    HOME_WIN = 1
    competitions = [
        ['HTML', 'C#'],
        ['C#', 'Python'],
        ['Python', 'HTML']
    ]
    ''' 
        * Enumerate through input list and map competitions
        * Then update scores array as loops pass 
    '''
    results = [0, 0, 1]

    for index, teamSet in enumerate(competitions):
        result = results[index]
        home, away = teamSet  # splits array into two sepearte

        # if result == HOME_WIN:
        #     winning_team = home
        # else:
        #     winning_team = away
        #
        if result == 0:
            setWinner = away
            score_logger(setWinner, result)
        else:
            setWinner = home
            score_logger(setWinner, result)

## function to log wins and scors

def main():
    results=whosWinner()
    print(results)
main()



## another version 
HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    currentBestTeam = ''
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]

        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points






