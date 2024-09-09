import os
import cairosvg
import json

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

def main():
    if not os.path.exists(config["import_folder"]): os.makedirs(config["import_folder"])
    if not os.path.exists(config["export_folder"]): os.makedirs(config["export_folder"])

    files = os.listdir(config["import_folder"])
    
    if files:
        for file in files:
            for size in config["sizes"]:
                if not os.path.exists(f"{config["export_folder"]}/{size[0]}x{size[1]}"): os.makedirs(f"{config["export_folder"]}/{size[0]}x{size[1]}")

                cairosvg.svg2png(url=f"{config["import_folder"]}/{file}", write_to=f"{config["export_folder"]}/{size[0]}x{size[1]}/{os.path.splitext(file)[0]}.png", output_width=size[0], output_height=size[1])
                print(f"- Converted {file} to {os.path.splitext(file)[0]}.png ({size[0]}x{size[1]})")
    else:
        print(f"- There are no files in the '{config["import_folder"]}' folder.")

main()