library merc_client;

import 'package:polymer/polymer.dart';

@CustomTag('merc-client')
class MercClientElement extends PolymerElement {
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void startUp(Map config) {
    this.config = config;

    var dateElement = createElement('current-date');
    shadowRoot.query('#navbar').children.add(dateElement);
    dateElement.xtag.startUp(config);
  }
}
