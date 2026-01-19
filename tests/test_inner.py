from threading import Thread

from denial import InnerNone, InnerNoneType


def test_inner_none_is_inner_none():
    assert InnerNone is InnerNone  # noqa: PLR0124


def test_inner_none_is_instance_of_inner_none_type():
    assert isinstance(InnerNone, InnerNoneType)


def test_str_inner_none():
    assert str(InnerNone) == 'InnerNone'


def test_repr_inner_none():
    assert repr(InnerNone) == 'InnerNone'


def test_new_instance_has_id_more_0():
    instance_1 = InnerNoneType()
    instance_2 = InnerNoneType()

    assert isinstance(instance_1.id, int)
    assert isinstance(instance_2.id, int)

    assert InnerNone.id == 0
    assert instance_1.id > 0
    assert instance_2.id > 0
    assert instance_2.id == instance_1.id + 1


def test_new_instance_repr():
    new_instance = InnerNoneType()
    assert repr(new_instance) == f'InnerNoneType({new_instance.id})'
    assert repr(InnerNoneType('kek')) == "InnerNoneType('kek')"
    assert repr(InnerNoneType(123)) == "InnerNoneType(123)"


def test_eq():
    new_instance = InnerNoneType()

    assert InnerNone == InnerNone  # noqa: PLR0124
    assert InnerNone != new_instance
    assert InnerNone != InnerNoneType('kek')
    assert InnerNone != InnerNoneType(123)

    assert new_instance == new_instance  # noqa: PLR0124
    assert new_instance != InnerNoneType()
    assert InnerNoneType() != InnerNoneType()

    assert InnerNoneType(123) == InnerNoneType(123)
    assert InnerNoneType('kek') == InnerNoneType('kek')

    assert InnerNoneType(123) != InnerNoneType(124)
    assert InnerNoneType('kek') != InnerNoneType(123)
    assert InnerNoneType('kek') != InnerNoneType('lol')

    assert InnerNone != None  # noqa: E711
    assert InnerNoneType() != None  # noqa: E711
    assert InnerNoneType(123) != None  # noqa: E711

    assert InnerNoneType(123) != 123
    assert InnerNoneType('kek') != 'kek'


def test_hashing_and_use_as_key_in_dict():
    assert hash(InnerNone) == hash(InnerNone.id)
    assert hash(InnerNoneType(123)) == hash(123)
    assert hash(InnerNoneType('123')) == hash('123')

    new_instance = InnerNoneType()
    assert hash(new_instance) == hash(new_instance.id)

    dict_with_it = {new_instance: 'kek'}
    assert dict_with_it[new_instance] == 'kek'


def test_thread_safety():
    number_of_iterations = 10_000
    number_of_threads = 10

    nones = []

    def go_increment():
        for _ in range(number_of_iterations):
            nones.append(InnerNoneType())

    threads = [Thread(target=go_increment()) for _ in range(number_of_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert len(set(x.id for x in nones)) == number_of_iterations * number_of_threads
