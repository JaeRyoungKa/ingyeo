package cs206b;
import cs206b.Node;
import cs206b.SinglyLinkedList;
import java.io.*;
import java.util.*;
public class Main {

	public static void main(String args[]) {
		SinglyLinkedList list = new SinglyLinkedList();
		SinglyLinkedList sorted_list, reversed_list;
/*
		int[] inputs = {454,12,295,99,1,48,7};

		for(int i=0; i<inputs.length; i++){
				list.append(inputs[i]);
		}
		*/
		Scanner scanner = new Scanner(System.in);
		String line = scanner.nextLine();
		String[] inputs = line.split("\\{")[1].split("}")[0].split(",");

		for(int i = 0; i<inputs.length; i++) {
			list.append(Integer.parseInt(inputs[i]));
		}
		
		sorted_list = sort(list);
		sorted_list.printAll();
		reversed_list = reverse(list);
		reversed_list.printAll();
		System.out.println(recursiveSum(list));
	}

	public static SinglyLinkedList sort(SinglyLinkedList list){
		// copy
		SinglyLinkedList listR = new SinglyLinkedList();
		Node temp2 = list.getFirst();
		while(temp2 != null) {
			listR.append(temp2.elem);
			temp2 = temp2.next;
		}
		// end of copy
		SinglyLinkedList result = new SinglyLinkedList();
		
		while(listR.getFirst() != null) {
		Node temp = listR.getFirst();
		int min = 2147483647;
			while(temp != null) {
				if(min > temp.elem) {
					min = temp.elem;
				}
				temp = temp.next;
			}
		if (min != 2147483647) {
		result.append(min);
		listR.remove(min);
		}
		}
		return result;
	}
	public static SinglyLinkedList reverse(SinglyLinkedList list){
		
		SinglyLinkedList listR = new SinglyLinkedList();
		int[] lemme_sleep = new int[30];
		int counter = 0;
		Node temp2 = list.getFirst();
		while(temp2 != null) {
			lemme_sleep[counter] = temp2.elem;
			temp2 = temp2.next;
			counter++;
		}
		for (int i=counter-1; i>=0; i--) {
			int temp = (int) lemme_sleep[i];
			listR.append(temp);
		}
		return listR;
	}
	public static int recursiveSum(SinglyLinkedList list){
				// copy
		SinglyLinkedList listR = new SinglyLinkedList();
		Node temp2 = list.getFirst();
		while(temp2 != null) {
			listR.append(temp2.elem);
			temp2 = temp2.next;
		}
		// end of copy
		int sum = 0;
		while(listR.getFirst() != null) {
			sum += listR.getFirst().elem;
			listR.remove(listR.getFirst().elem);
		}
		return sum;
	}
}
