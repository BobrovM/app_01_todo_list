import zipfile
import pathlib


def make_archive(filepaths, folder):
    dest_path = pathlib.Path(folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["bonus_01.py"], folder="dest")
