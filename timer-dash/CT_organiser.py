

'timer-dash/CT_convert_mishapfile.py'

'timer-dash/CT_finding_sm_collision_data.py'


#read text file
with open(bot2bot_dronecollision, "r") as f:
    notes = f.readlines()

#convert ONLINE CSV to df
def convert2df(url):
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df = pd.read_csv(path)
    if df.empty:
        print('empty')
    return df

# densify points on graph
def fita2blen(f_val, x_desired):
    MAX_X = len(f_val)
    FINALLEN_X = x_desired
    CURRENTLEN_X = len(f_val)
    #x on 10 points, then 100 points
    x_current = list(np.linspace(1,MAX_X,CURRENTLEN_X))
    x_final = list(np.linspace(1,MAX_X,FINALLEN_X))
    # interpolate on 100 values.
    interp = np.interp(x_final, x_current, f_val )
    interp = list(interp)
    return interp
'/home/txa/Documents/DashBeginnerTutorials/TUT_data_fit_function.py' #densify function tester.