import dataProcessor
import logger
dp = dataProcessor
lg = logger


def give_points_by_id(id_num, points):
    prev_bal = dp.get_children_balance(id_num)
    dp.set_children_balance(id_num, prev_bal + points)
    lg.log_balance_change(id_num, prev_bal, prev_bal + points)


def give_points_by_name(name, points):
    id_num = dp.id_by_name(name)
    give_points_by_id(id_num, points)


def give_points_to_group(group, points):
    for child in group:
        give_points_by_id(child, points)

