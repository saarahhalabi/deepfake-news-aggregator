# Deepfake News Aggregator

A Python command-line tool that collects recent news articles about deepfakes, saves them to a database, and uses Claude AI to summarize and categorize each one.

## What it does

- Pulls articles from Google News, The Verge, and BBC News
- Only keeps articles that mention "deepfakes"
- Saves everything to a local database (so you don't get duplicates if you run it twice)
- Uses the Claude API to write a short summary and label each article as: Detection, Misuse, Legislation, Research, or Other

## How to run it

First make sure you have Python installed. Then:

**1. Clone the repo**
git clone https://github.com/saarahhalabi/deepfake-news-aggregator.git
cd deepfake-news-aggregator

**2. Install the required libraries**
pip3 install -r requirements.txt

**3. Add your Anthropic API key**

You need a Claude API key to make this work. You can get one at platform.anthropic.com. Once you have it, run:
export ANTHROPIC_API_KEY=your key here

**4. Run it**
python3 main.py

You should see it printing out each article as it classifies them. When it's done it saves everything to a file called news.db on your computer.

## Files
- `main.py` - runs everything
- `scraper.py` - fetches the articles from news feeds
- `database.py` - sets up the database
- `classifier.py` - sends articles to Claude and gets back a summary
- `requirements.txt` - list of libraries needed
