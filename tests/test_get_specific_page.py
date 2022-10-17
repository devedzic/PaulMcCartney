def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    if page > 1:
        # url_chunks = start_url.split('&searchpage=')
        # page_to_return = url_chunks[0] + '&searchpage=' + str(page)
        # print(page)
        # print(page_to_return)
        # return page_to_return
        return start_url.split('&searchpage=')[0] + '&searchpage=' + str(page)
    # elif '&searchpage=' not in start_url and page > 1:
    #     return start_url.split('&searchpage=')[0] + '&searchpage=' + str(page)
    return start_url.split('&searchpage=')[0]


start_url = 'https://ultimateclassicrock.com/search/?s=paul%20mccartney'

# Test get_specific_page(start_url, page)
print(get_specific_page(start_url + '&searchpage=1'))
print()
print(get_specific_page(start_url + '&searchpage=1', 2))
print()
print(get_specific_page(start_url, 2))


# # Test get_specific_page(start_url, page)
# print(get_specific_page(start_url))
# print()
# print(get_specific_page(start_url, 2))

