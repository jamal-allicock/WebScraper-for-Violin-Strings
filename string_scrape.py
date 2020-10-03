import requests, csv, bs4



#Type (synthetic, steel, gut)
#String (G, D, A, E, Full set)
#Brand (Evah Pirazzi, Thomastik-Infeld, Larsen, etc)
#Name (Dominants, Peter Infeld, Pirastro Gold)
#link
#Price

#the original url is so that href can be attatched to the end later in the code
original_url = 'https://www.thesoundpost.com'
url = 'https://www.thesoundpost.com/en/store/violin-strings'

request = requests.get(url)
request.raise_for_status()
soup = bs4.BeautifulSoup(request.text, 'html.parser')

# Opens a csv file to insert the data
with open('soundpost_pricings.csv', 'w') as csv_file:
    # Puts the headers in
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Price'])

    ## This function scrapes the page with the price of the strings
    def violinstring_scrape(href):
        string_url = original_url + href
        request_string = requests.get(string_url)
        request_string.raise_for_status()
        soup_string = bs4.BeautifulSoup(request_string.text, 'html.parser')
        options = soup_string.select('.shade')

        lst = []
        #Finds the name and price for every item on the page, and appends them to a list
        for option in options:
            name = option.find(class_ = 'second').get_text()
            price = option.find(class_ = 'price').get_text()
            lst.append([name,price])
        return lst

    #Finds all of the links to string pages, and excludes the featured and the products 
        #on sale because they already occur 
    strings = soup.find_all('dl')
    strings = strings[6:-4]

    for page in strings:
        href = page.find('a')['href']
        title = page.find('img')['title']
        print(href, title)
        # data = violinstring_scrape(href)

        # for row in data:
        #     csv_writer.writerow(row)
    

    

