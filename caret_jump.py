import sublime
import sublime_plugin

OPTIONS_LAST_REGEX = "jump_caret_last_regex"


class CaretJumpCommand(sublime_plugin.TextCommand):
    def run(self, edit, jump=True, jump_to=None, repeat_previous_jump=False):
        view = self.view

        def get_next_sels(user_input):
            new_sels = []
            for sel in view.sel():
                next_sel = view.find(user_input, sel.end(), sublime.IGNORECASE)
                if next_sel.begin() != -1:
                    new_sels.append(next_sel)
            return new_sels

        def jump_last_regex():
            last_reg = self.view.settings().get(OPTIONS_LAST_REGEX)
            if last_reg:
                select_next_regex(last_reg)

        def select_next_regex(user_input):
            view.erase_regions("caret_jump_preview")
            if not user_input:
                # jump_last_regex()
                return
            self.view.settings().set(OPTIONS_LAST_REGEX, user_input)

            new_sels = get_next_sels(user_input)

            if jump and new_sels:
                view.sel().clear()

            view.sel().add_all(new_sels)

        def input_changed(user_input):
            new_sels = get_next_sels(user_input)
            view.add_regions("caret_jump_preview",
                             new_sels,
                             "source, text",
                             "dot",
                             sublime.DRAW_OUTLINED)

        def input_canceled():
            view.erase_regions("caret_jump_preview")

        selection = view.substr(view.sel()[0]) if view.sel() else ""

        if jump_to:
            select_next_regex(jump_to)
        elif repeat_previous_jump:
            jump_last_regex()
        else:
            default = selection if selection \
                else self.view.settings().get(OPTIONS_LAST_REGEX, "")
            view.window().show_input_panel("Seach for",
                                           default,
                                           select_next_regex,
                                           input_changed,
                                           input_canceled)
