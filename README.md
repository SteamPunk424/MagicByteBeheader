# MagicByteBeheader
Injects magic bytes of a specified file type into other files in order to bypass magic byte checks.

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

