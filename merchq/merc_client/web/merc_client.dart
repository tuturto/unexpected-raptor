library merc_client;

import 'dart:html';
import 'dart:json';
import 'dart:async';
import 'package:dart_config/default_browser.dart';

DateTime currentDate = null;
DateTime shownDate = null;
Map config = null;

void main() {
  
  loadConfig('/static/config.yaml')
    .catchError((e) => loadConfig()).then((Map c) {
      config = c;
  });
}
