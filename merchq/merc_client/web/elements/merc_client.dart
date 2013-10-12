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
    
    show_gm_application();
  }
  
  void show_gm_application() {
    shadowRoot.query('#app_menu1')
      ..setInnerHtml('<a href="#gm_logs">Logs</a>')
      ..onClick.listen((e) => show_gm_logs());
    
    shadowRoot.query('#app_menu2')
      ..setInnerHtml('<a href="#gm_cycle">Cycle</a>')
      ..onClick.listen((e) => show_gm_cycle());
  }
  
  void show_gm_cycle() {
    var gmLogElement = createElement('gm-cycle');
    shadowRoot.query('#appcontent')
      ..children.clear()
      ..children.add(gmLogElement);   
  }
  
  void show_gm_logs() {   
    var gmLogElement = createElement('gm-log');
    shadowRoot.query('#appcontent')
      ..children.clear()
      ..children.add(gmLogElement);
    gmLogElement.xtag.startUp(config);    
  }
}
