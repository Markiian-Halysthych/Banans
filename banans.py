import unittest


def find_min_speed_per_hour(piles, hours):

    max_speed = 0
    all_bananas = 0
    for index in range(len(piles)):
        all_bananas += piles[index]
        if max_speed < piles[index]:
            max_speed = piles[index]
    optimized_min_speed = all_bananas // hours
    if len(piles) == hours:
        return max_speed
    return binary_search(piles, optimized_min_speed, max_speed, hours)


def binary_search(piles, min_speed, max_speed, hours):

    if len(piles) > hours:
        return -1
    average_speed = (min_speed + max_speed) // 2
    if min_speed < max_speed:
        if able_to_eat_in_time(piles, average_speed, hours):
            return binary_search(piles, min_speed, average_speed, hours)
        else:
            return binary_search(piles, average_speed + 1, max_speed, hours)
    return min_speed


def able_to_eat_in_time(piles, speed, hours):

    real_hours = 0
    for pile in piles:
        real_hours += pile // speed
        if pile % speed != 0:
            real_hours += 1
    return real_hours <= hours


class TestTaskMethods(unittest.TestCase):

    def test_finding_min_speed(self):
        self.assertEqual(find_min_speed_per_hour([3, 6, 7, 11], 8), 4)
        self.assertEqual(find_min_speed_per_hour([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(find_min_speed_per_hour([30, 11, 23, 4, 20], 6), 23)
        self.assertEqual(find_min_speed_per_hour([10, 3], 3), 5)
        self.assertEqual(find_min_speed_per_hour([3, 7, 1], 2), -1)

    def test_binary_search(self):
        self.assertEqual(binary_search([4, 7, 2, 8, 9], 1, 9, 6), 8)
        self.assertEqual(binary_search([4, 7, 2, 8, 9], 1, 9, 3), -1)

    def test_capability_to_eat_all(self):
        self.assertTrue(able_to_eat_in_time([3, 9, 4, 7, 8], 4, 9), True)
        self.assertEqual(able_to_eat_in_time([3, 9, 4, 7, 8], 5, 7), False)


if __name__ == '__main__':
    unittest.main()