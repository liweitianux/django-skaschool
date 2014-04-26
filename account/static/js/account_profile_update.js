/*
 * account_profile_update.js
 * for 'profile_update.html' template
 */

$(document).ready(function() {
    // modify styles of supplment textarea within 'mainform'
    $(".mainform textarea#id_supplement").attr('rows', 1);
    $(".mainform textarea#id_supplement").focus(function() {
        // show 5 rows when focused
        $(this).attr('rows', 5);
    }).blur(function() {
        // show only 1 row when unfocus
        $(this).attr('rows', 1);
    });

    // modify styles of file description textarea of subforms
    $(".subform textarea").attr('rows', 1);
    $(".subform textarea").focus(function() {
        // show 3 rows when focused
        $(this).attr('rows', 3);
    }).blur(function() {
        // show only 1 row when unfocus
        $(this).attr('rows', 1);
    });

    // remove 'required' attribute of subform
    $(".subform input").filter('[required]').removeAttr('required');

    // add-subform button
    // ref: http://stackoverflow.com/questions/501719/dynamically-adding-a-form-to-a-django-formset-with-ajax
    function cloneMore(selector, type) {
        var newElement = $(selector).clone(true);
        var total = $('#id_' + type + '-TOTAL_FORMS').val();
        newElement.find(':input').each(function() {
            // update name and id attributes
            var name = $(this).attr('name').replace('-'+(total-1)+'-', '-'+total+'-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        newElement.find('label').each(function() {
            // update for attributes if exists
            if ($(this).attr('for')) {
                var newFor = $(this).attr('for').replace('-'+(total-1)+'-', '-'+total+'-');
                $(this).attr('for', newFor);
            }
        });
        // remove 'has-success has-error' classes and help-block
        newElement.children().removeClass('has-success has-error');
        newElement.find('.help-block').remove();
        // update management_form settings
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);
    }

    // Register the click event handlers
    $("#add-subform").click(function () {
        cloneMore('div.subform:last', 'userfile_set');
    });
});

