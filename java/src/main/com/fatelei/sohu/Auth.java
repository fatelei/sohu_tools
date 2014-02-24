package com.fatelei.sohu;

import java.io.IOException;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerConfigurationException;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.*;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import com.fatelei.common.Macro;
import com.fatelei.utils.Crypto;

public class Auth implements SohuClient {

	private static final String GID = "02ffff11061111ef90d4ea6bf9f4c1c59fb44da709fd1a";
	private static final String SIG = "a622b02686a27feb456dc856e7d81fdd";
	private static final String APPID = "1106";
	private String email;
	private String password;
	
	public Auth(String email, String password) {
		this.email = email;
		this.password = password;
	}
	
	public String build_arguments() {
		DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
		try {
			DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
			Document doc = docBuilder.newDocument();
			Element root = doc.createElement("root");
			doc.appendChild(root);
			
			Element gid = doc.createElement("gid");
			gid.appendChild(doc.createTextNode(this.GID));
			root.appendChild(gid);
			
			Element userid = doc.createElement("userid");
			userid.appendChild(doc.createTextNode(this.email));
			root.appendChild(userid);
			
			Element appid = doc.createElement("appid");
			appid.appendChild(doc.createTextNode(this.APPID));
			root.appendChild(appid);
			
			Element pwd = doc.createElement("password");
			pwd.appendChild(doc.createTextNode(this.password));
			root.appendChild(pwd);
			
			Element sig = doc.createElement("sig");
			sig.appendChild(doc.createTextNode(this.SIG));
			root.appendChild(sig);
			
			TransformerFactory tf = TransformerFactory.newInstance();
			Transformer ts = tf.newTransformer();
			ts.setOutputProperty("encoding", "utf8");
			ts.setOutputProperty("standalone", "yes");
			StringWriter writer = new StringWriter();
			ts.transform(new DOMSource(doc), new StreamResult(writer));
			String output = writer.getBuffer().toString().replaceAll("\n|\r", "");
			return output;
			
		} catch (ParserConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		} catch (TransformerConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		} catch (TransformerException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
	}
	
	@Override
	public String get() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String post() {
		// TODO Auto-generated method stub
		this.password = Crypto.get_crypto_password(this.password);
		String xml = this.build_arguments();
		String loginUrl = Macro.login_url();
		HttpClient httpClient = new DefaultHttpClient();
		HttpPost postMethod = new HttpPost(loginUrl);
		postMethod.addHeader("User-Agent", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1");
		try {
			StringEntity requestEntity = new StringEntity(xml);
			postMethod.setEntity(requestEntity);
			try {
				HttpResponse resp = httpClient.execute(postMethod);
				String body = EntityUtils.toString(resp.getEntity());
				return body;
			} catch (ClientProtocolException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return null;
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return null;
			}
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
	}
	
}
