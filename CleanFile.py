def clean_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Remove unprintable characters while preserving newline characters
        cleaned_content = ''.join(c if c.isprintable() or c == '\n' else '' for c in content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print("File cleaned successfully.")
    except Exception as e:
        print("Error cleaning file:", e)



# Example usage:
file_path = "/Users/susheet.kumar/Downloads/ami-026a8f37c2b8cbbfc.md"
clean_file(file_path)
