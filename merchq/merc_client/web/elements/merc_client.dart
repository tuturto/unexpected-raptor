library merc_client;

import 'package:polymer/polymer.dart';
import 'current_date.dart';

@CustomTag('merc-client')
class MercClientElement extends PolymerElement {
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void startUp(Map config) {
    this.config = config;    
    CurrentDateElement dateElement = shadowRoot.query('#datefield').xtag;
    dateElement.startUp(config);
  }
}
