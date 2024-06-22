import argparse
import random

char_mapping = {
    'a': ['а', 'ɑ', 'ɒ'],
    'b': ['Ь', 'Ъ', 'Ƅ'],
    'c': ['с', 'ϲ'],
    'd': ['ԁ', 'ժ'],
    'e': ['е', '℮', 'ҽ'],
    'i': ['і', 'ɪ', 'ı'],
    'l': ['ӏ', 'ʟ'],
    'n': ['ո', 'ռ'],
    'o': ['о', 'σ'],
    'p': ['р', 'ρ'],
    'r': ['г', 'ѓ'],
    's': ['ѕ', 'ʃ'],
    'x': ['х', 'ҳ'],
    'y': ['у', 'ү']
}

def obfuscate(word, mapping, num_recommendations=5):
    recommendations = []
    for _ in range(num_recommendations):
        obfuscated_word = []
        for char in word:
            if char.lower() in mapping:
                # Choose a random replacement if available
                replacements = mapping[char.lower()]
                new_char = random.choice(replacements)
                
                # Preserve the case of the original character
                if char.isupper():
                    new_char = new_char.upper()
                obfuscated_word.append(new_char)
            else:
                obfuscated_word.append(char)
        recommendations.append(''.join(obfuscated_word))
    return recommendations

def main():
    parser = argparse.ArgumentParser(description='Obfuscate a given word using Unicode characters.')
    parser.add_argument('word', type=str, help='The word to obfuscate')
    args = parser.parse_args()

    obfuscated_versions = obfuscate(args.word, char_mapping)
    for version in obfuscated_versions:
        print(version)

if __name__ == '__main__':
    main()