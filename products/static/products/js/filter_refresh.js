// Fix refresh
$('#filter-products').click(function() {
    var formSelector = $(this);
    var openUrl = new URL(window.location);

    var selectedCategory = formSelector.val();
    if(selectedCategory != "sort_by"){
        var allElements = selectedCategory.split("_")
        var sortValue = allElements[0];
        var searchDirection = allElements.slice(-1);
        if (sortValue == 'bag') {
            sortValue = 'bag_100g_USD';
        }

        openUrl.searchParams.set("sort", sortValue);
        openUrl.searchParams.set("direction", searchDirection);
        window.location.replace(openUrl);
    } else {
        openUrl.searchParams.delete("sort");
        openUrl.searchParams.delete("direction");

        window.location.replace(openUrl);
    }
})