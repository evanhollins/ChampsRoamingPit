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
teamInfo = {}
teams = []
with open("teams.csv", 'r') as f:
	teamsString = f.read()
	teams = teamsString.split(',')

for team in teams:
	print(team)
	teamData = {}
	teamData['info'] = requests.get(url + "team/%s" %team, headers = head).json()
	teamData['events'] = requests.get(url + "team/%s/events" %team, headers = head).json()
	teamData['districs'] = requests.get(url + "team/%s/districts" %team, headers = head).json()
	teamData['awards'] = requests.get(url + "team/%s/awards" % team, headers=head).json()
	with open("Teams Info/" + team + ".json", 'w') as f:
		json.dump(teamData, f)