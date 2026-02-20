package com.utilitarian.judgeyourbias

import android.os.Bundle
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val gameWebView: WebView = findViewById(R.id.gameWebView)
        gameWebView.settings.javaScriptEnabled = true
        gameWebView.settings.domStorageEnabled = true
        gameWebView.settings.cacheMode = WebSettings.LOAD_DEFAULT
        gameWebView.webViewClient = WebViewClient()
        gameWebView.webChromeClient = WebChromeClient()
        gameWebView.loadUrl("file:///android_asset/judge_your_bias.html")
    }

    override fun onBackPressed() {
        val gameWebView: WebView = findViewById(R.id.gameWebView)
        if (gameWebView.canGoBack()) {
            gameWebView.goBack()
        } else {
            super.onBackPressed()
        }
    }
}
