window.raptor = (function () {

    var raptor = {
    
        generateBoxes: function (maxval, currval, node) {
            if (maxval > 10) {
                currval = currval / maxval * 10;
                maxval = 10;
            }
            for (var i = 0; i < maxval; i++) {
                if (i < currval) {
                    if (currval <= Math.floor(maxval / 3)) {
                        node.append($("<span class='hp_colourbox red'></span>"));
                    }
                    else {
                        if (currval <= Math.floor(maxval / 3 * 2)) {
                            node.append($("<span class='hp_colourbox yellow'></span>"));
                        }
                        else {
                            node.append($("<span class='hp_colourbox green'></span>"));
                        }
                    }
                }
                else {
                    node.append($("<span class='hp_colourbox'></span>"));
                }
            }
        }
    };

    return raptor;  
}());

