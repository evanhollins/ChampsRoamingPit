import json
from htmlTable import htmlTable
import webbrowser
import Weights

# teams = ['frc6304', 'frc6361', 'frc3132', 'frc254', 'frc118', 'frc6434', 'frc2896', 'frc5515', 'frc3324']
# teams = ['frc3132']

eventDataForTeamList = {}
with open("Events Info/2017cmptx.json") as f:
    eventDataForTeamList = json.load(f)

teams = eventDataForTeamList['  ']
year = 2017

teamsFinalData = {}

# Team Number, Nickname, Rookie Year, Country, # of Champs, # of Regionals, Regionals Countries, Max OPR, Average OPR

for team in teams:
    teamData = {}
    teamsFinalData[team] = {}
    with open("Teams Info/%s.json" % team, 'r') as f:
        teamData = json.load(f)

    teamsFinalData[team]['team_number'] = teamData['info']['team_number']
    teamsFinalData[team]['nickname'] = teamData['info']['nickname']
    teamsFinalData[team]['rookie_year'] = teamData['info']['rookie_year']
    teamsFinalData[team]['country'] = teamData['info']['country']

    champs = 0
    regionals = []
    OPRS = []
    highestRank = 1000

    for event in teamData['events']:
        if event['event_type'] == 0 and event['year'] == year:
            regionals.append(event['country'])
            with open("Events Info/%s.json" % event['key'], 'r') as f:
                eventData = json.load(f)
                OPRS.append(eventData['oprs'][team])
                for rank in eventData['rankings']:
                    if rank['team_key'] == team:
                        highestRank = min([rank['rank'], highestRank])
                        break
        elif event['event_type'] == 3:
            champs += 1

        if OPRS == []:
            OPRS = [0]

    teamsFinalData[team]['highest_rank'] = highestRank
    teamsFinalData[team]['champs'] = champs
    teamsFinalData[team]['regionals'] = len(regionals)
    teamsFinalData[team]['max_opr'] = max(OPRS)
    teamsFinalData[team]['average_opr'] = sum(OPRS) / float(len(OPRS))

    with open("Teams Info/%s.json" %team, 'r') as f:
        awards = json.load(f)['awards']
        awardsInYear = []
        for award in awards:
            if award['year'] == year:
                awardsInYear.append(award)

    awardPart = 100
    for award in awardsInYear:
        if award['name'] in Weights.awardsWeight:
            awardPart = min([awardPart, Weights.awardsWeight[award['name']]])

        if awardPart == 0 or awardPart == 2:
            eventDataForAward = {}
            with open("Events Info/%s.json" %(award['event_key']), 'r') as f:
                eventDataForAward = json.load(f)

            if eventDataForAward['alliances'][0]['picks'][1] == team:
                awardPart += 1
            elif eventDataForAward['alliances'][0]['picks'][2] == team:
                awardPart += 5

    # If it's still 100, must be waitlist
    if awardPart == 100:
        awardPart = 10

    teamsFinalData[team]['qualified'] = awardPart

    countryPart = Weights.countryWeight[teamsFinalData[team]['country']]


    # Full Formula (split into lines for easier reading)
    teamsFinalData[team]['help_number'] = 0
    teamsFinalData[team]['help_number'] -= year - teamsFinalData[team]['rookie_year']
    teamsFinalData[team]['help_number'] -= teamsFinalData[team]['champs']
    teamsFinalData[team]['help_number'] += teamsFinalData[team]['highest_rank']
    teamsFinalData[team]['help_number'] += teamsFinalData[team]['qualified']
    teamsFinalData[team]['help_number'] *= countryPart


with open("result.html", 'w') as f:
    f.write(htmlTable(teamsFinalData))

webbrowser.open_new("result.html")
