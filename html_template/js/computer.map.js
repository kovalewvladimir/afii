var containerMap = document.getElementById('divCanvasComputerMap');

var backgroundImg = new Image();
backgroundImg.src = "img/maps/n16_1_floor.jpg";
var backgroundLayer = new Konva.Layer();

var computerImg = new Image();
computerImg.src = "img/maps/computer.png";
var computerLayer = new Konva.Layer();

var stage, backgroundKonvaImg, computerKonvaImg;

function scaleStage() {
    var w = backgroundImg.width;
    var h = backgroundImg.height;
    var scale = containerMap.clientWidth / w;

    stage.width(w * scale);
    stage.height(h * scale);
    stage.scale({x: scale, y: scale});
    stage.draw();
}

window.onload = function(e) {
    var w = backgroundImg.width;
    var h = backgroundImg.height;

    stage = new Konva.Stage({
        container: 'divCanvasComputerMap',
        width: w,
        height: h
    });

    backgroundKonvaImg = new Konva.Image({
        x: 0,
        y: 0,
        image: backgroundImg,
        width: w,
        height: h
    });

    computerKonvaImg = new Konva.Image({
        x: 10,
        y: 10,
        image: computerImg,
        draggable: true
    });

    computerKonvaImg.on('dragmove', function() {
        console.log(`dragmove  x: ${this.x()}, y: ${this.y()}`);
    });
    
    computerKonvaImg.on('dragstart', function() {
        console.log(`dragstart x: ${this.x()}, y: ${this.y()}`);
    });
    
    computerKonvaImg.on('dragend', function() {
        console.log(`dragend   x: ${this.x()}, y: ${this.y()}`);
    });

    backgroundLayer.add(backgroundKonvaImg);
    computerLayer.add(computerKonvaImg);
    stage.add(backgroundLayer);
    stage.add(computerLayer);

    scaleStage()
}

window.onresize = function(e) {
    scaleStage()
}
