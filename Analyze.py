import json
from htmlTable import htmlTable
import webbrowser
import Weights


def analyze(year = 2017):

    # teams = ['frc6304', 'frc6361', 'frc3132', 'frc254', 'frc118', 'frc6434', 'frc2896', 'frc5515', 'frc3324']
    # teams = ['frc3132']
    teams = []
    events = []

    with open("events%i.json" %year, 'r') as f:
        eventsInfo = json.load(f)

    for event in eventsInfo:
        if event['event_type'] == 3:
            events.append(event['key'])

    for event in events:
        with open("Events Info/%i/%s.json" %(year, event), 'r') as f:
            temp = json.load(f)
            teams += temp['teams']

    teamsFinalData = {}

    for team in teams:
        teamInfo = {}
        teamsFinalData[team] = {}
        with open("Teams Info/%s.json" % team, 'r') as f:
            teamInfo = json.load(f)

        teamsFinalData[team]['team_number'] = teamInfo['info']['team_number']
        teamsFinalData[team]['nickname'] = teamInfo['info']['nickname']
        teamsFinalData[team]['rookie_year'] = teamInfo['info']['rookie_year']
        teamsFinalData[team]['country'] = teamInfo['info']['country']

        champs = 0
        regionals = []
        OPRS = []
        highestRank = 1000

        for event in teamInfo['events']:
            if (event['event_type'] == 0 or event['event_type'] == 2 or event['event_type'] == 1) and event['year'] == year:
                regionals.append(event['country'])
                with open("Events Info/%i/%s.json" %(year, event['key']), 'r') as f:
                    eventData = json.load(f)
                    try:
                        OPRS.append(eventData['oprs'][team])
                    except:
                        pass
                    for rank in eventData['rankings']:
                        if rank['team_key'] == team:
                            normalizedRank = (rank['rank']/float(len(eventData['teams']))) * 10
                            highestRank = min([normalizedRank, highestRank])
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

        qualifyPart = 100
        for award in awardsInYear:
            if award['name'] in Weights.awardsWeight:
                qualifyPart = min([qualifyPart, Weights.awardsWeight[award['name']]])
                teamsFinalData[team]['qualified_string'] = award['name']

                if qualifyPart == 0 or qualifyPart == 2:
                    eventDataForAward = {}

                    with open("Events Info/%i/%s.json" %(year, award['event_key']), 'r') as f:
                        eventDataForAward = json.load(f)

                    if eventDataForAward['alliances'][0]['picks'][1] == team:
                        qualifyPart += 1
                        teamsFinalData[team]['qualified_string'] += " Pick 1"
                    elif eventDataForAward['alliances'][0]['picks'][2] == team:
                        qualifyPart += 5
                        teamsFinalData[team]['qualified_string'] += " Pick 2"

        # If it's 100, then it could be district.
        if qualifyPart == 100:
            teamDistrictKey = ""
            for i in teamInfo['districs']:
                if i['year'] == year:
                    teamDistrictKey = i['key']
                    break

            if teamDistrictKey == "":
                # Team is not in a district, so must be waitlist
                qualifyPart = Weights.awardsWeight['Waitlist']
                teamsFinalData[team]['qualified_string'] = "Waitlist"

            else:
                teamDistrictInfo = {}
                with open("Districts Info/%i/%s.json" %(year, teamDistrictKey), 'r') as f:
                    teamDistrictInfo = json.load(f)
                teamDistrictRank = 0
                for i in teamDistrictInfo['rankings']:
                    if i['team_key'] == team:
                        teamDistrictRank = i['rank']

                qualifyPart = int((teamDistrictRank/len(teamDistrictInfo['teams']))*10)
                if qualifyPart > 4:
                    qualifyPart = 4

                teamsFinalData[team]['qualified_string'] = "District Points"

        teamsFinalData[team]['qualified'] = qualifyPart

        countryPart = Weights.countryWeight[teamsFinalData[team]['country']]


        # Full Formula (split into lines for easier reading)
        teamsFinalData[team]['help_number'] = 0
        teamsFinalData[team]['help_number'] -= year - teamsFinalData[team]['rookie_year']
        teamsFinalData[team]['help_number'] -= teamsFinalData[team]['champs']
        teamsFinalData[team]['help_number'] += teamsFinalData[team]['highest_rank']
        teamsFinalData[team]['help_number'] += teamsFinalData[team]['qualified']
        teamsFinalData[team]['help_number'] *= countryPart

        if teamsFinalData[team]['help_number'] < 0:
            teamsFinalData[team]['help_number'] = 0

    return htmlTable(teamsFinalData)
