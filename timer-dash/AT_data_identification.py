
import pandas as pd

df_log= pd.read_csv('/home/txa/Documents/data/DATA_zone_monitoring/03_12_58_log_message_0.csv')
df_adc= pd.read_csv('/home/txa/Documents/data/DATA_zone_monitoring/03_12_58_adc_report_0.csv')
df_gps= pd.read_csv('/home/txa/Documents/data/DATA_zone_monitoring/03_12_58_vehicle_local_position_0.csv')
df_dht11_2 = pd.read_csv('/home/txa/Documents/data/DATA_zone_monitoring/DHT11_2.CSV', decimal=".", sep=',', index_col=False)

print('len log:', len(df_log))
print('len adc:', len(df_adc))
print('len gps:', len(df_gps), df_gps['timestamp'][0], df_gps['timestamp'][len(df_gps)-1])

def fs_calc (df):
    microseconds_gps = df['timestamp'][len(df)-1] - df['timestamp'][0]
    print (microseconds_gps/1000000)
    fs_gps = len(df) / (microseconds_gps/1000000)
    return fs_gps

print (fs_calc(df_adc))
print (fs_calc(df_gps))
print (df_dht11_2)

milliseconds_gps = df_dht11_2['Time (ms)'][len(df_dht11_2)-1] - df_dht11_2['Time (ms)'][0]
print (milliseconds_gps/1000)
fs_arduino = len(df_dht11_2) / (milliseconds_gps/1000)
print(fs_arduino)

print (247945064/1000000)
print (712 - 248)