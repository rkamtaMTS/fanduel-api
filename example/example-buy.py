# import packages
import sys
import time

# import custom packages
sys.path.append('..')

from config import config as cfg
from browser import driver as dri
from browser import navigate as nav
from browser import account as act
from browser import buy as by

# define static variables
username = ''
password = ''

# define dynamic variables
config = cfg.CONFIG
bri = config.browser_refresh_int
dci = config.data_collection_int
slw = config.screen_load_wait
dh = config.driver_headless
dl = config.driver_location
lfp = config.log_file_path
dbg = config.debug
url = config.url


def main():

    # create driver object
    driver = dri.DRIVER(browser_refresh_int=bri, driver_headless=dh, driver_location=dl, log_file_path=lfp, debug=dbg, url=url)
    navigate = nav.NAVIGATE(driver=driver)
    account = act.ACCOUNT(driver=driver, screen_load_wait=slw)
    buy = by.BUY(driver=driver, screen_load_wait=slw)

    try:

		# check if internet connection exists
        if not driver.check_internet_connection():
            raise Exception('No Internet Connection')

        # wait a second for the modal window to load
		# close modal window
        time.sleep(1)
        navigate.close_modal_window()

        # login to account
        # close modal window
        # close plugin
        # click Live group event tab
        account.login(username=username, password=password)
        navigate.close_modal_window()
        navigate.close_plugin()

        # check if logged in
        # attempt to submit bet
        # attempt to submit bet
        if account.check_logged_in():
            navigate.click_tab(tab_type='bet_status', tab_name='Betslip')
            buy.buy(bet_amount=1, league='NHL', team_name='Edmonton Oilers', compare_bet_type_value=600, bet_type='moneyline', type='less')
            account.logout()

    except Exception as e:
        print(str(e))

	# check if driver instance exists
	# close current driver instance windows
    if driver.driver:
        driver.driver.quit()


if __name__ == '__main__':
    main()
