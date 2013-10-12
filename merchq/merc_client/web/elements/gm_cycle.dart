import 'package:polymer/polymer.dart';

@CustomTag('gm-cycle')
class MyExample extends PolymerElement {
  @observable num daysToAdvance;
  
  Map config;
  
  bool get applyAuthorStyles => true;
  
  void startUp(Map config) {
    this.config = config;
    
    shadowRoot.query('#proceed')
      ..onClick.listen((e) => cycle());
  }
  
  void cycle() {
    
  }
  
}
