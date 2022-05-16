<?php

    class Node {
        public function __construct(public $data, public $nextNode = null) 
        {}
    }

    class LinkedList {
        public function __construct(private $firstNode)
        {}

        public function read($index) 
        {
            $currentNode = $this->firstNode;
            $currentIndex = 0;
            while ($currentIndex < $index) {
                $currentNode = $currentNode->nextNode;
                $currentIndex++;
                if ($currentNode === null) return;
            }
            return $currentNode->data;
        }

        public function indexOf($value)
        {
            $currentNode = $this->firstNode;
            $currentIndex = 0;
            while ($currentNode) {
                if ($currentNode->data == $value) return $currentIndex;
                $currentNode = $currentNode->nextNode;
                $currentIndex++;
            }
            return null;
        }

        public function insertAtIndex($index, $value) {
            $newNode = new Node($value);
            if ($index === 0) {
                $newNode->nextNode = $this->firstNode;
                $this->firstNode = $newNode;
                return;
            }
            
            $currentNode = $this->firstNode;
            $currentIndex = 0;
            while ($currentIndex < ($index - 1)) {
                $currentNode = $currentNode->nextNode;
                $currentIndex++;
            }
            $newNode->nextNode = $currentNode->nextNode;
            $currentNode->nextNode = $newNode;
        }
    }

    $node_1 = new Node('v1');
    $node_2 = new Node('v2');
    $node_3 = new Node('v3');
    $node_4 = new node('v4');

    $node_1->nextNode = $node_2;
    $node_2->nextNode = $node_3;
    $node_3->nextNode = $node_4;

    $list = new LinkedList($node_1);

    // echo $list->read(1);
    echo $list->indexOf('v2');