library gm_log;

import 'package:polymer/polymer.dart';
import 'dart:html';
import 'dart:json';
import 'dart:async';

@CustomTag('gm-log')
class GMLogElement extends PolymerElement 
    with ObservableMixin{
  
  bool get applyAuthorStyles => true;

  Map config = null;
  
  void startUp(Map config) {
    this.config = config;    
    showLog();
  }
    
  void showLog() {
    var path = new StringBuffer();
    path..write(config['servicePath'])
      ..write('logs/?date=current');
  
    Uri url = new Uri(scheme: 'http',
                      host: config['host'],
                      port: config['port'],
                      path: path.toString());
    
    var request = HttpRequest.getString(url.toString()).then(onDataLoaded);
  }

  void onDataLoaded(String jsonString) {
    List data = parse(jsonString);
    var entry = data[0]['text'];

    var entries = shadowRoot.query('#logEntries').xtag;
    
    entries.clear();    
    data.forEach((elem) => entries.addEntry(elem['entry_date'], 
                                            elem['text']));

  }
}

