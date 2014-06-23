/*
 * traffic.js
 * used with 'traffic.html' page
 *
 * 2014/06/23
 */

/* bootstrap 3 built-in modal plugin */
$(document).ready(function() {
    $("img.modal-images").on("click", function() {
        var src = $(this).attr('src');
        var img_html = '<img src="'+src+'" class="img-responsive">';
        var orig_html = $('#imageviewer-modal .modal-body').html();
        // modal
        $('#imageviewer-modal').modal('toggle');
        // action
        $('#imageviewer-modal').on('shown.bs.modal', function() {
            $('#imageviewer-modal .modal-body').html(img_html);
        });
        $('#imageviewer-modal').on('hidden.bs.modal', function() {
            $('#imageviewer-modal .modal-body').html(orig_html);
        });
    });
});

