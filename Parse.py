import requests
from bs4 import BeautifulSoup

def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    response = requests.get(url, headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'reviews-view__review')
    
    rating = ''
    evaluation = 0
    organizations = []
    comments = []
    
    for item in items:
        evaluationBlock = item.find('div', class_ = 'business-review-view__header').find('div', class_ = 'business-rating-badge-view__stars').findAll('span', class_ = 'business-rating-badge-view__star _size_m')
        for char in evaluationBlock:
            evaluation += 1

        ratingBlock = soup.find('span', class_ = 'business-summary-rating-badge-view__rating').findAll('span', class_ = 'business-summary-rating-badge-view__rating-text')
        for char in ratingBlock:
            rating += char.text

        comments.append({
            'author': item.find('div', class_ = 'business-review-view__author').find('span').text,
            'evaluation': evaluation,
            'date': item.find('div', class_ = 'business-review-view__header').find('span', class_ = 'business-review-view__date').find('span').text,
            'text': item.find('div', class_ = 'business-review-view__body-text _collapsed').text
        })

        organizations.append({
            'name': soup.find('h1', class_ = 'orgpage-header-view__header').text,
            'rating': rating,
            'comments': comments
        })

        evaluation = 0

    return organizations