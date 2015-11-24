$(function () {
    var code = $("#code");
    var out = $("#output");
    var editor = CodeMirror.fromTextArea(code[0], {
        lineNumbers: true,
        mode: "text",
        theme: 'blackboard'
    });
    var output = CodeMirror.fromTextArea(out[0], {
        lineNumbers: true,
        mode: "text",
        theme: 'blackboard'
    });
    window.onkeydown = function (event) {
        if (event.keyCode == 13) {
            $.post("/exeComm",
                {"commands": editor.getLine(editor.getCursor().line - 1)},
                function (msg) {
                    output.setValue(msg);
                });
            editor.onfocus();
        }
    }
});
