import requests
from bs4 import BeautifulSoup

def get_products():
    divar = requests.get("https://divar.ir/s/neyshabur/mobile-phones/apple?goods-business-type=all")
    soup = BeautifulSoup(divar.content, "html.parser")

    productsPrice = soup.find_all(class_='kt-post-card__description')
    productsBottom = soup.find_all(class_='kt-post-card__bottom')

    productPriceCount = 1
    productCount = 0
    products = []

    for div in soup.find_all(class_='post-card-item-af972'):
        for childdiv in div.find_all('a'):
            link = f"https://divar.ir{childdiv['href']}"
            title = childdiv.article.div.h2.string.strip()
            price = productsPrice[productPriceCount].string.strip()
            isProductSalesByShop = productsBottom[productCount].span['class'][0] == "kt-post-card__red-text"
            
        divarSingleProduct = requests.get(link)
        soupSingle = BeautifulSoup(divarSingleProduct.content, "html.parser")

        picturesUL = soupSingle.find(class_="kt-carousel__thumbnail-scroller")
        pictures = []
        if picturesUL and picturesUL.li:
            for productPicture in picturesUL:
                pictures.append(productPicture.div.picture.img['src'].split("?")[0])
        else:
            picturesHTML = soupSingle.find_all(class_="kt-image-block__image")
            for productPicture in picturesHTML:
                try:
                    pictures.append(productPicture['src'].split("?")[0])
                except:
                    pass

        products.append({
            "title" : title,
            "price" : price,
            "link" : link,
            "pictures" : pictures,
            "isProductSalesByShop" : isProductSalesByShop
        })

        productPriceCount+=2
        productCount += 1

    return products