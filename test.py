import bs4
import requests

res = requests.get('https://cookpad.com')

soup = bs4.BeautifulSoup(res.text, 'html.parser')  
# ↑この部分でサーバーから情報を取得しているからこの後の操作で負担量などは変わらない

# # <title>の情報を取得 タグの中身を取ってくることができるsoup.タグ名で可能
# title_tag = soup.title
# print(title_tag.text)  # レシピ検索No.1／料理レシピ載せるなら クックパッド

# div_tags = soup.find_all('div')
# div_tag_texts = [div_tag.text for div_tag in div_tags]
# # 内包表記　.textの部分のみをとってきた結果　for文の中の処理がdiv_tag.text
# print(div_tag_texts)

# left_containerを検索
# tags = soup.find_all('div', class_='left_container')
# # class_は関数のclassとは別物のclass_という名前の変数名
# tag_texts = [tag.text for tag in tags]
# print(tag_texts)

# 関連サービスのURLを取得
tags = soup.find('div', class_='left_container')  # 最初に見つかったdivクラス？を取ってくる？
a_tag = tags.find('a')  # aタグのみ探してね
url = f"https://cookpad.com{a_tag.attrs['href']}"  # attrsは属性
print(url)