package com.fatelei.utils;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Crypto {
	public static String get_crypto_password(String password) {
		MessageDigest messageDigest;
		try {
			messageDigest = MessageDigest.getInstance("MD5");
			messageDigest.update(password.getBytes());
			byte[] b = messageDigest.digest();
			StringBuffer sb=new StringBuffer();
			for (int i = 0;i < b.length; i++) {
				int v = b[i] & 0xff;
				if (v < 16) {
					sb.append(0);
				} else {
					sb.append(Integer.toHexString(v));
				}
			}
			return sb.toString();
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
	}
}
