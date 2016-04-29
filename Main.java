package cs206b;

import cs206b.Node;
import cs206b.SinglyLinkedList;
import java.io.*;
import java.util.Scanner;


public class Main {
	public static void main(String args[]) {
		SinglyLinkedList linkedlist = new SinglyLinkedList();
		Scanner scanner = new Scanner(System.in);
		String line = scanner.nextLine(); // how to duplicate line?
		String check = line.split("null")[0];
		if (!check.equals("int[] inputs = ")) {
		String[] inputs = line.split("\\{")[1].split("}")[0].split(", ");
		for(int i = 0; i<inputs.length; i++) {
			linkedlist.append(Integer.parseInt(inputs[i]));
		}
		}
		linkedlist.remove(44);
		linkedlist.remove(24);
		linkedlist.remove(74);
		linkedlist.printAll();
	}
}