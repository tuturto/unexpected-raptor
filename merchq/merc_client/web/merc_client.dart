library merc_client;

import 'dart:html';
//import 'dart:json';
import 'dart:async';
import 'package:dart_config/default_browser.dart';
import 'elements/merc_client.dart';

Map config = null;

void main() {
  
  loadConfig('/static/config.yaml')
    .catchError((e) => loadConfig()).then((Map c) {
      config = c;
      Element elem = query('#client');
      MercClientElement myElement = elem.xtag;
      myElement.setConfig(config);
  });
}
