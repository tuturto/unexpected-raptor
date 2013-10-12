import 'package:polymer/polymer.dart';
import 'dart:html';
import 'dart:json';
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
  
    Uri url = new Uri(scheme: 'http',
                      host: config['host'],
                      port: config['port'],
                      path: 'cycle/');
    
    int days = int.parse(daysToAdvance);
    String jsonData = '{"days":$days}';
    
    var request = HttpRequest.request(url.toString(),
        method: 'POST',
        sendData: jsonData).then(onCycleCompleted);
  }
  
  void onCycleCompleted(HttpRequest request) {
    if (request.status == 200) {
      Map data = parse(request.responseText);
      print(data);      
    }
  }
}
