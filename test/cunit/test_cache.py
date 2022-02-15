from test.cunit import C
from test.cunit.cache import Chain, HashTable, LruCache, Queue, QueueItem

import pytest

NULL = 0


def test_queue_item():
    value = C.malloc(16)
    queue_item = QueueItem(value, 42)
    assert queue_item.__cself__

    queue_item.destroy(C.free)


@pytest.mark.parametrize("qsize", [0, 10, 100, 1000])
def test_queue(qsize):
    q = Queue(qsize, C.free)

    assert q.is_empty()
    assert qsize == 0 or not q.is_full()

    assert q.dequeue() is NULL

    values = [C.malloc(16) for _ in range(qsize)]
    assert all(values)

    for k, v in enumerate(values):
        assert q.enqueue(v, k)

    assert qsize == 0 or not q.is_empty()
    assert q.is_full()
    assert q.enqueue(42, 42) is NULL

    assert values == [q.dequeue() for _ in range(qsize)]


def test_chain():
    head = Chain(0, NULL)

    head.add(42, 24)

    assert head.has(42)
    assert not head.has(43)
    assert head.find(42) == 24
    assert head.find(43) is NULL

    head.remove(42)
    assert not head.has(42)
    assert head.find(42) is NULL


def test_hash_table():
    t = HashTable(10)
    assert t.get(42) is NULL

    t.set(42, 24)
    assert t.get(42) == 24

    getattr(t, "del")(42)
    assert t.get(42) is NULL


def test_hash_table_full():
    t = HashTable(10)

    for i in range(11):
        t.set(42 + i, i + 1)

    assert t.get(52) is NULL

    assert t.get(42) == 1

    t.set(42, 24)
    assert t.get(42) == 24


def test_lru_cache():
    c = LruCache(10, C.free)
    assert c.maybe_hit(42) is NULL

    values = [(42 + i, C.malloc(8)) for i in range(10)]
    for k, v in values:
        c.store(k, v)

    for i in range(8):
        assert c.maybe_hit(42 + i) == values[i][1]

    assert c.maybe_hit(51) == values[9][1]

    c.store(100, C.malloc(8))
    assert c.maybe_hit(50) is NULL