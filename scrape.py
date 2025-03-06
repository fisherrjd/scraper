import requests
from bs4 import BeautifulSoup

def get_hacker_news_top_story():
    """
    Scrapes the top story from Hacker News.
    """
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    top_story = soup.find("tr", class_="athing submission")

    if top_story:
        title_element = top_story.find("span", class_="titleline")
        title = title_element.text if title_element else "Title not found"
        link_element = (
            title_element.find("a")["href"]
            if title_element and title_element.find("a")
            else None
        )

        return {
            "title": title,
            "link": link_element,
        }
    else:
        return {"error": "Top story not found."}

if __name__ == "__main__":
    top_story_data = get_hacker_news_top_story()

    if "error" in top_story_data:
        print(f"Error: {top_story_data['error']}")
    else:
        print(f"Top Story:")
        print(f"  Title: {top_story_data['title']}")
        print(f"  Link: {top_story_data['link']}")