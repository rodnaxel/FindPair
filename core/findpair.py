# -*- coding: utf-8 -*-

from math import sqrt, pow
from core.utils import load_gain_from_excel

gain_dp = [205, 125, 79, 69, 56, 47, 38, 32, 28, 26,
           25, 24, 22, 20, 19, 16.5, 15.6, 15, 14, 13.5,
           13, 12.3, 12, 11.2, 11, 10.3, 10, 9.5, 9.3, 9,
           8.5, 8.1, 7.8, 7.6, 7.5, 7.4, 7.2, 7, 6.9, 6.7,
           6.5, 6.4, 6.3, 6.1, 6, 5.8, 5.7, 5.6, 5.5, 5.4,
           5.3, 5.2, 5.1, 5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4,
           4.3, 4.2, 4.1, 4, 3.97, 3.95, 3.9, 3.85, 3.8, 3.75,
           3.7, 3.65, 3.6, 3.55, 3.5, 3.45, 3.4, 3.35, 3.3, 3.25,
           3.2, 3.15, 3.1, 3.05, 3, 2.95, 2.9, 2.88, 2.85, 2.82,
           2.8, 2.79, 2.78, 2.76, 2.74, 2.72, 2.71, 2.7, 2.69, 2.68,
           2.64, 2.6, 2.57, 2.53, 2.5, 2.47, 2.44, 2.42, 2.4, 2.38,
           2.35, 2.32, 2.3, 2.28, 2.26, 2.24, 2.23, 2.2, 2.18, 2.16,
           2.15, 2.13, 2.12, 2.1, 2.08, 2.06, 2.04, 2.02, 2.01, 2,
           1.99, 1.97, 1.95, 1.93, 1.92, 1.9, 1.89, 1.88, 1.87, 1.85,
           1.83, 1.82, 1.81, 1.8, 1.79, 1.78, 1.77, 1.75, 1.74, 1.73,
           1.71, 1.7, 1.69, 1.68, 1.67, 1.66, 1.65, 1.63, 1.62, 1.61,
           1.6, 1.59, 1.58, 1.57, 1.56, 1.55, 1.55, 1.54, 1.53, 1.52,
           1.51, 1.5, 1.49, 1.49, 1.48, 1.48, 1.48, 1.47, 1.46, 1.45,
           1.44, 1.43, 1.42, 1.41, 1.4, 1.4, 1.39, 1.38, 1.37, 1.36,
           1.36, 1.35, 1.34, 1.34, 1.33, 1.32, 1.31, 1.31, 1.3, 1.29,
           1.29, 1.28, 1.27, 1.27, 1.26, 1.26, 1.25, 1.24, 1.24, 1.23,
           1.23, 1.22, 1.21, 1.21, 1.2, 1.2, 1.19, 1.19, 1.18, 1.17,
           1.17, 1.16, 1.16, 1.15, 1.15, 1.14, 1.14, 1.13, 1.13, 1.12,
           1.12, 1.11, 1.11, 1.1, 1.1, 1.09, 1.09, 1.08, 1.08, 1.07,
           1.07, 1.06, 1.06, 1.06, 1.05, 1.05, 1.04, 1.04, 1.03, 1.03,
           1.02, 1.02, 1.02, 1.01, 1.01, 1]

class RainbowTable(object):
    def __init__(self, gains):
        self.gains = gains

    def __iter__(self):
        """
        return:
            ((gain1, gain2), gain1 x gain2, S1 - S2, (Step 1,Step 2))
        """
        for i, m in enumerate(self.gains):
            for j, n in enumerate(self.gains[i:]):
                yield ((m, n), m * n, abs(j), (i, j + i))


def get_nearest_value(iterable, value):
    """ Возвращает ближайшее к заданному значение в списке"""
    return min(iterable, key=lambda x: abs(x - value))


def find_pair(gain, table, limit):
    filtered = [item for item in table if item[2] <= limit]
    calculated_gains = [item[1] for item in filtered]
    near = get_nearest_value(calculated_gains, gain)
    index = calculated_gains.index(near)

    dp_gains,*_, dp_steps = filtered[index]
    
    return dp_gains, dp_steps


def get_amplifier_pairs(gains, deltas, table):
    result = []
    for gain in gains:
        (k1, k2), (s1, s2) = find_pair(gain, table, deltas)
        delta = gain - k1 * k2
        result.append((k1, k2, k1 * k2, gain - k1 * k2, s1, s2))
    return result


def make_it_beatiful(src, **param):
    gains = load_gain_from_excel(
        src['filename'],
        src['sheet'],
        src["column"] + src["min_row"],
        src["column"] + src["max_row"]
    )

    #Fixme:
    if not param['points']:
        table = RainbowTable(gain_dp)
    else:
        table = RainbowTable(param['points'])

    normalize_gains = [gain / param.get('m', 1) for gain in gains]

    result = get_amplifier_pairs(normalize_gains, param["tolerance"], table)

    # [gains, k1xk2, k1, k2, diff gain, s1, s2 ]
    k1 = [x[0] for x in result]
    k2 = [x[1] for x in result]
    k1xk2 = [x[2] for x in result]
    diff = [x[3] for x in result]
    step1 = [x[4] for x in result]
    step2 = [x[5] for x in result]

    return (normalize_gains,
            k1xk2,
            k1,
            k2,
            diff,
            step1,
            step2
            )

