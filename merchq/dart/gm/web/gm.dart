import 'dart:html';
import 'dart:json';
import 'dart:async';
import 'package:dart_config/default_browser.dart';

DateTime currentDate = null;
DateTime shownDate = null;
Map config = null;

void main() {
  
  loadConfig('/static/config.yaml')
    .catchError((e) => loadConfig()).then((Map c) {
      config = c;
      showDay();
  });

  String dateString = query('#current_date').innerHtml;   
  currentDate = DateTime.parse(dateString);
  shownDate = currentDate;  
  registerListeners();
}

void registerListeners() {
  query('#yesterday').onClick.listen((e) {
    shownDate = shownDate.add(const Duration(days: -1));
    showDay();      
    e.preventDefault();
  });   
    
  query('#today').onClick.listen((e) {
    shownDate = currentDate;
    showDay();
    e.preventDefault();
  });
    
  query('#tomorrow').onClick.listen((e) {
    shownDate = shownDate.add(const Duration(days: 1));
    showDay();
    e.preventDefault();
  });
}

void showDay() {
  var path = new StringBuffer();
  path..write('/gm/log_entries/')
      ..write('${shownDate.year}/')
      ..write('${shownDate.month}/')
      ..write('${shownDate.day}/');
  
  Uri url = new Uri(scheme: 'http',
                    host: config['host'],
                    port: config['port'],
                    path: path.toString());
    
  var request = HttpRequest.getString(url.toString()).then(onDataLoaded);
  
}

void onDataLoaded(String jsonString) {
  Map data = parse(jsonString);
  var entries = data['entries'];
  
  TableElement table = query('#log_table');
  
  
  while(table.rows.length > 1) {
    table.rows[1].remove();
  }
    
  entries.forEach((entry) => addLogEntry(table, 
      entry['entry_date'], 
      entry['text']));
}

void addLogEntry(TableElement table, String date, String entry) {
  TableRowElement row = table.insertRow(-1);
  
  row.insertCell(0)
    ..text = date;
  row.insertCell(1)
    ..text = entry;
}
