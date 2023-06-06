function disableButtons(ProductID) {
    var specificProductQuantity = parseInt($(`.quantity_of_${ProductID}`).val());
    var disablePlusButton = specificProductQuantity > 48;
    var disableMinusButton = specificProductQuantity < 2;

    $(`#minus_button_of_${ProductID}`).prop('disabled', disableMinusButton);
    $(`#plus_button_of_${ProductID}`).prop('disabled', disablePlusButton);
    
}