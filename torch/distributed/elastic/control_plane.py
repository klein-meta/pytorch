from contextlib import contextmanager
from torch.distributed.elastic.multiprocessing.errors import record

@contextmanager
@record
def main() -> None:
    from torch._C._distributed_c10d import (
        _WorkerServer,
    )
    server = _WorkerServer("/tmp/foo.socket")
    yield
    server.shutdown()
