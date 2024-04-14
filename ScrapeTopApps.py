import requests
import pandas as pd

"""
App Store Scraper utility classes
"""
import json

class AppStoreUtils:
	"""
	Helper class to access the names of the other classes
	"""
	@staticmethod
	def get_entries(clazz_name):
		"""
		Get the members and their names from the function

		:param object clazz_name: the class object be called. 
		:returns object method_names: a JSON representation of the names.
		"""
		methods  = {}
		for collection in dir(clazz_name):
			if not collection.startswith('__'):
				methods[str(collection)] = getattr(clazz_name, str(collection))
		return methods

class AppStoreCollections:
	"""
	App store collection IDs

	Borrowed from https://github.com/facundoolano/app-store-scraper. These are
	the various collections displayed in the app store, usually on the front
	page.
	"""
	TOP_MAC = 'topmacapps'
	TOP_FREE_MAC = 'topfreemacapps'
	TOP_GROSSING_MAC = 'topgrossingmacapps'
	TOP_PAID_MAC = 'toppaidmacapps'
	NEW_IOS = 'newapplications'
	NEW_FREE_IOS = 'newfreeapplications'
	NEW_PAID_IOS = 'newpaidapplications'
	TOP_FREE_IOS = 'topfreeapplications'
	TOP_FREE_IPAD = 'topfreeipadapplications'
	TOP_GROSSING_IOS = 'topgrossingapplications'
	TOP_GROSSING_IPAD = 'topgrossingipadapplications'
	TOP_PAID_IOS = 'toppaidapplications'
	TOP_PAID_IPAD = 'toppaidipadapplications'

class AppStoreCategories:
	"""
	App Store category IDs

	Borrowed from https://github.com/facundoolano/app-store-scraper. These are
	the app's categories.
	"""
	BOOKS = 6018
	BUSINESS = 6000
	CATALOGS = 6022
	EDUCATION = 6017
	ENTERTAINMENT = 6016
	FINANCE = 6015
	FOOD_AND_DRINK = 6023
	GAMES = 6014
	GAMES_ACTION = 7001
	GAMES_ADVENTURE = 7002
	GAMES_ARCADE = 7003
	GAMES_BOARD = 7004
	GAMES_CARD = 7005
	GAMES_CASINO = 7006
	GAMES_DICE = 7007
	GAMES_EDUCATIONAL = 7008
	GAMES_FAMILY = 7009
	GAMES_MUSIC = 7011
	GAMES_PUZZLE = 7012
	GAMES_RACING = 7013
	GAMES_ROLE_PLAYING = 7014
	GAMES_SIMULATION = 7015
	GAMES_SPORTS = 7016
	GAMES_STRATEGY = 7017
	GAMES_TRIVIA = 7018
	GAMES_WORD = 7019
	HEALTH_AND_FITNESS = 6013
	LIFESTYLE = 6012
	MAGAZINES_AND_NEWSPAPERS = 6021
	MAGAZINES_ARTS = 13007
	MAGAZINES_AUTOMOTIVE = 13006
	MAGAZINES_WEDDINGS = 13008
	MAGAZINES_BUSINESS = 13009
	MAGAZINES_CHILDREN = 13010
	MAGAZINES_COMPUTER = 13011
	MAGAZINES_FOOD = 13012
	MAGAZINES_CRAFTS = 13013
	MAGAZINES_ELECTRONICS = 13014
	MAGAZINES_ENTERTAINMENT = 13015
	MAGAZINES_FASHION = 13002
	MAGAZINES_HEALTH = 13017
	MAGAZINES_HISTORY = 13018
	MAGAZINES_HOME = 13003
	MAGAZINES_LITERARY = 13019
	MAGAZINES_MEN = 13020
	MAGAZINES_MOVIES_AND_MUSIC = 13021
	MAGAZINES_POLITICS = 13001
	MAGAZINES_OUTDOORS = 13004
	MAGAZINES_FAMILY = 13023
	MAGAZINES_PETS = 13024
	MAGAZINES_PROFESSIONAL = 13025
	MAGAZINES_REGIONAL = 13026
	MAGAZINES_SCIENCE = 13027
	MAGAZINES_SPORTS = 13005
	MAGAZINES_TEENS = 13028
	MAGAZINES_TRAVEL = 13029
	MAGAZINES_WOMEN = 13030
	MEDICAL = 6020
	MUSIC = 6011
	NAVIGATION = 6010
	NEWS = 6009
	PHOTO_AND_VIDEO = 6008
	PRODUCTIVITY = 6007
	REFERENCE = 6006
	SHOPPING = 6024
	SOCIAL_NETWORKING = 6005
	SPORTS = 6004
	TRAVEL = 6003
	UTILITIES = 6002
	WEATHER = 6001

