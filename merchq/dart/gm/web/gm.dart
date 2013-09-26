import 'dart:html';
import 'dart:json';
import 'package:dart_config/default_browser.dart';

void main() {
  loadData();
}

void loadData() {
  
  loadConfig('/static/config.yaml').then(
      (Map config) {
        var url = config["myServerUrl"] + "/gm/log_entries";
        var request = HttpRequest.getString(url).then(onDataLoaded);
      }, 
      onError: (error) => loadConfig().then(
          (Map config) {
            var url = config["myServerUrl"] + "/gm/log_entries";
            var request = HttpRequest.getString(url).then(onDataLoaded);
          }, 
          onError: (error) => print(error)));
}

void onDataLoaded(String jsonString) {
  Map data = parse(jsonString);
  var entries = data["entries"];
  entries.forEach((entry) => addLogEntry(entry["entry_date"], entry["text"]));
}

void addLogEntry(String date, String entry) {
  TableElement table = query('#log_table');
  TableRowElement row = table.insertRow(-1);
  
  row.insertCell(0)
    ..text = date;
  row.insertCell(1)
    ..text = entry;
}
