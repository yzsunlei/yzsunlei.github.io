/**
 * Created by lei.sun on 2017/8/13.
 */
// 测试平台类
function CArray(numElements) {
   this.dataStore = [];
   this.pos = 0;
   this.numElements = numElements;
   this.insert = insert;
   this.toString = toString;
   this.clear = clear;
   this.setData = setData;
   this.swap = swap;

   for (var i = 0; i < numElements; ++i) {
      this.dataStore[i] = i;
   }
}

function setData() {
   for (var i = 0; i < this.numElements; ++i) {
      this.dataStore[i] = Math.floor(Math.random() *
                          (this.numElements+1));
   }
}

function clear() {
   for (var i = 0; i < this.dataStore.length; ++i) {
      this.dataStore[i] = 0;
   }
}

function insert(element) {
   this.dataStore[this.pos++] = element;
}

function toString() {
   var retstr = "";
   for (var i = 0; i < this.dataStore.length; ++i) {
      retstr += this.dataStore[i] + " ";
      if (i > 0 && i % 10 == 0) {
         retstr += "\n";
      }
   }
   return retstr;
}

function swap(arr, index1, index2) {
   var temp = arr[index1];
   arr[index1] = arr[index2];
   arr[index2] = temp;
}

// test
// var numElements = 100;
// var myNums = new CArray(numElements);
// myNums.setData();
// console.log(myNums.toString());


// 冒泡排序
function bubbleSort() {
   var numElements = this.dataStore.length;
   var temp;
   for (var outer = numElements; outer >= 2; --outer) {
      for (var inner = 0; inner <= outer-1; ++inner) {
         if (this.dataStore[inner] > this.dataStore[inner+1]) {
            swap(this.dataStore, inner, inner+1);
         }
      }
   }
}

// test
// var numElements = 10;
// var mynums = new CArray(numElements);
// mynums.setData();
// console.log(mynums.toString());
// mynums.bubbleSort();
// console.log();
// console.log(mynums.toString());


// 选择排序
function selectionSort() {
   var min, temp;
   for (var outer = 0; outer <= this.dataStore.length-2; ++outer) {
      min = outer;
      for (var inner = outer + 1;
           inner <= this.dataStore.length-1; ++inner) {
         if (this.dataStore[inner] < this.dataStore[min]) {
            min = inner;
         }
      }
      swap(this.dataStore, outer, min);
   }
}

// test


// 插入排序
function insertionSort() {
   var temp, inner;
   for (var outer = 1; outer <= this.dataStore.length-1; ++outer) {
      temp = this.dataStore[outer];
      inner = outer;
      while (inner > 0 && (this.dataStore[inner-1] >= temp)) {
         this.dataStore[inner] = this.dataStore[inner-1];
         --inner;
      }
      this.dataStore[inner] = temp;
   }
}

// test 冒泡排序、选择排序、插入排序的排序计时比较
// var numElements = 100;
// var nums = new CArray(numElements);
// nums.setData();
// var start = new Date().getTime();
// nums.bubbleSort();
// var stop = new Date().getTime();
// var elapsed = stop - start;
// console.log("Elapsed time for the bubble sort on " + 
//       numElements + " elements is: " + elapsed + " milliseconds.");
// start = new Date().getTime();
// nums.selectionSort();
// stop = new Date().getTime();
// elapsed = stop - start;
// console.log("Elapsed time for the selection sort on " + 
//       numElements + " elements is: " +  elapsed + " milliseconds.");
// start = new Date().getTime();
// nums.insertionSort();
// stop = new Date().getTime();
// elapsed = stop - start;
// console.log("Elapsed time for the insertion sort on " + 
//        numElements + " elements is: " + elapsed + " milliseconds.");


// 希尔排序-硬编码间隔序列
function shellsort() {
   for (var g = 0; g < this.gaps.length; ++g) {
      for (var i = this.gaps[g]; i < this.dataStore.length; ++i) {
         var temp = this.dataStore[i];
         for (var j = i; j >= this.gaps[g] &&
                         this.dataStore[j-this.gaps[g]] > temp;
              j -= this.gaps[g]) {
            this.dataStore[j] = this.dataStore[j - this.gaps[g]];
         }
         this.dataStore[j] = temp;
      }
   }
}

