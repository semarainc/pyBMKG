from bs4 import BeautifulSoup as soup
from requests import get

#I'm currently trying to detect only the earthquake right now cuzz my area often get earthquake so i want to make early notification for my server to notify me at home ^_^

def GetLatestEarthQuake():
	data_raw = get('http://dataweb.bmkg.go.id/inatews/gempadirasakan.xml')
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

def GetListEarthQuake():
	dict_list_gempa = {}
	data_raw = get('http://dataweb.bmkg.go.id/inatews/gempadirasakan.xml')
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
