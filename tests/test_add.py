#!/usr/bin/env python3
# pylint: disable=no-self-use
"""Test unit."""

import unittest


class OnlineTestCase(unittest.TestCase):
    """Main class."""

    def test_main(self):
        """Call main."""
        from umbr_api.add import main

        main()


if __name__ == "__main__":
    unittest.main()
