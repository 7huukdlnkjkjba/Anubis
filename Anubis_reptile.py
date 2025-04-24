# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import random
import time
from bs4 import BeautifulSoup
import os
import sys

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]


def get_html(url):
    headers = {
        "User-Agent": random.choice(user_agents)
    }
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        return response.read().decode("utf-8", errors="ignore")
    except:
        print(f"访问失败：{url}")
        return ""


def search_duckduckgo(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("a", class_="result__a")

    output = ["🔍 DuckDuckGo 搜索结果：\n"]
    for a in results[:5]:
        output.append(f"{a.get_text(strip=True)}\n{a['href']}\n")
    return "\n".join(output)


def search_bing(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("li", class_="b_algo")

    output = ["🔍 Bing 搜索结果：\n"]
    for r in results[:5]:
        title_tag = r.find("h2")
        if title_tag:
            a_tag = title_tag.find("a")
            if a_tag and a_tag.has_attr("href"):
                title = a_tag.get_text(strip=True)
                link = a_tag["href"]
                output.append(f"{title}\n{link}\n")
    return "\n".join(output)


def search_github(query):
    url = f"https://github.com/search?q={urllib.parse.quote(query)}"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    repo_links = soup.find_all("a", href=True)

    output = ["🔍 GitHub 搜索结果：\n"]
    seen = set()
    for link in repo_links:
        href = link["href"]
        if href.count("/") == 2 and not href.endswith("/search") and href not in seen:
            seen.add(href)
            output.append(f"{link.get_text(strip=True)}\nhttps://github.com{href}\n")
            if len(seen) >= 5:
                break
    return "\n".join(output)


def save_results(content, filename="search_results.txt"):
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ 搜索结果已保存到：{filepath}")


def main():
    if len(sys.argv) >= 4:
        query = " ".join(sys.argv[3:])
        if sys.argv[1] == "-d":
            results = search_duckduckgo(query)
        elif sys.argv[1] == "-g":
            results = search_github(query)
        elif sys.argv[1] == "-b":
            results = search_bing(query)
        else:
            print("无效的选项。使用 -d, -g 或 -b。")
            return

        save_results(results)
    else:
        print("用法: python Anubis_reptile.py -d/-g/-b \"关键词\"")
        print("示例: python Anubis_reptile.py -d \"Python 编程\"")
        print("示例: python Anubis_reptile.py -g \"Machine Learning\"")
        print("示例: python Anubis_reptile.py -b \"OpenAI GPT\"")


if __name__ == "__main__":
    main()
