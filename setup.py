import zipfile

zip_path = '.\\dataset.zip'
extract_folder = './'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("ZIP文件解压完成")
