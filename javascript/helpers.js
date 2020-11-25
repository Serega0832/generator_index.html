url_adviec = "https://api.adviceslip.com/advice"

$("#main-header").click(function (){

    $.getJSON(url_adviec, function (data) {
        advice = (data["slip"].advice);
        set_hello(advice)
    });
});
function  set_hello(msg) {
    p = $("#second-paragraphs")
    p.html(msg)
    p.css('color', 'red')
}