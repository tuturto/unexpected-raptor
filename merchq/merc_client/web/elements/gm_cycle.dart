import 'package:polymer/polymer.dart';
import 'dart:html';
import 'dart:convert';
import 'dart:async';

@CustomTag('gm-cycle')
class MyExample extends PolymerElement 
    with ObservableMixin {
  
  @observable String daysToAdvance;
  
  Map config;
  
  bool get applyAuthorStyles => true;
  
  void startUp(Map config) {
    this.config = config;
    
    shadowRoot.query('#proceed')
      ..onClick.listen((e) => cycle());
  }
  
  void cycle() {

    var path = new StringBuffer();
    path
      ..write(config['servicePath'])
      ..write('cycle/');
    
    Uri url = new Uri(scheme: 'http',
                      host: config['host'],
                      port: config['port'],
                      path: path.toString());
    
    int days = int.parse(daysToAdvance);

    var request = new HttpRequest();
    request.open('POST', url.toString());
    request.onLoadEnd.listen((e) => onCycleCompleted);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.encode({'days': days}));
  }
  
  void onCycleCompleted(HttpRequest request) {
    
  }
}
