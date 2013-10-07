library gm_log;

import 'package:polymer/polymer.dart';
import 'dart:html';
import 'dart:json';
import 'dart:async';

@CustomTag('gm-log')
class GMLogElement extends PolymerElement 
    with ObservableMixin{
  
  bool get applyAuthorStyles => true;

  Map config;
  DateTime currentDate;
  DateTime shownDate;
  
  void startUp(Map config) {
    this.config = config;
    
    shadowRoot.query('#yesterday')
      ..onClick.listen((e) => moveToPreviousDay());
    shadowRoot.query('#today')
      ..onClick.listen((e) => moveToToday());
    shadowRoot.query('#tomorrow')
      ..onClick.listen((e) => moveToNextDay());
    
    getCurrentDate();
    showLog(null);
  }

  void moveToPreviousDay() {
    shownDate = shownDate.subtract(const Duration(days: 1));
    showLog(shownDate);
  }
  
  void moveToToday() {
    shownDate = currentDate;
    showLog(shownDate);
  }
  
  void moveToNextDay() {
    shownDate = shownDate.add(const Duration(days: 1));
    showLog(shownDate);
  }
  
  void showLog(DateTime dayToShow) {
    var path = new StringBuffer();
    
    if (dayToShow != null) {       
      path..write(config['servicePath'])
        ..write('logs/?date=')
        ..write(dayToShow.year.toString())
        ..write('-')
        ..write(dayToShow.month.toString())
        ..write('-')
        ..write(dayToShow.day.toString());
    }
    else {      
      path..write(config['servicePath'])
        ..write('logs/?date=current');      
    }
  
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
  
  void getCurrentDate() {
    var path = new StringBuffer();
    path..write(config['servicePath'])
      ..write('current_date/');
  
    Uri url = new Uri(scheme: 'http',
                      host: config['host'],
                      port: config['port'],
                      path: path.toString());
    
    var request = HttpRequest.getString(url.toString()).then(onDateRequestLoaded);
  }

  void onDateRequestLoaded(String jsonString) {
    Map data = parse(jsonString);
    var entry = data['current_date'];
    
    currentDate = DateTime.parse(entry);
    shownDate = currentDate;
  }
}

