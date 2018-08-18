import math
from pybmkg import PyBMKGApi as gempa
import time

#For Count Distance Between To Coordinates (6371 adalah radius bumi dalam KM)
def haversine(latitude_awal,longitude_awal,latitude_kedua,longitude_kedua, R=6371):
	latitude_awal = math.radians(latitude_awal)
	longitude_awal = math.radians(longitude_awal)
	latitude_kedua = math.radians(latitude_kedua)
	longitude_kedua = math.radians(longitude_kedua)

	a = (math.sin((latitude_kedua-latitude_awal)/2)**2) + ((math.cos(latitude_kedua) * math.cos(latitude_awal)) * (math.sin((longitude_kedua-longitude_awal)/2)**2))
	c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a))
	d = R*c

	return math.ceil(d) #to make it in KM distance :P

def main():

	#Latitude And Longitude Bali
	latitude_bali = float(115.2167)
	longitude_bali = float(-8.650000001)

	print("[Starting] Starting App")
	print("Welcome To EarthQuake Analyzer Powered By: PyBMKG")
	print("[DEBUG] Getting Latest EarthQuake News")
	try:
		temp = gempa.GetLatestEarthQuake()
		tanggal = str(temp["tanggal"])

		bali_terdampak = "Null"
		if ('denpasar' in str(temp["dirasakan"]).lower()) or ('bali' in str(temp["dirasakan"]).lower()):
			bali_terdampak = "Ya"
		else:
			bali_terdampak = "Tidak"

		#dalam BMKG cara baca koordinatnya (longitude, latitude)
		temp_coord = str(temp["koordinat"]).split(', ')
		latitude_gempa = float(temp_coord[1])
		longitude_gempa = float(temp_coord[0])

		print("\n\n[NEWS].................INFO GEMPA...............[NEWS]\n")
		print("\tTanggal: %s" % (temp["tanggal"]))
		print("\tKoordinat: %s Posisi: %s" % (temp["koordinat"], temp["posisi"]))
		print("\tMagnitude: %s SR(Skala Ritcher)" % (temp["magnitude"]))
		print("\tKedalaman: %s" % (temp["kedalaman"]))
		print("\tKeterangan: \n\t%s\n" % (temp["keterangan"]))
		print("\tDirasakan: \n\t%s\n" % (temp["dirasakan"]))
		print("\tJarak Dari Bali (Denpasar): %s KM" % (haversine(latitude_bali, longitude_bali, latitude_gempa, longitude_gempa)) )
		print("\tPerkiraan Bali Terkena Dampak: %s" % (bali_terdampak))
		print("\n[News]..................INFO GEMPA...............[NEWS]\n\n")
		print("Waiting For Newest EarthQuake Info....")
		while True:
			now = gempa.GetLatestEarthQuake()
			time.sleep(5)
			if str(tanggal) != str(now["tanggal"]):

				bali_terdampak = "Null"
				if ('denpasar' in str(temp["dirasakan"]).lower()) or ('bali' in str(temp["dirasakan"]).lower()):
					bali_terdampak = "Ya"
				else:
					bali_terdampak = "Tidak"

				temp_coord = str(now["koordinat"]).split(', ')
				latitude_gempa = float(temp_coord[1])
				longitude_gempa = float(temp_coord[0])

				print("\n\n[NEWS].................INFO GEMPA...............[NEWS]")
				print("\tTanggal: %s" % (temp["tanggal"]))
				print("\tKoordinat: %s Posisi: %s" % (temp["koordinat"], temp["posisi"]))
				print("\tMagnitude: %s SR(Skala Ritcher)" % (temp["magnitude"]))
				print("\tKedalaman: %s" % (temp["kedalaman"]))
				print("\tKeterangan: \n\t%s\n" % (temp["keterangan"]))
				print("\tDirasakan: \n\t%s\n" % (temp["dirasakan"]))
				print("\tJarak Dari Bali (Denpasar): %s KM" % (haversine(latitude_bali, longitude_bali, latitude_gempa, longitude_gempa)) )
				print("\tPerkiraan Bali Terkena Dampak: %s" % (bali_terdampak))
				print("[News]..................INFO GEMPA...............[NEWS]\n\n")
				print("Waiting For Newest EarthQuake Info....")

	except Exception as e:
		print("[Error] Detected Error")
		print(e)

if __name__ == "__main__":
	main()