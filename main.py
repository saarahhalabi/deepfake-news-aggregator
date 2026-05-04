import os
from scraper import fetch_articles
from database import init_db
from classifier import classify_article

def main():
    conn = init_db()
    articles = fetch_articles()
    print(f"Found {len(articles)} articles")

    for article in articles:
        result = conn.execute(
            "INSERT OR IGNORE INTO articles (url, title, source, published) VALUES (?,?,?,?)",
            (article["url"], article["title"], article["source"], article["published"])
        )
        if result.rowcount == 0:
            print(f"Skipping duplicate: {article['title']}")
            continue

        print(f"Classifying: {article['title']}")

        try:
            response = classify_article(article["title"], article["content"])

            lines = response.strip().split("\n")
            summary = next((l.replace("SUMMARY:", "").strip() for l in lines if l.startswith("SUMMARY:")), "")
            category = next((l.replace("CATEGORY:", "").strip() for l in lines if l.startswith("CATEGORY:")), "Other")

        except Exception as e:
            print(f"Error classifying: {e}")
            summary = ""
            category = "Other"

        conn.execute("UPDATE articles SET summary=?, classification=? WHERE url=?",
             (summary, category, article["url"]))

    conn.commit()
    conn.close()
    print("Done!")

if __name__ == "__main__":
    main()
