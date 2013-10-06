library current_date;

import 'dart:html';
import 'dart:json';
import 'dart:async';
import 'package:polymer/polymer.dart';

@CustomTag('current-date')
class CurrentDateElement extends PolymerElement 
    with ObservableMixin{
  
  bool get applyAuthorStyles => true;

  Map config = null;
  @observable String displayedDate;
  
  void startUp(Map config) {
    this.config = config;
    showDay();
  }

  void showDay() {
    var path = new StringBuffer();
    path..write(config['servicePath'])
      ..write('current_date/');
  
  Uri url = new Uri(scheme: 'http',
                    host: config['host'],
                    port: config['port'],
                    path: path.toString());
    
  var request = HttpRequest.getString(url.toString()).then(onDataLoaded);
  }

  void onDataLoaded(String jsonString) {
    Map data = parse(jsonString);
    var entry = data['current_date'];
    
    displayedDate = entry;
  }
}
