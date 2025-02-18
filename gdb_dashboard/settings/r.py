class R:
    @staticmethod
    def attributes():
        return {
            # miscellaneous
            "ansi": {
                "doc": "Control the ANSI output of the dashboard.",
                "default": True,
                "type": bool,
            },
            "syntax_highlighting": {
                "doc": """Pygments style to use for syntax highlighting.

Using an empty string (or a name not in the list) disables this feature. The
list of all the available styles can be obtained with (from GDB itself):

    python from pygments.styles import *
    python for style in get_all_styles(): print(style)""",
                "default": "monokai",
            },
            "discard_scrollback": {
                "doc": """Discard the scrollback buffer at each redraw.

This makes scrolling less confusing by discarding the previously printed
dashboards but only works with certain terminals.""",
                "default": True,
                "type": bool,
            },
            # values formatting
            "compact_values": {
                "doc": "Display complex objects in a single line.",
                "default": True,
                "type": bool,
            },
            "max_value_length": {
                "doc": "Maximum length of displayed values before truncation.",
                "default": 100,
                "type": int,
            },
            "value_truncation_string": {
                "doc": "String to use to mark value truncation.",
                "default": "…",
            },
            "dereference": {
                "doc": "Annotate pointers with the pointed value.",
                "default": True,
                "type": bool,
            },
            # prompt
            "prompt": {
                "doc": """GDB prompt.

This value is used as a Python format string where `{status}` is expanded with
the substitution of either `prompt_running` or `prompt_not_running` attributes,
according to the target program status. The resulting string must be a valid GDB
prompt, see the command `python print(gdb.prompt.prompt_help())`""",
                "default": "{status}",
            },
            "prompt_running": {
                "doc": """Define the value of `{status}` when the target program is running.

See the `prompt` attribute. This value is used as a Python format string where
`{pid}` is expanded with the process identifier of the target program.""",
                "default": r"\[\e[1;35m\]>>>\[\e[0m\]",
            },
            "prompt_not_running": {
                "doc": """Define the value of `{status}` when the target program is running.

See the `prompt` attribute. This value is used as a Python format string.""",
                "default": r"\[\e[90m\]>>>\[\e[0m\]",
            },
            # divider
            "omit_divider": {
                "doc": "Omit the divider in external outputs when only one module is displayed.",
                "default": False,
                "type": bool,
            },
            "divider_fill_char_primary": {
                "doc": "Filler around the label for primary dividers",
                "default": "─",
            },
            "divider_fill_char_secondary": {
                "doc": "Filler around the label for secondary dividers",
                "default": "─",
            },
            "divider_fill_style_primary": {
                "doc": "Style for `divider_fill_char_primary`",
                "default": "36",
            },
            "divider_fill_style_secondary": {
                "doc": "Style for `divider_fill_char_secondary`",
                "default": "90",
            },
            "divider_label_style_on_primary": {
                "doc": "Label style for non-empty primary dividers",
                "default": "1;33",
            },
            "divider_label_style_on_secondary": {
                "doc": "Label style for non-empty secondary dividers",
                "default": "1;37",
            },
            "divider_label_style_off_primary": {
                "doc": "Label style for empty primary dividers",
                "default": "33",
            },
            "divider_label_style_off_secondary": {
                "doc": "Label style for empty secondary dividers",
                "default": "90",
            },
            "divider_label_skip": {
                "doc": "Gap between the aligning border and the label.",
                "default": 3,
                "type": int,
                "check": lambda x: x >= 0,
            },
            "divider_label_margin": {
                "doc": "Number of spaces around the label.",
                "default": 1,
                "type": int,
                "check": lambda x: x >= 0,
            },
            "divider_label_align_right": {
                "doc": "Label alignment flag.",
                "default": False,
                "type": bool,
            },
            # common styles
            "style_selected_1": {"default": "1;32"},
            "style_selected_2": {"default": "32"},
            "style_low": {"default": "90"},
            "style_high": {"default": "1;37"},
            "style_error": {"default": "31"},
            "style_critical": {"default": "0;41"},
        }
