from bs4 import BeautifulSoup as soup
from requests import get



#I'm currently trying to detect only the earthquake right now cuzz my area often get earthquake so i want to make early notification for my server to notify me at home ^_^
class EarthQuake:
	def __init__(self,proxy=None):
		if proxy == None:
			self.proxy = proxy
		else:
			self.proxy = {
						"http" : proxy,
						"https" : proxy
					}

		self.headers = {
				'Connection': 'keep-alive', 
				'Accept': 'application/json, text/plain, */*', 
				'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36',
				'Accept-Language': 'en-ID,en-US;q=0.8',
				'X-Requested-With': 'com.Info_BMKG',
				'Cache-Control' : 'no-cache'
		}

	def GetLatestEarthQuake(self):
		data_raw = get('http://dataweb.bmkg.go.id/inatews/gempaterkini.xml?decache=0.755139865912497',headers=self.headers,proxies=self.proxy)
		if data_raw.status_code != 200:
			print("There Is Problem With Your Internet Connection or The Website Server is Down")
		else:
			soup_gempa = soup(data_raw.text, 'lxml')
			data_gempa = soup_gempa.find('gempa')
			dict_latest_gempa = {
				"tanggal" : data_gempa.find('tanggal').get_text(),
				"jam" : data_gempa.find('jam').get_text(),
				"koordinat" : data_gempa.find('coordinates').get_text(),
				"posisi" : data_gempa.find('lintang').get_text() + ' '+ data_gempa.find('bujur').get_text(),
				"magnitude" : float(data_gempa.find('magnitude').get_text().replace('SR','')),
				"kedalaman" : data_gempa.find('kedalaman').get_text(),
				"wilayah" : str(data_gempa.find('wilayah').get_text()).replace("\t",' ')
			}
		return dict_latest_gempa

	#i just realized that this method is slower than GetLatestEarthQuake, so this is optional if you want to get more info like perceived earthquake :v
	def GetPerceivedEarthQuake(self):
		data_raw = get('http://dataweb.bmkg.go.id/inatews/gempadirasakan.xml?decache=0.755139865912497',headers=self.headers,proxies=self.proxy)
		if data_raw.status_code != 200:
			print("There Is Problem With Your Internet Connection or The Website Server is Down")
		else:
			soup_gempa = soup(data_raw.text, 'lxml')
			data_gempa = soup_gempa.find('gempa')
			dict_gempa = {
				"tanggal" : data_gempa.find('tanggal').get_text(),
				"koordinat" : data_gempa.find('coordinates').get_text(),
				"posisi" : data_gempa.find('posisi').get_text(),
				"magnitude" : data_gempa.find('magnitude').get_text(),
				"kedalaman" : data_gempa.find('kedalaman').get_text(),
				"keterangan" : str(data_gempa.find('keterangan').get_text()).replace("\t",' '),
				"dirasakan" : str(data_gempa.find('dirasakan').get_text()).replace("\t",' ')
			}
		return dict_gempa

	def GetListEarthQuake(self):
		dict_list_gempa = {}
		data_raw = get('http://dataweb.bmkg.go.id/inatews/gempadirasakan.xml?decache=0.755139865912497', headers=self.headers, proxies=self.proxy)
		if data_raw.status_code != 200:
			print("There Is Problem With Your Internet Connection or The Website Server is Down")
		else:
			soup_gempa = soup(data_raw.text, 'lxml')
			data_gempa = soup_gempa.find_all('gempa')

			for i in range(len(data_gempa)):

				dict_list_gempa[i] = {
					"tanggal" : data_gempa[i].find('tanggal').get_text(),
					"koordinat" : data_gempa[i].find('coordinates').get_text(),
					"posisi" : data_gempa[i].find('posisi').get_text(),
					"magnitude" : data_gempa[i].find('magnitude').get_text(),
					"kedalaman" : data_gempa[i].find('kedalaman').get_text(),
					"keterangan" : data_gempa[i].find('keterangan').get_text(),
					"dirasakan" : data_gempa[i].find('dirasakan').get_text()
				}

		return dict_list_gempa
