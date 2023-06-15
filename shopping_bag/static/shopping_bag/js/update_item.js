$('.update-item').click(function(event) {
    var form = $(this).prev('.update-form');
    form.submit();
})