// test
// testload("CArray.js")
// var nums = new CArray(10);
// nums.setData();
// console.log("Before Shellsort: \n");
// console.log(nums.toString());
// console.log("\nDuring Shellsort: \n");
// nums.shellsort();
// console.log("\nAfter Shellsort: \n");
// console.log(nums.toString());


// 希尔排序 - 动态间隔序列
function shellsort1() {
   var N = this.dataStore.length;
   var h = 1;
   while (h < N/3) {
      h = 3 * h + 1;
   }
   while (h >= 1) {
      for (var i = h; i < N; i++) {
         for (var j = i; j >= h && this.dataStore[j] < this.dataStore[j-h];
              j -= h) {
            swap(this.dataStore, j, j-h);
         }
      }
      h = (h-1)/3;
   }
}

// test
// load("CArray.js")
// var nums = new CArray(100);
// nums.setData();
// console.log("Before Shellsort1: \n");
// console.log(nums.toString());
// nums.shellsort1();
// console.log("\nAfter Shellsort1: \n");
// console.log(nums.toString());

// test 两种希尔排序算法的比较
// load("CArray.js");
// var nums = new CArray(10000);
// nums.setData();
// var start = new Date().getTime();
// nums.shellsort();
// var stop = new Date().getTime();
// var elapsed = stop - start;
// console.log("Shellsort with hard-coded gap sequence: " + elapsed + " ms.");
// nums.clear();
// nums.setData();
// start = new Date().getTime();
// nums.shellsort1();
// stop = new Date().getTime();
// console.log("Shellsort with dynamic gap sequence: " + elapsed + " ms.");


// 归并排序
function mergeSort(arr) {
   if (arr.length < 2) {
      return;
   }
   var step = 1;
   var left, right;
   while (step < arr.length) {
      left = 0;
      right = step;
      while (right + step <= arr.length) {
         mergeArrays(arr, left, left+step, right, right+step);
         left = right + step;
         right = left + step;
      }
      if (right < arr.length) {
         mergeArrays(arr, left, left+step, right, arr.length);
      }
      step *= 2;
   }
}

function mergeArrays(arr, startLeft, stopLeft, startRight, stopRight) {
   var rightArr = new Array(stopRight - startRight + 1);
   var leftArr = new Array(stopLeft - startLeft + 1);
   k = startRight;
   for (var i = 0; i < (rightArr.length-1); ++i) {
      rightArr[i] = arr[k];
      ++k;
   }

   k = startLeft;
   for (var i = 0; i < (leftArr.length-1); ++i) {
      leftArr[i] = arr[k];
      ++k;
   }

   rightArr[rightArr.length-1] = Infinity; // a sentinel value
   leftArr[leftArr.length-1] = Infinity; // a sentinel value
   var m = 0;
   var n = 0;
   for (var k = startLeft; k < stopRight; ++k) {
      if (leftArr[m] <= rightArr[n]) {
         arr[k] = leftArr[m];
         m++;
      }
      else {
         arr[k] = rightArr[n];
         n++;
      }
   }
   console.log("left array - ", leftArr);
   console.log("right array - ", rightArr);
}

// test
// var nums = [6,10,1,9,4,8,2,7,3,5];
// console.log(nums);
// console.log();
// mergeSort(nums);
// console.log();
// console.log(nums);


// 快速排序
function qSort(arr)
{
    if (arr.length == 0) {
        return [];
    }
    var left = [];
    var right = [];
    var pivot = arr[0];
    for (var i = 1; i < arr.length; i++) {

        if (arr[i] < pivot) {

           left.push(arr[i]);
        } else {

           right.push(arr[i]);
        }
    }
    return qSort(left).concat(pivot, qSort(right));
}

// test
// var a = [];
// for (var i = 0; i < 10; ++i) {
//    a[i] = Math.floor((Math.random()*100)+1);
// }
// console.log(a);
// console.log();
// console.log(qSort(a));
