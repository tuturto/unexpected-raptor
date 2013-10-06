library gm_log_table;

import 'package:polymer/polymer.dart';


class LogEntry {
  String entryDate;
  String text;
  
  LogEntry(this.entryDate, this.text);
}

@CustomTag('gm-log-table')
class GMLogTable extends PolymerElement with ObservableMixin {
  
  @observable List logEntries = [];
  
  void addEntry(date, text) {
    logEntries.add(new LogEntry(date, text));
  }
  
  void clear() {
    logEntries.clear();
  }
}
