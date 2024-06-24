function updateTable() {
    $.post('api:8080/execute', {tickets: $('#tickets').val(), threshold: $('#threshold').val(), timestamp: $('#timestamp').val()}).done(function(data) {
        $('#tbody').empty();
        for (const [key, value] of Object.entries(data)) {
            $('#tbody').append("<tr><td>" + key + "</td><td>" + value + "</td></tr>")
        }
    });
}