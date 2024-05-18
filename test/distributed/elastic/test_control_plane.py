import unittest

from torch.testing._internal.common_utils import run_tests

from torch.distributed.elastic.control_plane import main

class WorkerServerTest(unittest.TestCase):
    def test_worker_server(self):
        @main()
        def my_main():
            pass

        my_main()

if __name__ == "__main__":
    run_tests()