class AppStoreMarkets:
	"""
	App Store store IDs per country

	Borrowed from https://github.com/facundoolano/app-store-scraper.
	"""
	DZ = 143563
	AO = 143564
	AI = 143538
	AR = 143505
	AM = 143524
	AU = 143460
	AT = 143445
	AZ = 143568
	BH = 143559
	BB = 143541
	BY = 143565
	BE = 143446
	BZ = 143555
	BM = 143542
	BO = 143556
	BW = 143525
	BR = 143503
	VG = 143543
	BN = 143560
	BG = 143526
	CA = 143455
	KY = 143544
	CL = 143483
	CN = 143465
	CO = 143501
	CR = 143495
	HR = 143494
	CY = 143557
	CZ = 143489
	DK = 143458
	DM = 143545
	EC = 143509
	EG = 143516
	SV = 143506
	EE = 143518
	FI = 143447
	FR = 143442
	DE = 143443
	GB = 143444
	GH = 143573
	GR = 143448
	GD = 143546
	GT = 143504
	GY = 143553
	HN = 143510
	HK = 143463
	HU = 143482
	IS = 143558
	IN = 143467
	ID = 143476
	IE = 143449
	IL = 143491
	IT = 143450
	JM = 143511
	JP = 143462
	JO = 143528
	KE = 143529
	KW = 143493
	LV = 143519
	LB = 143497
	LT = 143520
	LU = 143451
	MO = 143515
	MK = 143530
	MG = 143531
	MY = 143473
	ML = 143532
	MT = 143521
	MU = 143533
	MX = 143468
	MS = 143547
	NP = 143484
	NL = 143452
	NZ = 143461
	NI = 143512
	NE = 143534
	NG = 143561
	NO = 143457
	OM = 143562
	PK = 143477
	PA = 143485
	PY = 143513
	PE = 143507
	PH = 143474
	PL = 143478
	PT = 143453
	QA = 143498
	RO = 143487
	RU = 143469
	SA = 143479
	SN = 143535
	SG = 143464
	SK = 143496
	SI = 143499
	ZA = 143472
	ES = 143454
	LK = 143486
	SR = 143554
	SE = 143456
	CH = 143459
	TW = 143470
	TZ = 143572
	TH = 143475
	TN = 143536
	TR = 143480
	UG = 143537
	UA = 143492
	AE = 143481
	US = 143441
	UY = 143514
	UZ = 143566
	VE = 143502
	VN = 143471
	YE = 143571


class AppStoreException(Exception):
	"""
	Thrown when an error occurs in the App Store scraper
	"""
	pass


COUNTRIES = [
    'ad', # Andorra
    'at', # Austria
    'be', # Belgium
    'ca', # Canada
    'ch', # Switzerland
    'cy', # Cyprus
    'cz', # Czechia
    'de', # Germany
    'dk', # Denmark
    'ee', # Estonia
    'es', # Spain
    'fi', # Finland
    'fr', # France
    'gb', # Great Britain
    'gi', # Gibraltar
    'gr', # Greece
    'hr', # Hungary
    'ie', # Ireland
    'im', # Isle of Man
    'is', # Iceland
    'it', # Italy
    'lu', # Luxembourg
    'lv', # Latvia
    'mc', # Monaco
    'me', # Montenegro
    'mt', # Malta
    'nl', # Netherlands
    'no', # Norway
    'pl', # Poland
    'pt', # Portugal
    'ro', # Romania
    'rs', # Serbia
    'se', # Sweden
    'si', # Slovenia
    'sk', # Slovakia
    'sr', # ???
    'tr', # Turkey
    'ua', # Ukraine
    'us', # United States of America
]
"""
iTunes App Store Scraper
"""
import requests
import json
import time
import re
import os
from datetime import datetime

