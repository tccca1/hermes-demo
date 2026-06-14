import urllib.request, xml.etree.ElementTree as ET, json, os, time

DB_PATH = os.path.expanduser("~/.blogwatcher_data.json")

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"articles": [], "last_scan": {}}

def save_db(db):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def fetch_feed(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Hermes-BlogWatcher/1.0"})
    resp = urllib.request.urlopen(req, timeout=15)
    data = resp.read()
    articles = []
    root = ET.fromstring(data)
    for item in root.iter("item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        pub_date = item.findtext("pubDate", "")
        articles.append({"title": title.strip(), "url": link.strip(), "date": pub_date.strip()})
    if not articles:
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.iter("{http://www.w3.org/2005/Atom}entry"):
            title = entry.findtext("atom:title", "", ns)
            link_el = entry.find("atom:link", ns)
            link = link_el.get("href", "") if link_el is not None else ""
            updated = entry.findtext("atom:updated", "", ns)
            articles.append({"title": title.strip(), "url": link.strip(), "date": updated.strip()})
    return articles

def scan_blogs():
    blogs = [
        {"name": "Simon Willison", "url": "https://simonwillison.net/atom/everything/"},
        {"name": "Hacker News", "url": "https://hnrss.org/frontpage"},
        {"name": "Planet Python", "url": "https://planetpython.org/rss20.xml"},
        {"name": "Real Python", "url": "https://realpython.com/atom.xml"},
        {"name": "Dev.to", "url": "https://dev.to/feed"},
    ]
    db = load_db()
    new_articles = []
    for blog in blogs:
        name = blog["name"]
        url = blog["url"]
        existing_keys = {f"{a['blog']}::{a['url']}" for a in db["articles"]}
        try:
            articles = fetch_feed(url)
            count = 0
            for a in articles:
                key = f"{name}::{a['url']}"
                if key not in existing_keys:
                    a["blog"] = name
                    new_articles.append(a)
                    db["articles"].append(a)
                    count += 1
            db["last_scan"][name] = time.strftime("%Y-%m-%d %H:%M")
            print(f"  {name}: {len(articles)} articles, {count} new")
        except Exception as e:
            print(f"  {name}: ERROR - {e}")
    save_db(db)
    return new_articles

if __name__ == "__main__":
    print("Blog Monitor Scan")
    print("=" * 40)
    new = scan_blogs()
    print(f"\nTotal new: {len(new)}")
    for a in new[:5]:
        print(f"\n  {a['title']}")
        print(f"  {a['blog']}")
        print(f"  {a['url']}")
