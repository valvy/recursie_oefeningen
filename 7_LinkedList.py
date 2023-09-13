import unittest


class LinkedList(object):
    """
    Linkedlist is een datastructuur vergelijkbaar met een lijst.
    Dit is een recursieve datastructuur.
    Er is een root met verschillende nodes.
    """
    class Node(object):
        """
        De interne nodes.
        Deze heeft zichzelf als datastructuur (Zie self.__next)
        En een waarde
        """
        def __init__(self, item):
            """
            Next is de volgende node
            data is de weaarde
            """
            self.__next = None

            self.__data = item

        def __iadd__(self, other):
            """
            Voeg een node toe als de huidige next None is.
            Wanneer er al wel een node is, delegeer dit naar de volgende node
            """
            if self.__next is None:
                self.__next = LinkedList.Node(other)
            else:

                self.__next += other
            return self

        def remove(self, n):
            """
            Wanneer de volgende node de laatste is, verwijder deze.
            Anders geef een error
            Wanneer weet dat de volgende node niet de laatste is, delegeer de taak naar die node
            """
            pass

        def __len__(self):
            pass

        def __getitem__(self, n) -> object:
            pass

        def get_next(self):
            return self.__next

        def get_item(self):
            return self.__data

    def __init__(self, *args: object):
        self.__root = None
        for i in args:
            self.__iadd__(i)


    def __len__(self) -> int:
        """
        Speciale methode
        Geef de lengte van de lijst terug
        """
        pass


    def add_front(self, item):
        """
        Geef de eerste element terug
        """
        pass

    def remove(self, n):
        """
        Verwijder de element op de gegeven nummer
        """

    def remove_front(self):
        self.remove(0)

    def __iadd__(self, item) -> object:
        """
        element toe
        """
        pass

    def __getitem__(self, n: int) -> object:
        """Haal een element op"""
        pass

class TestLinkedList(unittest.TestCase):
    def test_add_get_linked_list(self):
        my_list = LinkedList()
        get_element = 0
        should_return = 1

        my_list += should_return
        result = my_list[get_element]

        self.assertEqual(should_return, result)

    def test_create_linked_list_multiple_parameters(self):
        my_list = LinkedList(1, 2, 3, 4)
        get_element = 2
        should_return = 3

        result = my_list[get_element]

        self.assertEqual(should_return, result)

    def test_create_linked_list_second(self):
        my_list = LinkedList(1, 2, 3)
        add_item = 4
        linked_list_length = 3

        my_list += add_item
        result = my_list[linked_list_length]

        self.assertEqual(add_item, result)

    def test_test_len_list(self):
        my_list = LinkedList(1, 2, 3, 4)
        length = 4

        result = len(my_list)

        self.assertEqual(length, result)

    def test_out_of_bounds(self):
        my_list = LinkedList(1, 2)
        length = 4
        self.assertRaises(IndexError, my_list.__getitem__, length)

    def test_add_front(self):
        my_list = LinkedList(1, 2)
        to_add = 42

        my_list.add_front(to_add)

        self.assertEqual(to_add, my_list[0])

    def test_remove_front(self):
        my_list = LinkedList(1, 2)
        resulting_length = 1

        my_list.remove_front()

        self.assertEqual(resulting_length, len(my_list))

    def test_remove_Last(self):
        my_list = LinkedList(1, 2, 3)
        last_value = 2

        my_list.remove(len(my_list))

        print(my_list)
        #self.assertEqual(last_value, my_list[len(my_list)])
