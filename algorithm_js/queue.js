class Node {
	constructor(item) {
		this.item = item;
		this.next = null;
		this.prev = null;
	}
}

class Deque {
	constructor() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}

	push(item) {
		const node = new Node(item);
		if (this.head === null) {
			this.head = node;
			this.head.next = this.tail;
		} else this.tail.next = node;

		node.prev = this.tail;
		this.tail = node;
		this.size += 1;
	}

	push_front(item){
		const node = new Node(item);
		if(this.head === null){
			this.head = node;
			this.head.next = this.tail;
		}
		else{
			node.next = this.head;
		}
		this.head.prev = node;
		this.head = node;
		this.size += 1;
	}

	length() {
		return this.size;
	}

	popLeft() {
		if(this.size === 0) return false
		const popedItem = this.head;
		this.head = this.head.next;
		this.size -= 1;
		if(this.size === 0){
			this.head = null;
			this.tail = null;
		}
		return popedItem.item;
	}

	pop() {
		if (this.size === 0) return false
		const popedItem = this.tail;
		this.tail = this.tail.prev;
		this.size -= 1;
		if (this.size === 0) {
			this.head = null;
			this.tail = null;
		}
		return popedItem.item;
	}

	front() {
		let current = this.head;
		if (current !== null) {
			return current.item;
		}
		else{
			return false;
		}
	}

	back(){
		let current = this.tail;
		if (current !== null) {
			return current.item;
		}
		else{
			return false;
		}
	}
}