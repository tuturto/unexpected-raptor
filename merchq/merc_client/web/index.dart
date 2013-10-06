library merc_main;

import 'dart:html';
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
      
      myElement.startUp(config);
  });
}
