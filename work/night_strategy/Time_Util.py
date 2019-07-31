import datetime

def get_after_date_time(interval  = 0):
    """获取基于当前时间后几天"""
    return datetime.date.today() + datetime.timedelta(interval)

def get_before_date_time(interval  = 0):
    """获取基于当前时间前几天"""
    return datetime.date.today() - datetime.timedelta(interval)

