import pathlib

# Constant values required for Execution
HOME_PATH = pathlib.Path.home()
XL_FILE_PATH = str(HOME_PATH) + '\\Desktop\\Simblock\\mobile_numbers.xlsx'
PROCESSED_XL_FILE_PATH = str(HOME_PATH) + '\\Desktop\\Simblock\\mobile_numbers_processed.xlsx'
PAYTM_URL = 'https://digitalapiproxy.paytm.com/v1/mobile/getopcirclebyrange/'
EASEMYDEAL_URL = 'https://www.easemydeal.com/recharge/service/mobile_details_finder'
PAYRUP_URL = 'https://api.payrup.com/api/prepaid/lookup'