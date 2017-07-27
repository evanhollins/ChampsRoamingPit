import json
from htmlTable import htmlTable
import webbrowser

teams = ['frc6304', 'frc6361', 'frc3132', 'frc254', 'frc118', 'frc6434', 'frc2896', 'frc1403', 'frc5515']
# teams = ['frc3132']
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

    for event in teamData['events']:
        if event['event_type'] == 0 and event['year'] == year:
            regionals.append(event['country'])
            with open("Events Info/%s.json" % event['key'], 'r') as f:
                eventData = json.load(f)
                OPRS.append(eventData['oprs'][team])
        elif event['event_type'] == 3:
            champs += 1

        if OPRS == []:
            OPRS = [0]

    teamsFinalData[team]['champs'] = champs
    teamsFinalData[team]['regionals'] = len(regionals)
    teamsFinalData[team]['regionals_countries'] = regionals
    teamsFinalData[team]['max_opr'] = max(OPRS)
    teamsFinalData[team]['average_opr'] = sum(OPRS) / float(len(OPRS))
    teamsFinalData[team]['help_number'] = teamData['info']['team_number']

with open("result.html", 'w') as f:
    f.write(htmlTable(teamsFinalData))

webbrowser.open_new("result.html")
