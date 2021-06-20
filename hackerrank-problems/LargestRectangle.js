function findLargestRectangularArea(hist) {
    let h, pos;
    let tempH, tempPos;
    let hStack = [];
    let pStack = [];
    let maxSize = -Infinity;
    let tempSize = 0;

    function popThatShit() {
        tempH = hStack.pop();
        tempPos = pStack.pop();
        tempSize = tempH * (pos - tempPos);
        maxSize = Math.max(tempSize, maxSize);
    }

    for (pos = 0; pos < hist.length; pos++) {
        h = hist[pos];
        if (hStack.length === 0 || h > hStack[hStack.length - 1]) {
            hStack.push(h);
            pStack.push(pos);
        } else if (h < hStack[hStack.length - 1]) {
            while (hStack.length && h < hStack[hStack.length - 1]) {
                popThatShit();
            }
            hStack.push(h);
            pStack.push(tempPos);
        }
    }
    while (hStack.length) {
        popThatShit();
    }
    return maxSize;
}

function test(hist, result) {
    var area = findLargestRectangularArea(hist);
    console.log(
        'Testing ' + hist.join(',') +
        ' - Answer should be: ' + result +
        ', Discovered Answer: ' + area
    );
    if (area !== result) {
        console.log('!!! shit is fucked !!!');
    }
    console.log("\n");
}


test([20, 25, 15, 10, 20], 50)
test([1, 2, 3, 4, 2, 3, 5, 2, 1, 0, 8], 14);
test([5, 5, 1, 0, 1, 0, 1], 10);
test([6, 5, 4, 0, 1, 0, 1], 12);
test([0, 1, 0, 1, 0, 5, 6], 10);
test([5, 1, 1, 1, 1, 1, 0], 6);
test([5, 0, 3, 3, 3], 9);
test([0, 1, 0], 1);
test([1, 2, 3, 4, 5], 9);
test([5, 4, 3, 2, 1], 9);
test([0, 1, 0, 1, 3, 2, 0, 1, 0, 1], 4);
test([], -Infinity);
test([1], 1);

