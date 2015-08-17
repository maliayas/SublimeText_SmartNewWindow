import sublime
import sublime_plugin


class SmartNewWindowCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        current_window = sublime.active_window()

        if current_window.project_file_name():
            # A project file is already open. Sublime Text covers this case with a
            # command.

            current_window.run_command("new_window_for_project")

        elif current_window.folders():
            # No project is open. There are just open folders added to the window.
            # We will replicate the in-memory project manually.

            current_window.run_command("new_window")
            new_window = sublime.active_window()

            new_window.set_project_data(current_window.project_data())

        else:
            # No project or open folders. We will just create a plain new window.

            current_window.run_command("new_window")

    def is_enabled(self):
        return True
