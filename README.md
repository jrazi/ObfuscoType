# ObfuscoType

ObfuscoType is a Python script that obfuscates text using Unicode characters. It can be used to bypass simple rule-based text filters for English writings.

## Overview

This tool replaces standard Latin characters with visually similar Unicode alternatives. It generates multiple obfuscated versions of the input text, preserving the original case of each character. The goal is to make the text harder to detect by simple text filters, while keeping it readable for target human readers.

## Installation

No installation is required. Simply clone the repository or download the `obfuscate.py` file.

## Usage

Run the script from the command line, providing the text to obfuscate as an argument:

```bash
python obfuscate.py "Your text here"
```

This will output several versions of the input text, with each version having some characters replaced by visually similar Unicode characters.

### Example

**Input**:

```bash
python obfuscate.py "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters"
```

**Output**:

```bash
Th℮ роıոt σf uѕіոg ʟσгҽm Iрʃum ɪѕ thɑt іt hɑѕ ɒ mогҽ-оѓ-ӏеʃʃ ոσѓmɑӏ ԁıʃtгіƄutıоո σf ӏ℮tt℮гѕ
Thҽ ρоіոt σf uʃıռg ʟσгеm Ірѕum ıʃ thɑt ɪt hɒѕ ɑ mσге-σг-ӏҽʃʃ ոσгmаӏ ԁɪʃtѓіЪutіоո оf ʟеttегʃ
Thҽ ρσіոt оf uʃıոg ʟσѓ℮m Iρѕum іʃ thаt іt hɒʃ ɑ mσгҽ-ог-ӏ℮ʃʃ ռσѓmɑӏ ժіѕtгɪЪutɪоռ оf ӏҽttҽѓʃ
Thҽ ρσıռt σf uʃіռg ʟσѓеm Ірѕum ıѕ thɒt ıt hɒѕ ɑ mоѓе-σг-ʟеѕѕ ռоѓmаʟ ԁіʃtѓıЬutɪоո σf ʟеttҽгѕ
Thҽ роіոt оf uѕіոg Ӏогҽm Іρѕum іѕ thɑt іt hɒʃ ɒ mσгҽ-ог-ʟеѕѕ ռσѓmɑʟ ժɪѕtѓіƄutɪσո σf ʟеttҽгʃ
```


## License

This project is unlicensed and released into the public domain.