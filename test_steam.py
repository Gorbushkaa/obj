from steam import Steam


def test_steam():
    steam_market = Steam()
    steam_market.go_to_site()
    steam_market.click_welcome()
    steam_market.click_download()







