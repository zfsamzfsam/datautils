import os

SOURCE = os.environ.get("SOURCE", "mongodb")

MONGODB_URI = os.environ.get("MONGODB_URI", "localhost")

STOCK_D = os.environ.get("STOCK_D", "Stock_D")
STOCK_H = os.environ.get('STOCK_H', "Stock_H")
STOCK_1M = os.environ.get("STOCK_1M", "Stock_1M")

FACTOR = os.environ.get("FACTOR", "factors")
FXDAYU_FACTOR = os.environ.get("FXDAYU_FACTOR", "fxdayu_factors")
DAILY_INDICATOR = os.environ.get("DAILY_INDICATOR", "SecDailyIndicator")

API_LIST = os.environ.get("API_LIST", "jz.apiList")
API_PARAM = os.environ.get("API_PARAM", "jz.apiParam")
INST_INFO = os.environ.get("INST_INFO", "jz.instrumentInfo")
TRADE_CAL = os.environ.get("TRADE_CAL", "jz.secTradeCal")

BALANCE_SHEET = os.environ.get("BALANCE_SHEET", "lb.balanceSheet")
CASH_FLOW = os.environ.get("CASH_FLOW", "lb.cashFlow")
FIN_INDICATOR = os.environ.get("FIN_INDICATOR", "lb.finIndicator")
INCOME = os.environ.get("INCOME", "lb.income")
INDEX_CONS = os.environ.get("INDEX_CONS", "lb.indexCons")
INDEX_WEIGHT_RANGE = os.environ.get("INDEX_WEIGHT_RANGE", "lb.indexWeightRange")
PROFIT_EXPRESS = os.environ.get("PROFIT_EXPRESS", "lb.profitExpress")
S_STATE = os.environ.get("S_STATE", "lb.sState")
SEC_DIVIDEND = os.environ.get("SEC_DIVIDEND", "lb.secDividend")
SEC_INDUSTRY = os.environ.get("SEC_INDUSTRY", "lb.secIndustry")
SEC_RESTRICTED = os.environ.get("SEC_RESTRICTED", "lb.secRestricted")
SEC_SUSP = os.environ.get("SEC_SUSP", "lb.secSusp")
WIND_FINANCE = os.environ.get("WIND_FINANCE", "lb.windFinance")
SEC_ADJ_FACTOR = os.environ.get("SEC_ADJ_FACTOR", "lb.secAdjFactor")

VARIABLES = (
    "STOCK_D", "STOCK_H", "FACTOR", "DAILY_INDICATOR", "STOCK_1M", "API_LIST", "API_PARAM", "INST_INFO", "TRADE_CAL",
    "BALANCE_SHEET", "CASH_FLOW", "FIN_INDICATOR", "INCOME", "INDEX_CONS", "INDEX_WEIGHT_RANGE", "PROFIT_EXPRESS",
    "S_STATE", "SEC_DIVIDEND", "SEC_INDUSTRY", "SEC_SUSP", "SEC_RESTRICTED", "WIND_FINANCE", "SEC_ADJ_FACTOR",
    "FXDAYU_FACTOR", "MONGODB_URI"
)


def variables():
    return {name: str(globals()[name]) for name in VARIABLES}
