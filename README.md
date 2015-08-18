# Caret Jump

Search for text for every caret starting from the current position.

## Usage

Press `ctrl+k ctrl+n` to start a search for every caret. Then type the search regex into the field and the caret will jump to the match. Use `ctrl+k ctrl+shift+n` to keep the old caret and create a additional one at the target position. Alternative use `ctrl+k ctrl+alt+n` and `ctrl+k ctrl+alt+shift+n` to reuse the last search keyword instead of typing a new one.


## Options

- **jump [*bool*]**:
    Whether the current cursor should be removed (jump) or stay (no jump).
- **jump_to [*string*]:**
    If specified the caret will jump to this (regex-)expression instead of asking for a new expression.
- **repeat_previous_jump [*bool*]:**
    If true then the last jump will be repeated instead of asking for a new expression. This option will be ignored if **jump_to** is specified.


## Questions

### What is the difference to a usual search?

This packet is for the use of multiple carets and starts the search for every caret instead of one global search of the document. The goal of this package is not to replace the search functionality, but to add an additional and easy-to-use multiple-caret feature.


## Demonstration

__TODO__

