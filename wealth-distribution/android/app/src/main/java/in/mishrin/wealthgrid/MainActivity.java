package in.mishrin.wealthgrid;
import android.app.Activity;import android.os.Bundle;import android.webkit.WebView;import android.webkit.WebSettings;
public class MainActivity extends Activity{public void onCreate(Bundle b){super.onCreate(b);WebView w=new WebView(this);w.setBackgroundColor(0xfff5f7f2);WebSettings s=w.getSettings();s.setJavaScriptEnabled(true);s.setDomStorageEnabled(true);w.loadUrl("https://raw.githubusercontent.com/amanjuniorxd-wq/Utilitarian-Game-Theory/main/wealth-distribution/index.html");setContentView(w);}}
