import pandas as pd

activity_df = pd.read_csv('neimanmarcus_activityv2.txt', sep='|', header=None)
item_df = pd.read_csv('neimanmarcus_itemv2.txt', sep='|', header=None)


#print activity_df
#print item_df

label = activity_df.columns[7]
label2 = item_df.columns[8]
#print label
#print label2

#activity_df.rename(columns={[7]
#print activity_df[7]
#print item_df[8]

output_file = 'Combined_Records.csv'
target = open(output_file, 'wb')



combined_df = pd.merge(left=activity_df, right=item_df, left_on=7, right_on=8)


print combined_df

combined_df.to_csv(r'combined.txt', header=None, index=None, sep='|') 

target.close()