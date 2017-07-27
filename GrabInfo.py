import requests
import csv
import json

head = {"X-TBA-Auth-Key": "0Af0CBYCqQGZK4t8LontwIrhhJiJgUl1eJLEN5LsEIAXb9D7Vncjo4VUYAQHIydz"}
url = "https://www.thebluealliance.com/api/v3/"

#   Grabbing teams for a team list csv
# teams = []
#
# for i in range(0, 14):
# 	teams = teams + requests.get(url + "teams/%i/keys" %(i), headers = head).json()
#
#
# with open("teams.csv", 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(teams)

#  Grab info for each team
# teamInfo = {}
# teams = []
# with open("teams.csv", 'r') as f:
# 	teamsString = f.read()
# 	teams = teamsString.split(',')
#
# for team in teams:
# 	print(team)
# 	teamData = {}
# 	teamData['info'] = requests.get(url + "team/%s" %team, headers = head).json()
# 	teamData['events'] = requests.get(url + "team/%s/events" %team, headers = head).json()
# 	teamData['districs'] = requests.get(url + "team/%s/districts" %team, headers = head).json()
# 	teamData['awards'] = requests.get(url + "team/%s/awards" % team, headers=head).json()
# 	with open("Teams Info/" + team + ".json", 'w') as f:
# 		json.dump(teamData, f)

#  Grab info for all events
#  eventInfo = {}
#
# with open("events.json", 'w') as f:
# 	eventInfo = requests.get(url + "events/2017", headers=head).json()
# 	json.dump(eventInfo, f)
#
# events = {}
# with open("events.json", 'r') as f:
# 	events = json.load(f)
#
# for event in events:
# 	eventData = {}
# 	key = event['key']
#
# 	eventData['teams'] = requests.get(url + "event/%s/teams/keys" %key, headers=head).json()
# 	eventData['alliances'] = requests.get(url + "event/%s/alliances" % key, headers=head).json()
# 	eventData['oprs'] = requests.get(url + "event/%s/oprs" % key, headers=head).json()
# 	eventData['rankings'] = requests.get(url + "event/%s/rankings" % key, headers=head).json()
# 	eventData['matches'] = requests.get(url + "event/%s/matches" % key, headers=head).json()
# 	eventData['awards'] = requests.get(url + "event/%s/awards" % key, headers=head).json()
#
# 	with open("Events Info/%s.json" %key, 'w') as f:
# 		json.dump(eventData, f)

# Grab info for all events
# districtInfo = {}
#
# with open("districts.json", 'w') as f:
# 	districtInfo = requests.get(url + "districts/2017", headers=head).json()
# 	json.dump(districtInfo, f)
#
# districts = {}
# with open("districts.json", 'r') as f:
# 	districts = json.load(f)
#
# for district in districts:
# 	districtData = {}
# 	key = district['key']
#
# 	districtData['events'] = requests.get(url + "district/%s/events" %key, headers=head).json()
# 	districtData['teams'] = requests.get(url + "district/%s/teams/keys" % key, headers=head).json()
# 	districtData['rankings'] = requests.get(url + "district/%s/rankings" % key, headers=head).json()
#
# 	with open("Districts Info/%s.json" %key, 'w') as f:
# 		json.dump(districtData, f)