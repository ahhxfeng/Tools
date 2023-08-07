import argparse
import json

from get_network import *

# from . import config
# from config import *


def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--transcation", help="the transcation id")
    # parser.add_argument("")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    get_network_info("/info", "network_info.json")

    # args = args_parse()
    # print(args.transcation)
    # # data = check_block_time(200)
    cacu_block_time_interval(50, "block_time.json")
    # db_test()
    get_tran_info(1, "transaction_res.json")
