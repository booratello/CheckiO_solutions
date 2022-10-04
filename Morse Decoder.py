"""
Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input: The secret message (string).
Output: The decrypted text (string).
"""

# So... I tried to do this using binary search.
# I couldn't make a function to build a binary tree and wrote it myself.
# It wasn't easy, but... it works!

ENG_MORSE_ALPHANUMERIC = {
                        '.': {
                            'symbol': 'e',
                            '.': {
                                'symbol': 'i',
                                '.': {
                                    'symbol': 's',
                                    '.': {
                                        'symbol': 'h',
                                        '.': {
                                            'symbol': '5'
                                        },
                                        '-': {
                                            'symbol': '4'
                                        }
                                    },
                                    '-': {
                                        'symbol': 'v',
                                        '-': {
                                            'symbol': '3'
                                        }
                                    }
                                },
                                '-': {
                                    'symbol': 'u',
                                    '.': {
                                        'symbol': 'f',
                                    },
                                    '-': {
                                        '.': {
                                            '.': {
                                                'symbol': '?'
                                            },
                                            '-': {
                                                'symbol': '_'
                                            }
                                        },
                                        '-': {
                                            'symbol': '2'
                                        }
                                    }
                                }
                            },
                            '-': {
                                'symbol': 'a',
                                '.': {
                                    'symbol': 'r',
                                    '.': {
                                        'symbol': 'l',
                                        '-': {
                                            '.': {
                                                'symbol': '\"'
                                            }
                                        }
                                    },
                                    '-': {
                                        '.': {
                                            'symbol': '+',
                                            '-': {
                                                'symbol': '.'
                                            }
                                        }
                                    }
                                },
                                '-': {
                                    'symbol': 'w',
                                    '.': {
                                        'symbol': 'p',
                                        '-': {
                                            '.': {
                                                'symbol': '@'
                                            }
                                        }
                                    },
                                    '-': {
                                        'symbol': 'j',
                                        '-': {
                                            'symbol': '1',
                                            '.': {
                                                'symbol': '\''
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        '-': {
                            'symbol': 't',
                            '.': {
                                'symbol': 'n',
                                '.': {
                                    'symbol': 'd',
                                    '.': {
                                        'symbol': 'b',
                                        '.': {
                                            'symbol': '6',
                                            '-': {
                                                'symbol': '-'
                                            }
                                        },
                                        '-': {
                                            'symbol': '='
                                        }
                                    },
                                    '-': {
                                        'symbol': 'x',
                                        '.': {
                                            'symbol': '/'
                                        }
                                    }
                                },
                                '-': {
                                    'symbol': 'k',
                                    '.': {
                                        'symbol': 'c',
                                        '-': {
                                            '.': {
                                                'symbol': ';'
                                            },
                                            '-': {
                                                'symbol': '!'
                                            }
                                        }
                                    },
                                    '-': {
                                        'symbol': 'y',
                                        '.': {
                                            '-': {
                                                'symbol': '()'
                                            }
                                        }
                                    }
                                }
                            },
                            '-': {
                                'symbol': 'm',
                                '.': {
                                    'symbol': 'g',
                                    '.': {
                                        'symbol': 'z',
                                        '.': {
                                            'symbol': '7'
                                        },
                                        '-': {
                                            '-': {
                                                'symbol': ','
                                            }
                                        }
                                    },
                                    '-': {
                                        'symbol': 'q'
                                    }
                                },
                                '-': {
                                    'symbol': 'o',
                                    '.': {
                                        '.': {
                                            'symbol': '8',
                                            '.': {
                                                'symbol': ':'
                                            }
                                        }
                                    },
                                    '-': {
                                        '.': {
                                            'symbol': '9'
                                        },
                                        '-': {
                                            'symbol': '0'
                                        }
                                    }
                                }
                            }
                        }
                    }


def research_tree(tree, code_symbol):
    return research_tree(tree[f'{code_symbol[0]}'], code_symbol[1:]) \
        if len(code_symbol) > 0 else tree['symbol']


def morse_decoder(code_phrase):
    code_phrase = code_phrase.split('   ')
    decode_phrase = ''
    for word in code_phrase:
        word = word.split(' ')
        for symbol in word:
            try:
                decode_phrase += research_tree(ENG_MORSE_ALPHANUMERIC, symbol)
            except KeyError:
                decode_phrase += '<n/a>'
        decode_phrase += ' '
    decode_phrase = decode_phrase.rstrip().capitalize()
    return decode_phrase


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
