from unittest import mock
import unittest


from facts_store import TextFileFactsStore, HardCodedFactsStore, FactsStore, get_facts_store
import texts


class FactsStoreBaseTestCase:

    def test_get_random_wombat_fact(self):
        #print(self.__class__)
        self.fact_store.get_random_wombat_fact()


class FactsStoreTestCase(FactsStoreBaseTestCase, unittest.TestCase):
    def setUp(self):
        self.fact_store = FactsStore()

    def test_get_random_wombat_fact(self):
        with self.assertRaises(NotImplementedError):
            self.fact_store.get_random_wombat_fact()


class TextFileFactsStoreTestCase(FactsStoreBaseTestCase, unittest.TestCase):
    def setUp(self):
        self.fact_store = TextFileFactsStore()

    def test_get_random_wombat_fact_textfilefactsstore(self):
        pass

    def test_get_facts_store_text(self):
        with mock.patch('config.FACTS_STORE_TYPE', new='text'):
            self.assertIsInstance(get_facts_store(), TextFileFactsStore)

class HardCodedFactsStoreTestCase(FactsStoreBaseTestCase, unittest.TestCase):
    def setUp(self):
        self.fact_store = HardCodedFactsStore()

    # def test_get_facts_store_hardcoded(self):
    #    self.assertIsInstance(get_facts_store(), FactsStore)

    def test_get_random_wombat_fact_hardcodedfactsstore(self):
        self.assertIn(HardCodedFactsStore.get_random_wombat_fact(self), texts.WOMBAT_FACT)

    def test_get_facts_store_hardcoded(self):
        with mock.patch('config.FACTS_STORE_TYPE', new='hardcoded') as m:
            self.assertIsInstance(get_facts_store(), HardCodedFactsStore)


if __name__ == "__main__":
    unittest.main()

