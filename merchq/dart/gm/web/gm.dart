import 'dart:html';
import 'dart:json';
import 'package:dart_config/default_browser.dart';

DateTime shownDate = null;

void main() {
  getConfig();
}

void getConfig() {
  
  loadConfig('/static/config.yaml').then(
        (Map config) {
          loadData(config);
        }, 
        onError: (error) => loadConfig().then(loadData));
}

void loadData(Map config) {
  
  if (shownDate == null) {
    shownDate = new DateTime(3068, 3, 20);
  }
  
  var path = new StringBuffer();
  path..write("/gm/log_entries/")
      ..write("${shownDate.year}/")
      ..write("${shownDate.month}/")
      ..write("${shownDate.day}/");
  
  Uri url = new Uri(scheme: 'http',
                    host: config["host"],
                    port: config["port"],
                    path: path.toString());
    
  var request = HttpRequest.getString(url.toString()).then(onDataLoaded);
}

void onDataLoaded(String jsonString) {
  Map data = parse(jsonString);
  var entries = data["entries"];
  
  TableElement table = query('#log_table');
  
  while(table.rows.length > 1) {
    table.rows[1].remove();
  }
    
  entries.forEach((entry) => addLogEntry(table, 
      entry["entry_date"], 
      entry["text"]));
}

void addLogEntry(TableElement table, String date, String entry) {
 
  TableRowElement row = table.insertRow(-1);
  
  row.insertCell(0)
    ..text = date;
  row.insertCell(1)
    ..text = entry;
}
