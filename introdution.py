import datetime

now = datetime.datetime.now()
name = input("お名前は?")

if now.hour > 4 and now.hour < 9:
	print(name, "さん、おはようございます。")
elif now.hour >= 9 and now.hour < 17:
	print(name, "さん、こんにちは。")
else:
	print(name, "さん、こんばんは。")


