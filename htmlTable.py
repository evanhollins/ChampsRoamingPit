
preTable = """
<head>
<link href="css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<table id="myTable" class="table tablesorter">
<thead>
<tr>
<th>Team Number</th>
<th>Help Number</th>
<th>Name</th>
<th>Rookie Year</th>
<th>Country</th>
<th># of Champs</th>
<th># of Regionals</th>
<th>Regional Countries</th>
<th>Max OPR</th>
<th>Average OPR</th>
</tr>
</thead>
<tbody>
"""

postTable = """
</tbody>
<script src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script>
	$(document).ready(function() 
    { 
        $("#myTable").tablesorter( {sortList: [[1,-1]]} ); 
    } 
);
</script>
</body>
"""

def htmlTable(teamFinalData):
    finalString = ""

    # Make table
    table = ""

    for team in teamFinalData:
        table += """
            <tr>
                <td>%s</td>
                <td>%i</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%i</td>
                <td>%i</td>
                <td>%s</td>
                <td>%f</td>
                <td>%f</td>
            </tr>\n
        """ %(	teamFinalData[team]['team_number'], teamFinalData[team]['help_number'],
				teamFinalData[team]['nickname'],teamFinalData[team]['rookie_year'],
				teamFinalData[team]['country'], teamFinalData[team]['champs'],
				teamFinalData[team]['regionals'], teamFinalData[team]['regionals_countries'],
				teamFinalData[team]['max_opr'], teamFinalData[team]['average_opr'])

    finalString = preTable + table + postTable
    return finalString