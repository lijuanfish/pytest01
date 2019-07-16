import pytest
import random


class TestLogin:
    # def test_log1(self):
    #     num = random.randint(1,3)
    #     if num == 2:
    #         assert 1
    #         print("1")
    #     else:
    #         assert 0
    def test_log2(self):
        print("2")
        assert 1
    # @pytest.mark.run(order=0)
    # @pytest.mark.skipif(True,reason="跳过该函数")
    def test_log3(self):
        print("3")
        assert 1
    # @pytest.mark.run(order=1)
    def test_log4(self):
        print("4")
        assert 1

if __name__ == '__main__':
    pytest.main(["-s","test_login.py"])