from urllib.parse import quote_plus

class Regex:
	STARS = re.compile(r"<span class=\"total\">[\s\S]*?</span>")


class AppStoreScraper:
	"""
	iTunes App Store scraper

	This class implements methods to retrieve information about iTunes App
	Store apps in various ways. The methods are fairly straightforward. Much
	has been adapted from the javascript-based app-store-scraper package, which
	can be found at https://github.com/facundoolano/app-store-scraper.
	"""

	def get_app_ids_for_query(self, term, num=50, page=1, country="us", lang="us"):
		"""
		Retrieve suggested app IDs for search query

		:param str term:  Search query
		:param int num:  Amount of items to return per page, default 50
		:param int page:  Amount of pages to return
		:param str country:  Two-letter country code of store to search in,
		                     default 'nl'
		:param str lang:  Language code to search with, default 'nl'

		:return list:  List of App IDs returned for search query
		"""
		if term is None or term == "":
			raise AppStoreException("No term was given")

		url = "https://search.itunes.apple.com/WebObjects/MZStore.woa/wa/search?clientApplication=Software&media=software&term="
		url += quote_plus(term)

		amount = int(num) * int(page)

		country = self.get_store_id_for_country(country)
		headers = {
			"X-Apple-Store-Front": "%s,24 t:native" % country,
			"Accept-Language": lang
		}

		try:
			result = requests.get(url, headers=headers).json()
		except ConnectionError as ce:
			raise AppStoreException("Cannot connect to store: {0}".format(str(ce)))
		except json.JSONDecodeError:
			raise AppStoreException("Could not parse app store response")

		return [app["id"] for app in result["bubbles"][0]["results"][:amount]]

	def get_app_ids_for_collection(self, collection="", category="", num=50, country="us", lang=""):
		"""
		Retrieve app IDs in given App Store collection

		Collections are e.g. 'top free iOS apps'.

		:param str collection:  Collection ID. One of the values in
		                        `AppStoreCollections`.
		:param int category:  Category ID. One of the values in
		                      AppStoreCategories. Can be left empty.
		:param int num:  Amount of results to return. Defaults to 50.
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		:param str lang: Dummy argument for compatibility. Unused.

		:return:  List of App IDs in collection.
		"""
		if not collection:
			collection = AppStoreCollections.TOP_FREE_IOS

		country = self.get_store_id_for_country(country)
		params = (collection, category, num, country)
		url = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/%s/%s/limit=%s/json?s=%s" % params

		try:
			result = requests.get(url).json()
		except json.JSONDecodeError:
			raise AppStoreException("Could not parse app store response")

		return [entry["id"]["attributes"]["im:id"] for entry in result["feed"]["entry"]]

	def get_app_ids_for_developer(self, developer_id, country="us", lang=""):
		"""
		Retrieve App IDs linked to given developer

		:param int developer_id:  Developer ID
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		:param str lang: Dummy argument for compatibility. Unused.

		:return list:  List of App IDs linked to developer
		"""
		url = "https://itunes.apple.com/lookup?id=%s&country=%s&entity=software" % (developer_id, country)

		try:
			result = requests.get(url).json()
		except json.JSONDecodeError:
			raise AppStoreException("Could not parse app store response")

		if "results" in result:
			return [app["trackId"] for app in result["results"] if app["wrapperType"] == "software"]
		else:
			# probably an invalid developer ID
			return []

	def get_similar_app_ids_for_app(self, app_id, country="us", lang="nl"):
		"""
		Retrieve list of App IDs of apps similar to given app

		This one is a bit special because the response is not JSON, but HTML.
		We extract a JSON blob from the HTML which contains the relevant App
		IDs.

		:param app_id:  App ID to find similar apps for
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		:param str lang:  Language code to search with, default 'nl'

		:return list:  List of similar app IDs
		"""
		url = "https://itunes.apple.com/us/app/app/id%s" % app_id

		country = self.get_store_id_for_country(country)
		headers = {
			"X-Apple-Store-Front": "%s,32" % country,
			"Accept-Language": lang
		}

		result = requests.get(url, headers=headers).text
		if "customersAlsoBoughtApps" not in result:
			return []

		blob = re.search(r"customersAlsoBoughtApps\":\s*(\[[^\]]+\])", result)
		if not blob:
			return []

		try:
			ids = json.loads(blob[1])
		except (json.JSONDecodeError, IndexError):
			return []

		return ids

	def get_app_details(self, app_id, country="us", lang="", add_ratings=False, flatten=True, sleep=None, force=False):
		"""
		Get app details for given app ID

		:param app_id:  App ID to retrieve details for. Can be either the
		                numerical trackID or the textual BundleID.
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		:param str lang: Dummy argument for compatibility. Unused.
		:param bool flatten: The App Store response may by multi-dimensional.
		                     This makes it hard to transform into e.g. a CSV,
		                     so if this parameter is True (its default) the
		                     response is flattened and any non-scalar values
		                     are removed from the response.
		:param int sleep: Seconds to sleep before request to prevent being
						  temporary blocked if there are many requests in a
						  short time. Defaults to None.
		:param bool force:  by-passes the server side caching by adding a timestamp
		                    to the request (default is False)

		:return dict:  App details, as returned by the app store. The result is
		               not processed any further, unless `flatten` is True
		"""
		try:
			app_id = int(app_id)
			id_field = "id"
		except ValueError:
			id_field = "bundleId"

		if force:
			# this will by-pass the serverside caching
			import secrets
			timestamp = secrets.token_urlsafe(8)
			url = "https://itunes.apple.com/lookup?%s=%s&country=%s&entity=software&timestamp=%s" % (id_field, app_id, country, timestamp)
		else:
			url = "https://itunes.apple.com/lookup?%s=%s&country=%s&entity=software" % (id_field, app_id, country)

		try:
			if sleep is not None:
				time.sleep(sleep)
			result = requests.get(url).json()
		except Exception:
			try:
				# handle the retry here.
				# Take an extra sleep as back off and then retry the URL once.
				time.sleep(2)
				result = requests.get(url).json()
			except Exception:
				raise AppStoreException("Could not parse app store response for ID %s" % app_id)

		try:
			app = result["results"][0]
		except (KeyError, IndexError):
			raise AppStoreException("No app found with ID %s" % app_id)

		if add_ratings:
			try:
				ratings = self.get_app_ratings(app_id, countries=country)
				app['user_ratings'] = ratings
			except AppStoreException:
				# Return some details
				self._log_error(country, 'Unable to collect ratings for %s' % str(app_id))
				app['user_ratings'] = 'Error; unable to collect ratings'

		# 'flatten' app response
		# responses are at most two-dimensional (array within array), so simply
		# join any such values
		if flatten:
			for field in app:
				if isinstance(app[field], list):
					app[field] = ",".join(app[field])
				elif isinstance(app[field], dict):
					app[field] = ", ".join(["%s star: %s" % (key, value) for key,value in app[field].items()])

		return app

	def get_multiple_app_details(self, app_ids, country="us", lang="", add_ratings=False, sleep=1, force=False):
		"""
		Get app details for a list of app IDs

		:param list app_id:  App IDs to retrieve details for
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		:param str lang: Dummy argument for compatibility. Unused.
		:param int sleep: Seconds to sleep before request to prevent being
						  temporary blocked if there are many requests in a
						  short time. Defaults to 1.
		:param bool force:  by-passes the server side caching by adding a timestamp
		                    to the request (default is False)

		:return generator:  A list (via a generator) of app details
		"""
		for app_id in app_ids:
			try:
				yield self.get_app_details(app_id, country=country, lang=lang, add_ratings=add_ratings, sleep=sleep, force=force)
			except AppStoreException as ase:
				self._log_error(country, str(ase))
				continue

	def get_store_id_for_country(self, country):
		"""
		Get store ID for country code

		:param str country:  Two-letter country code
		:param str country:  Two-letter country code for the store to search in.
		                     Defaults to 'nl'.
		"""
		country = country.upper()

		if hasattr(AppStoreMarkets, country):
			return getattr(AppStoreMarkets, country)
		else:
			raise AppStoreException("Country code not found for {0}".format(country))

	def get_app_ratings(self, app_id, countries=None, sleep=1):
		"""
		Get app ratings for given app ID

		:param app_id:  App ID to retrieve details for. Can be either the
		                numerical trackID or the textual BundleID.
		:countries:     List of countries (lowercase, 2 letter code) or single country (e.g. 'de')
		                to generate the rating for
		                if left empty, it defaults to mostly european countries (see below)
		:param int sleep: Seconds to sleep before request to prevent being
						  temporary blocked if there are many requests in a
						  short time. Defaults to 1.

		:return dict:  App ratings, as scraped from the app store.
		"""
		dataset = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }
		if countries is None:
			countries = COUNTRIES
		elif isinstance(countries, str): # only a string provided
			countries = [countries]
		else:
			countries = countries

		for country in countries:
			url = "https://itunes.apple.com/%s/customer-reviews/id%s?displayable-kind=11" % (country, app_id)
			store_id = self.get_store_id_for_country(country)
			headers = { 'X-Apple-Store-Front': '%s,12 t:native' % store_id }

			try:
				if sleep is not None:
					time.sleep(sleep)
				result = requests.get(url, headers=headers).text
			except Exception:
				try:
					# handle the retry here.
					# Take an extra sleep as back off and then retry the URL once.
					time.sleep(2)
					result = requests.get(url, headers=headers).text
				except Exception:
					raise AppStoreException("Could not parse app store rating response for ID %s" % app_id)

			ratings = self._parse_rating(result)

			if ratings is not None:
				dataset[1] = dataset[1] + ratings[1]
				dataset[2] = dataset[2] + ratings[2]
				dataset[3] = dataset[3] + ratings[3]
				dataset[4] = dataset[4] + ratings[4]
				dataset[5] = dataset[5] + ratings[5]

        # debug
		#,print("-----------------------")
		#,print('%d ratings' % (dataset[1] + dataset[2] + dataset[3] + dataset[4] + dataset[5]))
		#,print(dataset)

		return dataset

	def _parse_rating(self, text):
		matches = Regex.STARS.findall(text)

		if len(matches) != 5:
			# raise AppStoreException("Cant get stars - expected 5 - but got %d" % len(matches))
			return None

		ratings = {}
		star = 5

		for match in matches:
			value = match
			value = value.replace("<span class=\"total\">", "")
			value = value.replace("</span>", "")
			ratings[star] = int(value)
			star = star - 1

		return ratings

	def _log_error(self, app_store_country, message):
		"""
		Write the error to a local file to capture the error.

		:param str app_store_country: the country for the app store
		:param str message: the error message to log
		"""
		log_dir = 'log/'
		if not os.path.isdir(log_dir):
			os.mkdir(log_dir)

		app_log = os.path.join(log_dir, "{0}_log.txt".format(app_store_country))
		errortime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
		fh = open(app_log, "a")
		fh.write("%s %s \n" % (errortime,message))
		fh.close()
