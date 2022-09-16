import pytest















def test_home(client):
    res = client.get('/')

    expected="home"
    assert set(expected)==set(res.get_data(as_text= True))

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here"""


if __name__ == '__main__':
    unittest.main()
