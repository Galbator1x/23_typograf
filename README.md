# Typograf Service

This is typograph with the web interface. Typograph - is a tool of the russian text preparation
for publication on the Web. He takes over the most routine tasks, such as: – replacement
quotes ' and " to « » - in the right places to replace hyphens with dashes - replacing
dashes for a short dash in phone numbers - binding numbers followed by the words non-breaking
hyphen - removing extra spaces and line breaks - binding unions and any words of 1-2 symbol
followed by the words.

## Installation

```
pip install -r requirements.txt
```

## Usage

```
$ python3
>>> from typograph import typograph
>>> typograph('"qwe"')
'«qwe»'
```
or use web interface
```
$ python server.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Requirements

- Python >= 3.5

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
