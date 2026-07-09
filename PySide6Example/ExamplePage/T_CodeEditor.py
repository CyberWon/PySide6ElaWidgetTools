from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ElaWidgetTools import (
    ElaCodeEditor,
    ElaComboBox,
    ElaScrollPageArea,
    ElaText,
)
from ExamplePage.T_BasePage import T_BasePage

_CPP = (
    "#include <QApplication>\n"
    '#include "ElaWindow.h"\n\n'
    "// ElaWidgetTools C++ example\n"
    "int main(int argc, char *argv[])\n"
    "{\n"
    "    QApplication app(argc, argv);\n"
    "    ElaWindow window;\n"
    '    window.setWindowTitle("Hello");\n'
    "    window.resize(1200, 740);\n"
    "    window.show();\n"
    "    return app.exec();\n"
    "}\n"
)

_C = (
    "#include <stdio.h>\n"
    "#include <stdlib.h>\n\n"
    "/* Classic C example */\n"
    "int main(int argc, char *argv[])\n"
    "{\n"
    "    int count = 10;\n"
    "    for (int i = 0; i < count; i++)\n"
    "    {\n"
    '        printf("Hello %d\\n", i);\n'
    "    }\n"
    "    return 0;\n"
    "}\n"
)

_CSHARP = (
    "using System;\n"
    "using System.Linq;\n\n"
    "namespace ElaDemo\n"
    "{\n"
    "    // C# example\n"
    "    public class Program\n"
    "    {\n"
    "        static async Task Main(string[] args)\n"
    "        {\n"
    "            var items = new List<int> { 1, 2, 3 };\n"
    "            foreach (var item in items)\n"
    "            {\n"
    '                Console.WriteLine($"Item: {item}");\n'
    "            }\n"
    "            await Task.Delay(1000);\n"
    "        }\n"
    "    }\n"
    "}\n"
)

_PYTHON = (
    "import os\n"
    "from dataclasses import dataclass\n\n"
    "@dataclass\n"
    "class Widget:\n"
    "    name: str\n"
    "    version: float = 2.0\n\n"
    "# Python example\n"
    "def main():\n"
    '    widgets = [Widget("Button"), Widget("Slider", 1.5)]\n'
    "    for w in widgets:\n"
    '        print(f"Widget: {w.name} v{w.version}")\n\n'
    "    count = len(widgets)\n"
    "    if count > 0:\n"
    '        print(f"Total: {count} widgets")\n\n'
    'if __name__ == "__main__":\n'
    "    main()\n"
)

_JS = (
    "import { createApp } from 'vue';\n\n"
    "// JavaScript example\n"
    "class WidgetManager {\n"
    "    constructor() {\n"
    "        this.widgets = [];\n"
    "    }\n\n"
    "    async loadWidgets() {\n"
    "        const response = await fetch('/api/widgets');\n"
    "        this.widgets = await response.json();\n"
    "        console.log(`Loaded ${this.widgets.length} widgets`);\n"
    "    }\n"
    "}\n\n"
    "const manager = new WidgetManager();\n"
    "manager.loadWidgets();\n"
)

_LUA = (
    "-- Lua example\n"
    "local Widget = {}\n"
    "Widget.__index = Widget\n\n"
    "function Widget.new(name, version)\n"
    "    local self = setmetatable({}, Widget)\n"
    '    self.name = name or "Unknown"\n'
    "    self.version = version or 1.0\n"
    "    return self\n"
    "end\n\n"
    "function Widget:display()\n"
    '    print(string.format("%s v%.1f", self.name, self.version))\n'
    "end\n\n"
    "local widgets = {\n"
    '    Widget.new("Button", 2.0),\n'
    '    Widget.new("Slider", 1.5),\n'
    "}\n\n"
    "for i, w in ipairs(widgets) do\n"
    "    w:display()\n"
    "end\n"
)

_RUST = (
    "use std::collections::HashMap;\n\n"
    "/// Rust example\n"
    "struct Widget {\n"
    "    name: String,\n"
    "    version: f64,\n"
    "}\n\n"
    "impl Widget {\n"
    "    fn new(name: &str, version: f64) -> Self {\n"
    "        Widget {\n"
    "            name: name.to_string(),\n"
    "            version,\n"
    "        }\n"
    "    }\n"
    "}\n\n"
    "fn main() {\n"
    "    let widgets = vec![\n"
    '        Widget::new("Button", 2.0),\n'
    '        Widget::new("Slider", 1.5),\n'
    "    ];\n"
    "    for w in &widgets {\n"
    '        println!("{} v{}", w.name, w.version);\n'
    "    }\n"
    "}\n"
)

_PHP = (
    "<?php\n"
    "declare(strict_types=1);\n\n"
    "// PHP example\n"
    "class Widget\n"
    "{\n"
    "    public function __construct(\n"
    "        private string $name,\n"
    "        private float $version = 1.0\n"
    "    ) {}\n\n"
    "    public function display(): void\n"
    "    {\n"
    "        echo \"{$this->name} v{$this->version}\\n\";\n"
    "    }\n"
    "}\n\n"
    "$widgets = [\n"
    '    new Widget("Button", 2.0),\n'
    '    new Widget("Slider", 1.5),\n'
    "];\n\n"
    "foreach ($widgets as $w) {\n"
    "    $w->display();\n"
    "}\n"
)

_DEMOS = [_CPP, _C, _CSHARP, _PYTHON, _JS, _LUA, _RUST, _PHP]


class T_CodeEditor(T_BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ElaCodeEditor")
        self.createCustomWidget("代码编辑器，支持行号显示和多语言语法高亮")

        centralWidget = QWidget(self)
        centralWidget.setWindowTitle("ElaCodeEditor")

        langCombo = ElaComboBox(self)
        langCombo.addItems(["C++", "C", "C#", "Python", "JavaScript", "Lua", "Rust", "PHP"])

        langArea = ElaScrollPageArea(self)
        langLayout = QHBoxLayout(langArea)
        langText = ElaText("语言", self)
        langText.setTextPixelSize(15)
        langLayout.addWidget(langText)
        langLayout.addWidget(langCombo)
        langLayout.addStretch()

        self._codeEditor = ElaCodeEditor(self)
        self._codeEditor.setIsReadOnly(True)
        self._codeEditor.setLanguage(ElaCodeEditor.Language.CPP)
        self._codeEditor.setCode(_CPP)

        def onLangChanged(index):
            self._codeEditor.setLanguage(ElaCodeEditor.Language(index))
            self._codeEditor.setCode(_DEMOS[index])

        langCombo.currentIndexChanged.connect(onLangChanged)

        centerVLayout = QVBoxLayout(centralWidget)
        centerVLayout.setContentsMargins(0, 0, 0, 0)
        centerVLayout.addWidget(langArea)
        centerVLayout.addWidget(self._codeEditor)
        self.addCentralWidget(centralWidget, True, False, 0)
