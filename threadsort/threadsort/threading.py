import os
import shutil


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
            dest_folder = None
            for k, v in extensions.items():
                if extension.lower() in v:
                    dest_folder = os.path.join(src_folder, k)
                    break
            if dest_folder is None:
                dest_folder = os.path.join(src_folder, 'other')
            dest_file_path = os.path.join(dest_folder, filename)
            shutil.move(source_file_path, dest_file_path)
            
            
def remove_empty_folders(src_folder):
    for root, dirs, files in os.walk(src_folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

                
def process_subfolder(subfolder):
    sort_files_by_extension(subfolder, extensions)


def main():
    src_folder = "D:\dl_test"
    create_dest_folders(src_folder, extensions)
    sort_files_by_extension(src_folder, extensions)
    remove_empty_folders(src_folder)


if __name__ == "__main__":
    main()

