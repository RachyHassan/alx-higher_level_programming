$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
        var films = data.films;
        $('UL#list_movies').empty();
        $.each(films, function(number, url) {
            $.get(url, function(filmdata){
                var titles = filmdata.title;
                $('UL#list_movies').append('<li>'+ titles + '</li>');
            })
        })
    });
});
// $.each(films, function(index, filmUrl) {
//     $.get(filmUrl, function(filmData) {
//         var movieTitle = filmData.title;