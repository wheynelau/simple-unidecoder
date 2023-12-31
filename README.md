# simple-unidecoder

This is a simple unidecoder that converts unicode characters to ASCII characters. It is built using [Streamlit](https://www.streamlit.io/).
It uses the [unidecode](https://pypi.org/project/Unidecode/) library to convert special characters to ASCII characters. This is especially useful when you are working with microsoft word that contains special characters and you want to convert them to ASCII characters.

- [simple-unidecoder](#simple-unidecoder)
  - [To run on local machine](#to-run-on-local-machine)
  - [Known issues](#known-issues)


## To run on local machine

1. Requirements:
    - python
    - pip

2. Run these commands in your terminal:

```bash
git clone https://github.com/wheynelau/simple-unidecoder.git
cd simple-unidecoder
pip install -r requirements.txt
streamlit run 1-Converter.py
```

## Known issues

The known issues are shared by the unidecode library. You can find the list of known issues [here](https://pypi.org/project/Unidecode/).

Here are the more important ones:

1. German umlauts are transliterated incorrectly
2. Japanese Kanji is transliterated as Chinese

Ideally, it is best to use this for english only.