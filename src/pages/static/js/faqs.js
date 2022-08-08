for (let i=0; i<6; i++){
    $(".faq-drop-"+ i).click(function(){

        $('.faq-drop-'+ i).next().toggle(500);
    
    });
}

