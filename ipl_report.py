#import the pandas library and aliasing as pd
import pandas as pd
from collections import Counter
import pprint

matches_data = pd.read_csv('./matches.csv')

try:
	choosen_year = int(input('\nChoose season to get the IPL Report :\n'))
	season_avail = matches_data['season'].unique()

	if choosen_year not in season_avail :
		print( "\nSorry, data for choosen season is not available !\n")

	else:
		#To get the number of occurrence, we will use Counter of collections packages
		print('\n\n1. Top 4 teams in terms of wins')
		sorted_match_winners = Counter(matches_data[matches_data['season'] == choosen_year]['winner']).most_common(4)

		for key, val in dict(sorted_match_winners).items():
			print('   Team Name - ',key, " Matches - ", val)


		print('\n\n2. Which team won the most number of tosses', end=" -> ")
		toss_wins = Counter(matches_data[matches_data['season'] == choosen_year]['toss_winner']).most_common(1)[0][0]
		print(toss_wins)
		

		print('\n\n3. Which player won num of player of the match award')
		man_of_match = Counter(matches_data[matches_data['season'] == choosen_year]['player_of_match']).most_common()
		
		# print(max(man_of_match)[1])	
		max_man_of_match = max(dict(man_of_match).values())

		for key, value in dict(man_of_match).items():
			if value == max_man_of_match:
				print("    Player Name - ",key, " Matches - ",value)
		
		print('\n\n4. Which team won max matches')
		print("    ",sorted_match_winners.most_common(1)[0][0])
		
		print('\n\n5. Which location has the most number of wins')
		season_location = matches_data[matches_data['season'] == choosen_year]
		# normal , tie, no result
		season_location = Counter(season_location[season_location['result'] == 'normal']['city'])
		max_season_location = max(dict(season_location).values())
		for key, value in dict(season_location).items():
			if value == max_season_location:
				print("Location - ",key," Matches - ",value)
				
		print('\n\n6. Which % of teams decided to bat when they won the toss')
		total_matches 	= matches_data[matches_data['season'] == choosen_year]
		bat_percentage 	= round((total_matches[total_matches['toss_decision']== 'bat']['toss_decision'].count()/len(total_matches))* 100, 2)
		print("    ",bat_percentage)
except:
	print("Enter a valid year to get the IPL Report.")



# Additional Questions
# loc = access particular cell, idxmax = index of first occurrence of maximum 
print('\n\nWhich team won by the highest margin of runs')
print(matches_data.loc[matches_data['win_by_runs'].idxmax()])

print('\n\nWhich team won by the highest number of wickets')
print(matches_data.loc[matches_data['win_by_wickets'].idxmax()])

