// ajax.js

$(document).ready(function() {
    $('#send-btn').click(function() {
        var msg = $('#user-input').val();
        $('#user-input').val('');
        $.ajax({
            type: 'POST',
            url: '/get/',  // URL endpoint for your Django view handling chat requests
            data: {'msg': msg},
            success: function(response) {
                // Handle successful response
                console.log(response);
                // Update the chat box with the response
                $('#chat-box').append('<div class="message">' + response.response + '</div>');
                // Scroll to the bottom of the chat box
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function(xhr, textStatus, errorThrown) {
                // Handle errors
                console.error('Error:', errorThrown);
            }
        });
    });
});
