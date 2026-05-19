import re
import sys

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = {
        r'#FFC107': '#0D5EAF',
        r'255,\s*193,\s*7': '13, 94, 175',
        r'#FFD54F': '#4A90E2',
        r'#FFAD01': '#005b9f',
        r'#FFB000': '#005b9f',
        r'255,\s*176,\s*0': '0, 91, 159',
        r'#FFC733': '#4A90E2',
        r'#E09900': '#0D5EAF',
        r'#FFEB3B': '#E0F2FE',
        r'255,\s*235,\s*59': '224, 242, 254',
        r'#ff9800': '#f59e0b', # ensure warning orange isn't modified if it's explicitly typed, but wait, warning orange is fine as orange!
        r'255,\s*152,\s*0': '245, 158, 11' # orange RGB
    }
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
if __name__ == "__main__":
    process_file(sys.argv[1])
