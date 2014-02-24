package com.fatelei.tests;

import com.fatelei.sohu.Auth;

public class TestSohuAuth {
	public static void main(String[] args) {
		Auth sohuAuth = new Auth("fate_lei@sohu.com", "fate123");
		String resp = sohuAuth.post();
		System.out.println(resp);
	}
}
