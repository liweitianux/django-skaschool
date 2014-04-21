/*
 * email_resend.js for 'account/email_resend.html'
 */

$(document).ready(function() {
    // disable email field by default
    $("input#id_email").prop("disabled", true);

    // update email field when 'is_update_email' checkbox changed
    $("input#id_is_update_email").change(function(e) {
        if ($(this).prop("checked")) {
            $("input#id_email").prop("disabled", false);
        }
        else {
            $("input#id_email").prop("disabled", true);
        }
    });
});

