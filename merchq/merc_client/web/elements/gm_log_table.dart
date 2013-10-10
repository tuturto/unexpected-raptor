library gm_log_table;

import 'package:polymer/polymer.dart';


class LogEntry {
  String entryDate;
  String text;
  
  LogEntry(this.entryDate, this.text);
}

@CustomTag('gm-log-table')
class GMLogTable extends PolymerElement with ObservableMixin {
  
  //final ObservableList logEntries = toObservable([]);
  @observable List logEntries = [];
  
  bool get applyAuthorStyles => true;
  
  void addEntry(date, text) {
    //TODO: ugly hack, because I don't know how to get template to notice the change
    List newEntries = new List();
    newEntries.addAll(logEntries);
    newEntries.add(new LogEntry(date, text));
    
    logEntries = newEntries;
  }
  
  void clear() {
    logEntries = [];
  }
}
