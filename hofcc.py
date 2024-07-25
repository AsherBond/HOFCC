import os
import random
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, MarianMTModel, MarianTokenizer

class CognitiveCompiler:
    """
    A class representing the cognitive compiler for generating code and translations.
    
    This compiler uses pre-trained models to generate 'Hello, World!' code snippets in various 
    programming languages and translates those snippets into multiple spoken languages.
    """

    def __init__(self):
        """
        Initialize the CognitiveCompiler with pre-trained models for code generation and translation.
        """
        print("Loading DistilGPT-2 model...")
        self.code_model = GPT2LMHeadModel.from_pretrained('distilgpt2')
        self.code_tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')

        print("Loading translation tokenizers...")
        self.translation_tokenizers = {
            'es': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es'),
            'fr': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-fr'),
            'de': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-de'),
            'zh': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh'),
            'ru': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-ru')
        }
        self.programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
        self.spoken_languages = ['es', 'fr', 'de', 'zh', 'ru']

    def generate_code(self, language):
        """
        Generate 'Hello, World!' code in the specified programming language.
        
        Args:
            language (str): The programming language in which to generate the code.
        
        Returns:
            str: The generated 'Hello, World!' code snippet.
        """
        print(f"Generating 'Hello, World!' code in {language}...")
        prompt = f"Write 'Hello, World!' in {language}."
        input_ids = self.code_tokenizer.encode(prompt, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
        output = self.code_model.generate(input_ids, attention_mask=attention_mask, max_length=50, pad_token_id=self.code_tokenizer.eos_token_id)
        code = self.code_tokenizer.decode(output[0], skip_special_tokens=True)
        return code

    def translate_text(self, text, target_lang):
        """
        Translate the given text to the specified target language.
        
        Args:
            text (str): The text to translate.
            target_lang (str): The target language code (e.g., 'es' for Spanish).
        
        Returns:
            str: The translated text.
        """
        print(f"Loading translation model for {target_lang}...")
        model = MarianMTModel.from_pretrained(f'Helsinki-NLP/opus-mt-en-{target_lang}')
        tokenizer = self.translation_tokenizers[target_lang]
        
        print(f"Translating text to {target_lang}...")
        input_ids = tokenizer.encode(text, return_tensors='pt')
        translated_ids = model.generate(input_ids)
        translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        return translated_text

    def compile(self, output_dir='output', num_programming_languages=5, num_spoken_languages=5):
        """
        Compile the application to generate 'Hello, World!' in multiple programming and spoken languages.
        
        Args:
            output_dir (str): The directory to save the generated files.
            num_programming_languages (int): The number of programming languages to use.
            num_spoken_languages (int): The number of spoken languages to use.
        
        Returns:
            dict: A dictionary containing the generated code snippets and their translations.
        """
        print(f"Creating output directory at {output_dir}...")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print("Selecting languages...")
        selected_programming_languages = random.sample(self.programming_languages, num_programming_languages)
        selected_spoken_languages = random.sample(self.spoken_languages, num_spoken_languages)

        results = {}
        
        for prog_lang in selected_programming_languages:
            try:
                code = self.generate_code(prog_lang)
            except Exception as e:
                print(f"Error generating code for {prog_lang}: {e}")
                continue

            prog_lang_dir = os.path.join(output_dir, prog_lang)
            if not os.path.exists(prog_lang_dir):
                os.makedirs(prog_lang_dir)

            code_file_path = os.path.join(prog_lang_dir, f'hello_world.{prog_lang.lower()}')
            print(f"Writing code to {code_file_path}...")
            with open(code_file_path, 'w') as code_file:
                code_file.write(code)

            translations = {}
            for lang in selected_spoken_languages:
                try:
                    translated_text = self.translate_text(code, lang)
                except Exception as e:
                    print(f"Error translating to {lang}: {e}")
                    continue
                translations[lang] = translated_text
                translation_file_path = os.path.join(prog_lang_dir, f'hello_world_{lang}.txt')
                print(f"Writing translation to {translation_file_path}...")
                with open(translation_file_path, 'w') as translation_file:
                    translation_file.write(translated_text)

            results[prog_lang] = {
                'code': code_file_path,
                'translations': {lang: os.path.join(prog_lang_dir, f'hello_world_{lang}.txt') for lang in translations}
            }
        
        return results

