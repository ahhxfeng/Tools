# coding=utf-8

import requests
import json

from config import HOST
from cac_time import add_time_file
from db import do_sql


def get_network_info(url: str, file: str) -> bool:
    """
    get the network info  and wirte to given file format json
    """

    url = HOST + url
    res = requests.get(url)
    filename = add_time_file(file)

    with open(filename, "w+") as f:
        json.dump(res.json(), f)

    return True


def check_block_time(block_num: int) -> dict:
    """
    get the last given num block timestamp return as a dict
    """

    url = HOST + "/info"
    res = requests.get(url)
    data = res.json()
    # ret {height, timestamp}
    ret = dict()

    # caculation the given num block timestamp
    for i in range(0, block_num):
        height = data["height"] - i
        print(height)
        url = HOST + "/block/height/{}".format(height)
        res = requests.get(url)
        timestamp = res.json()["timestamp"]
        ret.update({height: timestamp})

    return ret


def cacu_block_time_avg_interval(num: int = 0, data: dict = None) -> str:
    """
    caculate the avg time about the given num blocks
    """
    ret = dict

    if data is None:
        data = check_block_time(num)

    # get the last and on value from dict
    list_key = list(data.keys())

    total_time = data[list_key[0]] - data[list_key[-1]]
    total_block = list_key[0]-list_key[-1]
    avg_time = total_time/total_block

    return avg_time


def cacu_block_time_interval(num: int, file: str):
    """
    caculate the time interval about the given num blocks

    """

    data = check_block_time(num)
    print("data:", data)
    avg_time = cacu_block_time_avg_interval(data=data)
    ret = dict()
    ret.update({"avg_time": str(avg_time)+"s"})
    ret.update({"blcok_time_interval": "seconds"})
    filename = add_time_file(file)

    try:
        for key in data.keys():
            # print("height:{0}, timestamp: {1}".format(key, data[key]))
            height = key
            pre_height = key - 1
            secends_between = str(data[height] - data[pre_height]) + "s"
            print("{0} - {1}: {2}s".format(height, pre_height, secends_between))
            block_interval = "{0} - {1}".format(height, pre_height)
            ret.update({block_interval: secends_between})
    except KeyError as e:
        print(e)

    with open(filename, "w+") as f:
        json.dump(ret, f)

    return True


def get_tran_info(num: int = 1, file: str = "default.josn"):
    """
    get the newest transcation info 
    default get one 
    """

    sql = "select JSON_OBJECT \
        ('id', id, 'create_time', created_at, 'update_time', updated_at, \
        'tx_id', tx_id, 'last_tx', last_tx, 'owner', owner, 'target', target,\
        'quantity', quantity, 'data_root', data_root, 'data_size', data_size, \
        'fee', fee, 'height', height, 'hash', hash, 'timestamp', timestamp, \
        'tags', tags, 'settled', settled, 'private', private,\
         'notes', notes) from e_transaction ORDER BY id DESC limit {}".format(num)
    res = do_sql(sql=sql)
    # print(type(res[0][0]))

    filename = add_time_file(file)
    data_dict = json.loads(res[0][0])

    with open(filename, "w+") as f:
        json.dump(data_dict, f, indent=4)

    return True
