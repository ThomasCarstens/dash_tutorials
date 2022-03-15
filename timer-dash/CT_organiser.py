

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

template_graph.add_trace(go.Scatter(x=x_cf3, y=y_cf3,
                            mode='lines',
                            name='Trace 1',
                            marker=dict( color='#ff7400')))

template_graph.add_trace(go.Scatter(x=x_cf4, y=y_cf4,
                            mode='lines',
                            name='Trace 2',
                            marker=dict( color='#d9dadc')))

# GRAPHING UTILITIES.
_3d_traj_graph = go.Figure(layout = dark_layout)
traj_graph.update_layout(
    title="Timeline View",
    title_x=0.5,
    #xaxis_title="",
    #yaxis_title="Gain",
)
template_graph.update_xaxes(range=(-1, 1))
template_graph.update_yaxes(range=(-1, 1))



CT_colourfilter
cdata = imread('EcyOd.jpg');       % Load image
hsvImage = rgb2hsv(cdata);         % Convert the image to HSV space
hPlane = 360.*hsvImage(:, :, 1);   % Get the hue plane scaled from 0 to 360
sPlane = hsvImage(:, :, 2);        % Get the saturation plane
nonRedIndex = (hPlane > 20) & ...  % Select "non-red" pixels
              (hPlane < 340);
sPlane(nonRedIndex) = 0;           % Set the selected pixel saturations to 0
hsvImage(:, :, 2) = sPlane;        % Update the saturation plane
rgbImage = hsv2rgb(hsvImage);      % Convert the image back to RGB space