$(document).ready(function() {
    $.ajax({
        method: "post",
        url: "/search",
        data: { query: $("#search-box").val() },
        success: function(data) {
            $("#courses").html(data)
        }
    })


    $("#search-box").on("input", function(e) {
        $.ajax({
            method: "post",
            url: "/search",
            data: { query: $("#search-box").val() },
            success: function(data) {
                $("#courses").html(data)
            }
        })
    })
})