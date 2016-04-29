package cs206b;
import cs206b.Node;

public class SinglyLinkedList{
	private Node first;
	private Node last;

	public SinglyLinkedList(){// constructor
		first = null;
		last = null;
	}

	public boolean isEmpty() {
		if (first == null && last == null) {
			return true;
		}
		return false;
	}

	public void append(int element){
		if (first == null) {
			first = new Node(element,null);
			last = first;
		}
		else {
			Node temp = new Node(element,null);
			last.next = temp;
			last = temp;
		}
	}

	public void remove(int element){
		Node cur = first;
		if (cur == null) {
		}
		else if (cur.elem == element && cur.next == null) {
			first = null;
			last = null;
		}
		else if (cur.elem != element && cur.next == null) {
			
		}
		else if (cur.elem == element) {
			first = cur.next;
		}
		else {
			while (cur.next.elem != element) {
				cur = cur.next;
				if (cur.next == null)
				break;
			}
			if (cur.next != null) {
				cur.next = cur.next.next;
			}
	}
	}

	public void printAll(){
		String rt = "";
		Node cur = first;
		if (first != null) {
		while (cur.next != null) {
			rt += cur.elem;
			rt += ", ";
			cur = cur.next;
		}
		rt += cur.elem;
		}
		System.out.println(rt);
	}

	public Node getFirst(){
		return first;
	}
    
	public void printNode(Node e){
		System.out.println(e);
	}
}