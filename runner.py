from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class TunnerTest(TestCase):
    def test_walk(self):
        run = Runner('Ted')
        for i in range(10):
            run.walk()
        return self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner('Ted')
        for i in range(10):
            run.run()
        return self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = Runner('Ted')
        run2 = Runner('Bil')
        for i in range(10):
            run1.run()
            run2.walk()
        return self.assertNotEqual(run1.distance, run2.distance)
