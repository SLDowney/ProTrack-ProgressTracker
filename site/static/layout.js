$(document).ready(function() {
    $("#percentToggle").click(function() {
        $(".percentage").slideToggle();
    });

    // Check if the screen width is less than a certain threshold (e.g., 600px)
    function checkWindowSize() {
        if ($(window).width() <= 600) {
            $(".percentage").hide();
        } else {
            $(".percentage").show();
        }
    }

    // Initially check the window size and adjust the table visibility
    checkWindowSize();

    // Listen for window resize events
    $(window).resize(function() {
        checkWindowSize();
    });
});