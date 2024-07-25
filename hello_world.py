
from hofcc import CognitiveCompiler

# Number of programming and spoken languages to use
num_programming_languages = 5
num_spoken_languages = 5

def get_message():
    return "Hello, World!"

message = get_message()
    
compiler = CognitiveCompiler()
results = compiler.compile(message=message, output_dir='output', num_programming_languages=num_programming_languages, num_spoken_languages=num_spoken_languages)
    
for prog_lang, data in results.items():
    print(f"Programming Language: {prog_lang}")
    print(f"Generated Code File: {data['code']}")
    print("Translations:")
    for spoken_lang, translation_path in data['translations'].items():
        print(f"{spoken_lang}: {translation_path}")
    print()

