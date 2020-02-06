import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('実行開始')

logging.info('1を0で割る')

print(1 / 0)

logging.info('割り算成功')

logging.info('実行終了')
