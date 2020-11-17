#!/usr/bin/env python

"""Tests for `freud_api_crawler` package."""


import unittest
from click.testing import CliRunner

from freud_api_crawler import freud_api_crawler
from freud_api_crawler import cli


class TestFreud_api_crawler(unittest.TestCase):
    """Tests for `freud_api_crawler` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'freud_api_crawler.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
