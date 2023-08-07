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

# def db_test():
#     # sql = "SELECT * FROM e_transaction ORDER BY id DESC LIMIT 10"
#     sql = "select JSON_OBJECT('id', id, 'create_time', created_at, 'update_time', updated_at, 'tx_id', tx_id, 'last_tx', last_tx, 'owner', owner, 'target', target, 'quantity', quantity, 'data_root', data_root, 'data_size', data_size, 'fee', fee, 'height', height, 'hash', hash, 'timestamp', timestamp, 'tags', tags, 'settled', settled, 'private', private, 'notes', notes) from e_transaction ORDER BY id DESC limit 1"
#     res = get_cursor(sql=sql)
#     # print("Sql res", res)
#     # print(type(res[0][0]))

#     data_dict = json.loads(res[0][0])

#     with open("trancation_res.json", "w+") as f:
#         json.dump(data_dict, f, indent=4)


if __name__ == "__main__":
    get_network_info("/info", "network_info.json")

    # args = args_parse()
    # print(args.transcation)
    # # data = check_block_time(200)
    cacu_block_time_interval(50, "block_time.json")
    # db_test()
    get_tran_info(1, "transaction_res.json")
