# Gomo phone number scoring

## Description

This is a simple script to find the best phone number available on https://buy.gomo.sg/select-number/

## Scoring system

Number are divided into 2 and 4 digits to help algorithm to find patterns.

- Check if multiple of 10 or 11 (2 digits)
- Check if multiple of 1111 (4 digits)
- Check if suite if numbers exists (4 digits) (ex: 1234, 5432) ascending and descending
- Check if suite of decimal exists (2 digits) (ex: 21, 22) only ascending
- Check if favorite numbers exists (2 digits and 4 digits)
- Check if numbers appears multiple times (2 digits and 4 digits)

## How to use

Define your favorite numbers and adjust the score points

```python
scorePoints = {
  "multiple10": 2,
  "multiple11": 2,
  "multiple1111": 10,
  "suiteOfNumbers": 8,
  "suiteOfDecimals": 6,
  "favorite2digits": 3,
  "favorite4digits": 6,
  "multiple2digits": 4,
  "multiple4digits": 20
}

favorite2digits = ["21"]
favorite4digits = ["0012"]
```

Run the script

```bash
python3 gomo.py
```
