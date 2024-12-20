# Kramer Deobfuscator

This repository provides a Python script designed to deobfuscate Python scripts obfuscated using the [Kramer](https://github.com/billythegoat356/Kramer) script. It supports automatic encoding detection and decryption using a specified key. The script allows you to recover readable source code from obfuscated Python files.

## Prerequisites

- Python 3.6 or later
- Dependency : chardet

## Usage

The script accepts three arguments:

1. **Input file path**: Path to the obfuscated Python file.
2. **Decryption key**: The integer key used to obfuscate the file.
3. **Output file path**: Path where the deobfuscated file will be saved.

### Example Command

```bash
python deobfuscate.py path/to/obfuscated-file.py 123456 path/to/deobfuscated-file.py
```

### Explanation

- `path/to/obfuscated-file.py`: The obfuscated file you want to decrypt.
- `123456`: The decryption key that was used during obfuscation.
- `path/to/deobfuscated-file.py`: The location where the deobfuscated file will be saved.

## Output

The script will generate the deobfuscated file at the specified output path. If any errors occur during the process, they will be displayed in the terminal for troubleshooting.

## Find the kramer encryption key

To find the encryption key, you can analyze the bytecode and look for the values of the LOAD_CONST fields. You will find a 6-digit key.

Credits : https://x.com/lasq88/status/1834787302255563041
Thanks @lasq88 :)

To obtain the bytecode, you just need to install and use pycdas : https://youtu.be/J_vzY2P_ALE

```bash
   pycdas obfuscate_script.py > obfuscate_script.txt
```

## Example Workflow

1. Clone this repository:

   ```bash
   git clone https://github.com/WizardlyCat/kramer_deobfuscator
   ```

2. Navigate to the directory:

   ```bash
   cd kramer_deobfuscator
   ```

3. Install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python deobfuscate.py obfuscated.py 123456 deobfuscated.py
   ```

5. The deobfuscated file will be saved as `deobfuscated.py`.


## Notes

- Ensure that the decryption key matches the one used during obfuscation with the Kramer script, or the script will produce invalid output.
- If the script detects an unknown encoding or encounters invalid data, it will print an error message.


