function get_sufix(string) {
    regex = new RegExp('\\w+_');
    return string.replace(regex, '');
}

$(document).ready(function() {
    $("input[type='checkbox']").change(function() {
        var todo_id = get_sufix(
            $(this).attr('id')
        );
        var todolist_id = get_sufix(
            $(this).attr('todolist')
        );

        $.getJSON("/todolist/" + todolist_id + "/todo/" + todo_id + "/change/state/");
    });
});
