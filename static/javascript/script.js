let active_courses = [];


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

                $('.title').each(function(i, t) {
                    if (active_courses.indexOf(t.innerHTML.split(":")[0]) > -1) {
                        if (!t.className.includes(" active")) {
                            t.className += " active";
                        }
                    }
                });
            }
        })

    })

    $("#plan-button").on("click", function(e) {
        courses_selected = active_courses.join(",")

        $.ajax({
            method: "post",
            url: "/show",
            data: { query: courses_selected },
            success: function(data) {
                $("#selected").html(data)

                $('.title').each(function(i, t) {
                    if (active_courses.indexOf(t.innerHTML.split(":")[0]) > -1) {
                        if (!t.className.includes(" active")) {
                            t.className += " active";
                        }
                    } else {
                        if (t.className.includes(" active")) {
                            t.className = t.className.replace(" active", "");
                        }
                    }
                });
            }
        })
    })


    document.getElementById("defaultOpen").click();

})


function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

    $('.title').each(function(i, t) {
        if (active_courses.indexOf(t.innerHTML.split(":")[0]) > -1) {
            if (!t.className.includes(" active")) {
                t.className += " active";
            }
        } else {
            if (t.className.includes(" active")) {
                t.className = t.className.replace(" active", "");
            }
        }
    });

}


function addCourse(evt, course) {

    if (evt.currentTarget.className.includes(" active")) {
        let idx = active_courses.indexOf(course)
        if (idx > -1) {
            active_courses.splice(idx, 1);
        }

        evt.currentTarget.className = evt.currentTarget.className.replace(" active", "");
        $("#counter").html(parseInt($("#counter").html()) - 1)

    } else {
        active_courses.push(course);
        evt.currentTarget.className += " active";
        $("#counter").html(parseInt($("#counter").html()) + 1)
    }

}