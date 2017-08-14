/**
 * Created by lei.sun on 2017/8/13.
 */
// 队列
function Queue() {
  this.dataStore = [];
  this.enqueue = enqueue; // 入队
  this.dequeue = dequeue; // 出队
  this.front = front;
  this.back = back;
  this.toString = toString;
  this.empty = empty;
}

function enqueue(element) {
  this.dataStore.push(element);
}

function dequeue() {
  return this.dataStore.shift();
}

function front() {
  return this.dataStore[0];
}

function back() {
  return this.dataStore[this.dataStore.length - 1];
}

function toString() {
  var retStr = "";
  for (var i = 0; i < this.dataStore.length; ++i) {
    retStr += this.dataStore[i] + "\n";
  }
  return retStr;
}

function empty() {
  if (this.dataStore.length == 0) {
    return true;
  } else {
    return false;
  }
}

// test
var q = new Queue();
q.enqueue("Cynthia");
q.enqueue("Raymond");
q.enqueue("Barbara");
console.log(q.toString());
q.dequeue();
console.log(q.toString());
console.log("Front of queue：" + q.front());
console.log("Back of queue：" + q.back());

// 更多实例
// 使用队列：方块舞的舞伴分配问题
// 使用队列对数据进行排序
// 优先队列