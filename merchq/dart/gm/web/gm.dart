import 'dart:html';
import 'dart:json';

void main() {
  loadData();
}

void loadData() {
  var url = "http://127.0.0.1:8000/gm/log_entries";

  // call the web server asynchronously
  var request = HttpRequest.getString(url).then(onDataLoaded);
  //var request = '{"entries": [{"text": "Test entry", "entry_date": "3068-03-21"}, {"text": "2nd test entry", "entry_date": "3068-03-21"}]}';  
  //onDataLoaded(request);
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
