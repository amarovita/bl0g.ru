
function insertAtCursor(myField, myValue) {
    //IE support
    if (document.selection) {
        myField.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
    }
    //MOZILLA and others
    else if (myField.selectionStart || myField.selectionStart == '0') {
        var startPos = myField.selectionStart;
        var endPos = myField.selectionEnd;
        myField.value = myField.value.substring(0, startPos)
            + myValue
            + myField.value.substring(endPos, myField.value.length);
    } else {
        myField.value += myValue;
    }
}



$(document).ready(function(){

    document.getElementById('id_text').onpaste = function (event) {
        // use event.originalEvent.clipboard for newer chrome versions
        var items = (event.clipboardData  || event.originalEvent.clipboardData).items;
        console.log(JSON.stringify(items)); // will give you the mime types
        // find pasted image among pasted items
        var blob = null;
        for (var i = 0; i < items.length; i++) {
        if (items[i].type.indexOf("image") === 0) {
            blob = items[i].getAsFile();
        }
        }
        // load image if there is a pasted image
        if (blob !== null) {
        var reader = new FileReader();
        reader.onload = function(event) {
            console.log(event.target.result); // data url!
            insertAtCursor(document.getElementById('id_text'), '![Figure]('+event.target.result+')');
            //document.getElementById("pastedImage").src = event.target.result;
        };
        reader.readAsDataURL(blob);
        }
    }

});