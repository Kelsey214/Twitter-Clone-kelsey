//////////////////////////////
////Java script for Posts page
///////////////////////////////

$(function(){
 // execute when js-menu-icon is clicked
    $('.js-menu-icon').click(function(){
        // $(this) : Self element, namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.menu
        // toggle() : switch show and hide
        $(this).next().toggle();
    })
})