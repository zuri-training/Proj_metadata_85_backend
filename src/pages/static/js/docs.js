$("#docs-intro").click(function(){
    $(".main-docs").show();
    $(".getting_started").hide();
    $(".libraries").hide();
});

$("#docs-started").click(function(){
    $(".main-docs").hide();
    $(".getting_started").show();
    $(".libraries").hide();
});


$("#docs-libraries").click(function(){
    $(".main-docs").hide();
    $(".getting_started").hide();
    $(".libraries").show();
});
