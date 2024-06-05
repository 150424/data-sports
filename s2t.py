#將多個檔案標題檢體改成繁體

import os
import pandas as pd

# 定義CSV檔案所在的目錄
folder_path = r'‪C:\Users\tinalu\Desktop\反向跳測驗_高中棒球_51'

# 遍歷目錄中的每個檔案
for filename in os.listdir(folder_path):
    # 檢查檔案是否為CSV
    if filename.endswith('.csv'):
        # 構建完整的檔案路徑
        file_path = os.path.join(folder_path, filename)
        
        # 讀取CSV檔案到DataFrame
        df = pd.read_csv(file_path)
        
        columns = pd.DataFrame(df.columns)
        # print(columns)
        df.columns = ["時間(s)", "右腳法向力(N)", "左腳法向力(N)", "合力(N)"]

        # modifided = df_csv.columns()
        # print (pd.DataFrame(df))
        processed_file_name = filename[:-4] + '.csv'
        processed_file_path = os.path.join(folder_path, processed_file_name)
        df.to_csv(processed_file_path, encoding='utf-8-sig' ,index=False)
        # 在DataFrame上執行所需的處理
        # 例如，我們想要添加一個新列，