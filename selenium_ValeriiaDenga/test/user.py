class User (object):

	def __init__(self, username=None, password=None, email=None):
		self.username = username
		self.password = password
		self.email = email

@classmethod
def Admin (cls):
	return cls (username = "admin", password = "admin")

class Movie (object):

	def __init__(self, imdbid=None, name = None, aka = None, year = none, duration = none, rating = none, text_languages_0=None, subtitles =None, audio = None, video = None, country= None):
		self.imdbid = imdbid
		self.name = name
		self.aka = aka
		self.year = year
		self.duration = duration
		self.rating = rating
		self.text_languages_0=text_languages_0
		self.subtitles=subtitles
		self.audio = audio
		self.video = video
		self.country= country
		
@classmethod
def Movie (cls)
	return cls (imdbid = "1234578", name= "Cold Heart", aka = "Frozen", year = "2016", duration = "202", rating = "2", text_languages_0 = "French, German, English", subtitles = "no", audio = "good", video = "excellent", country = "USA" )
