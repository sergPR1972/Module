import re
import os
import shutil
import sys
from pathlib import Path

list_image = []
list_video = []
list_doc = []
list_audio = []
list_arch = []
list_other = []
known_exp = set()
unknown_exp = set()
our_dir = ('images', 'video', 'documents', 'audio', 'archives', 'other')

CYRILLEC_SYMBOLS = "абвгдежзийклмнопрстуфхцчшщъьюяєії"
LATYN_SYMBOLS = ('a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'y', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
                 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', '', 'yu', 'ya', 'ye', 'i', 'yi')
TRANSLATOR = {}
for cyril, latyn in zip(CYRILLEC_SYMBOLS, LATYN_SYMBOLS):
    TRANSLATOR[ord(cyril)] = latyn
    TRANSLATOR[ord(cyril.upper())] = latyn.upper()

def normalize(str_text: str)->str:
    name_t = str_text.translate(TRANSLATOR)
    name_t = re.sub(r"\W+", "_", name_t)
    return name_t

def handle_folders(filename: Path, ext: Path):
    new_path = TARGET_FOLDER / ext
    new_path.mkdir(parents=True, exist_ok=True)
    filename.replace(new_path / normalize(filename.name))

def folder_image(filename: Path):
    ext = Path('images')
    handle_folders(filename, ext)

def folder_video(filename: Path):
    ext = Path('video')
    handle_folders(filename, ext)

def folder_documents(filename: Path):
    ext = Path('documents')
    handle_folders(filename, ext)

def folder_audio(filename: Path):
    ext = Path('audio')
    handle_folders(filename, ext)

def folder_archives(filename: Path):
    ext = Path('archives')
    new_path = TARGET_FOLDER / ext
    new_path.mkdir(parents=True, exist_ok=True)
    folder_for_file = new_path / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(parents=True, exist_ok=True)
    try:
        shutil.unpack_archive(filename.resolve(), folder_for_file.resolve())
        filename.unlink()
    except shutil.ReadError:
        print("It's not archive")
        folder_for_file.rmdir()
        return None

def folder_other(filename: Path):
    ext = Path('other')
    handle_folders(filename, ext)

def evaluation_dir_none(path: Path):
    if not os.listdir(path) and path.name not in our_dir:
        path.rmdir()

def read_folder(path: Path):

    for elem in path.iterdir():
        if elem.suffix.lower() == '.jpeg' or elem.suffix.lower() == '.png' or elem.suffix.lower() == '.jpg' or elem.suffix.lower() == '.svg':
            list_image.append(elem.name)
            known_exp.add(elem.suffix)
            folder_image(filename=elem)

        elif elem.suffix.lower() == '.avi' or elem.suffix.lower() == '.mp4' or elem.suffix.lower() == '.mov' or elem.suffix.lower() == '.mkv':
            list_video.append(elem.name)
            known_exp.add(elem.suffix)
            folder_video(filename=elem)

        elif elem.suffix.lower() == '.doc' or elem.suffix.lower() == '.docx' or elem.suffix.lower() == '.txt' or elem.suffix.lower() == '.pdf'\
            or elem.suffix.lower() == '.xlsx' or elem.suffix.lower() == 'pptx':
            list_doc.append(elem.name)
            known_exp.add(elem.suffix)
            folder_documents(filename=elem)

        elif elem.suffix.lower() == '.mp3' or elem.suffix.lower() == '.ogg' or elem.suffix.lower() == '.wav' or elem.suffix.lower() == '.amr':
            list_audio.append(elem.name)
            known_exp.add(elem.suffix)
            folder_audio(filename=elem)

        elif elem.suffix.lower() == '.zip' or elem.suffix.lower() == '.gz' or elem.suffix.lower() == '.tar':
            list_arch.append(elem.name)
            known_exp.add(elem.suffix)
            folder_archives(filename=elem)

        elif elem.is_file():
            list_other.append(elem.name)
            unknown_exp.add(elem.suffix)
            folder_other(filename=elem)

        elif elem.is_dir() and elem.name not in our_dir:
            if os.listdir(elem):
                read_folder(elem)
                evaluation_dir_none(elem)
            else:
                elem.rmdir()

    return f"list_image => {list_image}\nlist_video => {list_video}\nlist_doc => {list_doc}\n"\
           f"list_audio => {list_audio}\nlist_arch => {list_arch}\nlist_unknown => {list_other}"\
           f"\n\nknown expansion => {known_exp}\nunknown expansion => {unknown_exp}"

parser = sys.argv[1]
TARGET_FOLDER = Path(parser)

if __name__ == "__main__":
    print(read_folder(TARGET_FOLDER))

