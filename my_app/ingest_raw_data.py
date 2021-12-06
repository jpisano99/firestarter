import pandas as pd
import os
from settings import app_cfg
import time
#
# Get Directories and Paths to Files
#
my_sheet_dir = os.path.join(app_cfg['HOME'], app_cfg['MOUNT_POINT'], app_cfg['MY_APP_DIR'],
                            app_cfg['WORKING_SUB_DIR'])


def ingest_raw_data():
    #
    # Open the raw input data
    #
    raw_fs_sheet = os.path.join(my_sheet_dir, app_cfg['RAW_FIRESTARTER'])
    df_fs_requests = pd.read_csv(raw_fs_sheet)

    # # iterating the columns
    # for col in df_fs_requests.columns:
    #     print(col)

    jim = df_fs_requests[['Issue key',
                          'Custom field (Customer Name)',
                          'Issue Type',
                          'Customer Request Type',
                          'Status',
                          'Creator',
                          'Created',
                          'Assignee',
                          'Updated',
                          'Summary',
                          'Description',
                          # 'Custom field (Aha Link)',
                          'Custom field (Customer Segment)',
                          'Custom field (Geo)',
                          'Custom field (Requestor Reported Deal Size)',
                          'Custom field (Workload Deploymt)',
                          ]]
    print(jim)
    jim.to_excel('jim.xlsx', index=False)
    exit()
    for index, value in df_fs_requests.iterrows():
        # print(index, value)
        # issue_key = value['Issue key']
        # print(value['Assignee'], value['Creator'])
        # print(index, issue_key, value['Summary'], '\t\t', value['Issue Type'])
        jim = df_fs_requests[['Assignee', 'Creator']]
        print(jim)

    return()


if __name__ == "__main__":
    print (my_sheet_dir)
    ingest_raw_data()
