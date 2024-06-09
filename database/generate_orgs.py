"""
"""

import requests
from bs4 import BeautifulSoup


def clean_wiki_entry(entry: str) -> str:
    """
    Cleans a wiki entry to remove details like the refrences setion to prepare for encoding

    :param entry: The wiki entry to clean
    :returns: A cleaned wiki entry
    """
    # Remove the refrences section
    key = "References[edit]"
    references_index = entry.find(key)
    if references_index != -1:
        entry = entry[: references_index + len(key)]

    return entry


def get_orgs() -> list[str]:
    """
    Scrapes Wikipedia for sustanability / ecological organizations

    :returns: A list of the entries
    """
    links_page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_environmental_organizations"
    )
    page_soup = BeautifulSoup(links_page.text)
    link_anchors = page_soup.find("div", id="mw-content-text", _class="").find_all("li")
    links = [
        li.find("a")["href"]
        for li in link_anchors
        if li.find("a") is not None and "href" in li.find("a").attrs.keys()
    ]

    corpus = []
    for link in links:
        if "https:" in link or "File:" in link or "Category:" in link:
            continue
        res = requests.get(f"https://en.wikipedia.org{link}")
        soup = BeautifulSoup(res.text)
        text = soup.find("div", id="mw-content-text").text
        if not text:
            continue
        text = clean_wiki_entry(text)
        corpus.append(text)

    return corpus


def get_people() -> list[str]:
    """
    Gets the people
    """
    res = requests.get(
        "https://en.wikipedia.org/wiki/Category:American_environmentalists"
    )
    american_soup = BeautifulSoup(res.text)
    links = american_soup.find("div", id="mw-pages").find_all("a")
    links = [link["href"] for link in links]

    people = []
    for link in links:
        if (
            "wiki" not in link
            or "FAQ" in link
            or "File:" in link
            or "Category:" in link
        ):
            continue
        res = requests.get(f"https://en.wikipedia.org{link}")
        soup = BeautifulSoup(res.text)
        bio = soup.find("div", id="mw-content-text").text
        bio = clean_wiki_entry(bio)
        people.append(bio)

    return people


def generate_sql_state(sql_id, website, name, contact, bio, vectorized_bio) -> str:
    return f"insert into NGO (id, website, name, contact, bio, vectorized_bio) values ({sql_id}, '{website}', '{name}', '{contact}', '{bio}', '{vectorized_bio}');"
