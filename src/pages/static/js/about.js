
$(".js-btn").click(function(){
    $('.js-btn').hide(500);
    $('.js-btn-x').show(500);
    $('#toggle-div').addClass('toggle');
    $('.nav-mid').show(500);
    $('.nav-right').show(500);
    $('.brands-toggle').show('500');
});

$(".js-btn-x").click(function(){
    $('.nav-right').hide(500);
    $('.nav-mid').hide(500);
    $('.brands-toggle').hide('500');
    $('#toggle-div').removeClass('toggle');
    $('.js-btn-x').hide(500);
    $('.js-btn').show(500);
});