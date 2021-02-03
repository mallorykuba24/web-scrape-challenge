import pandas as pd
from splinter import Browser
import requests
import os

def scrape():
    browser = Browser('chrome','chromedriver')
    title, paragraph = news(browser)
    mars = {
        'title': title,
        'paragraph': paragraph,
        # 'image': image(browser),
        'facts': facts(),
        'hemispheres': hemi(browser)
    }
    return mars

# ### NASA Mars News
# * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
def news(browser):
    browser.visit('https://mars.nasa.gov/news/')
    title = browser.find_by_css('div.content_title a').text
    paragraph = browser.find_by_css('div.article_teaser_body').text
    return title, paragraph

# ### JPL Mars Space Images - Featured Image
# * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
# * Make sure to find the image url to the full size `.jpg` image.
# * Make sure to save a complete url string for this image.
# def image(browser):
#     JPL_image_url = 'https://www.jpl.nasa.gov/images/?search=&category=Mars'
#     browser.visit(JPL_image_url)
#     return browser.find_by_css("figure.lede a img")["src"]

# ### Mars Facts
# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# * Use Pandas to convert the data to a HTML table string.
def facts():
    return pd.read_html('https://space-facts.com/mars/')[0].to_html()

# # Mars Hemispheres
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
#visit USGS Astrogeology site (actually use Seans link not HW link)
def hemi(browser):
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)
    links = browser.find_by_css('a.itemLink h3')
    hemispheres = []
    for i in range(len(links)):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()
    return hemispheres

