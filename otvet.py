from .. import loader, utils
import random
def register(cb):
	cb(DaunMod())
class DaunMod(loader.Module):
	"""Собеседник(Долбоеб 100%)"""
	strings = {'name':'Otvet na vopros'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def otvetcmd(self, message):
		""".otvet действие
		"""
		do = utils.get_args_raw(message)
		rnd = random.choice(["Ты совсем долбоеб такие вопросы задавать?", "Неа, потому что ты гей", "Могу со 100% уверенностью сказать, что я не уверен", "Не думаю(я сегодня тупой)", "Возможно", "Да", "Определённо нет, ты аутист ещё", "Не знаю, я тебе не Ванга блять!", "Да-Пизда", "Могу со 100% уверенностью сказать, что я не уверен", "Нет, потому что ты ебал мышь", "Определённо да", "Нет, АУЕ", "Возможно(а почему ты сегодня дрочил на  меня, я же бот?)", "Да, я лох", "Определённо нет", "Не знаю", "Не думаю", "Да", "Нет", "Не знаю, я тебе не Ванга блять", "Возможно", "Не думаю", "Определённо да, ты пидарас :3", "Определённо нет","Могу со 100% уверенностью сказать, что я не уверен", "Определённо да", "Могу со 100% уверенностью сказать, что я не уверен", "Да", "Не знаю, но знаю что ты красавчик :D", "Возможно", "Не думаю", "Нет", "Определённо нет", "Нет", "Определённо да", "Возможно", "Не думаю", "Определённо нет, но я думаю что ты топ","Могу со 100% уверенностью сказать, что я  уверен", "Да", "Не знаю, я тебе не Ванга блять!", ])
		await message.edit(f"<b>{do}</b>\n\n<code>{rnd}</code>")


		
