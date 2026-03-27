# ========================================
# 第7章: HTML解析・スクレイピング基礎
# ========================================
# 実行: pip install beautifulsoup4
# ※ 実際のWebサイトをスクレイピングするにはrequestsも必要
#    pip install requests

from bs4 import BeautifulSoup

# ===== HTMLファイルの解析 =====

# サンプルHTMLを文字列で用意（実際はrequests.get()で取得）
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>選手成績一覧</title>
</head>
<body>
    <h1>FC Python 選手成績</h1>
    <p class="season">2025-2026シーズン</p>
    
    <table id="stats">
        <thead>
            <tr>
                <th>名前</th>
                <th>ポジション</th>
                <th>ゴール</th>
                <th>アシスト</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="name">田中</td>
                <td>FW</td>
                <td>20</td>
                <td>8</td>
            </tr>
            <tr>
                <td class="name">鈴木</td>
                <td>MF</td>
                <td>8</td>
                <td>15</td>
            </tr>
            <tr>
                <td class="name">佐藤</td>
                <td>GK</td>
                <td>0</td>
                <td>1</td>
            </tr>
        </tbody>
    </table>
    
    <ul id="news">
        <li><a href="/news/1">優勝しました！</a></li>
        <li><a href="/news/2">新選手加入</a></li>
        <li><a href="/news/3">練習試合の結果</a></li>
    </ul>
</body>
</html>
"""

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html_content, "html.parser")

# ===== タグの取得 =====
print("=== タイトル ===")
print(soup.title.text)          # → 選手成績一覧
print(soup.h1.text)             # → FC Python 選手成績

# ===== クラス・IDで要素を検索 =====
print("\n=== シーズン ===")
season = soup.find("p", class_="season")
print(season.text)              # → 2025-2026シーズン

# ===== テーブルのデータを取得 =====
print("\n=== 選手成績テーブル ===")
table = soup.find("table", id="stats")
rows = table.find("tbody").find_all("tr")

players = []
for row in rows:
    cols = row.find_all("td")
    player = {
        "name":     cols[0].text,
        "position": cols[1].text,
        "goals":    int(cols[2].text),
        "assists":  int(cols[3].text),
    }
    players.append(player)
    print(f"{player['name']}({player['position']}): {player['goals']}G {player['assists']}A")

# ===== リンクの取得 =====
print("\n=== ニュースリンク ===")
news_list = soup.find("ul", id="news")
for item in news_list.find_all("a"):
    print(f"  {item.text} → {item['href']}")

# ===== データを活用 =====
print("\n=== ゴール数トップ ===")
top = max(players, key=lambda p: p["goals"])
print(f"得点王: {top['name']}（{top['goals']}ゴール）")

# ===== 実際のWebから取得する場合のテンプレート =====
# import requests
# url = "https://example.com"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)
# response.encoding = "utf-8"
# soup = BeautifulSoup(response.text, "html.parser")
# ※ robots.txtを確認し、スクレイピングが許可されているか確認すること
