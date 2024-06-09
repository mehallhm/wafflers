"""
"""

import io
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix, save_npz
import numpy as np
from faker import Faker


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

    entry = entry.replace("\n", " ")
    entry = entry.replace("'", "")

    return entry


def get_org_links() -> list[str]:
    """ """
    links_page = requests.get(
        "https://en.wikipedia.org/wiki/List_of_environmental_organizations"
    )
    page_soup = BeautifulSoup(links_page.text, features="html.parser")
    link_anchors = page_soup.find("div", id="bodyContent").find_all("li")
    links = [
        li.find("a")["href"]
        for li in link_anchors
        if li.find("a") is not None and "href" in li.find("a").attrs.keys()
    ]

    shortened_links = links[: links.index("/wiki/Woodland_Trust")]

    return shortened_links


def get_orgs(links: list[str]) -> list[dict[str:str]]:
    """
    Scrapes Wikipedia for sustanability / ecological organizations

    :returns: A list of the entries
    """

    corpus = []
    for link in links:
        # None of the good links have a `:`, only bad things do
        if ":" in link:
            continue

        res = requests.get(f"https://en.wikipedia.org{link}")
        soup = BeautifulSoup(res.text, features="html.parser")
        print(f"Processing: {link}")
        name = soup.find("h1", id="firstHeading").text
        text = soup.find("div", id="mw-content-text").text
        if not text:
            continue
        text = clean_wiki_entry(text)
        corpus.append({"name": name, "text": text})

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


def sparse_matrix_to_string(sparse_matrix):
    """
    Converts a SciPy sparse matrix to a string representation.

    Parameters:
    sparse_matrix (scipy.sparse.spmatrix): The input sparse matrix.

    Returns:
    str: String representation of the sparse matrix.
    """
    if not isinstance(sparse_matrix, csr_matrix):
        raise ValueError("Input matrix must be a CSR (Compressed Sparse Row) matrix.")

    rows, cols = sparse_matrix.shape
    entries = []

    # Get the row, col, and data arrays from the sparse matrix
    row_indices, col_indices = sparse_matrix.nonzero()
    data = sparse_matrix.data

    # Iterate through the non-zero elements
    for i in range(len(data)):
        row = row_indices[i]
        col = col_indices[i]
        value = data[i]
        entries.append(f"({row}, {col}, {value})")

    return f"SparseMatrix({rows}, {cols}, [{', '.join(entries)}])"


def main():
    fake = Faker()
    links = get_org_links()
    orgs = get_orgs(links)

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([org["text"] for org in orgs])

    sql_statements = [
        generate_sql_state(
            i,
            fake.domain_name(),
            org["name"],
            fake.ascii_email(),
            org["text"],
            sparse_matrix_to_string(vectors[i]),
        )
        for i, org in enumerate(orgs)
    ]

    try:
        with open("output.sql", "w", encoding="UTF-8") as file:
            for statement in sql_statements:
                file.write(statement + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
