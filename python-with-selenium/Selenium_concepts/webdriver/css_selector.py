"""
css = cascading style sheet
syntax: tag[attribute='value']
'#' for id     '.' for class
ex: input[id=displayed-text] or #displayed-text or input#displayed-text
ex: input[class=displayed-class] or .dispalyed-class or input.displayed-class
if u find two or more classes then append with "."
ex: class=inputs displayed-class {two classes here}
.inputs.displayed-class {appended class}

Using	wildcards	in	CSS	Selectors:
“^”	->	Represents	the	starting	text
“$”	->	Represents the	ending	text
“*”	->	Represents	the	text	contained
Syntax:
tag[attribute<special	character>=’value’]
Examples:
input[class='inputs']	->	Only	1	matching	node
input[class^='inputs']	->	Two	matching	nodes
input[class='displayed-class']	- No	matching	nodes
input[class$='class']	->	One	matching	node
input[class*='displayed-class']	->	One	matching	node

Finding	Children
fieldset	->	10	matching	nodes
Fieldset>table
fieldset>#product	->	One	matching	node
fieldset>button	->	One	matching	node
Fieldset>a
fieldset>input#name
"""