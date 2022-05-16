class Node {
    constructor(data) {
        this.data = data;
        this.nextNode = null;
    }
}

class LinkedList {
    constructor(firstNode) {
        this.firstNode = firstNode;
    }

    read(index) {
        let currentNode = this.firstNode;
        let currentIndex = 0;
        while (currentIndex < index) {
            currentNode = currentNode.nextNode;
            currentIndex++;
            if (currentNode === null) return;
        }
        return currentNode.data;
    }

    indexOf(value) {
        let currentNode = this.firstNode;
        let currentIndex = 0;
        while (currentNode) {
            if (currentNode.data == value) return currentIndex
            currentNode = currentNode.nextNode
            currentIndex++;
        }
    }
}

let node1 = new Node('marcos');
let node2 = new Node('joao');
let node3 = new Node('maria');
let node4 = new Node('carla');

node1.nextNode = node2;
node2.nextNode = node3;
node3.nextNode = node4;

let list = new LinkedList(node1);

console.log(list.indexOf('joao'))