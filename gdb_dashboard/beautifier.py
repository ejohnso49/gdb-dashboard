from gdb_dashboard.settings.r import R


class Beautifier:
    def __init__(self, hint, tab_size=4):
        self.tab_spaces = " " * tab_size if tab_size else None
        self.active = False
        if not R.ansi or not R.syntax_highlighting:
            return
        # attempt to set up Pygments
        try:
            import pygments
            from pygments.lexers import GasLexer, NasmLexer
            from pygments.formatters import Terminal256Formatter

            if hint == "att":
                self.lexer = GasLexer()
            elif hint == "intel":
                self.lexer = NasmLexer()
            else:
                from pygments.lexers import get_lexer_for_filename

                self.lexer = get_lexer_for_filename(hint, stripnl=False)
            self.formatter = Terminal256Formatter(style=R.syntax_highlighting)
            self.active = True
        except ImportError:
            # Pygments not available
            pass
        except pygments.util.ClassNotFound:
            # no lexer for this file or invalid style
            pass

    def process(self, source):
        # convert tabs if requested
        if self.tab_spaces:
            source = source.replace("\t", self.tab_spaces)
        if self.active:
            import pygments

            source = pygments.highlight(source, self.lexer, self.formatter)
        return source.rstrip("\n")
