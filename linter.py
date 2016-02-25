"""This module exports the OneScriptLint plugin class."""

from SublimeLinter.lint import Linter, util

class OneScriptLint(Linter):
    """Provides an interface to OneScriptLint."""

    syntax = '1c'
    cmd = ('oscript -encoding=utf-8 -check @')
    regex = r'\{\S+\s+(?P<error>.*)\s\/\s.*:\s+(?P<line>\d+)\s+\/\s+(?P<message>.*)\}'
    error_stream = util.STREAM_BOTH
    comment_re = r'\s*//'
