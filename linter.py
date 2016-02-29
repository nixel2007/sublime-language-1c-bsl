"""This module exports the OneScriptLint plugin class."""

import sublime
from SublimeLinter.lint import Linter, util

class OneScriptLint(Linter):
    """Provides an interface to OneScriptLint."""

    lintBSLFiles = sublime.load_settings('1c.sublime-settings').get('lintBSLFiles');
    file_name = sublime.active_window().active_view().file_name();

    syntax = '1c'
    if not (file_name.endswith('.bsl') and not lintBSLFiles):
	    cmd = ('oscript -encoding=utf-8 -check @')
	    regex = r'\{\S+\s+(?P<error>.*)\s\/\s.*:\s+(?P<line>\d+)\s+\/\s+(?P<message>.*)\}'
	    error_stream = util.STREAM_BOTH
	    comment_re = r'\s*//'
