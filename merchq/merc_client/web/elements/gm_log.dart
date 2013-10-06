library gm_log;

import 'package:polymer/polymer.dart';

@CustomTag('gm-log')
class GMLogElement extends PolymerElement 
    with ObservableMixin{
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void startUp(Map config) {
    this.config = config;
  }
}
