import dataProcessor
import datetime
import logging
dp = dataProcessor
dt = datetime

logging.basicConfig(filename="history.log", level=logging.INFO)


def log_balance_change(id_num, prev_balance, post_balance):
    logging.info(str(dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")) + " " + str(dp.name_by_id(id_num)) + " (ID: " +
                 str(id_num) + ') changed balance from ' +
          str(prev_balance) + ' to ' + str(post_balance))
    print(dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), dp.name_by_id(id_num), '( ID:', id_num, ') changed balance '
                                                                                                   'from',
          prev_balance, 'to', post_balance)