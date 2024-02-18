
function bubSort(arr, n) {
  let temp;
  let swap;
  for (let i = 0; i < n - 1; i++) {
    swap = false;
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swap = true;
      }
    }
    if (swap == false) {
      break;
    }
  }
}

function printArr(arr) {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}

let myArr = [10, 14, 2, 11, 6];
let n = myArr.length;

bubSort(myArr, n);
printArr(myArr);