class AppStoreException(Exception):
    pass

class AppInfoScraper:
    def __init__(self):
        pass

    def get_top_chart_app_ids(self, category, limit):
        """
        This function retrieves the top app IDs from the iTunes App Store for a specified category and limit.

        Parameters:
        - category (str): The category of the apps for which to retrieve the top chart. Valid values include "music", "games", "business", etc.
        - limit (int): The maximum number of app IDs to retrieve from the top chart.

        Returns:
        - app_ids (list): A list of app IDs from the top chart, including both free and paid applications.

        Exceptions:
        - AppStoreException: Raised when there is an error retrieving the app IDs from the App Store.

        Usage Example:
        app_ids = get_top_chart_app_ids("games", 10)
        print(app_ids)

        Output:
        ['1234567890', '0987654321', '3456789012', ...]

        Notes:
        - The function makes use of the iTunes App Store API to retrieve the top app IDs.
        - It first retrieves the IDs of the top free applications and then the IDs of the top paid applications for the specified category and limit.
        - The function combines the IDs from both categories and returns the resulting list.
        """
        try:
            us_url = f"https://itunes.apple.com/us/rss/topfreeapplications/genre={category}/limit={limit}/json"
            us_response = requests.get(us_url)

            if us_response.status_code == 200:
                us_data = us_response.json()
                us_entries = us_data['feed']['entry']
                us_free_app_ids = [entry['id']['attributes']['im:id'] for entry in us_entries]

                us_paid_app_ids = []

                us_paid_url = f"https://itunes.apple.com/us/rss/toppaidapplications/genre={category}/limit={limit}/json"
                us_paid_response = requests.get(us_paid_url)

                if us_paid_response.status_code == 200:
                    us_paid_data = us_paid_response.json()
                    us_paid_entries = us_paid_data['feed']['entry']
                    us_paid_app_ids = [entry['id']['attributes']['im:id'] for entry in us_paid_entries]

                    app_ids = us_free_app_ids + us_paid_app_ids
                    return app_ids
                else:
                    raise AppStoreException("Failed to retrieve top paid applications. Please check the category or try again later.")
            else:
                raise AppStoreException("Failed to retrieve top free applications. Please check the category or try again later.")

        except Exception as e:
            print("An error occurred:", str(e))
            return []

    def scrape_app_info(self, limit):
        """
        This function scrapes app information from the iTunes App Store for multiple categories.

        Parameters:
        - limit (int): The maximum number of app IDs to retrieve from the top chart for each category.

        Usage Example:
        scrape_app_info(10)

        Notes:
        - The function retrieves the top app IDs for each category from a predefined dictionary of categories and genre IDs.
        - It uses the `get_top_chart_app_ids` function to retrieve the app IDs.
        - The function then uses an `AppStoreScraper` object to fetch detailed information for each app ID.
        - Certain entries are removed from the app information dictionaries.
        - The resulting app information is converted to a pandas DataFrame and saved as a CSV file named "app_info.csv".
        """
        categories = {'Book':'6018', 'Business':'6000','Developer Tools' :'6026','Eduaction':'6017','Entertainment':'6016',
                      'Finance':'6015','Food & Drink':'6023','Graphics & Design':'6027','Health & Fitness':'6013','Lifestyle':'6012',
                      'Medical':'6020','Music':'6011','Navigation':'6010','News':'6009','Photo & Video':'6008',
                      'Reference':'6006','Weather':'6001', 'Sports':'6004','Utilites':'6002','Shopping':'6024','Travel':'6003','Game':'6014'}

        apps_ids = []

        for index, val in categories.items():
            apps_ids.extend(self.get_top_chart_app_ids(val, limit))
        scraper = AppStoreScraper()
        app_info = []
        print(f"Scraping app information for {(apps_ids)} apps...")
        for index, val in enumerate(apps_ids):
            try:
                app_details = scraper.get_app_details(apps_ids[index])
                app_details.update({'appId': str(apps_ids[index])})
                app_info.append(app_details)
            except Exception as e:
                print(f"Error retrieving app info for ID {apps_ids[index]}: {str(e)}")
                continue

        entries_to_remove = ('supportedDevices','isGameCenterEnabled','appletvScreenshotUrls','advisories','features',
                             'screenshotUrls','ipadScreenshotUrls','artworkUrl60','artworkUrl100','artistViewUrl',
                             'contentAdvisoryRating','kind','trackViewUrl','releaseDate','version','wrapperType',
                             'userRatingCount','minimumOsVersion','releaseNotes','artistId','artistName',
                             'trackCensoredName','languageCodesISO2A','fileSizeBytes','currency',
                             'averageUserRatingForCurrentVersion','userRatingCountForCurrentVersion','trackContentRating',
                             'genreIds','isVppDeviceBasedLicensingEnabled','bundleId','currentVersionReleaseDate','trackId'
                             ,'sellerName','sellerUrl','formattedPrice')

        for index, val in enumerate(app_info):
            for k in entries_to_remove:
                try:
                    del app_info[index][k]
                except KeyError as ke:
                    print('Key Not Found in Employee Dictionary:', ke)

        app_info_df = pd.DataFrame()

        for index, val in enumerate(app_info):
            app_info_df = pd.concat([app_info_df, pd.DataFrame.from_dict(app_info[index], orient='index').transpose()], ignore_index=True)
            
        app_info_df.to_csv("app_info.csv", index=False)

def main():
    scraper = AppInfoScraper()
    limit = 2
    scraper.scrape_app_info(limit)

if __name__ == '__main__':
    main()