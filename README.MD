# CSV to N-grams demo (+ `pyinstaller` example)

A simple demo script I created for creating N grams.

Included an example `input.csv`. If you want to use your own data, you will want to make sure you are using the same format (`.csv` file, single column, no header).

Once libraries installed from `requirements.txt`, you can either run:
- `demo_script.py`
- `demo_ngrams.ipynb` - this notebook shows the step-by-step outputs from the main script. 

It's also packageable into a single executable with `pyinstaller`. Just run:

```
pyinstaller --onefile --add-data "input.csv:." demo_script.py
```

`input.csv` - This sample data came from [Crowdflower's Data for Everyone library](https://www.kaggle.com/crowdflower/twitter-airline-sentiment?select=Tweets.csv)