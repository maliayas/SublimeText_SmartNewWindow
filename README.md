# SmartNewWindow

SmartNewWindow is a Sublime Text plugin that combines 3 commands in one
keybinding:

* New workspace for the project
* New workspace for the open folders
* New window

Picking the appropriate one is based on the context:

1.  If there is an open project, a new workspace is created.
2.  If there is no open project but there are open folders, then the
    unsaved workspace is replicated (only folders). Sublime Text doesn't
    offer this natively.
3.  Otherwise an empty window is created.

The keybinding is <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>N</kbd> for
Windows/Linux and <kbd>⌘</kbd><kbd>⇧</kbd><kbd>N</kbd> for OS X.

## Overview

* [Installation](#installation)
* [Configuration](#configuration)
* [License](#license)

## Installation

You can install the plugin via

* Package Manager by searching `SmartNewWindow`
* `git clone https://github.com/maliayas/SublimeText_SmartNewWindow.git SmartNewWindow`
* Downloading the [zip][] of the repo and extracting into `Packages/SmartNewWindow`

## Configuration

For customizing the keybinding, you can use the `Preferences > Package Settings > Smart New Window` menu.

## License

SmartNewWindow is released under the [MIT License][mit].

[mit]:         http://www.opensource.org/licenses/MIT
[zip]:         https://github.com/maliayas/SublimeText_SmartNewWindow/archive/master.zip
