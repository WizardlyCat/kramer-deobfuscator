import argparse
from binascii import unhexlify
import chardet

strings = "abcdefghijklmnopqrstuvwxyz0123456789"

class Kyrie:
    @staticmethod
    def _dkyrie(text: str) -> str:
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a) + 1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    @staticmethod
    def _decrypt(text: str, key: int) -> str:
        return "".join(chr(ord(t) - key) if t != "ζ" else "\n" for t in text)

class Key:
    @staticmethod
    def decrypt(e: str, key: int) -> str:
        decrypted = Kyrie._decrypt(e, key)
        return Kyrie._dkyrie(decrypted)

def deobfuscate(content: str, key: int) -> str:
    hex_lines = content.split("/")
    decoded_lines = []
    for line in hex_lines:
        try:
            decoded_line = unhexlify(line).decode("utf-8", errors="ignore")
            decoded_lines.append(decoded_line)
        except ValueError:
            continue
    joined_content = "".join(decoded_lines)
    return Key.decrypt(joined_content, key)

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    detected = chardet.detect(raw_data)
    print(f"Detected encoding: {detected['encoding']}")
    return raw_data.decode(detected['encoding'], errors="ignore")

def main():
    parser = argparse.ArgumentParser(description="Deobfuscate a file obfuscated using the Kramer script.")
    parser.add_argument("file", type=str, help="Path to the obfuscated file.")
    parser.add_argument("key", type=int, help="Decryption key used to obfuscate the file.")
    parser.add_argument("output", type=str, help="Path to save the deobfuscated file.")
    args = parser.parse_args()

    encrypted_file = args.file
    decryption_key = args.key
    output_file = args.output

    try:
        encrypted_content = detect_encoding(encrypted_file)
    except UnicodeDecodeError:
        print("Unable to detect encoding or read the file.")
        exit(1)

    decrypted_content = deobfuscate(encrypted_content, decryption_key)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_content)

    print(f"Deobfuscated file saved as {output_file}")

if __name__ == "__main__":
    main()
