import random

import texts
import config


class FactsStore:

    def get_random_wombat_fact(self):
        raise NotImplementedError


class TextFileFactsStore(FactsStore):

    def get_random_wombat_fact(self):
        pass


class HardCodedFactsStore(FactsStore):

    def get_random_wombat_fact(self):
        return random.choice(texts.WOMBAT_FACT)


def get_facts_store():
    if config.FACTS_STORE_TYPE == 'hardcoded':
        return HardCodedFactsStore()
    elif config.FACTS_STORE_TYPE == 'text':
        return TextFileFactsStore()
    else:
        raise NotImplementedError
