
#10_06_37 NO
import pandas as pd
#df_log= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/10_05_12_log_message_0.csv')
#df_log= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/10_06_37_log_message_0.csv')
df_log= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/03_12_58_log_message_0.csv')

df_adc= pd.read_csv('/home/txa/Documents/data/DATA_ zone_monitoring/03_12_58_adc_report_0.csv')


#log_5_2021-8-10-05-26-30.ulg
word=''
print(df_log['text[1]'])
print(range(len(df_log.values)-1))
print(range(len(df_log)))
print("CALC:", 127-82)
print("CALC:", 127-82)
log_list = []
for j in range(len(df_log)):
    log_list.append(word)
    word = str(df_log['timestamp'][j])
    for i in range(0,127):
            #print((df_log['text['+str(i)+']'][4]))
            #try:
            log_value = (df_log['text['+str(i)+']'][j])

            if log_value < 0:
                break
                #log_value = 256-abs(log_value)
                #1 2 4 8 16 32 62 128 -> -85 = 85+128
            letter = chr(log_value)
            #print(log_value, letter)
            word=word+letter
            # except:
            #     #pass
            #     print("issue:", log_value, "at line", j, "text:", i)

#print(log_list)
for each in log_list:
    if 'slice' in each:
        print (each)
#if 'vehicle_magnetometer' in 
#247945064