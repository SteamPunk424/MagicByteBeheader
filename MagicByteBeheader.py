#!/usr/bin/env python3
import sys
import os

MAGIC_BYTES = {
    # Images
    "gif":  b"GIF89a",
    "gif87": b"GIF87a",
    "png":  bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    "jpeg": bytes([0xFF, 0xD8, 0xFF]),
    "jpg":  bytes([0xFF, 0xD8, 0xFF]),

    # Executables / docs
    "exe":  b"MZ",
    "pdf":  b"%PDF-",
    "zip":  bytes([0x50, 0x4B, 0x03, 0x04]),
    "rar":  bytes([0x52, 0x61, 0x72, 0x21]),
    "7z":   bytes([0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C]),

    # Audio / video
    "mp3":  b"ID3",
    "mp4":  bytes([0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70]),
}

def usage():
    print(f"""
Usage:
  {sys.argv[0]} <type> <input_file> [output_file]

Available types:
  {', '.join(sorted(MAGIC_BYTES.keys()))}

Examples:
  {sys.argv[0]} gif Evil.java
  {sys.argv[0]} png payload.bin out.png
  {sys.argv[0]} pdf shellcode.raw report.pdf
""")
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        usage()

    file_type = sys.argv[1].lower()
    input_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else f"magic_{os.path.basename(input_file)}"

    if file_type not in MAGIC_BYTES:
        print("[-] Unknown magic type")
        usage()

    with open(input_file, "rb") as f:
        original_data = f.read()

    with open(output_file, "wb") as f:
        f.write(MAGIC_BYTES[file_type])
        f.write(original_data)

    print(f"[+] Applied '{file_type}' magic bytes → {output_file}")

if __name__ == "__main__":
    main()
