library merc_client;

import 'package:polymer/polymer.dart';

@CustomTag('merc-client')
class MercClientElement extends PolymerElement {
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void startUp(Map config) {
    this.config = config;

    show_gm_application();
  }
  
  void show_gm_application() {
    shadowRoot.query('#app_menu1').setInnerHtml('Logs');
    shadowRoot.query('#app_menu2').setInnerHtml('Cycle');
    
    show_gm_logs();
  }
  
  void show_gm_logs() {
    var dateElement = createElement('current-date');
    shadowRoot.query('#navbar').children.add(dateElement);
    dateElement.xtag.startUp(config);
    
    var gmLogElement = createElement('gm-log');
    shadowRoot.query('#appcontent').children.add(gmLogElement);
    gmLogElement.xtag.startUp(config);    
  }
}
