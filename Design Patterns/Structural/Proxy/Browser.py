from BrowserCache import BrowserCache
if __name__ == '__main__':
    browser = BrowserCache()

    data1 = browser.fetchData('https://www.google.com')
    print(data1)

    data2 = browser.fetchData('https://www.safari.com')
    print(data2)

    print(f'cache: ${browser.cache}')

    data3 = browser.fetchData('https://www.google.com')
    print(data3)
