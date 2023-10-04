import requests
import re
import bs4

class currencyconvert():
    
    def __init__(self):
        """Initialising the list of available currencies"""
        self.available_currency = {'AED': ['UAE', 'Dirham'], 'AFN': ['Afghan', 'Afghani'], 'ALL': ['Albanian', 'Lek'],
            'AMD': ['Armenian', 'Dram'], 'ANG': ['Netherlands', 'Antillean', 'Guilder'], 'AOA': ['Angolan', 'Kwanza'],
            'ARS': ['Argentine', 'Peso'], 'AUD': ['Australian', 'Dollar'], 'AWG': ['Aruban', 'Florin'], 'AZN': ['Azerbaijani',
            'Manat'], 'BAM': ['Bosnia-Herzegovina', '(CM)'], 'BBD': ['Barbadian', 'Dollar'], 'BDT': ['Bangladeshi', 'Taka'],
            'BGN': ['Bulgarian', 'Lev'], 'BHD': ['Bahraini', 'Dinar'], 'BIF': ['Burundian', 'Franc'], 'BMD': ['Bermudan', 'Dollar'],
            'BND': ['Brunei', 'Dollar'], 'BOB': ['Bolivian', 'Boliviano'], 'BRL': ['Brazilian', 'Real'], 'BSD': ['Bahamian', 'Dollar'],
            'BTC': ['Bitcoin'], 'BTN': ['Bhutanese', 'Ngultrum'], 'BTS': ['BitShares'], 'BWP': ['Botswanan', 'Pula'],
            'BYN': ['Belarusian', 'Ruble'], 'BZD': ['Belize', 'Dollar'], 'CAD': ['Canadian', 'Dollar'], 'CDF': ['Congolese', 'Franc'],
            'CHF': ['Swiss', 'Franc'], 'CLF': ['Chilean', 'Unit', 'of', 'Account', '(UF)'], 'CLP': ['Chilean', 'Peso'],
            'CNH': ['Chinese', 'Yuan', '(Offshore)'], 'CNY': ['Chinese', 'Yuan'], 'COP': ['Colombian', 'Peso'],
            'CRC': ['Costa', 'Rican', 'Colón'], 'CUC': ['Cuban', 'Convertible', 'Peso'], 'CUP': ['Cuban', 'Peso'],
            'CVE': ['Cape', 'Verdean', 'Escudo'], 'CZK': ['Czech', 'Koruna'], 'DASH': ['Dash'], 'DJF': ['Djiboutian', 'Franc'],
            'DKK': ['Danish', 'Krone'], 'DOGE': ['DogeCoin'], 'DOP': ['Dominican', 'Peso'], 'DZD': ['Algerian', 'Dinar'],
            'EAC': ['EarthCoin'], 'EGP': ['Egyptian', 'Pound'], 'EMC': ['Emercoin'], 'ERN': ['Eritrean', 'Nakfa'],
            'ETB': ['Ethiopian', 'Birr'], 'ETH': ['Ethereum'], 'EUR': ['Euro'], 'FCT': ['Factom'], 'FJD': ['Fijian', 'Dollar'],
            'FKP': ['Falkland', 'Islands', 'Pound'], 'FTC': ['Feathercoin'], 'GBP': ['British', 'Pound', 'Sterling'],
            'GEL': ['Georgian', 'Lari'], 'GGP': ['Guernsey', 'Pound'], 'GHS': ['Ghanaian', 'Cedi'], 'GIP': ['Gibraltar', 'Pound'],
            'GMD': ['Gambian', 'Dalasi'], 'GNF': ['Guinean', 'Franc'], 'GTQ': ['Guatemalan', 'Quetzal'], 'GYD': ['Guyanaese', 'Dollar'],
            'HKD': ['Hong', 'Kong', 'Dollar'], 'HNL': ['Honduran', 'Lempira'], 'HRK': ['Croatian', 'Kuna'], 'HTG': ['Haitian', 'Gourde'],
            'HUF': ['Hungarian', 'Forint'], 'IDR': ['Indonesian', 'Rupiah'], 'ILS': ['Israeli', 'New', 'Sheqel'], 'IMP': ['Manx', 'pound'],
            'INR': ['Indian', 'Rupee'], 'IQD': ['Iraqi', 'Dinar'], 'IRR': ['Iranian', 'Rial'], 'ISK': ['Icelandic', 'Króna'],
            'JEP': ['Jersey', 'Pound'], 'JMD': ['Jamaican', 'Dollar'], 'JOD': ['Jordanian', 'Dinar'], 'JPY': ['Japanese', 'Yen'],
            'KES': ['Kenyan', 'Shilling'], 'KGS': ['Kyrgystani', 'Som'], 'KHR': ['Cambodian', 'Riel'], 'KMF': ['Comorian', 'Franc'],
            'KPW': ['North', 'Korean', 'Won'], 'KRW': ['South', 'Korean', 'Won'], 'KWD': ['Kuwaiti', 'Dinar'], 'KYD': ['Cayman', 'Islands', 'Dollar'],
            'KZT': ['Kazakhstani', 'Tenge'], 'LAK': ['Laotian', 'Kip'], 'LBP': ['Lebanese', 'Pound'], 'LD': ['Linden', 'Dollar'],
            'LKR': ['Sri', 'Lankan', 'Rupee'], 'LRD': ['Liberian', 'Dollar'], 'LSL': ['Lesotho', 'Loti'], 'LTC': ['LiteCoin'],
            'LYD': ['Libyan', 'Dinar'], 'MAD': ['Moroccan', 'Dirham'], 'MDL': ['Moldovan', 'Leu'], 'MGA': ['Malagasy', 'Ariary'],
            'MKD': ['Macedonian', 'Denar'], 'MMK': ['Myanma', 'Kyat'], 'MNT': ['Mongolian', 'Tugrik'], 'MOP': ['Macanese', 'Pataca'],
            'MRU': ['Mauritanian', 'Ouguiya'], 'MUR': ['Mauritian', 'Rupee'], 'MVR': ['Maldivian', 'Rufiyaa'], 'MWK': ['Malawian', 'Kwacha'],
            'MXN': ['Mexican', 'Peso'], 'MYR': ['Malaysian', 'Ringgit'], 'MZN': ['Mozambican', 'Metical'], 'NAD': ['Namibian', 'Dollar'],
            'NGN': ['Nigerian', 'Naira'], 'NIO': ['Nicaraguan', 'Córdoba'], 'NMC': ['Namecoin'], 'NOK': ['Norwegian', 'Krone'],
            'NPR': ['Nepalese', 'Rupee'], 'NVC': ['NovaCoin'], 'NXT': ['Nxt'], 'NZD': ['New', 'Zealand', 'Dollar'], 'OMR': ['Omani', 'Rial'],
            'PAB': ['Panamanian', 'Balboa'], 'PEN': ['Peruvian', 'Nuevo', 'Sol'], 'PGK': ['Papua', 'New', 'Guinean', 'Kina'],
            'PHP': ['Philippine', 'Peso'], 'PKR': ['Pakistani', 'Rupee'], 'PLN': ['Polish', 'Zloty'], 'PPC': ['Peercoin'],
            'PYG': ['Paraguayan', 'Guarani'], 'QAR': ['Qatari', 'Rial'], 'RON': ['Romanian', 'Leu'], 'RSD': ['Serbian', 'Dinar'],
            'RUB': ['Russian', 'Ruble'], 'RWF': ['Rwandan', 'Franc'], 'SAR': ['Saudi', 'Riyal'], 'SBD': ['Solomon', 'Islands', 'Dollar'],
            'SCR': ['Seychellois', 'Rupee'], 'SDG': ['Sudanese', 'Pound'], 'SEK': ['Swedish', 'Krona'], 'SGD': ['Singapore', 'Dollar'],
            'SHP': ['Saint', 'Helena', 'Pound'], 'SLL': ['Sierra', 'Leonean', 'Leone'], 'SOS': ['Somali', 'Shilling'], 'SRD': ['Surinamese', 'Dollar'],
            'SSP': ['South', 'Sudanese', 'Pound'], 'STD': ['São', 'Tomé', '&amp;', 'Príncipe', 'Dobra'], 'STN': ['São', 'Tomé', '&amp;', 'Príncipe', 'Dobra'],
            'STR': ['Stellar'], 'SVC': ['Salvadoran', 'Colón'], 'SYP': ['Syrian', 'Pound'], 'SZL': ['Swazi', 'Lilangeni'], 'THB': ['Thai', 'Baht'],
            'TJS': ['Tajikistani', 'Somoni'], 'TMT': ['Turkmenistani', 'Manat'], 'TND': ['Tunisian', 'Dinar'], 'TOP': ['Tongan', 'Pa&#039;anga'],
            'TRY': ['Turkish', 'Lira'], 'TTD': ['Trinidad', '&amp;', 'Tobago', 'Dollar'], 'TWD': ['New', 'Taiwan', 'Dollar'],
            'TZS': ['Tanzanian', 'Shilling'], 'UAH': ['Ukrainian', 'Hryvnia'], 'UGX': ['Ugandan', 'Shilling'], 'USD': ['United', 'States', 'Dollar'],
            'UYU': ['Uruguayan', 'Peso'], 'UZS': ['Uzbekistan', 'Som'], 'VEF': ['Venezuelan', 'Bolívar', 'Fuerte'], 'VES': ['Venezuelan', 'Bolívar', 'Soberano'],
            'VND': ['Vietnamese', 'Dong'], 'VTC': ['VertCoin'], 'VUV': ['Vanuatu', 'Vatu'], 'WST': ['Samoan', 'Tala'], 'XAF': ['CFA', 'Franc', 'BEAC'],
            'XAG': ['Silver', 'Ounce'], 'XAU': ['Gold', 'Ounce'], 'XCD': ['East', 'Caribbean', 'Dollar'], 'XDR': ['Special', 'Drawing', 'Rights'],
            'XMR': ['Monero'], 'XOF': ['CFA', 'Franc', 'BCEAO'], 'XPD': ['Palladium', 'Ounce'], 'XPF': ['CFP', 'Franc'], 'XPM': ['Primecoin'],
            'XPT': ['Platinum', 'Ounce'], 'XRP': ['Ripple'], 'YER': ['Yemeni', 'Rial'], 'ZAR': ['South', 'African', 'Rand'],
            'ZMW': ['Zambian', 'Kwacha'], 'ZWL': ['Zimbabwean', 'Dollar']
            }

    def _CurrencyConfirmation(self, currency: str):
        """Returns the currency code based on currency parameter"""
        currency_list = []

        # Changes currency to a list of words
        for name in currency.split():
            currency_list.append(name.capitalize())
        
        #Loops through the codes, currencies and countries
        for key, value in self.available_currency.items():

            if currency.upper() == key or key.capitalize() in currency_list:
                return key
    
            for item in currency_list:

                if item == "Dollar":
                    continue

                if item.capitalize() in value:
                    return key


    def _HtmlPage(self, first_currency: str, second_currency: str, amount):
        """Scrapes the internet for the currency conversions"""

        first_currency = first_currency.lower()
        second_currency = second_currency.lower()

        #Gets the currency conversion page using request
        html_page = requests.get(f'https://www.forbes.com/advisor/money-transfer/currency-converter/{first_currency}-{second_currency}/?amount={amount}')

        #Asserts that request was successfully connected
        if html_page.raise_for_status()==requests.codes.ok is False:
            return "Couldn't connect to the internet"
        else:
            return html_page.text


    def _AmountConversion(self, html_page):
        """Gets all necessary information from the html_page variable"""

        ConvertAmount = ''
        RateAmount = ''
        TimeUpdate = ''

        Page = bs4.BeautifulSoup(html_page, "html.parser")
        
        # Find the conversion amounts, conversion rates and updated time location
        conversion = Page.find('h2', class_='result-box-conversion')
        rates = Page.find('div', class_='result-box-c1-c2')
        dates = Page.find('p', class_='updated-string')

        #Text of conversion amount, conversion rates and update time
        for span in conversion.find_all('span'): #conversion ammount information
            ConvertAmount += span.get_text() + ' '

        for div in rates.find_all('div'): #conversion rates information
            RateAmount += ' '.join(div.get_text().split()) + '\n'

        for Time in dates.find_all('time'): #rates upload time
            TimeUpdate += Time.get_text()

        return ConvertAmount, RateAmount, TimeUpdate


    def convert(self, from_currency: str, to_currency: str, amount: int):
        """Returns all information about the currencies"""

        if from_currency.lower() == 'list':

            content=''''''

            for key, value in self.available_currency.items():
                value = ' '.join(value)

                content += '    ' + f"{key}: {value}" + '\n'
            return content

        if not amount:
            return "Please enter an amount."

        try:
            amount = float(amount)
        except ValueError:
            return "Invalid amount input."

        if to_currency.lower() == 'list':

            content=''''''

            for key, value in self.available_currency.items():
                value = ' '.join(value)
                
                content += '    ' + f"{key}: {value}" + '\n'
            return content

        #Getting currency code from dictionary
        currency1 = self._CurrencyConfirmation(from_currency)
        currency2 = self._CurrencyConfirmation(to_currency)

        if currency1 is None or currency2 is None or currency1 and currency2 is None:

            content=''''''

            for key, value in self.available_currency.items():
                value = ' '.join(value)

                content += '    ' + f"{key}: {value}" + '\n'

            content += f"\nInvalid currency format\n\nList of available currencies\n----------------------------".upper()
            return content

        if currency1 == currency2:
            return "Can not convert the same currency"

        #Get html page from the internet
        html_page = self._HtmlPage(currency1, currency2, amount)
        if html_page == "Couldn't connect to the internet":

            return f"no internet connection".upper()


        #Gets info from the html page
        Information = self._AmountConversion(html_page)

        # Returns all info of the currencies
        return currency1, currency2, amount, Information[0], Information[1], Information[2]


if __name__ == '__main__':
    sam = currencyconvert()

    print(sam.convert('usd', 'ngn', 1))
