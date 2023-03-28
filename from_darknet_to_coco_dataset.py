from pathlib import Path
from tqdm import tqdm
import shutil


def copy_images_from_txt(txt_file, dataset_path):
    with open(txt_file, "r") as f:
        lines = f.read().splitlines()
        for line in tqdm(lines, desc='Copy'):
            if len(line.strip()) == 0:
                print(f"found an end of line {lines.index(line)}")
            else:
                image_path = Path(line)
                dataset_root = image_path.parents[1]
                folder_name = image_path.parent.name
                image_name = image_path.name
                new_image_name = folder_name + "_" + image_name

                # print(image_path)
                # print(folder_name)
                # print(image_name)
                # print(dataset_root)
                p = Path(dataset_path / new_image_name)
                p = str(dataset_root) + str(p)
                # print(p)
                shutil.copyfile(line, p)


def copy_labels_from_txt(txt_file, dataset_path):
    with open(txt_file, "r") as f:
        lines = f.read().splitlines()
        for line in tqdm(lines, desc='Copy'):
            if len(line.strip()) == 0:
                print(f"found an end of line {lines.index(line)}")
            else:
                image_path = Path(line)
                txt_path = image_path.with_suffix('.txt')

                # print(image_path)
                # print(txt_path)

                dataset_root = txt_path.parents[1]
                # print(dataset_root)
                folder_name = txt_path.parent.name
                txt_name = txt_path.name
                new_txt_name = folder_name + "_" + txt_name
                # print(new_txt_name)

                p = Path(dataset_path / new_txt_name)
                p = str(dataset_root) + str(p)
                # print(p)
                shutil.copyfile(txt_path, p)


def main():
    train_images_path = Path("/train/images")
    train_labels_path = Path("/train/labels")
    val_images_path = Path("/val/images")
    val_labels_path = Path("/val/labels")
    train_set_txt = "/home/alexsh/temp/rv_yolo_18cl/train.txt"
    val_set_txt = "/home/alexsh/temp/rv_yolo_18cl/valid.txt"

    copy_images_from_txt(train_set_txt, train_images_path)
    copy_labels_from_txt(train_set_txt, train_labels_path)
    copy_images_from_txt(val_set_txt, val_images_path)
    copy_labels_from_txt(val_set_txt, val_labels_path)


if __name__ == "__main__":
    main()
