import os
import shutil
import concurrent.futures


extensions = {
    "images": ('jpeg', 'png', 'jpg', 'ico', 'gif', 'tiff', 'webp', 'svg', 'raw'),
    "documents": ('doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'ppt', 'pptx', 'rtf', 'fb2'),
    "audio": ('mp3', 'ogg', 'wav', 'amr', 'wma', 'dts', 'aac', 'aiff', 'flac', 'midi', 'mpc', 'voc', 'vox', 'cd'),
    "video": ('webm', 'mkv', 'flv', 'vob', 'avi', 'mts', 'ts', 'mov', 'wmv', 'asf', 'amv', 'mp4', 'm4v', 'mpg', 'mp2', 'mpeg', 'm2v', 'svi', '3gp'),
    "archives": ('zip', 'gz', 'tar', 'arj', 'rar', 'cab', '7z'),
    "other": (),
}


def create_dest_folders(src_folder, extensions):
    for folder in extensions.keys():
        new_folder_path = os.path.join(src_folder, folder)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)


def sort_files_by_extension(src_folder, extensions):
    for root, _, files in os.walk(src_folder):
        for filename in files:
            extension = filename.split('.')[-1]
            source_file_path = os.path.join(root, filename)
            for k, v in extensions.items():
                if extension.lower() in v:
                    dest_file_path = os.path.join(src_folder, k)
                else:
                    dest_file_path = os.path.join(src_folder, 'other')
                shutil.move(source_file_path, dest_file_path)

def process_subfolder(subfolder):
    sort_files_by_extension(subfolder, extensions)

def main():
    src_folder = "D:\dl_test"  # Вказати шлях до папки
    
    create_dest_folders(src_folder, extensions)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, subfolders, _ in os.walk(src_folder):
            for subfolder in subfolders:
                executor.submit(process_subfolder, os.path.join(root, subfolder))

    sort_files_by_extension(src_folder, extensions)

if __name__ == "__main__":
    main()
