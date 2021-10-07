import re
import random
import requests
import discord

# make TOKEN
TOKEN = "TOKEN"

client = discord.Client()

@client.event
async def on_message(message):
	if (re.findall('立てて|たてて|作って|つくって|作成|さくせい', message.content) != []):
		if (re.findall('くるる|クルル', message.content) != []):

			send_message = ""
			rand_num = random.randint(10, 99)

			if rand_num % 3 == 0:
				send_message = 'いいですねぇ いいですねぇ！ちゃちゃっと立てますよぅ！'
			elif rand_num %3 == 1:
				send_message = 'さーば立てるんですかぁ？ふっふっふー。いいでしょう！くるるんお手製全自動しゅみれーた生成器を動かしましょーっ！'
			else:
				send_message = 'さーばぁ？あー立てるんですかぁ？いまくるるんはねむいのでさくっとやっちゃいますよぉー。ぽちっとな'

			await message.channel.send(send_message)

		    api_url = 'https://furuyoni-simulator.herokuapp.com/tables.create'

		    res = requests.post(api_url).json()

			p1 = res['p1Url']
			p2 = res['p2Url']
			watch = res['watchUrl']

			if rand_num % 3 == 0:
				send_message = 'これで完了ですぅ！せっかくなのでぇ、つくったさーばをちょろーっといじってらいふ２０点とかくるるんお手製神渉装置を7枚つんでみたりしたいですねぇ！わっくわくしますねぇ！'
			elif rand_num %3 == 1:
				send_message = 'くるるーん☆ひらめきましたっ！神渉装置でこのしゅみれーたをくるるん専用しゅみれーたにしちゃいましょう！きっとぐれいとぅでみすてりぃなゲームができますよぉ！'
			else:
				send_message = 'たてましたぁ！ついでにさーばにはくるるんしか宿せないようにしておいたのでぇ、いーっぱいくるるんのぱぅわーを体験できますよぉ！たのしみですねぇ！'

			send_message = "するひと１: " + str(p1.get_attribute("href")) + "\n" + "するひと２: " + str(p2.get_attribute("href")) + "\n" + "みるひと: " + str(watch.get_attribute("href")) + "\n" + send_message

			await message.channel.send(send_message)


print("start server")
client.run(TOKEN)
