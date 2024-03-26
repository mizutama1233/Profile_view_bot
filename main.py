from sites import lit_link, solo_to

print("\n1: lit.link\n2: solo.to\n")
website = input("使用するサイトの番号を入力 >> ")

sites = {
    "1": "lit.link",
    "2": "solo.to"
}
name: str = input(f'名前を入力してください: https://{sites[website]}/')

if website == "1":
    lit_link.start(name)
elif website == "2":
    solo_to.start(name)