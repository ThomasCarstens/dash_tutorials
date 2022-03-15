#psrecord $(pgrep proc-name1) --interval 1 --plot plot1.png
pointstring = '213212111211223431521133132371211123119112412413236113312321313123211213411222142111335214121322422116513112121112152121131121134126251261221261313111131421121136123211313112416332512352319211112522244131112124311114123111412132322331515111111137111151612113112113714211121371311212111211341312211141312113131111131511121111125123211241121137231281431431521125112323131511211121321111251132121221322113132114511123112221142112552122121211313291131121312131331121111131352113111121'
def split(word):
    return [char for char in word]

def split_no1(word):
    array = []
    for char in word:
        #if char != '1' and char != '2' and char != '3':
        array.append(char)
    return array


each = split_no1(pointstring)

indices = []
for i in range (len(each)):
    indices.append(i)


print (each)
print (indices)


import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure([go.Bar(x=(indices), y=each ) ])
fig.show()