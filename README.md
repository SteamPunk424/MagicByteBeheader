# MagicByteBeheader
Injects magic bytes of a specified file type into other files in order to bypass magic byte checks for file uploads. \
This is a very niche usecase tool and probably not the one you are looking for but mess with it a bit if ya want.
```(I am not responisble for damages caused by the use this tool. This tool is for research purposes only.)``` 

```
Usage:
  magicbytebuster.py <type> <input_file> [output_file]

Available types:
  7z, exe, gif, gif87, jpeg, jpg, mp3, mp4, pdf, png, rar, zip

Examples:
  magicbytebuster.py gif Evil.java
  magicbytebuster.py png payload.bin out.png
  magicbytebuster.py pdf shellcode.raw report.pdf
```

