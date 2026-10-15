import unittest
from examples.accounting_example import Account, account_nav, executed_lot

class TestIllustrativeAccounting(unittest.TestCase):
    def test_nav_includes_pending_once(self):
        a = Account(1000., 500., 10, 2, 100.)
        self.assertEqual(account_nav(a), 2700.)
    def test_adv_limit_and_lot(self):
        self.assertEqual(executed_lot(26000, 30000, 512305), 25600)
    def test_historical_order_size_is_an_illustration_only(self):
        # Tham số từ ví dụ B4 01/10/2026; minh họa độc lập, không tái hiện hệ thống.
        executed = executed_lot(37700, 37700, 512305)
        self.assertEqual(executed, 25600)
        self.assertEqual(37700 - executed, 12100)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            executed_lot(100, 100, -1)

if __name__ == '__main__':
    unittest.main()
