/*
 * schedule.js
 * used with 'schedule.html' page
 *
 * 2014/06/24
 */

/* animated slidedown and slideup div */
$(document).ready(function() {
    /* hide() all .event-contents and .event-attchments body */
    $(".event-contents .panel-body").hide().removeClass('shown').addClass('hidden');
    $(".event-attachments .panel-body").hide().removeClass('shown').addClass('hidden');

    /* click .event-contents heading to toggle its body contents */
    $(".event-contents .panel-heading").on("click", function(e) {
        e.stopPropagation();
        ec_body = $(this).siblings(".panel-body");
        if ($(ec_body).hasClass('hidden')) {
            $(ec_body).show().removeClass('hidden').addClass('shown');
            // update heading icon and text
            span_icon = $(this).children("span.glyphicon");
            $(span_icon).removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
            span_action = $(this).children("span.action");
            $(span_action).html('隐藏');
        }
        else {
            $(ec_body).hide().removeClass('shown').addClass('hidden');
            // update heading icon and text
            span_icon = $(this).children("span.glyphicon");
            $(span_icon).removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
            span_action = $(this).children("span.action");
            $(span_action).html('显示');
        }
    });

    /* click .event-attachments heading to toggle its body attachments */
    $(".event-attachments .panel-heading").on("click", function(e) {
        e.stopPropagation();
        ec_body = $(this).siblings(".panel-body");
        if ($(ec_body).hasClass('hidden')) {
            $(ec_body).show().removeClass('hidden').addClass('shown');
            // update heading icon and text
            span_icon = $(this).children("span.glyphicon");
            $(span_icon).removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
            span_action = $(this).children("span.action");
            $(span_action).html('隐藏');
        }
        else {
            $(ec_body).hide().removeClass('shown').addClass('hidden');
            // update heading icon and text
            span_icon = $(this).children("span.glyphicon");
            $(span_icon).removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
            span_action = $(this).children("span.action");
            $(span_action).html('显示');
        }
    });
});

