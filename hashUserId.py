import os
import csv
import hashlib

def hash_user_id(user_id):
    # 使用 hashlib 计算 SHA3-256 散列值
    sha3_hash = hashlib.sha3_256()
    sha3_hash.update(user_id.encode('utf-8'))
    return sha3_hash.hexdigest()

def hash_user_ids_in_directory(input_directory, output_directory):
    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename)

            with open(input_file, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                fieldnames = reader.fieldnames

                with open(output_file, 'w', newline='') as output_csvfile:
                    writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for row in reader:
                        # 将每个用户 ID 的值重新编码为 SHA3-256 散列值
                        row['user_id'] = hash_user_id(row['user_id'])
                        writer.writerow(row)

# 指定输入和输出目录路径
input_directory = '/path/to/input/directory'
output_directory = '/path/to/output/directory'

# 对输入目录中的所有 CSV 文件中的用户 ID 进行哈希编码，并将结果写入输出目录中的相应文件
hash_user_ids_in_directory(input_directory, output_directory)
