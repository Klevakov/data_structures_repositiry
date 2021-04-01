from double_linked_list import LinkedList
import pytest


@pytest.mark.parametrize("lst", [[i for i in range(1, 10)], [i ** 2 for i in range(10, 2, -1)]])
def test_append(lst):
    lnkd_lst = LinkedList()
    for i in lst:
        lnkd_lst.append(i)
    for i in range(len(lst) - 1, 0, -1):
        assert lst[i] == lnkd_lst.get(i).value


@pytest.mark.parametrize("lst", [[i for i in range(10)], [i ** 2 for i in range(10, 2, -1)]])
def test_out(lst):
    lnkd_lst = LinkedList()
    test_str = ''
    for i in lst:
        lnkd_lst.append(i)
        test_str += f'{i} '
    assert lnkd_lst.out() == test_str


@pytest.mark.parametrize("lst", [[i for i in range(1, 10)], [i ** 2 for i in range(10, 2, -1)]])
def test_insert(lst):
    lnkd_lst = LinkedList()
    for i in lst:
        lnkd_lst.insert(i, 0)
    for i in range(len(lst) - 1, 0, -1):
        assert lst[::-1][i] == lnkd_lst.get(i).value


@pytest.mark.parametrize("a", [-1, 10, 15])
def test_insert_extreme_values(a):
    with pytest.raises(IndexError):
        lnkd_lst = LinkedList()
        lnkd_lst.append('Hello')
        lnkd_lst.append('World')
        lnkd_lst.append('!')
        lnkd_lst.append('Today')
        lnkd_lst.append('I')
        lnkd_lst.append('will')
        lnkd_lst.append('conquer')
        lnkd_lst.append('you')
        lnkd_lst.append('!')
        lnkd_lst.insert(5, a)


@pytest.mark.parametrize("a", [1, 2, 3,
                               'Hello', 'world', '!',
                               ('Who', 'is', 'it', '?'),
                               {100, 2, 100},
                               {'name': 'Dmitry', 'surname': 'Klevalov'},
                               [333, 222, 111, 000],
                               2.5, 5.2,
                               True, False, None])
def test_get(a):
    lnkd_lst = LinkedList()
    lnkd_lst.append(a)
    assert lnkd_lst.get(0).value == a


@pytest.mark.parametrize("a", [0, 2, 15])
def test_get_extreme_values(a):
    with pytest.raises(IndexError):
        lnkd_lst = LinkedList()
        lnkd_lst.get(a)
        lnkd_lst.append('Hello')
        lnkd_lst.append('World')
        lnkd_lst.get(a)


@pytest.mark.parametrize("a", [0, 10, 15])
def test_pop_extreme_values(a):
    with pytest.raises(IndexError):
        lnkd_lst = LinkedList()
        lnkd_lst.pop(a)
        lnkd_lst.append('Hello')
        lnkd_lst.append('World')
        lnkd_lst.append('!')
        lnkd_lst.append('Today')
        lnkd_lst.append('I')
        lnkd_lst.append('will')
        lnkd_lst.append('conquer')
        lnkd_lst.append('you')
        lnkd_lst.append('!')
        lnkd_lst.pop(a)


@pytest.mark.parametrize("a", [(3, 10, 15), ('first', 'second', 'third')])
def test_pop(a):
    lnkd_lst = LinkedList()
    for i in a:
        lnkd_lst.append(i)
    assert lnkd_lst.get(0).value == lnkd_lst.pop(0)


@pytest.mark.parametrize("lst", [[i for i in range(1, 10)], [i ** 2 for i in range(10, 2, -1)]])
def test_assign(lst):
    lnkd_lst = LinkedList()
    for i in lst:
        lnkd_lst.append(i)
    for i in range(len(lst)):
        assert lnkd_lst.get(i).value == lnkd_lst.assign(50, i)
        assert lnkd_lst.get(i).value == 50


@pytest.mark.parametrize("a", [-1, 9, 15])
def test_assign_extreme_values(a):
    with pytest.raises(IndexError):
        lnkd_lst = LinkedList()
        lnkd_lst.append('Hello')
        lnkd_lst.append('World')
        lnkd_lst.append('!')
        lnkd_lst.append('Today')
        lnkd_lst.append('I')
        lnkd_lst.append('will')
        lnkd_lst.append('conquer')
        lnkd_lst.append('you')
        lnkd_lst.append('!')
        lnkd_lst.assign('Sun', a)
