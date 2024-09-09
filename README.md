# Convert SVG to PNG
First of all you need to install `cairosvg` with python, you just need to use the command `pip install cairosvg`, you can find more information in its [documentation](https://cairosvg.org/documentation/).

Y después para ejecutar el código solo debes usar el comando `python main.py`.

## `config.json`

* `import_folder`: Indicates the name of the import folder
* `export_folder`: Indicates the name of the export folder
* `sizes`: Indicates the sizes in pixels in which the file will be exported
* 
## Import folder

In this folder you will add all the `.svg` files that you want to convert, you can add as many files as you want, do not put them in subfolders and it does not matter if they have the `.svg` extension or not, but if they are not **SVG** files the code will give an error.

## Export folder

All converted files will be sent here, depending on how many sizes you have configured there will be some subfolders indicating the sizes, for example: `16x16`, `32x32` or `64x64`.