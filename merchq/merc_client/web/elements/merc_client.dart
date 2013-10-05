library merc_client;

import 'package:polymer/polymer.dart';

@CustomTag('merc-client')
class MercClientElement extends PolymerElement {
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void setConfig(Map config) {
     this.config = config;
  }
}
