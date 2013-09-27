import 'dart:html';
import 'dart:json';
import 'package:dart_config/default_browser.dart';

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
  var url = config["myServerUrl"] + "/gm/log_entries";
  var request = HttpRequest.getString(url).then(onDataLoaded);
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
