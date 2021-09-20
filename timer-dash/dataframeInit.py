import pandas as pd
#CHOOSE A PAGEd
# df_init = pd.DataFrame({'Week advance': ['Active Cloud Functions', 'Hackathons', 'GPU Jobs'],
#                    'Dedicated time': ['Papers replicated', '', ''],
#                    'Follow-ups': ['GPU Jobs', 'Radar Usefulness', '']})

# #WEEK ADVANCE PAGE 
# # This one must constantly be reinitialised. It stays.
# df_weekAdvance = pd.DataFrame()

# #DEDICATED TIME PAGE --temp a CRITERIA PAGE
# # Add-subtract format. ### DEADLINE year=2021 month=6, day=16, hour=23, minute=25, second=25
# df_dedicatedTime = pd.DataFrame({'Nb tickets resto': ["gauge+number+delta", '3', 200, 100, '', '0,150', 'green', "d replicated", '0.25,0.5', '', 'week', 'week', '', '0'],
#                         'Nb exercise routines': ["gauge", '0.4', 200, 100, '', '0,1', 'blue', "d", '0.5,1', '', 'week', 'week', '', '0'],
#                         'Nb potential sponsors': ["gauge", '27', 200, 100, '', '0,150', 'orange', "d deadline", '0,0.25', '', 'week', 'week', '', '0'],                        
#                         })

# #FOLLOWUPS PAGE --temp a CRITERIA PAGE
# df_Followups = pd.DataFrame({'Graph-it contact': ["gauge+number+delta", '3', 200, 100, '', '0,150', 'green', "Papers replicated", '0.25,0.5'],
#                         'Thesis write-up': ["gauge", '50', 200, 100, '', '0,150', 'blue', "Hackathons", '0.5,1'],
#                         'App deadline': ["gauge", '27', 200, 100, '', '0,150', 'orange', "App deadline", '0,0.25'],                        
#                         })

import pandas as pd
import datetime

#SAVE KEY AS A VALUE: TITLE PREP
def Title_setup(dict):
    for key in dict:
        dict[key][7] = key
        print(dict[key][7])

#USEFUL FOR EVERY SUBSEQUENT START_DAY
def Inittoday_setup(dict):
    for key in dict:
        now = datetime.datetime.today()
        timestamp = now.replace(tzinfo=datetime.timezone.utc).timestamp()
        dict[key][9] = timestamp
        print(dict[key][9])


#UPCOMING EVENTS PAGE -- temp a DEADLINES page
# df_Upcoming_events = pd.DataFrame({'Graph-it contact': ["gauge+number+delta", '2021,6,29,17,20,24', 200, 100, '', '0,150', 'green', "Papeyy", '0,1', '', '', ''],
#                         'Thesis response': ["gauge+number+delta", '2021,6,29,23,26,25', 200, 100, '', '0,150', 'blue', "yy", '0,0.5', '', '', ''],
#                         'Lab responses': ["gauge", '2021,6,29,18,25,59', 200, 100, '', '0,150', 'orange', "App yy", '0,0.25', '', '', ''],                        
#                         'Active Cloud Functions': ["gauge", '2021,6,30,18,20,24', 200, 100, '', '0,150', 'green', "Papeyy", '0,1', '', '', ''],
#                         'Hackathons': ["gauge", '2021,6,30,23,26,25', 200, 100, '', '0,150', 'blue', "yy", '0,0.5', '', '', ''],
#                         'App deadline': ["gauge", '2021,6,30,23,25,59', 200, 100, '', '0,150', 'orange', "App yy", '0,0.25', '', '', ''],                        
#                         })
# Title_setup(df_weekAdvance)
# Title_setup(df_dedicatedTime)
# Title_setup(df_Followups)
# Title_setup(df_Upcoming_events)

# Inittoday_setup(df_dedicatedTime)

#SAVE LATER...
# df_weekAdvance.to_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
# df_dedicatedTime.to_csv('~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv', index=False)
# df_Followups.to_csv('~/Documents/DashBeginnerTutorials/db_Followups.csv', index=False)
# df_Upcoming_events.to_csv('~/Documents/DashBeginnerTutorials/db_Upcoming_events.csv', index=False)
# df_init.to_csv('~/Documents/DashBeginnerTutorials/df_init.csv', index=False)



#RETRIEVE
#SAVE LATER...
def read_file():
    #RETRIEVE ALL...
    df_weekAdvance = pd.DataFrame()
    #df_weekAdvance= pd.read_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
    df_dedicatedTime= pd.read_csv('~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv')
    df_Upcoming_events= pd.read_csv('~/Documents/DashBeginnerTutorials/db_Upcoming_events.csv')
    return df_dedicatedTime, df_Upcoming_events

#SAVE LATER...

df_dedicatedTime, df_Upcoming_events = read_file()
df_Upcoming_events = df_Upcoming_events.drop(list(df_Upcoming_events.keys())[1], axis = 1)
print(df_Upcoming_events)
#df_weekAdvance.to_csv('~/Documents/DashBeginnerTutorials/db_Week_advancement.csv', index=False)
#df_dedicatedTime.to_csv('~/Documents/DashBeginnerTutorials/db_Dedicated_time.csv', index=False)
df_Upcoming_events.to_csv('~/Documents/DashBeginnerTutorials/db_Upcoming_events.csv', index=False)


# df = pd.read_csv("my_dashboard.csv")
# adc_water_log = pd.read_csv("11_09_32_adc_report_0.csv")
# params = list(adc_water_log)
# print(adc_water_log)
# max_length = len(adc_water_log)
# print(params, max_length)
# print(adc_water_log['timestamp'])

# INITIALIZE: empty SCATTERPLOT trace
#scat = go.Figure()

# scat.add_trace(go.Scatter(x=random_x, y=random_y1,
#                     mode='lines+markers',
#                     name='lines+markers'))
# scat.add_trace(go.Scatter(x=random_x, y=random_y2,
#                     mode='lines',
#                     name='lines'))
